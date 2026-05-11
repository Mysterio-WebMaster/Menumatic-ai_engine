import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class RecommendationService:

    def __init__(self):
        self.tfidf = TfidfVectorizer(ngram_range=(1, 2))
        self.tfidf_matrix = None
        self.menu_data = None

    def build(self, items: list):
        df = pd.DataFrame(items)

        # Normalize text fields
        df["name"] = df["name"].str.strip().str.lower()
        df["category"] = df["category"].str.strip().str.lower()
        df["veg_non_veg"] = df["veg_non_veg"].str.strip().str.lower()

        # Build features string
        df["features"] = (
            df["name"]
            + " "
            + df["category"]
            + " "
            + df["category"]
            + " "
            + df["veg_non_veg"]
            + " "
            + df["veg_non_veg"]
        )

        self.menu_data = df
        self.tfidf_matrix = self.tfidf.fit_transform(df["features"])

    def recommend(self, query, top_n=5, min_score=0.3):
        query_clean = query.lower().strip()

        query_vector = self.tfidf.transform([query_clean])

        similarity_score = cosine_similarity(query_vector, self.tfidf_matrix).flatten()

        top_indices = similarity_score.argsort()[::-1][:top_n]

        results = self.menu_data.iloc[top_indices][
            ["itemid", "name", "category", "price", "veg_non_veg"]
        ].copy()
        results["score"] = similarity_score[top_indices].round(4)

        results = results[results["score"] >= min_score]

        return results.reset_index(drop=True).to_dict(orient="records")
