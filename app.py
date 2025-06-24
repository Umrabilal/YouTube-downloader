import streamlit as st
from pytube import YouTube
from PIL import Image
import requests
from io import BytesIO
import os

st.set_page_config(page_title="YouTube Downloader", layout="centered")
st.title("📥 YouTube Downloader")
st.write("Paste a YouTube link below and choose format to download.")

url = st.text_input("🔗 Enter YouTube Video URL:")

if url:
    try:
        yt = YouTube(url)
        st.video(url)
        st.markdown(f"**🎞 Title:** {yt.title}")
        st.markdown(f"**📺 Channel:** {yt.author}")
        st.markdown(f"**⏱ Duration:** {yt.length // 60} min {yt.length % 60} sec")

        # Show thumbnail
        response = requests.get(yt.thumbnail_url)
        img = Image.open(BytesIO(response.content))
        st.image(img, caption="Thumbnail", use_column_width=True)

        option = st.radio("Select download format", ["📹 Video", "🎧 Audio Only"])

        if st.button("⬇️ Download"):
            st.info("⏳ Downloading... please wait.")
            if option == "📹 Video":
                stream = yt.streams.get_highest_resolution()
                stream.download()
                st.success("✅ Video downloaded successfully (on server).")
            else:
                audio_stream = yt.streams.filter(only_audio=True).first()
                audio_stream.download()
                st.success("✅ Audio downloaded successfully (on server).")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")