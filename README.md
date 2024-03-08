# Chatbot Application

## Project Description

This is a simple chatbot application built using Python and Streamlit. The chatbot is designed to engage in conversations and provide responses based on predefined patterns and intents. It utilizes natural language processing and machine learning to understand user input and generate appropriate responses.

## Technologies Used

- **Python 3.x:** The core programming language used for building the application.
- **Streamlit:** A Python library for creating web applications with minimal effort. Streamlit allows for the development of interactive and user-friendly interfaces.

## Libraries Used

### nltk

The Natural Language Toolkit (nltk) library is used for natural language processing tasks. It aids in tokenization, stemming, and other language-related operations.

### ssl

The Secure Sockets Layer (ssl) library is used to create a secure connection for downloading NLTK data.

### sklearn

The scikit-learn (sklearn) library is employed for machine learning tasks in this project. Specifically, the TfidfVectorizer is used for text vectorization, and LogisticRegression is used for intent classification.

### random

The random library is utilized for randomly selecting responses from predefined intents.

## Features

- Simple chatbot with predefined intents and responses.
- User-friendly interface built with Streamlit.
- Utilizes machine learning for intent classification.
- Provides responses based on user input patterns.

## How I Built This

### Intent Definition

The chatbot's behavior is defined through a set of intents. Each intent consists of patterns (user input), a tag, and corresponding responses. Intents cover greetings, goodbyes, expressions of gratitude, and specific topics like weather, budgeting, and credit scores.

### Machine Learning Model

A TfidfVectorizer is used to convert user input patterns into numerical features. A Logistic Regression classifier is trained on the vectorized data to predict the intent (tag) of a given user input.

### Streamlit Interface

Streamlit is employed to create a user-friendly web interface. The application allows users to type messages, receive responses, and engage in a chat-like interaction with the bot.
