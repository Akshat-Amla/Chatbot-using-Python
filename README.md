# 🎥 Movie Info Chatbot 🍿

## Project Description

This chatbot application helps users find movie information by allowing them to search based on movie initials or keywords. Built using Python and Streamlit, the chatbot filters movie titles from a dataset and displays detailed information about the selected movie.

## Technologies Used

- **Python 3.x:** The core programming language used for building the chatbot.
- **Streamlit:** A Python library for creating an interactive web application.
- **Pandas:** Used for loading and manipulating the dataset.

## Features

- Allows users to input movie initials or keywords.
- Filters and displays matching movies from a dataset.
- Displays detailed information about the selected movie, including:
  - Title
  - Vote average
  - Release date
  - Runtime
  - Genres
  - Popularity
  - Revenue
  - Production companies & countries
  - Spoken languages
  - Tagline, keywords, and more.
- User-friendly interface built with Streamlit.
- Shows a dropdown of filtered movie titles based on the user's input.

## How It Works

1. **Dataset Loading**: The application loads the "TMDB_movie_dataset.csv" which contains a list of movies and their associated details.
  
2. **Filtering Movies**: 
   - When a user enters movie initials or keywords in the search box, the chatbot filters through the dataset for matching movie titles.
   - The filtering is case-insensitive and allows partial matches.

3. **Movie Selection**:
   - If matching movie titles are found, a dropdown is displayed for users to select one of the filtered movies.
   - Once a movie is selected, its details are displayed in an organized layout.

4. **Movie Details**:
   - The chatbot displays movie details such as vote average, release date, runtime, genres, popularity, revenue, production companies, and more in two columns for better readability.
   - A footer with additional information such as tagline and keywords is displayed.

5. **Footer**: The app concludes with a friendly footer message made with love.

## Libraries Used

- **Pandas**: For reading the CSV dataset and manipulating data.
- **Streamlit**: For building the user interface and handling input/output.
- **Emoji**: Added in the interface to enhance user engagement.

## How to Run

1. Clone the repository and navigate to the project directory.
2. Install the required libraries using `pip install pandas streamlit`.
3. Run the application with the following command:
   ```bash
   streamlit run app.py
