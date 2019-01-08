from flask import Flask, request
import json
app = Flask(__name__)

@app.route("/test", methods=['POST'],strict_slashes=False)
def postmethod():
    input_json = request.get_json(force=True)
    return json.dumps("your json file contains: "+ str(input_json))


if __name__ == '__main__':
    app.run(use_reloader=False)