from flask import Flask, render_template
from blueprints.paper_checker import paper_bp
from auth import auth_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(paper_bp)

@app.route("/", methods=["GET"])
def chat():
    return "main.html"

if(__name__ == "__main__"):
    app.run()
