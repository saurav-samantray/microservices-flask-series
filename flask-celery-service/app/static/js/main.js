// custom scripts


$(document).ready(function(){
	$("form").submit(function(event){
		event.preventDefault();

	// Get form
	var form = $('#upload-form')[0];

    // Create an FormData object 
    var data = new FormData(form);
    console.log(form)

    // disabled the submit button
    $("#upload-button").prop("disabled", true);
    $("#status").removeClass().addClass("text-secondary").html("Uploading")
    $("#processing-status").prop("disabled", true);

    $.ajax({
    	type: "POST",
    	enctype: 'multipart/form-data',
    	url: "/upload",
    	data: data,
    	processData: false,
    	contentType: false,
    	cache: false,
    	timeout: 600,
    	success: function (data) {
    		console.log("SUCCESS : ", data);
    		$("#upload-button").prop("disabled", false);
    		$("#processing-status").prop("disabled", false);
    		
    		$("#status").removeClass().addClass("text-warning").html("Processing")
    		$("#upload-task-id").val(data.task_id)

    	},
    	error: function (e) {
    		console.log("ERROR : ", e);
    		$("#upload-button").prop("disabled", false);
    		$("#status").removeClass().addClass("text-danger").html("Upload Failed")
    		$("#processing-status").prop("disabled", true);
    	}
    });

});


	$("#processing-status").click(function(){
		$.get("/upload/"+ $("#upload-task-id").val(), function(data, status){
      //alert(data)
      
      if(data.status === "SUCCESS"){
      	$("#status").removeClass().addClass("text-success").html("Processed")
      	$("#download-button").prop("disabled", false);
      }

  });
	});

	$("#download-button").click(function(){
		$.get("/download/"+ $("#upload-file-name").val(), function(data, status){
			var blob = new Blob([data], { type: "application/octetstream" });
			
                    //Check the Browser type and download the File.
                    var isIE = false || !!document.documentMode;
                    if (isIE) {
                    	window.navigator.msSaveBlob(blob, $("#upload-file-name").val());
                    } else {
                    	var url = window.URL || window.webkitURL;
                    	link = url.createObjectURL(blob);
                    	var a = $("<a />");
                    	a.attr("download", $("#upload-file-name").val());
                    	a.attr("href", link);
                    	$("body").append(a);
                    	a[0].click();
                    	$("body").remove(a);
                    }
                });
	});

	$("#file-selection-button").on("change", function() {
		var fileName = $(this).val().split("\\").pop();
	  //alert(fileName)
	  //$(this).siblings(".custom-file-label").addClass("selected").html(fileName);
	  $("#upload-file-name").attr('value', fileName);
	});



});