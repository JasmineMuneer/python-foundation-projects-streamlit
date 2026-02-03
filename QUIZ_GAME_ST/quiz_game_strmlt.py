import streamlit as st
import dependencies as dp

st.title("The Guessing Game")

st.divider()

st.caption("Rule(s):"
            "\n1. Each question carries 1 mark"
            "\n2. No negative marks" \
            "\n3. You can view your total mark only at the end of the game")

st.divider()

with st.form("quiz_details"):
    topic = st.text_input("**Topic**", placeholder="Eg. Sky")
    num = st.number_input("**No. of questions**", min_value=5, max_value=25, 
                    placeholder="5-25", value=None)
    diff_level = st.select_slider("Difficulty level", options=["Easy", "Medium", "Hard"], value="Medium").lower()
    submitted = st.form_submit_button("Submit", type="secondary")

if submitted:
        questions = dp.generate_questions(num, topic, diff_level)
        st.write(questions)

        if questions == False:
              backup_ques = dp.backup_questions()
              st.write(backup_ques)