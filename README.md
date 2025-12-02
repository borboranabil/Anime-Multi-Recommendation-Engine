<p align="center">
  <img src="docs/banner.png" alt="Anime Recommendation Engine Banner" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Project-Anime%20%2F%20Manga%20%2F%20Manhwa%20Recommender-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/ML-Content--Based-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/github/license/borboranabil/Anime-Multi-Recommendation-Engine?style=for-the-badge"/>
</p>

# 🎌 Anime • Manga • Manhwa Multi-Recommendation Engine

A **content-based AI recommendation system** that can suggest similar titles from:

- 📺 **Anime**
- 📚 **Manga**
- 📙 **Manhwa (Korean Webtoons)**

The model uses **TF-IDF Vectorization** + **Cosine Similarity** on:
- titles  
- genres  
- descriptions  

This allows the engine to detect similarity between different works based only on their **content**, without ratings or user data.

---

## 🧭 Table of Contents

1. [Overview](#-overview)  
2. [Features](#-features)  
3. [Supported Datasets](#-supported-datasets)  
4. [Tech Stack](#-tech-stack)  
5. [Project Structure](#-project-structure)  
6. [How It Works](#-how-it-works)  
7. [How to Run](#-how-to-run)  
8. [Example Session](#-example-session)  
9. [Roadmap](#-roadmap)  
10. [License](#-license)  
11. [Acknowledgements](#-acknowledgements)

---

## 📌 Overview

This project implements a **multi-media content recommendation engine** as part of an AI/ML learning project.  
It supports three categories:

- **Anime**
- **Manga**
- **Manhwa**

The system recommends similar titles based on:
- Title keywords  
- Genre overlap  
- Plot description similarity  

It is fast ➝ simple ➝ expandable ➝ ideal for ML beginners and anime fans.

---

## ⭐ Features

- 🔍 **Content-Based Recommendations** using TF-IDF + cosine similarity  
- 📚 **Supports Anime, Manga, and Manhwa**  
- ⚡ **Fast lookup** thanks to precomputed matrices  
- 🧠 **Cleans & merges text fields** automatically  
- 🖥️ **Interactive CLI menu**  
- 🧩 **Modular design** (easy to extend or add new datasets)  
- 📂 **CSV-based datasets** for easy editing  

---

## 📂 Supported Datasets

All datasets are in `data/`:

| Type      | File              | Items |
|----------|-------------------|-------|
| Anime    | `anime.csv`       | 35+   |
| Manga    | `manga.csv`       | 35+   |
| Manhwa   | `manhwa.csv`      | 35+   |

Dataset schema:

item_id, title, genres, description

yaml
Copy code

Each row contains:

- **item_id** – unique numeric ID  
- **title** – name of the work  
- **genres** – pipe-separated tags (Action|Fantasy)  
- **description** – short plot summary  

---

## 🛠 Tech Stack

**Language:**  
- Python 3.x  

**Libraries:**  
- pandas  
- scikit-learn  
  - `TfidfVectorizer()`  
  - `linear_kernel()`  

**Environment:**  
- VS Code / any IDE  
- Git Bash / Terminal  

---

## 📁 Project Structure

Anime-Multi-Recommendation-Engine/
│
├── data/
│ ├── anime.csv
│ ├── manga.csv
│ └── manhwa.csv
│
├── docs/
│ ├── ARCHITECTURE.md
│ ├── QUICKSTART.md
│ └── banner.png
│
├── main.py
├── recommender.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

yaml
Copy code

---

## 🔬 How It Works

### **1️⃣ Mode selection (main.py)**
The user chooses:

1 → Anime
2 → Manga
3 → Manhwa

bash
Copy code

### **2️⃣ Load dataset**
Loads the correct CSV and creates a new text field:

```python
df["content"] = df["title"] + " " + df["genres"] + " " + df["description"]
3️⃣ Vectorization
Build TF-IDF matrix:

python
Copy code
TfidfVectorizer(stop_words="english")
4️⃣ Compute similarity
Using cosine similarity:

python
Copy code
linear_kernel(tfidf_matrix, tfidf_matrix)
5️⃣ Display recommendations
Sorted by similarity score.

🔧 How to Run
1️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
2️⃣ Run the engine
bash
Copy code
python main.py
3️⃣ Choose a category and get recommendations
🧪 Example Session
yaml
Copy code
=== Multi-Media Recommendation Engine ===
Select mode:
  1) Anime
  2) Manga
  3) Manhwa
Enter choice: 1

Loaded dataset: anime.csv

Available titles:
  1: Attack on Titan
  2: Naruto
  3: One Piece
  ...

Enter item_id: 1

Recommendations for: Attack on Titan
------------------------------------------------
9   Tokyo Ghoul
10  Tokyo Revengers
5   Demon Slayer
6   Jujutsu Kaisen
34  Idaten Deities Know Only Peace
🚀 Roadmap
🔧 Short-Term
Add 100+ entries per dataset

Clean genre tags

Add option for top-N recommendations

⚙️ Medium-Term
Integrate AniList / MAL / Webtoon APIs

Add title-based search

🧠 Long-Term
Build a Streamlit web UI

Add collaborative filtering

Use BERT / Sentence Transformers for semantic similarity

Deploy online

📝 License
Distributed under the MIT License.
See LICENSE for details.

🙌 Acknowledgements
Built as part of an AI/ML learning project

Inspired by modern recommendation systems

Uses Python’s scientific ecosystem

