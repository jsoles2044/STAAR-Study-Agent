
import streamlit as st
import random
import json
import os

# Dynamically determine file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "staar_topics_streamlit.json")

# Check if file exists
if not os.path.isfile(DATA_FILE):
    st.error(f"Topic data file '{DATA_FILE}' not found.")
    st.stop()

with open(DATA_FILE, "r", encoding="utf-8") as f:
    topics = json.load(f)

st.title("STAAR Study Agent 🤖")
st.write("Let’s get ready for the 8th Grade Social Studies STAAR!")

language = st.radio("Which language would you prefer to use for your study session?", ["English", "Spanish", "French"])

if 'topic_index' not in st.session_state:
    st.session_state.topic_index = random.randint(0, len(topics) - 1)

topic = topics[st.session_state.topic_index]
st.header(f"Topic: {topic['Topic']} ({topic['TEKS']})")

# Vocabulary
st.subheader("🧠 Vocabulary Time")
for word in topic['Vocabulary']:
    st.write(f"- **{word}**: Try to define this word in your own words!")

# Guided Question
st.subheader("💬 Let's Think About This")
st.write(topic['Guided Question'])
student_response = st.text_input("Your thoughts:")

# Quiz
st.subheader("✅ Quick Quiz")
quiz = topic['Quiz']
question = quiz['question']
choices = quiz['choices']
correct_index = quiz['correct']

# Randomize choices and keep track of correct answer
if 'shuffled_choices' not in st.session_state or st.session_state.get('shuffled_topic') != topic['Topic']:
    paired_choices = list(enumerate(choices))
    random.shuffle(paired_choices)
    st.session_state.shuffled_choices = [c for _, c in paired_choices]
    st.session_state.correct_answer = choices[correct_index]
    st.session_state.shuffled_topic = topic['Topic']

selected = st.radio(question, st.session_state.shuffled_choices)

if st.button("Submit Answer"):
    if selected == st.session_state.correct_answer:
        st.success("Great job! That's the correct answer. 🎉")
    else:
        st.error("Not quite—try reviewing the vocabulary and guided question again.")

st.info("Ready for another question? Click below!")
if st.button("Next Question"):
    st.session_state.topic_index = random.randint(0, len(topics) - 1)
    for key in ['shuffled_choices', 'shuffled_topic', 'correct_answer']:
        st.session_state.pop(key, None)
    st.experimental_rerun()
