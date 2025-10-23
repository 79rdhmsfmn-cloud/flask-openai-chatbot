FLASK OPENAI CHATBOT

This project walks through how I built a simple chatbot using Flask and the OpenAI API. Everything runs locally — no external web hosting, no extra frameworks. The goal was to understand how a Python web app can send and receive messages with OpenAI’s API while keeping things clean and easy to follow. 
The repo includes every step from creating the virtual environment to chatting with the bot in a browser. Each of the twelve screenshots in the images folder shows a different part of the process — setup, code, testing, and the final working chatbot.

What’s Inside:

Flask backend with a /chat endpoint that talks to the OpenAI API
.env configuration to keep your API key private
Simple HTML + JavaScript front end for sending messages
Curl examples for quick testing from the terminal
A full visual walkthrough in twelve screenshots

The Steps:

System setup and installing dependencies
Creating and activating a virtual environment
Installing Flask, python-dotenv, and openai
Adding an .env file with the API key
Writing the base Flask app (chatbot.py)
Running the Flask server locally
Testing responses with curl
Adding message memory to keep conversation context
Updating routes and response handling
Checking return codes and output
Building the index.html chat interface
Chatting with the finished bot in a browser

Tools Used:

Python 3
Flask
OpenAI API

HTML + JavaScript

python-dotenv
