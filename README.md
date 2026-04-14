# AI-chatbot-UPDATED
An AI chatbot which can be quite a helpful AI assistant when you are curious about any stuff.


An AI chatbot which can be quite a helpful AI assistant when you are curious about any stuff.

1. Install dependencie Open a terminal in the project folder and run: pip install -r requirements.txt

or run this: pip install flask openai python-dotenv

This installs all required libraries for the project.

2. Get an API key

Choose one of the following providers:

https://console.groq.com/ (free)

https://aistudio.google.com/ (free)

https://platform.openai.com/ (paid)

3. Secure your API key (.env file)

Do NOT write your API key inside app.py. Instead, create a .env file in the project folder.

Windows terminal shortcut (optional): notepad .env

Inside the file, write: OPENAI_API_KEY=YOUR_API_KEY

Replace YOUR_API_KEY with your real key.

4. Run the project

Run ONE of the following commands: python app.py OR flask run

Then open this in your browser: http://127.0.0.1:5000

You will see your AI chatbot running.
