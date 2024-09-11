import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
st.markdown(#GithubIcon {
  visibility: hidden;
})
# Load your data and preprocessed variables (replace these paths with your actual data paths)
with open('recomender.pkl', 'rb') as file:
    pt, similarity_score, popular_new_df = pickle.load(file)

# Streamlit UI
st.title("Book Recommendation System")

# Display developer information
st.sidebar.text("Developed by: Salim - ML Engineer")

# User input for book search
user_input = st.text_input("Search for your desired book:", "Serch Book here...")

# Search button
if st.button("Search"):
    try:
        # Check if the specified book is in the user-item matrix
        index = pt.index.get_loc(user_input)
    except KeyError:
        st.error(f"The book '{user_input}' is not found in the dataset.")
    else:
        # Getting the similarity scores for the specified book
        book_similarity = similarity_score[index]

        # Sorting the enumerated list of similar items based on similarity scores
        similar_items = sorted(enumerate(book_similarity), key=lambda x: x[1], reverse=True)

        # Extracting the top 5 recommended books
        top_recommendations = [pt.index[i[0]] for i in similar_items[1:6]]  # Exclude the input book itself

        # Displaying recommended books without images
        st.write("Top 5 recommended books for", user_input, "are:")
        for recommended_book in top_recommendations:
            st.write(recommended_book)
