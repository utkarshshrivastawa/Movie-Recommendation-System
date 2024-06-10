import pickle
import difflib
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved model and data
movie_data = pickle.load(open("movie_model.sav", 'rb'))
similarity = pickle.load(open("similarity.sav", 'rb'))

with st.sidebar:
    selected = option_menu("Movie Recommendation Assistant",
                           ['Movie Recommendation System'],
                           icons=['film'],
                           default_index=0)

# Movie Recommendation Page
if selected == 'Movie Recommendation System':
    # Page title
    st.title('Movie Recommendation System Using ML')
    
    movie_name = st.text_input('Enter your favourite movie name:')
    
    if movie_name:
        list_of_titles = movie_data['title'].tolist()
        close_matches = difflib.get_close_matches(movie_name, list_of_titles)
        
        if close_matches:
            close_match = close_matches[0]
            index_movie = movie_data[movie_data.title == close_match]['index'].values[0]
            similarity_score = list(enumerate(similarity[index_movie]))
            sorted_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
            
            st.write('Movies suggested for you:')
            i = 1
            for movie in sorted_movies:
                index = movie[0]
                title_from_index = movie_data[movie_data.index == index]['title'].values[0]
                if i <= 10:
                    st.write(f"{i}. {title_from_index}")
                    i += 1
        else:
            st.write("No close matches found for the entered movie name.")
