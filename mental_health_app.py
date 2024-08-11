import streamlit as st

# Dictionary mapping mental health issues to suggested self-help strategies
mental_health_resources = {
    'Anxiety': [
        'Practice deep breathing exercises.',
        'Engage in regular physical activity.',
        'Try mindfulness meditation or yoga.',
        'Avoid excessive caffeine and alcohol.',
        'Connect with supportive friends and family.',
        'Consider keeping a journal to express your thoughts and feelings.'
    ],
    'Depression': [
        'Seek professional help from a therapist or counselor.',
        'Engage in physical exercise regularly.',
        'Set small, manageable goals each day.',
        'Maintain a healthy diet and sleep routine.',
        'Connect with loved ones and build a support network.',
        'Consider practicing gratitude or mindfulness exercises.'
    ],
    'Stress': [
        'Identify and manage stressors in your life.',
        'Practice relaxation techniques such as deep breathing or meditation.',
        'Make time for hobbies and activities you enjoy.',
        'Ensure you get adequate sleep and maintain a balanced diet.',
        'Seek social support from friends and family.',
        'Learn time management techniques to reduce feelings of being overwhelmed.'
    ],
    'Sleep Issues': [
        'Establish a regular sleep schedule and stick to it.',
        'Create a relaxing bedtime routine.',
        'Avoid screens and bright lights before bedtime.',
        'Ensure your sleep environment is comfortable and conducive to rest.',
        'Limit caffeine and heavy meals close to bedtime.',
        'Consider practicing relaxation techniques to ease into sleep.'
    ],
    'Low Self-Esteem': [
        'Practice positive self-talk and affirmations.',
        'Set achievable goals and celebrate small successes.',
        'Engage in activities that make you feel competent and valued.',
        'Seek feedback and support from trusted friends or mentors.',
        'Consider working with a therapist to explore underlying issues.',
        'Practice self-compassion and self-care regularly.'
    ],
    'Relationship Issues': [
        'Communicate openly and honestly with your partner.',
        'Seek to understand and validate each other’s feelings.',
        'Consider couples therapy if needed.',
        'Make time for quality interactions and shared activities.',
        'Address conflicts directly and constructively.',
        'Seek support from trusted friends or counselors if needed.'
    ]
}

def get_resources(issue):
    return mental_health_resources.get(issue, [])

def main():
    st.title('Mental Health Support App')
    
    st.sidebar.title('Input')
    issue = st.sidebar.selectbox(
        'Select a mental health issue:',
        options=list(mental_health_resources.keys())
    )
    
    if issue:
        resources = get_resources(issue)
        
        st.header(f'Support for {issue}')
        if resources:
            for resource in resources:
                st.write(f'- {resource}')
        else:
            st.write('No resources found for this issue. Please select another option.')
    else:
        st.write('Please select a mental health issue to get support suggestions.')

if __name__ == '__main__':
    main()
