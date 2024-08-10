from flask import Flask, render_template,request
import google.generativeai as palm

app = Flask(__name__)

model = {"model": "models/chat-bison-001"}

palm.configure(api_key="AIzaSyCaQcgKn95ZO6AR1t2PXzk9UydTkt4sWZQ")

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/genAI",methods=["GET","POST"])
def genAI():
    q = request.form.get("q")
    r = palm.chat(**model, messages=q)
    return(render_template("genAI.html",r=r.last))
    
if __name__ == "__main__":
    app.run()
