from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
@app.route("/")
def home():
    return """
    <h2>AI Chatbot</h2>
    <input id='msg' placeholder='Type message'>
    <button onclick='send()'>Send</button>
    <div id='chat'></div>
    
<style>
body { font-family: Arial; max-width: 600px; margin: auto; }
#chat { margin-top: 20px; }
input { width: 70%; padding: 8px; }
button { padding: 8px; }
</style>
    <script>
async function send() {
    let msg = document.getElementById("msg").value;

    if (!msg) return;

    document.getElementById("chat").innerHTML +=
        "<p><b>You:</b> " + msg + "</p>";

    document.getElementById("msg").value = "";

    let res = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: msg})
    });

    let data = await res.json();

    document.getElementById("chat").innerHTML +=
        "<p><b>Bot:</b> " + data.reply + "</p>";
}


document.getElementById("msg").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        send();
    }
});
</script>
    """

messages = []

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    reply = response.choices[0].message.content

    messages.append({"role": "assistant", "content": reply})

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)