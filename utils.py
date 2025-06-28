import matplotlib.pyplot as plt

def plot_ratings_distribution(data):
    """Plot distribution of ratings."""
    plt.hist(data['rating'], bins=10)
    plt.title('Ratings Distribution')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.savefig('ratings_distribution.png')
    plt.close()