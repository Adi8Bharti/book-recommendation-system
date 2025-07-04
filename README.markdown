# Personalized Book Recommendation System

A Python-based recommendation system that suggests books to users based on collaborative filtering using Singular Value Decomposition (SVD). Built with Flask for a web interface and SQLite for data storage.

## Features
- Loads book ratings from a CSV file.
- Stores data in a SQLite database.
- Uses SVD for collaborative filtering.
- Provides a Flask web interface to input user ID and view recommendations.


## Usage
- Enter a User ID (e.g., 1–4 for the sample dataset) to get book recommendations.
- The system uses collaborative filtering to suggest books based on user ratings.

## Project Structure
```
book-recommendation-system/
├── data/
│   └── book_ratings.csv       # Sample dataset
├── src/
│   ├── data_preprocessing.py  # Data loading and SQL setup
│   ├── model.py              # Collaborative filtering model
│   ├── app.py                # Flask app
│   └── utils.py              # Helper functions
├── templates/
│   ├── index.html            # Input form
│   └── results.html          # Results page
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
├── LICENSE                   # MIT License
└── .gitignore                # Ignore unnecessary files
```

## Dataset
- `book_ratings.csv`: Contains `user_id`, `book_id`, `rating`, and `title`.
- Sample data includes 12 ratings for 6 books by 4 users.
