import streamlit as st

# -------------------------
# Quiz Questions Data
# -------------------------
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which programming language is known as the language of the web?",
        "options": ["Python", "C++", "JavaScript", "Java"],
        "answer": "JavaScript"
    },
    {
        "question": "Who created Python?",
        "options": ["James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which company developed Java?",
        "options": ["Microsoft", "Apple", "Sun Microsystems", "Google"],
        "answer": "Sun Microsystems"
    }
]

# -------------------------
# Streamlit Page Config
# -------------------------
st.set_page_config(page_title="Quiz Game", page_icon="🎯", layout="centered")
st.title("🎯 Quiz Game App")
st.write("Answer the questions and test your knowledge!")

# -------------------------
# Session State
# -------------------------
if "score" not in st.session_state:
    st.session_state.score = 0
if "q_index" not in st.session_state:
    st.session_state.q_index = 0

# -------------------------
# Quiz Logic
# -------------------------
if st.session_state.q_index < len(quiz_data):
    q = quiz_data[st.session_state.q_index]

    st.subheader(f"Q{st.session_state.q_index+1}: {q['question']}")

    choice = st.radio("Choose your answer:", q["options"], key=st.session_state.q_index)

    if st.button("Submit Answer"):
        if choice == q["answer"]:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Wrong! Correct answer: {q['answer']}")

        st.session_state.q_index += 1
        st.experimental_rerun()

else:
    st.success(f"🎉 You finished the quiz! Final Score: {st.session_state.score}/{len(quiz_data)}")

    if st.session_state.score == len(quiz_data):
        st.balloons()

    if st.button("Restart Quiz"):
        st.session_state.score = 0
        st.session_state.q_index = 0
        st.experimental_rerun()
