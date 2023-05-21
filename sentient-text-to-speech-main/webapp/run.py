import streamlit as st
import pyttsx3
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

with open('te.pkl', 'rb') as f:
    model = pickle.load(f)

def decode_sentiment(score, include_neutral=True):
    HAPPY = "happy"
    SAD = "sad"
    ANGRY = "angry"
    if score == 1 or score == 3:
        label = "SAD"
    elif score == 2:
        label = "HAPPY"
    elif score == 4:
        label = "ANGRY"

    return lable;    
    


   
    
def predict(text, include_neutral=True):
    x_test = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=300)
    score = model.predict([x_test])[0]
    label = decode_sentiment(score, include_neutral=include_neutral)
    return label

def convert_to_audio(text, emotion=None, gender="female"):
    engine = pyttsx3.init()

    if emotion is None:
        emotion = predict(text)

    # Set voice properties based on emotion and gender
    if gender == "female":
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    else:  # male
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')

    # Adjust speech rate, volume, and pitch based on emotion
    if emotion == "happy":
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1)
        engine.setProperty('pitch', 1.2)
    elif emotion == "sad":
        engine.setProperty('rate', 90)
        engine.setProperty('volume', 0.6)
        engine.setProperty('pitch', 0.7)
    elif emotion == "love":
        engine.setProperty('rate', 90)
        engine.setProperty('volume', 0.6)
        engine.setProperty('pitch', 0.7)
    elif emotion == "angery":
        engine.setProperty('rate', 90)
        engine.setProperty('volume', 0.6)
        engine.setProperty('pitch', 0.7)        
    

    engine.say(text)
    engine.runAndWait()


# Set up the app layout and styling
st.set_page_config(page_title="Emotion-Based TTS", page_icon=":microphone:", layout="centered", initial_sidebar_state="expanded")
st.markdown('<style>body{background-color: #F0F2F6;}h1{color: #1F2937;}</style>', unsafe_allow_html=True)

# App title
st.title('Emotion-Based Text-to-Speech :microphone:')

# Text input
text = st.text_area("Enter your text:", height=100)

# Gender and emotion selection
col1, col2 = st.columns(2)
gender = col1.selectbox("Select voice gender:", ["female", "male"])
emotion = col2.selectbox("Select emotion (optional):", ["auto", "happy", "angry", "sad", "love"])

# Convert to audio button
if st.button("Convert to audio"):
    if emotion == "":
        emotion = None

    convert_to_audio(text, emotion, gender)

# App description and instructions
st.markdown("""
## :information_source: About the app

This app converts the input text to speech based on the selected gender and emotion. If no emotion is selected, the app will automatically detect the emotion from the text.

## :arrow_forward: How to use

1. Enter your text in the provided text box.
2. Select the desired voice gender (female or male).
3. Optionally, select an emotion (happy, sad, or neutral). If you leave it blank, the app will auto-detect the emotion.
4. Click on the "Convert to audio" button to listen to the synthesized speech.
""")
