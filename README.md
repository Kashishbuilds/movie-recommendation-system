# 🎬 Movie Recommendation System

This is a **Streamlit app** that recommends movies similar to your favorite ones.  
It uses a precomputed similarity matrix to suggest top 10 movies.

## How It Works

1. Choose a movie from the dropdown.
2. Click "Recommend Movies".
3. Get a list of similar movies.

The app automatically downloads the similarity file from Google Drive.

## Deployment

You can deploy this app on **Streamlit Cloud, Heroku, or any Python web hosting platform**.

### Requirements

- Python 3.x
- Streamlit
- gdown
- pandas
- pickle5 (if required)

## Run Locally

1. Install dependencies:
```bash
pip install -r requirements.txt
2.Run the app:
streamlit run app.py
