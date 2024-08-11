import streamlit as st

# Dictionary mapping body regions to exercises
exercise_data = {
    'Chest': [
        'Push-ups',
        'Bench Press',
        'Chest Dips',
        'Incline Dumbbell Press'
    ],
    'Back': [
        'Pull-ups',
        'Bent Over Rows',
        'Lat Pulldowns',
        'Deadlifts'
    ],
    'Legs': [
        'Squats',
        'Lunges',
        'Leg Press',
        'Hamstring Curls'
    ],
    'Arms': [
        'Bicep Curls',
        'Tricep Dips',
        'Hammer Curls',
        'Tricep Extensions'
    ],
    'Abs': [
        'Crunches',
        'Planks',
        'Leg Raises',
        'Russian Twists'
    ],
    'Shoulders': [
        'Shoulder Press',
        'Lateral Raises',
        'Front Raises',
        'Reverse Flyes'
    ]
}

def main():
    st.title('Exercise Suggestion App')
    
    st.sidebar.title('Select Body Region')
    body_region = st.sidebar.selectbox(
        'Choose a body region:',
        options=list(exercise_data.keys())
    )
    
    st.header(f'Exercises for {body_region}')
    exercises = exercise_data.get(body_region, [])
    
    if exercises:
        for exercise in exercises:
            st.write(f'- {exercise}')
    else:
        st.write('No exercises found for this body region.')

if __name__ == '__main__':
    main()
