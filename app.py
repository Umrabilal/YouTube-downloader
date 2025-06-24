
import streamlit as st
import yt_dlp
import os

st.title("📥 YouTube Video Downloader (yt_dlp)")
st.write("Paste a YouTube link below and download the video.")

# User input
url = st.text_input("🔗 Enter YouTube URL")

# Download button
if st.button("Download Video"):
    if url:
        try:
            st.info("⏳ Starting download...")

            ydl_opts = {
                'outtmpl': '%(title)s.%(ext)s',
                'quiet': True
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            st.success("✅ Video downloaded successfully!")

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
    else:
        st.warning("⚠️ Please paste a valid YouTube link.")
