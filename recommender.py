from pathlib import Path
from difflib import get_close_matches

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


# ----------------------------
# Data loading & preparation
# ----------------------------

def load_items(csv_path: Path) -> pd.DataFrame:
    """
    Load a CSV file and build a 'content' column used for TF-IDF.

    Expected columns:
      - item_id
      - title
      - genres
      - description
    """
    df = pd.read_csv(csv_path)

    # Basic cleaning
    df["genres"] = df["genres"].fillna("")
    df["description"] = df["description"].fillna("")
    df["title"] = df["title"].fillna("")

    # Combined text field for TF-IDF
    df["content"] = (
        df["title"].astype(str) + " " +
        df["genres"].astype(str) + " " +
        df["description"].astype(str)
    )

    return df


def build_tfidf_matrix(items: pd.DataFrame):
    """
    Build a TF-IDF matrix over the 'content' column.
    Returns the fitted vectorizer and the sparse matrix.
    """
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(items["content"])
    return vectorizer, matrix


# ----------------------------
# Helper: title search
# ----------------------------

def resolve_title_to_index(items: pd.DataFrame, query: str):
    """
    Resolve a free-text title query to a row index in the dataframe.
    Uses simple fuzzy matching (difflib.get_close_matches).

    Returns:
      (index, matched_title)  or  (None, None) if not found.
    """
    if not query:
        return None, None

    titles = items["title"].astype(str).tolist()
    # Use lowercased titles for more robust matching
    lookup = {t.lower(): t for t in titles}

    matches = get_close_matches(query.lower(), lookup.keys(), n=1, cutoff=0.4)
    if not matches:
        return None, None

    best_title = lookup[matches[0]]
    # get index of the first row whose title matches this best title
    idx_list = items.index[items["title"] == best_title].tolist()
    if not idx_list:
        return None, None

    return idx_list[0], best_title


# ----------------------------
# Recommendation
# ----------------------------

def recommend_content(items: pd.DataFrame, matrix, *, item_index: int, topn: int = 5) -> pd.DataFrame:
    """
    Given a row index and TF-IDF matrix, return top-N similar items
    with a similarity_score column.
    """
    # Compute cosine similarity between this item and all others
    cosine_sim = linear_kernel(matrix[item_index:item_index + 1], matrix).flatten()

    # Get indices sorted by similarity (highest first)
    indices = cosine_sim.argsort()[::-1]

    # Remove the item itself
    indices = [i for i in indices if i != item_index]

    # Take top-N
    indices = indices[:topn]

    # Build result table
    result = items.iloc[indices][["item_id", "title", "genres"]].copy()
    result["similarity_score"] = [round(float(cosine_sim[i]), 3) for i in indices]

    # Reorder columns for nicer display
    result = result[["item_id", "title", "genres", "similarity_score"]]

    return result
