import streamlit as st
import random
from PIL import Image

st.title("Unblocked Rock, Paper, Scissors Game")

# 1. Load images and define variables properly


# Using web URLs so you don't need local files
rock_url = "https://png.pngtree.com/png-clipart/20220824/ourmid/pngtree-cartoon-rock-transparent-png-image_6122807.png"
paper_url = "paper.png"
scissors_url = "https://images.vexels.com/media/users/3/256357/isolated/preview/2644fd66c3d4de114b00ea2e6a36dd62-scissors-playful-cartoon.png"

# Map choices directly to URLs
#{} are called dictionaries they are used in python to pair a key and value together.  
choices = {
    "Rock": rock_url,
    "Paper": paper_url,
    "Scissors": scissors_url
}


# In your st.image calls later, Streamlit handles URLs automatically:
# st.image(choices["Rock"], width=150)
st.write("### Choose your move:")

# 3. Use columns to create a clean UI
#col1,2,3 is columns 1,2,3
#the st.columns(3) is splitting my webpage into 3 vertical sections
col1, col2, col3 = st.columns(3)
user_choice = None

#Column 1 represents rock.

with col1:
    st.image(rock_url)
    if st.button("Rock"):
        user_choice = "Rock"


with col2:
    st.image(paper_url)
    if st.button("Paper"):
        user_choice = "Paper"


with col3:
    st.image(scissors_url)
    if st.button("Scissors"):
        user_choice = "Scissors"


# 4. Game logic triggers only after a button is pressed
if user_choice:
    #in choices.keys keys represent the random choices among the 3 keys paper,scissor, and rock
    st.divider()
    #st.divider() is used for separation like a line just like the one chat gpt uses when you copy and paste something to google docs
    computer_choice = random.choice(list(choices.keys()))
  
    # Displays the 1 vs 1 computer vs me
    # st.columns is used to like make a number (my number is 2) of components in the same row/column
    #res_col(1 or 2) is my choice and the computers choice
    res_col1, res_col2 = st.columns(2)
  
    with res_col1:
        #st.markdown displays strings kind of like st.write
        st.markdown("### My Choice")
        #width=150 is making the width of the choices image into 150.
        st.image(choices[user_choice], width=150)
        #the purpose of f is allow you to format the string with the variables inside of these{}
        st.write(f"**{user_choice}**")


    with res_col2:
        st.markdown("### Computer Choice")
        st.image(choices[computer_choice], width=150)
        st.write(f"**{computer_choice}**")


# 5. Determine winner

    # Initialize counters (only once)
    #session_state remembers values between button clicks instead of reseting everything
    #then after session_state you add .wins or losses or ties to represent if you lost or won or tied
    if "wins" not in st.session_state:
        st.session_state.wins = 0
    if "losses" not in st.session_state:
        st.session_state.losses = 0
    if "ties" not in st.session_state:
        st.session_state.ties = 0

    #if they tie add 1 to tie column
    if user_choice == computer_choice:
        st.session_state.ties += 1
        st.info("It's a tie! Try again. ")

    #in these situations when they win add 1 to win column
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        
        st.session_state.wins += 1
        st.success("Congratulations! You win! ")
    #when I lose add 1 to the lose column
    else:
        st.session_state.losses += 1
        st.error("Womp Womp... You lose! ")


    # 6. Scoreboard
    st.divider()
    st.markdown("## Scoreboard")

    col1, col2, col3 = st.columns(3)
    #st.metric displays like a big font that like goes down vertically.
    with col1:
        st.metric("Wins ", st.session_state.wins)

    with col2:
        st.metric("Ties ", st.session_state.ties)

    with col3:
        st.metric("Losses ", st.session_state.losses)
