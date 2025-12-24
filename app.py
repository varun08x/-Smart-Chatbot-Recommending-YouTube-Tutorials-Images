import streamlit as st
from backend import search_youtube, rank_videos

st.set_page_config(page_title="Smart Learning Recommender", layout="wide")

st.title("🎓 Smart Learning Recommender (Intermediate Version)")
st.write("Get smarter recommendations powered by semantic search + ranking.")

query = st.chat_input("Ask for tutorials… (e.g., 'machine learning basics')")

if query:
    with st.chat_message("user"):
        st.write(query)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing and fetching results…"):
            items = search_youtube(query)
            ranked = rank_videos(query, items)

        st.subheader("Top Recommendations")

        for video in ranked[:3]:
            col1, col2 = st.columns([1, 3])

            with col1:
                st.image(video["thumbnail"])

            with col2:
                st.markdown(f"### [{video['title']}]({video['link']})")
                st.write(video["description"][:200] + "...")
                st.write(f"**Score:** {video['score']:.2f}")
