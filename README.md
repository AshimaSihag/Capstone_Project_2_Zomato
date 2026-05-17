# 🍽️ Zomato Restaurant Recommendation System

## 📌 Project Overview

This project is a **Content-Based Restaurant Recommendation System** developed using the **Zomato Restaurant Dataset**.

The system recommends similar restaurants based on:

- Cuisines
- Restaurant Type
- Dishes Liked
- Customer Reviews

The recommendation engine uses:

- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Cosine Similarity

A user simply selects a restaurant name, and the system recommends similar restaurants sorted by highest rating.

---

# 🚀 Features

✅ Restaurant Recommendation System  
✅ NLP-based Text Processing  
✅ TF-IDF Vectorization  
✅ Cosine Similarity Calculation  
✅ Streamlit Interactive Web App  
✅ WordCloud Visualization  
✅ Restaurant Rating Analysis  
✅ User-Friendly Interface

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLP
- TF-IDF Vectorizer
- Cosine Similarity
- Streamlit
- Matplotlib
- WordCloud

---

# 📂 Dataset Information

Dataset Used:
- Zomato Restaurant Dataset

Dataset contains:
- Restaurant Name
- Location
- Cuisines
- Restaurant Type
- Customer Reviews
- Ratings
- Votes
- Dishes Liked

---

# ⚙️ Project Workflow

## 1. Data Cleaning
- Removed duplicate rows
- Handled missing values
- Cleaned rating column

## 2. Feature Engineering
Combined important text features:
- cuisines
- dish_liked
- rest_type
- reviews_list

## 3. Text Preprocessing
- Lowercase conversion
- Removal of special characters
- Text normalization

## 4. TF-IDF Vectorization
Converted text data into numerical vectors using TF-IDF.

## 5. Cosine Similarity
Calculated restaurant similarity scores using cosine similarity.

## 6. Recommendation Generation
Recommended top similar restaurants based on user selection.

## 7. Data Visualization
Generated WordCloud visualization for restaurant features.

---

# 🖥️ Streamlit Web Application

The project also includes an interactive Streamlit web application where users can:

- Select a restaurant
- Get top restaurant recommendations
- View ratings and cuisines
- Explore restaurant similarity interactively

---

# 📊 Sample Recommendation Output

| Restaurant | Rating | Cuisine |
|------------|--------|----------|
| Jalsa Gold | 4.5 | North Indian, Mughlai |
| The Hidden Home | 4.3 | Asian, Chinese |
| Atithi | 3.9 | North Indian |

---

# 📈 Future Improvements

- Collaborative Filtering
- Hybrid Recommendation System
- Deep Learning Recommendation Engine
- Sentiment Analysis on Reviews
- Deployment on Cloud Platforms

---

# ▶️ How to Run the Project

## 1. Clone Repository

```bash
git clone <your-github-link>