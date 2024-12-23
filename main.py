import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    service = os.environ.get("K_SERVICE")
    revision = os.environ.get("K_REVISION")
    return f"Hello from cloud run Service : {service} with revision: {revision}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))