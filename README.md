# 👁️ SightMind AI Vision Assistant

A live computer vision application that captures frames from a webcam feed, processes the data using a Multimodal Large Language Model, and outputs both text analysis and synthesized speech.

## 🚀 Features
- **Live Webcam Integration:** Captures immediate image buffer frames using Streamlit components.
- **Multimodal AI Engine:** Uses Google Gemini 2.5 Flash to identify objects, read text, and interpret context.
- **Voice Synthesis:** Automatically converts textual analysis into clean, spoken audio.

## 🛠️ Tech Stack
- **Language:** Python
- **AI Core:** Google GenAI SDK (Gemini API)
- **Frontend Panel:** Streamlit Framework
- **Audio Output:** gTTS (Google Text-to-Speech)

## 📦 Local Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/Sindhuja0429/SightMind-AI.git](https://github.com/Sindhuja0429/SightMind-AI.git)
   ### 🔑 Setup API Key
To run this project, you need a Gemini API key from Google AI Studio. 
1. Get a free key at [Google AI Studio](https://aistudio.google.com/).
2. Create a `.env` file in the root directory.
3. Add your key like this: `GEMINI_API_KEY="your_api_key_here"`

## 🛠️ Requirements & Dependencies
This project relies on the following Python packages:
- **Streamlit**: For the web interface and live camera input.
- **google-genai**: To communicate with the Gemini 2.5 Flash multimodal model.
- **Pillow (PIL)**: For decoding and processing the camera's image buffer.
- **gTTS**: For converting the AI's text insights into spoken audio.

To install them all at once, run:
```bash
pip install -r requirements.txt
