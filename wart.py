import streamlit as st
import random
from PIL import Image


st.title("🎮 Rock, Paper, Scissors Game with Images")


# Load images (replace with your own image paths or URLs)
rock_img = Image.open("rock.jpeg")      # image of a rock
paper_img = Image.open("paper.jpeg")    # image of paper
scissors_img = Image.open("scissor.jpeg")  # image of scissors


# Map choices to images
choices = {"Rock": rock_img, "Paper": paper_img, "Scissors": scissors_img}


st.write("Click on an image to make your choice:")


# Display images as clickable buttons
col1, col2, col3 = st.columns(3)


user_choice = None
with col1:
   if st.button("Rock"):
       user_choice = "Rock"
       st.image(rock_img, width=100)
with col2:
   if st.button("Paper"):
       user_choice = "Paper"
       st.image(paper_img, width=100)
with col3:
   if st.button("Scissors"):
       user_choice = "Scissors"
       st.image(scissors_img, width=100)


# Game logic
if user_choice:
   computer_choice = random.choice(list(choices.keys()))
   st.write(f"🖐 You chose: {user_choice}")
   st.image(choices[user_choice], width=100)


   st.write(f"🤖 Computer chose: {computer_choice}")
   st.image(choices[computer_choice], width=100)


   # Determine winner
   if user_choice == computer_choice:
       st.write("It's a tie! Try Again")
   elif (user_choice == "Rock" and computer_choice == "Scissors") or \
        (user_choice == "Paper" and computer_choice == "Rock") or \
        (user_choice == "Scissors" and computer_choice == "Paper"):
       st.write("Congratulations You win!")
   else:
       st.write("Womp Womp You lose!")

