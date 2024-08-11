import streamlit as st
import random

# Predefined templates for pickup lines
pickup_line_templates = [
    "Are you a {}? Because you're making my heart race.",
    "Do you have a {}? Because I feel like I'm falling for you.",
    "I must be a {} because I can't stop looking at you.",
    "Is your name {}? Because you're the {} of my dreams.",
    "Do you believe in love at first sight, or should I walk by again with a {}?",
    "If you were a {}, you'd be a perfect match for me."
]

def generate_pickup_line(word):
    template = random.choice(pickup_line_templates)
    return template.format(word, word)

def main():
    st.title('Pickup Line Generator')
    
    st.sidebar.title('Input')
    random_word = st.sidebar.text_input('Enter a random word:')
    
    if random_word:
        pickup_line = generate_pickup_line(random_word)
        st.header('Your Pickup Line:')
        st.write(pickup_line)
    else:
        st.write('Please enter a word to generate a pickup line.')

if __name__ == '__main__':
    main()
