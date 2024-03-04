# Chatbot-using-Python
This repository contains a simple chatbot implemented using Python and Streamlit. The chatbot is trained to respond to various user inputs based on predefined intents. It uses the scikit-learn library for text vectorization (TF-IDF) and a logistic regression classifier for intent recognition.

-> How to Use:
1. Clone the repository to your local machine.
git clone https://github.com/your-username/chatbot.git
cd chatbot

2. Install the required dependencies.
pip install -r requirements.txt

3. Run the Streamlit app.
streamlit run chatbot_app.py

4. Open your web browser and go to http://localhost:8501 to interact with the chatbot.

-> Model Training:
The chatbot utilizes TF-IDF vectorization and a logistic regression classifier for intent recognition. The training data consists of predefined patterns for each intent.

-> Conversational Interface:
Users can type messages in the provided input box, and the chatbot will respond accordingly. The conversation is displayed in a text area, and the chatbot will provide responses based on the recognized intent.

-> Note:
The chatbot's responses are generated based on the patterns provided in the training data. Feel free to expand the intents and responses for a more interactive experience.
