// custom scripts

$(document).ready(function(){
  $("a").click(function(){
    $.get("/click", function(data, status){
      $("#counter-value").text(data.counter)
    });
  });
});