# Movie Recommendation System with Streamlit

## Overview
This project implements a Movie Recommendation System using Python and Streamlit for the front-end. The recommendation engine is built on cosine similarity, processing MovieLens dataset information such as movies, credits, genres, keywords, cast, and crew.

## Prerequisites

Make sure you have the required dependencies installed before running the application:

```bash
pip install streamlit numpy pandas matplotlib seaborn scikit-learn nltk

## Features
- **Streamlit Front-End:** Utilizes Streamlit to create an interactive and user-friendly web application for entering movie names and receiving personalized recommendations.
- **Cosine Similarity:** Implements cosine similarity to find movies with similar characteristics and provide relevant recommendations.
- **Data Preprocessing:** Cleans and processes movie data, including merging datasets, tokenizing and stemming text, and converting text data to numerical values.

## Project Structure
- `Front.py`: Python script containing the Streamlit web application code for user interaction.
- `Movie_reco.py`: Backend code for the movie recommendation system, including data preprocessing and the recommendation function.
- `movies.csv`: Dataset containing movie details.
- `credits.csv`: Dataset containing credits information.
- `README.md`: Documentation providing an overview, features, project structure, usage instructions, and customization guidelines.

## Usage
1. **Install dependencies:** `pip install streamlit numpy pandas matplotlib seaborn scikit-learn nltk`
2. **Run the Streamlit app:** `streamlit run Front.py`
3. **Access the interactive front-end in your web browser.**

## Instructions
1. Open `Front.py` and customize the Streamlit app as needed.
2. Ensure that `movies.csv` and `credits.csv` are present in the project directory.
3. Run the Streamlit app and enter a movie name to receive recommendations.
4. Explore the code in `Movie_reco.py` to understand the recommendation engine's implementation.

Feel free to customize and enhance the project based on your specific needs. Happy movie recommending!
