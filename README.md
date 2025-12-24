🎓 Smart Learning Recommender Chatbot



A Streamlit-based intelligent chatbot that recommends high-quality YouTube tutorials using:



YouTube Data API



Semantic search (embeddings)



Ranking algorithm (relevance + popularity)



Streamlit chat-style UI



This is the intermediate version of the project — combining API calls + ML embeddings + clean UI.



🚀 Features



✔ Search YouTube tutorials automatically

✔ Uses semantic understanding (not just keywords)

✔ Scores videos based on meaning + view count

✔ Shows clean UI with thumbnails \& descriptions

✔ Chat interface using Streamlit

✔ Short summary for the user

✔ Beginner-friendly setup



🧠 How It Works (Overview)

User Query

&nbsp;   ↓

Embedding Model (SentenceTransformer)

&nbsp;   ↓

YouTube API Search (Top 5 videos)

&nbsp;   ↓

Scoring Algorithm:

&nbsp;     - Semantic Similarity (70%)

&nbsp;     - View Count Score (30%)

&nbsp;   ↓

Ranked Recommendations

&nbsp;   ↓

Streamlit UI Display (Thumbnails + Title + Description)





This makes the system smarter than simple search.



📁 Project Structure

smart-recommender/

│── app.py                 # Streamlit UI

│── backend.py             # API + ranking logic

│── embeddings.py          # Embedding model + similarity

│── requirements.txt       # Dependencies

└── README.md              # Documentation



🔧 Installation \& Setup (Step-by-Step)

1️⃣ Clone the Repository

git clone https://github.com/yourusername/smart-recommender.git

cd smart-recommender



2️⃣ Create Virtual Environment (Recommended)

python -m venv venv

venv\\Scripts\\activate



3️⃣ Install Dependencies

pip install -r requirements.txt





If sentence-transformers fails, install manually:



pip install sentence-transformers



🔑 4️⃣ Get YouTube API Key (IMPORTANT)



Follow these exact steps:



Step A — Go to Google Cloud Console



https://console.cloud.google.com/



Step B — Create a Project



smart-recommender



Step C — Enable API

APIs \& Services → Library → YouTube Data API v3 → Enable



Step D — Create API Key

APIs \& Services → Credentials → Create Credentials → API Key



Step E — Restrict Key



Restrict to:



YouTube Data API v3



Step F — Paste into backend.py

API\_KEY = "YOUR\_API\_KEY\_HERE"



▶️ 5️⃣ Run the App

streamlit run app.py





Your browser will open with the chatbot UI.



🧪 Usage

Example Queries:



“machine learning basics”



“python chatbot tutorial”



“deep learning course beginners”



“HTML CSS crash course”



The app will show:



Top 3 ranked videos



Thumbnails



Titles + links



Description snippet



Relevance score



🧠 Technical Details

1\. Embeddings Model



Uses:



all-MiniLM-L6-v2 (SentenceTransformers)





This captures semantic meaning.



2\. Ranking Algorithm

final\_score = (0.7 \* embedding\_similarity) + (0.3 \* view\_score)



Why this matters:



You don’t rely only on keywords



High-view videos get slight priority



Relevance is still the main factor



3\. View Score Calculation

view\_score = log10(views + 1) / 7





Prevents huge channels from dominating.



🎨 UI Features



Chat-style input (st.chat\_input)



Video cards (thumbnail + info)



Streamlit columns layout



Spinner while fetching results



Auto summary



🛠 requirements.txt

streamlit

requests

sentence-transformers

numpy

