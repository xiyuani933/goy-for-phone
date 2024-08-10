from flask import Flask, render_template, request
import google.generativeai as palm
import os

app = Flask(__name__)

# Load the API token
api = os.getenv("MAKERSUITE_API_TOKEN")
palm.configure(api_key=api)

model = {"model": "models/chat-bison-001"}

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/genAI", methods=["POST"])
def genAI():
    q = request.form.get("q")
    try:
        response = palm.chat(**model, messages=[{"role": "user", "content": q}])
        r = response.get('candidates')[0].get('content')
    except Exception as e:
        r = "Sorry, something went wrong with the AI response."
    
    return render_template("genAI.html", r=r)

if __name__ == "__main__":
    app.run(debug=True)
