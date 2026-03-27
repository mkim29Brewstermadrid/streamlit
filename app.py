import streamlit as st
import random

st.title("✂️ Rock Paper Scissors 🪨")
st.write("Choose your weapon!")

EMOJIS = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}
WINS_AGAINST = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

if "user_choice" not in st.session_state:
    st.session_state.user_choice = None
if "computer_choice" not in st.session_state:
    st.session_state.computer_choice = None

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🪨\nRock", use_container_width=True):
        st.session_state.user_choice = "Rock"
        st.session_state.computer_choice = random.choice(list(EMOJIS.keys()))
with col2:
    if st.button("📄\nPaper", use_container_width=True):
        st.session_state.user_choice = "Paper"
        st.session_state.computer_choice = random.choice(list(EMOJIS.keys()))
with col3:
    if st.button("✂️\nScissors", use_container_width=True):
        st.session_state.user_choice = "Scissors"
        st.session_state.computer_choice = random.choice(list(EMOJIS.keys()))

user_choice = st.session_state.user_choice
computer_choice = st.session_state.computer_choice

if user_choice and computer_choice:
    st.markdown("---")
    col_you, col_vs, col_cpu = st.columns([2, 1, 2])
    with col_you:
        st.metric("You chose", EMOJIS[user_choice])
    with col_vs:
        st.markdown(
            "<h2 style='text-align:center;margin-top:20px'>VS</h2>",
            unsafe_allow_html=True,
        )
    with col_cpu:
        st.metric("Computer chose", EMOJIS[computer_choice])

    st.markdown("---")
    if user_choice == computer_choice:
        st.info("🤝 It's a tie! Try again.")
    elif WINS_AGAINST[user_choice] == computer_choice:
        st.success(f"🎉 You win! {EMOJIS[user_choice]} beats {EMOJIS[computer_choice]}")
    else:
        st.error(f"😢 You lose! {EMOJIS[computer_choice]} beats {EMOJIS[user_choice]}")
