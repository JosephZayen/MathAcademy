from flask import Flask, render_template
from other.paper_checker.app import bp

app = Flask(__name__)
app.register_blueprint(bp)

@app.route("/", methods=["GET"])
def chat():
    return "hi"

if(__name__ == "__main__"):
    app.run()