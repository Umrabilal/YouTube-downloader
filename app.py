import streamlit as st
from pytube import YouTube
from PIL import Image
import requests
from io import BytesIO
import re

st.set_page_config(page_title="YouTube Downloader", layout="centered")
st.title("📥 YouTube Downloader")
st.write("Paste a valid YouTube link below and choose a format to download.")

# Regex pattern to validate YouTube URLs
yt_pattern = re.compile(
    r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)[\w-]{11}'
)

url = st.text_input("🔗 Enter YouTube Video URL:")

def is_valid_youtube_url(link):
    return yt_pattern.match(link)

if url:
    if is_valid_youtube_url(url):
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
            st.error(f"⚠️ Something went wrong while processing the video.\nDetails: {e}")
    else:
        st.warning("⚠️ Please enter a valid YouTube video link.")