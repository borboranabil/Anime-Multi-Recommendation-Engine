<p align="center">
  <img src="docs/banner.png" alt="Otaku Recommender Banner" width="100%">
</p>

<h1 align="center">Otaku Recommender — Full-Stack AI Engine</h1>

<p align="center">
  AI-powered recommendations for Anime, Manga, and Manhwa  
  <br>
  Semantic Search • TF-IDF • Live Web Mode • FastAPI • React
</p>

<p align="center">

  <!-- Status Badges -->
  <img src="https://img.shields.io/badge/Frontend-Vercel-black?style=for-the-badge&logo=vercel" />
  <img src="https://img.shields.io/badge/Backend-Render-blue?style=for-the-badge&logo=render" />
  <img src="https://img.shields.io/badge/FastAPI-0.104.1-009485?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/React-18-blue?style=for-the-badge&logo=react" />
  <img src="https://img.shields.io/badge/TF--IDF-ML%20Engine-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />

</p>

---

# Otaku Recommender - Full-Stack AI Engine

> A next-gen recommendation system for **Anime, Manga, and Manhwa**.  
> Powered by **TF-IDF + Semantic Text Search + Live Web Mode (Jikan API)** using **FastAPI** and **React**.

[Live Demo (Frontend - Vercel)](https://anime-multi-recommendation-engine.vercel.app)  
[Backend API (Render)](https://anime-recommender-i8w3.onrender.com)

---

## ✨ What makes this special?

Unlike traditional recommendation systems, **Otaku Recommender is “alive”** — it understands:

✔ Title-based searches  
✔ Natural-language semantic searches (“samurai revenge tragedy”)  
✔ Unknown titles using live internet fallback  

### 1️⃣ Smart TF-IDF Brain  
Uses TF-IDF over `title + genres + description` to compute similarity by *vibe*, not just keywords.

### 2️⃣ Semantic Text Mode (NEW)  
If the user types a **descriptive prompt**:

sad story about a pianist
dark psychological thriller
samurai revenge tragedy
wholesome romance with comedy

yaml
Copy code

The engine treats the text as a **semantic description** and performs TF-IDF similarity on the entire dataset.

⚡ No API needed  
⚡ Works for ANY descriptive text  
⚡ Incredibly light and fast  

### 3️⃣ Live Web Fallback (Jikan API)  
If the query:

- does **not** exist in the dataset  
- AND looks like a title  
- AND semantic mode is ON  

The backend fetches:

- title  
- genres  
- synopsis  

from **MyAnimeList (via Jikan API)** and uses it to build similarity recommendations.

### 4️⃣ Multi-Media Support  
Separate universes for **Anime**, **Manga**, and **Manhwa**.

### 5️⃣ Infinite Discovery UI  
Click any card → instantly pivot recommendations to that title.

### 6️⃣ Trailer Button  
Jump straight to YouTube trailers.

---

# 🌟 Showcase — Smart Semantic Search in Action

Here are real screenshots from the deployed system:

---

## 🏠 1. Clean & Modern Homepage UI

<p align="center">
  <img src="docs/screenshot-home.png" width="85%" />
</p>

Features:

- Anime / Manga / Manhwa selector  
- Keyword vs Semantic toggle  
- Smooth animations  
- Fully responsive dark mode UI  

---

## 🗡️ 2. Semantic Query — *“samurai revenge tragedy”*

<p align="center">
  <img src="docs/screenshot-samurai.png" width="85%" />
</p>

Why this works:

- Identifies concepts like **samurai**, **revenge**, **tragedy**, **violence**, **historical tone**  
- Returns anime with similar emotional and thematic patterns  
- No embeddings, no GPU — just smart TF-IDF content matching

---

## 🧠 3. Semantic Query — *“dark psychological thriller”*

<p align="center">
  <img src="docs/screenshot-psychological.png" width="85%" />
</p>

Matches include:

- Psychological tension  
- Thriller structure  
- Dark themes  
- Mind games / horror elements  

This perfectly demonstrates the accuracy of TF-IDF semantic searching.

---

# 🧠 Tech Stack

### Frontend
- React (Vite)
- Tailwind CSS
- Framer Motion
- Lucide Icons
- Hosted on **Vercel**

### Backend
- Python + FastAPI
- TF-IDF vectorization (scikit-learn)
- Cosine similarity engine
- Jikan API for fallback search
- Hosted on **Render**

> ⚠️ This version does **NOT** use Sentence-BERT.  
> It is optimized for TF-IDF + smart query handling to run on low-RAM hosting (Render free tier).

---

# 🚀 How to Run Locally

## 1️⃣ Backend Setup (Python)

```bash
python -m venv .venv
source .venv/bin/activate         # Windows: .venv\Scripts\activate

pip install -r requirements.txt

uvicorn api:app --reload
Backend runs at:

cpp
Copy code
http://127.0.0.1:8000
Useful Endpoints
Endpoint	Description
/health	Health check
/recommend	Main recommendation endpoint
/docs	Swagger docs

Example:

bash
Copy code
curl "http://127.0.0.1:8000/recommend?media_type=anime&query=naruto&topn=5&use_smart_search=true"
2️⃣ Frontend Setup (React)
bash
Copy code
cd frontend
npm install
npm run dev
Frontend:

arduino
Copy code
http://localhost:5173
To use local backend, edit:

js
Copy code
const BACKEND_URL = "http://127.0.0.1:8000";
🧬 Project Structure
arduino
Copy code
Otaku-Recommender/
├── api.py                 
├── recommender.py         
├── data/                  
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── main.jsx
│   └── tailwind.config.js
├── docs/                  # screenshots for README
└── README.md
🔍 Recommendation Logic (Final Version)
✔ 1. Local Title Match
Exact or substring match in CSV

Uses TF-IDF similarity

Label: TF-IDF (Local Title Match)

✔ 2. Semantic Text Mode (Descriptive Prompts)
Triggered when:

Query is long / descriptive

AND not a known title

Engine:

Treats the prompt as a semantic description

Computes TF-IDF similarity

No API needed

Label: TF-IDF (Semantic Text Mode)

✔ 3. Live Web Mode (Unknown Titles)
Triggered when:

Query looks like a title

AND not found in local CSV

AND semantic mode ON

Engine:

Fetches plot + genres from Jikan

Builds synthetic content block

TF-IDF similarity

Label: TF-IDF (Live Web Mode)

✔ 4. Smart Mode OFF
If semantic mode = OFF and title not found → return a clear 404 message.

🛣 Roadmap
User accounts + favourites

Collaborative filtering

Mood-based search (happy, dark, wholesome)

Badge-based genre clustering

Anime detail pages

📜 License
MIT License — free for personal and commercial use.

🙌 Credits
Built with ❤️ by borboranabil
Powered by FastAPI, React, TF-IDF, and Jikan API
