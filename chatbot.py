import pandas as pd
import streamlit as st

# Load the dataset
df = pd.read_csv("TMDB_movie_dataset.csv")

# Function to filter movies based on the user's input
def filter_movies(user_input):
    if user_input:
        # Filter the dataset based on the movie titles that start with the user input
        filtered_df = df[df['title'].str.contains(user_input, case=False, na=False)]
        return filtered_df['title'].tolist()
    else:
        return []

# Streamlit UI
st.markdown("## 🎥 Movie Info Chatbot 🍿")

# User input for movie initials or keywords
user_input = st.text_input("🔍 Enter movie initials or keywords:")

# Get filtered movie titles based on user input
filtered_movies = filter_movies(user_input)

# Show dropdown for selecting a movie from filtered list
if filtered_movies:
    selected_movie = st.selectbox("🎬 Select a movie", filtered_movies)

    # Get movie details for the selected movie
    if selected_movie:
        movie_details = df[df['title'] == selected_movie].iloc[0]
        
        # Create columns to organize layout
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"**🎞️ Title**: {movie_details['title']}")
            st.markdown(f"**⭐ Vote Average**: {movie_details['vote_average']}")
            st.markdown(f"**📅 Release Date**: {movie_details['release_date']}")
            st.markdown(f"**🕒 Runtime**: {movie_details['runtime']} minutes")
            st.markdown(f"**🎭 Genres**: {movie_details['genres']}")
            st.markdown(f"**🎟️ Popularity**: {movie_details['popularity']}")
        
        with col2:
            st.markdown(f"**💲 Revenue**: ${movie_details['revenue']}")
            st.markdown(f"**🎥 Production Companies**: {movie_details['production_companies']}")
            st.markdown(f"**🌍 Production Countries**: {movie_details['production_countries']}")
            st.markdown(f"**🗣️ Spoken Languages**: {movie_details['spoken_languages']}")
            st.markdown(f"**🔗 Homepage**: {movie_details['homepage']}")
            st.markdown(f"**🎞️ Overview**: {movie_details['overview']}")

        # Display additional movie details at the bottom
        st.markdown("---")
        st.markdown(f"**📝 Tagline**: {movie_details['tagline']}")
        st.markdown(f"**🔑 Keywords**: {movie_details['keywords']}")
else:
    st.write("No movies found. Please enter different initials or keywords.")

# Footer with emojis
st.markdown("---")
st.markdown("### Made with ❤️ by MovieBot 🎬")
