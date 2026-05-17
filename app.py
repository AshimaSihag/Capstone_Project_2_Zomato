import streamlit as st
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="Zomato Recommendation System",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ Zomato Restaurant Recommendation System")

st.markdown("""
This app recommends similar restaurants using **Content-Based Recommendation System**,  
**TF-IDF Vectorization**, and **Cosine Similarity**.
""")

st.markdown("---")

@st.cache_data
def load_data():
    df = pd.read_csv("zomato_processed.csv")
    return df

@st.cache_resource
def build_model(df):
    tfidf = TfidfVectorizer(stop_words="english", max_features=5000)
    tfidf_matrix = tfidf.fit_transform(df["combined_features"])
    indices = pd.Series(df.index, index=df["name"])
    return tfidf_matrix, indices

def recommend_restaurants(restaurant_name, df, tfidf_matrix, indices):
    idx = indices[restaurant_name]

    similarity_scores = cosine_similarity(
        tfidf_matrix[idx],
        tfidf_matrix
    ).flatten()

    similar_indices = similarity_scores.argsort()[::-1][1:11]

    recommendations = df[[
        "name",
        "rate",
        "cuisines",
        "rest_type",
        "location"
    ]].iloc[similar_indices]

    recommendations = recommendations.sort_values(
        by="rate",
        ascending=False
    )

    return recommendations

df = load_data()
tfidf_matrix, indices = build_model(df)

st.header("Select a Restaurant")

restaurant_name = st.selectbox(
    "Choose a restaurant:",
    sorted(df["name"].unique())
)

if st.button("Recommend Restaurants"):
    recommendations = recommend_restaurants(
        restaurant_name,
        df,
        tfidf_matrix,
        indices
    )

    st.success(f"Top recommendations for: {restaurant_name}")

    st.dataframe(
        recommendations,
        use_container_width=True
    )

    top_rating = recommendations["rate"].max()
    st.success(f"⭐ Highest Rated Recommendation: {top_rating}")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Restaurants", len(df))

with col2:
    st.metric("Average Rating", round(df["rate"].mean(), 2))

with col3:
    st.metric("Unique Locations", df["location"].nunique())

st.markdown("---")

st.header("Project Techniques Used")

st.markdown("""
- Data Cleaning
- Text Preprocessing
- TF-IDF Vectorization
- Cosine Similarity
- Content-Based Recommendation System
- Streamlit Web Application
""")