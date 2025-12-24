import requests
import numpy as np
from embeddings import get_embedding, cosine_similarity

API_KEY = "AIzaSyANMiV57BQcdg5ChW7SPP83nEBbiXiznI4"
SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
VIDEO_DETAILS_URL = "https://www.googleapis.com/youtube/v3/videos"

def search_youtube(query):
    params = {
        "part": "snippet",
        "q": query,
        "maxResults": 5,
        "type": "video",
        "key": API_KEY
    }
    response = requests.get(SEARCH_URL, params=params).json()
    return response.get("items", [])

def get_video_stats(video_ids):
    params = {
        "part": "statistics",
        "id": ",".join(video_ids),
        "key": API_KEY
    }
    response = requests.get(VIDEO_DETAILS_URL, params=params).json()
    stats = {}

    for item in response.get("items", []):
        vid = item["id"]
        stats[vid] = int(item["statistics"].get("viewCount", 0))

    return stats

def rank_videos(query, items):
    query_emb = get_embedding(query)
    
    video_ids = [item["id"]["videoId"] for item in items]
    stats = get_video_stats(video_ids)

    ranked = []
    for item in items:
        vid = item["id"]["videoId"]
        title = item["snippet"]["title"]
        description = item["snippet"]["description"]

        text = title + " " + description
        text_emb = get_embedding(text)

        similarity = cosine_similarity(query_emb, text_emb)
        views = stats.get(vid, 0)

        view_score = np.log10(views + 1) / 7  # normalize
        
        final_score = (0.7 * similarity) + (0.3 * view_score)

        ranked.append({
            "id": vid,
            "title": title,
            "thumbnail": item["snippet"]["thumbnails"]["high"]["url"],
            "link": f"https://www.youtube.com/watch?v={vid}",
            "description": description,
            "score": final_score
        })

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked
