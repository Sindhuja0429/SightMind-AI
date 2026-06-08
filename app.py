import streamlit as st
import google.api_core.exceptions as google_exceptions
from google import genai
from PIL import Image
from gtts import gTTS
import io
import os

# Page setup
st.set_page_config(page_title="SightMind AI Assistant", page_icon="👁️", layout="centered")
st.title("👁️ SightMind AI Vision Assistant")
st.caption("A real-time multimodal application parsing environmental data into speech.")
st.write("---")

# Retrieve API Key securely from system environment or Streamlit Secrets
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    with st.sidebar:
        st.header("🔑 Authentication Setup")
        api_key = st.text_input("Enter Gemini API Key", type="password")
        st.markdown("[Get a Free Key Here](https://aistudio.google.com/)")

if not api_key:
    st.info("Please add your Gemini API Key in the sidebar to get started.", icon="🔒")
    st.stop()

# Initialize Client
@st.cache_resource
def get_ai_client(key: str):
    return genai.Client(api_key=key)

client = get_ai_client(api_key)

st.subheader("1. Stream Live Visual Input")
camera_feed = st.camera_input("Snap a photo of an object or text")

if camera_feed:
    pil_image = Image.open(camera_feed)
    st.image(pil_image, caption="Buffered Frame Preview", use_container_width=True)
    
    st.subheader("2. Real-Time Processing")
    
    with st.spinner("Executing multimodal analysis..."):
        prompt_directive = "Analyze the image and provide an accessible description. Include any visible text."
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=[prompt_directive, pil_image]
            )
            
            analysis_text = response.text

            st.success("Analysis Complete!")
            st.markdown(f"***AI Vision Output:***\n\n{analysis_text}")

            # Text-To-Speech Generation
            with st.spinner("Synthesizing audio..."):
                tts = gTTS(text=analysis_text, lang='en', tld='com')
                audio_buffer = io.BytesIO()
                tts.write_to_fp(audio_buffer)
                audio_buffer.seek(0)
            
            # Audio Player Interface Layout
            st.write("🔊 **Listen to Audio Description:**")
            st.audio(audio_buffer, format="audio/mp3", autoplay=True)

        except google_exceptions.ResourceExhausted:
            st.error("⚠️ **API Rate Limit Reached (Error 429):** The free tier of the Gemini API is temporarily restricted due to too many requests. Please wait a minute and click 'Take Photo' again.")

        except google_exceptions.ServiceUnavailable:
            st.error("🚦 **Google Servers Busy (Error 503):** Google's servers are experiencing high demand right now. Let's try sending the request again in a few moments.")

        except Exception as e:
            st.error(f"Something unexpected occurred: {e}")