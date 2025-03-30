import streamlit as st
import random
import json
import os

# Load topic data from JSON file with basic validation
DATA_FILE = "staar_topics_streamlit.json"

if not os.path.exists(DATA_FILE):
    st.error("Topic data file not found. Please check the file path.")
    st.stop()

try:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        topics = json.load(f)

    # Validate structure of topics
    required_keys = {"TEKS", "Topic", "Vocabulary", "Guided Question", "Quiz"}
    quiz_keys = {"question", "choices", "correct"}
    for topic in topics:
        if not required_keys.issubset(topic):
            raise ValueError("Topic entry missing required keys.")
        if not quiz_keys.issubset(topic["Quiz"]):
            raise ValueError("Quiz entry missing required fields.")
except (json.JSONDecodeError, ValueError) as e:
    st.error(f"Error loading topic data: {e}")
    st.stop()

# Simple translation dictionary
translations = {
    "Spanish": {
        "Try to define this word in your own words!": "\u00a1Intenta definir esta palabra con tus propias palabras!",
        "Why do you think": "\u00bfPor qu\u00e9 crees que",
        "was important in U.S. history?": "fue importante en la historia de EE.UU.?",
        "Choose the best answer:": "Elige la mejor respuesta:",
        "Great job! That's the correct answer.": "\u00a1Buen trabajo! Esa es la respuesta correcta.",
        "Not quite—try reviewing the vocabulary and guided question again.": "No exactamente. Revisa el vocabulario y la pregunta guiada nuevamente.",
        "Ready for another question? Click below!": "\u00a1Listo para otra pregunta? \u00a1Haz clic abajo!",
        "Next Question": "Siguiente pregunta"
    },
    "French": {
        "Try to define this word in your own words!": "Essayez de d\u00e9finir ce mot avec vos propres mots !",
        "Why do you think": "Pourquoi pensez-vous que",
        "was important in U.S. history?": "\u00e9tait important dans l'histoire des \u00c9tats-Unis ?",
        "Choose the best answer:": "Choisissez la meilleure r\u00e9ponse :",
        "Great job! That's the correct answer.": "Bravo ! C'est la bonne r\u00e9ponse.",
        "Not quite—try reviewing the vocabulary and guided question again.": "Pas tout \u00e0 fait. Essayez de revoir le vocabulaire et la question guid\u00e9e.",
        "Ready for another question? Click below!": "Pr\u00eat pour une autre question ? Cliquez ci-dessous !",
        "Next Question": "Question suivante"
    }
}

def t(text, lang):
    return translations.get(lang, {}).get(text, text)

# UI
st.title("STAAR Study Agent 🤖")
st.write("Let's get ready for the 8th Grade Social Studies STAAR!")

# Language selection
language = st.radio("Which language would you prefer to use for your study session?", ["English", "Spanish", "French"])

# Session state for topic index
if 'topic_index' not in st.session_state:
    st.session_state.topic_index = random.randint(0, len(topics) - 1)

if st.button(t("Next Question", language)):
    st.session_state.topic_index = random.randint(0, len(topics) - 1)

# Load current topic
topic = topics[st.session_state.topic_index]
st.header(f"Topic: {topic['Topic']} ({topic['TEKS']})")

# Vocabulary
st.subheader("🧠 Vocabulary Time")
for word in topic['Vocabulary']:
    st.write(f"- **{word}**: {t('Try to define this word in your own words!', language)}")

# Guided Question
st.subheader("💬 Let's Think About This")
question_text = topic['Guided Question']
if language != "English":
    question_text = question_text.replace("Why do you think", t("Why do you think", language))
    question_text = question_text.replace("was important in U.S. history?", t("was important in U.S. history?", language))

st.write(question_text)
student_response = st.text_input("Your thoughts:")

# Quiz
st.subheader("✅ Quick Quiz")
quiz = topic['Quiz']
quiz_question = quiz['question']
quiz_choices = quiz['choices']

if language != "English":
    quiz_question = quiz_question.replace("What is the significance of", t("Why do you think", language))
    quiz_question = quiz_question.replace("in U.S. history?", t("was important in U.S. history?", language))

st.write(quiz_question)
choice = st.radio(t("Choose the best answer:", language), quiz_choices)

if st.button("Submit Answer"):
    if quiz_choices.index(choice) == quiz['correct']:
        st.success(t("Great job! That's the correct answer.", language) + " 🎉")
    else:
        st.error(t("Not quite—try reviewing the vocabulary and guided question again.", language))

st.info(t("Ready for another question? Click below!", language))
