import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize the Translator
translator = Translator()

def translate_text(text, dest_language):
    """Translate text to the destination language."""
    try:
        translated = translator.translate(text, dest=dest_language)
        return translated.text
    except Exception as e:
        st.error(f"Error in translation: {e}")
        return text

# Title of the app
st.title('Fashion and Retail App')

# Sidebar for language selection
st.sidebar.title('Settings')
language = st.sidebar.selectbox(
    'Select Language',
    options=list(LANGUAGES.values())
)

# Detect the language code
lang_code = [code for code, name in LANGUAGES.items() if name == language][0]

# Sidebar for category selection
category = st.sidebar.selectbox(
    'Select Category',
    options=['Men', 'Women', 'Kids']
)

# Display the selected category
st.header(f'Fashion and Retail - {category}')

# Display content based on category
if category == 'Men':
    content = """
    **Men's Fashion**: Explore our latest collection of suits, shirts, trousers, and accessories. 
    Discover trending styles and high-quality apparel tailored for every occasion.
    """
elif category == 'Women':
    content = """
    **Women's Fashion**: Shop the latest trends in dresses, tops, skirts, and more. 
    Find elegant designs and stylish outfits for any event or everyday wear.
    """
else:
    content = """
    **Kids' Fashion**: Check out our playful and comfortable clothing for children. 
    From casual wear to special occasion outfits, we have something for every kid.
    """

# Translate content
translated_content = translate_text(content, lang_code)

# Display content
st.write(translated_content)

# Add a footer
st.markdown("""
    ---
    Created with ❤️ by Your Fashion Team
    """)
