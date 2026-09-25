import os
from groq import groq
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from openai import OpenAI

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Initialize Flask app
app = Flask(__name__)

# Store conversation in memory (basic list for now)
conversation = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")

    # Add user message to the conversation
    conversation.append({"role": "user", "content": user_input})

    # Send full conversation history to the model
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation
    )

    bot_reply = response.choices[0].message.content

    # Append bot response to the conversation too
    conversation.append({"role": "assistant", "content": bot_reply})

    return jsonify({"response": bot_reply})


if __name__ == "__main__":
    app.run(debug=True)

