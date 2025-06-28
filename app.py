from flask import Flask, request, render_template
import pandas as pd
from data_preprocessing import load_data, setup_database
from model import train_model, get_recommendations

app = Flask(__name__)

# Load data and train model
data = load_data('data/book_ratings.csv')
conn = setup_database(data)
svd, matrix_reduced, user_item_matrix = train_model(data)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    error = None
    if request.method == 'POST':
        try:
            user_id = int(request.form['user_id'])
            recommendations = get_recommendations(user_id, matrix_reduced, user_item_matrix, data)
            if recommendations.empty:
                error = f"No recommendations found for User ID {user_id}. Try a different ID (e.g., 1–4)."
        except ValueError:
            error = "Please enter a valid User ID (e.g., 1–4)."
    return render_template('index.html', recommendations=recommendations.to_dict('records'), error=error)

if __name__ == '__main__':
    app.run(debug=True)