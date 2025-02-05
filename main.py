import streamlit as st
import requests
# Streamlit UI
st.set_page_config(page_title="News App", layout="wide")


st.title("📰 Latest News App")
url = "https://newsapi.org/v2/everything?q=india&"\
      "from=2025-01-05&sortBy=yournews.orgapi"
request = requests.get(url)
content = request.json()

# Display News Articles
st.write("### Top Headlines")

for article in content['articles']:
    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(article["urlToImage"], width=150)
        with col2:
            st.subheader(article["title"])
            st.write(article["description"])
        st.divider()
