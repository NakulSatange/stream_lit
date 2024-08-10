import streamlit as st

# Define exercises for each body region
exercises = {
    'Chest': [
        "Push-ups: Great for building chest muscles. Do 3 sets of 10-15 reps.",
        "Bench Press: Effective for chest development. Start with 3 sets of 8-12 reps.",
        "Chest Dips: Target the chest and triceps. Perform 3 sets of 8-12 reps."
    ],
    'Back': [
        "Pull-ups: Excellent for upper back. Aim for 3 sets of 5-10 reps.",
        "Rows: Effective for mid-back. Perform 3 sets of 10-15 reps.",
        "Lat Pulldowns: Targets the latissimus dorsi. Do 3 sets of 8-12 reps."
    ],
    'Legs': [
        "Squats: Fundamental exercise for legs. Aim for 3 sets of 12-15 reps.",
        "Lunges: Great for quads and glutes. Perform 3 sets of 10-12 reps per leg.",
        "Leg Press: Effective for overall leg development. Do 3 sets of 10-12 reps."
    ],
    'Arms': [
        "Bicep Curls: Targets biceps. Do 3 sets of 10-15 reps.",
        "Tricep Dips: Effective for triceps. Perform 3 sets of 10-12 reps.",
        "Hammer Curls: Great for biceps and forearms. Aim for 3 sets of 10-15 reps."
    ],
    'Abs': [
        "Crunches: Classic ab exercise. Do 3 sets of 15-20 reps.",
        "Planks: Effective for core strength. Hold for 30-60 seconds, 3 sets.",
        "Leg Raises: Targets lower abs. Perform 3 sets of 10-15 reps."
    ]
}

# Streamlit app layout
def main():
    st.title('Exercise Suggestion App')
    st.write("Welcome to the Exercise Suggestion App.")
    st.write("Select a body region to get exercise suggestions.")
    
    body_part = st.selectbox(
        'Which body part would you like to exercise?',
        ['Select an option'] + list(exercises.keys())
    )
    
    if body_part != 'Select an option':
        st.subheader(f'Exercises for {body_part}')
        for exercise in exercises[body_part]:
            st.write(f"- {exercise}")

if __name_
