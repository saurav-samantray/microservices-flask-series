from flask import Flask, request

app = Flask(__name__)


@app.route('/' , methods=['GET'])
def get():
    #result = 1/0
    args = request.args
    return {
        "message": f"Hello {request.method} Request!",
        "args": args
        }, 200


@app.route('/' , methods=['POST'])
def post():
    args = request.args
    payload = request.json
    headers = request.headers
    return {
        "message": f"Hello {request.method} Request!",
        "request_params": args,
        "request_payload": payload,
        "request_headers": headers.get("name"),
        }, 201      

###
# Tasks 
# 1. Create PUT method
# 2. Create a method that can accept both POST and PUT
#
# #    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)