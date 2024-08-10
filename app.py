from flask import Flask, render_template, request
import google.generativeai as palm
import os

app = Flask(__name__)

# 加载 API Token
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
        # 调用 palm.chat，传递消息作为字符串而不是字典
        response = palm.chat(**model, messages=[q])
        # 从响应中获取生成的内容
        r = response['candidates'][0]['content']
    except Exception as e:
        r = f"Sorry, something went wrong with the AI response: {str(e)}"
    
    return render_template("genAI.html", r=r)

if __name__ == "__main__":
    app.run(debug=True)
