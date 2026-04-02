
import streamlit as st
import random
from PIL import Image




st.title("Unblocked Rock, Paper, Scissors Game")




# 1. Load images and define variables properly


# Using web URLs so you don't need local files
rock_url = "https://png.pngtree.com/png-clipart/20220824/ourmid/pngtree-cartoon-rock-transparent-png-image_6122807.png"
paper_url = "https://png.pngtree.com/element_our/20190531/ourmid/pngtree-yellow-paper-cartoon-illustration-image_1292433.jpg"
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
   st.divider()
   computer_choice = random.choice(list(choices.keys()))
  
   # Display the "Showdown"
   res_col1, res_col2 = st.columns(2)
  
   with res_col1:
       st.markdown("### 🖐 Your Choice")
       st.image(choices[user_choice], width=150)
       st.write(f"**{user_choice}**")




   with res_col2:
       st.markdown("### 🤖 Computer Choice")
       st.image(choices[computer_choice], width=150)
       st.write(f"**{computer_choice}**")




   # 5. Determine winner
   if user_choice == computer_choice:
       st.info("It's a tie! Try again. 🤝")
   elif (user_choice == "Rock" and computer_choice == "Scissors") or \
        (user_choice == "Paper" and computer_choice == "Rock") or \
        (user_choice == "Scissors" and computer_choice == "Paper"):
       st.success("Congratulations! You win! 🎉")
   else:
       st.error("Womp Womp... You lose! 😢")
