import streamlit as st
import random

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
        "Next Question": "Siguiente pregunta",
        "quiz_choices": {
            "Manifest Destiny": [
                "Justific\u00f3 la expansi\u00f3n hacia el oeste y el crecimiento territorial.",
                "Llev\u00f3 a la creaci\u00f3n de colonias europeas en los EE.UU.",
                "Caus\u00f3 que los EE.UU. abandonaran tierras en el Oeste.",
                "Solo se trataba del comercio entre estados."
            ],
            "Urbanization": [
                "Caus\u00f3 que las \u00e1reas rurales crecieran en poblaci\u00f3n.",
                "Cre\u00f3 grandes cambios en los m\u00e9todos de agricultura.",
                "Condujo al crecimiento de ciudades por el desarrollo industrial.",
                "Se trataba de expandir los ferrocarriles al sur."
            ]
        }
    },
    "French": {
        "Try to define this word in your own words!": "Essayez de d\u00e9finir ce mot avec vos propres mots !",
        "Why do you think": "Pourquoi pensez-vous que",
        "was important in U.S. history?": "\u00e9tait important dans l'histoire des \u00c9tats-Unis ?",
        "Choose the best answer:": "Choisissez la meilleure r\u00e9ponse :",
        "Great job! That's the correct answer.": "Bravo ! C'est la bonne r\u00e9ponse.",
        "Not quite—try reviewing the vocabulary and guided question again.": "Pas tout \u00e0 fait. Essayez de revoir le vocabulaire et la question guid\u00e9e.",
        "Ready for another question? Click below!": "Pr\u00eat pour une autre question ? Cliquez ci-dessous !",
        "Next Question": "Question suivante",
        "quiz_choices": {
            "Manifest Destiny": [
                "Elle justifiait l'expansion vers l'ouest et la croissance territoriale.",
                "Elle a men\u00e9 \u00e0 la cr\u00e9ation de colonies europ\u00e9ennes aux \u00c9tats-Unis.",
                "Elle a pouss\u00e9 les \u00c9tats-Unis \u00e0 abandonner des terres dans l'Ouest.",
                "Elle concernait uniquement le commerce entre \u00c9tats."
            ],
            "Urbanization": [
                "Elle a fait cro\u00eetre la population des zones rurales.",
                "Elle a cr\u00e9\u00e9 d'importants changements dans les m\u00e9thodes agricoles.",
                "Elle a entra\u00een\u00e9 la croissance des villes gr\u00e2ce \u00e0 l'industrialisation.",
                "Elle concernait l'expansion des chemins de fer vers le sud."
            ]
        }
    }
}

def t(text, lang):
    return translations.get(lang, {}).get(text, text)

# Sample data with placeholder for map/image/graph
image_map = {
    "Manifest Destiny": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Manifest_Destiny.jpg/640px-Manifest_Destiny.jpg",
    "Urbanization": "https://upload.wikimedia.org/wikipedia/commons/8/89/New_York_Times_building_and_factory_workers.jpg"
}

primary_sources = {
    "Manifest Destiny": "\"It is our manifest destiny to overspread the continent allotted by Providence.\" — John L. O'Sullivan, 1845",
    "Urbanization": "\"Cities grew rapidly as factories attracted workers from rural areas.\" — 19th Century Textbook"
}

# Sample topics
topics = [
    {
        "TEKS": "1(A)",
        "Topic": "Manifest Destiny",
        "Vocabulary": ["expansion", "territory"],
        "Guided Question": "Why do you think 'Manifest Destiny' was important in U.S. history?",
        "Quiz": {
            "question": "What is the significance of 'Manifest Destiny' in U.S. history?",
            "choices": [
                "It justified westward expansion and territorial growth.",
                "It led to the creation of European colonies in the U.S.",
                "It caused the U.S. to abandon land in the West.",
                "It was only about trade between states."
            ],
            "correct": 0
        }
    },
    {
        "TEKS": "3(B)",
        "Topic": "Urbanization",
        "Vocabulary": ["cities", "factories"],
        "Guided Question": "Why do you think 'Urbanization' was important in U.S. history?",
        "Quiz": {
            "question": "What is the significance of 'Urbanization' in U.S. history?",
            "choices": [
                "It caused rural areas to grow in population.",
                "It created major changes in farming methods.",
                "It led to the rise of cities due to industrial growth.",
                "It was about expanding railroads into the South."
            ],
            "correct": 2
        }
    }
]

# UI
st.title("STAAR Study Agent 🤖")
st.write("Let's get ready for the 8th Grade Social Studies STAAR!")

# Language selection
language = st.radio("Which language would you prefer to use for your study session?", ["English", "Spanish", "French"])

# Add a session state to track question refresh
if 'refresh' not in st.session_state:
    st.session_state.refresh = True

# Pick a topic
topic = random.choice(topics)
st.header(f"Topic: {topic['Topic']} ({topic['TEKS']})")

# Display map/image if available
if topic['Topic'] in image_map:
    st.image(image_map[topic['Topic']], caption=f"Map or Image related to {topic['Topic']}", use_container_width=True)

# Display primary source
if topic['Topic'] in primary_sources:
    st.markdown(f"**Primary Source Excerpt:**\n\n> {primary_sources[topic['Topic']]}")

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

if language in translations and 'quiz_choices' in translations[language]:
    translated_choices = translations[language]['quiz_choices'].get(topic['Topic'])
    if translated_choices:
        quiz_choices = translated_choices

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

# Move next button below the quiz
if st.button(t("Next Question", language)):
    st.session_state.refresh = not st.session_state.refresh

st.info(t("Ready for another question? Click below!", language))