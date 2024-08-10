from flask import Flask, render_template, request
import google.generativeai as palm
import os

app = Flask(__name__)

# 获取 API token
api = os.getenv("MAKERSUITE_API_TOKEN")
if not api:
    raise ValueError("API token is not set in the environment variables.")

palm.configure(api_key=api)

model = {"model": "models/chat-bison-001"}

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/genAI", methods=["POST"])
def genAI():
    q = request.form.get("q")
    try:
        # 调用 palm.chat，并将问题传递为一个列表
        response = palm.chat(**model, messages=[q])
        
        # 检查 response 是否有 candidates 属性
        if hasattr(response, 'candidates') and response.candidates:
            r = response.candidates[0]['content']
        else:
            r = "Sorry, the AI did not return any valid response."
    
    except AttributeError as e:
        r = f"Sorry, something went wrong with the AI response: {str(e)}"
    
    except Exception as e:
        r = f"Sorry, something went wrong with the AI response: {str(e)}"
    
    return render_template("genAI.html", r=r)

if __name__ == "__main__":
    app.run(debug=True)
