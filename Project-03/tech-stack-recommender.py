"""
    DecodeLabs Internship - Project 03
    Author: Rayyan Aamir
    Project Description: A content-based recommendation system that uses TF-IDF weighting and Cosine similarity
                         engine to mathematically map a user's skill-set to their ideal tech career paths
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_career_recommendations(user_skills, top_n=3, csv_path='raw_skills.csv'):
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: The file '{csv_path}' was not found!")
        return None

    df['skills'] = df['skills'].fillna('')
    user_input_str = " ".join(user_skills)
    corpus = df['skills'].tolist()
    
    vectorizer = TfidfVectorizer(lowercase=True)
    all_vectors = vectorizer.fit_transform(corpus + [user_input_str])
    job_vectors = all_vectors[:-1]
    user_vector = all_vectors[-1]
    
    similarity_scores = cosine_similarity(user_vector, job_vectors).flatten()
    results_df = df.copy()
    results_df['similarity_score'] = similarity_scores
    top_recommendations = results_df.sort_values(by='similarity_score', ascending=False).head(top_n)
    
    return top_recommendations[['job_role', 'similarity_score']]


def main():
    print("=" * 50)
    print("\t\tTech-Stack Recommender")
    print("=" * 50)

    user_inputs = []
    for i in range(3):
        user_str = input(f"Enter skill {i + 1}: ").strip()
        user_inputs.append(user_str)

    recommendations = get_career_recommendations(user_inputs, top_n=3, csv_path='raw_skills.csv')

    if recommendations is not None:
        print("\n\n--------------- Top 3 Career Path Recommendations ---------------")
        for index, row in recommendations.iterrows():
            match_percentage = row['similarity_score'] * 100
            print(f"Role: {row['job_role']}\t\t | Alignment Score: {match_percentage:.2f}%")


if __name__ == "__main__":
    main()