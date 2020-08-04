from flask import Flask
import os
import logging
import sys

app = Flask(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


@app.route("/")
def hello():
    logging.info('Hello, World!')
    return "Flask inside Docker!!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
    