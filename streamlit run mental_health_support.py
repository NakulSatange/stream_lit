import streamlit as st

# Define the support advice based on user's input
def provide_support(feeling):
    if feeling == 'Anxious':
        return "It's okay to feel anxious. Try taking deep breaths, and consider mindfulness exercises or talking to someone you trust."
    elif feeling == 'Depressed':
        return "Depression is serious. Please reach out to a mental health professional or counselor. Talking to friends or family can also help."
    elif feeling == 'Stressed':
        return "Stress management techniques such as regular exercise, meditation, and relaxation can be beneficial. Don’t hesitate to seek professional advice."
    elif feeling == 'Overwhelmed':
        return "Feeling overwhelmed can be challenging. Try breaking tasks into smaller steps and take regular breaks. Reach out for support if needed."
    elif feeling == 'Other':
        return "It's okay to have unique feelings. Try to identify what specifically is bothering you and consider seeking professional advice."
    else:
        return "Invalid input. Please select a valid option."

# Streamlit app layout
def main():
    st.title('Mental Health Support App')
    st.write("Welcome to the Mental Health Support App.")
    st.write("I'm here to offer some supportive advice based on your input.")
    st.write("Remember, this is not a substitute for professional help.")
    
    feeling = st.selectbox(
        'How are you feeling today?',
        ['Select an option', 'Anxious', 'Depressed', 'Stressed', 'Overwhelmed', 'Other']
    )
    
    if feeling != 'Select an option':
        advice = provide_support(feeling)
        st.write(advice)

if __name__ == "__main__":
    main()
