from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, Welcome to my Flask App!</h1>"


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000,
        # ssl_context=()
    )
