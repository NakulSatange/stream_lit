import streamlit as st

# Dictionary mapping muscle groups to exercises
exercise_data = {
    'Chest': [
        'Push-ups',
        'Bench Press',
        'Chest Dips',
        'Incline Dumbbell Press',
        'Chest Flyes',
        'Cable Crossovers'
    ],
    'Back': [
        'Pull-ups',
        'Bent Over Rows',
        'Lat Pulldowns',
        'Deadlifts',
        'T-Bar Rows',
        'Seated Cable Rows'
    ],
    'Legs': [
        'Squats',
        'Lunges',
        'Leg Press',
        'Hamstring Curls',
        'Leg Extensions',
        'Calf Raises'
    ],
    'Arms': [
        'Bicep Curls',
        'Tricep Dips',
        'Hammer Curls',
        'Tricep Extensions',
        'Concentration Curls',
        'Skull Crushers'
    ],
    'Abs': [
        'Crunches',
        'Planks',
        'Leg Raises',
        'Russian Twists',
        'Bicycle Crunches',
        'Hanging Leg Raises'
    ],
    'Shoulders': [
        'Shoulder Press',
        'Lateral Raises',
        'Front Raises',
        'Reverse Flyes',
        'Arnold Press',
        'Upright Rows'
    ],
    'Glutes': [
        'Hip Thrusts',
        'Glute Bridges',
        'Squats',
        'Lunges',
        'Deadlifts',
        'Cable Kickbacks'
    ],
    'Traps': [
        'Shrugs',
        'Deadlifts',
        'Upright Rows',
        'Face Pulls',
        'Farmer’s Walk',
        'Dumbbell Shrugs'
    ],
    'Forearms': [
        'Wrist Curls',
        'Reverse Wrist Curls',
        'Farmer’s Walk',
        'Hammer Curls',
        'Wrist Rollers',
        'Plate Pinches'
    ]
}

def suggest_exercises(muscle_group):
    exercises = exercise_data.get(muscle_group, [])
    return exercises[:6]  # Return only the first 6 exercises

def main():
    st.title('Muscle Group Exercise Suggestion App')
    
    st.sidebar.title('Input')
    muscle_group = st.sidebar.text_input('Enter a muscle group (e.g., Chest, Back, Legs):')
    
    if muscle_group:
        muscle_group = muscle_group.capitalize()
        exercises = suggest_exercises(muscle_group)
        
        st.header(f'Exercises for {muscle_group}')
        if exercises:
            for exercise in exercises:
                st.write(f'- {exercise}')
        else:
            st.write('No exercises found for this muscle group. Please enter a valid muscle group.')
    else:
        st.write('Please enter a muscle group to get exercise suggestions.')

if __name__ == '__main__':
    main()
