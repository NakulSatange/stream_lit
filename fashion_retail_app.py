import streamlit as st

# Define a function to display content for each category
def display_category_content(category):
    if category == 'Men':
        st.image('https://example.com/men_fashion.jpg', use_column_width=True)
        st.write("""
        ## Men's Fashion
        Discover the latest trends in men's fashion including suits, casual wear, and accessories.
        Explore our curated collections designed to keep you looking sharp and stylish.
        """)
        st.write("- **Suits**: Tailored to perfection.")
        st.write("- **Casual Wear**: Comfortable and trendy.")
        st.write("- **Accessories**: Complete your look with our range of accessories.")
    
    elif category == 'Women':
        st.image('https://example.com/women_fashion.jpg', use_column_width=True)
        st.write("""
        ## Women's Fashion
        From elegant dresses to casual wear, find the perfect outfit for any occasion.
        Browse through our diverse collection and embrace the latest fashion trends.
        """)
        st.write("- **Dresses**: Stylish and versatile.")
        st.write("- **Casual Wear**: Comfortable and chic.")
        st.write("- **Accessories**: Add a touch of glamour with our accessories.")
    
    elif category == 'Kids':
        st.image('https://example.com/kids_fashion.jpg', use_column_width=True)
        st.write("""
        ## Kids' Fashion
        Fun and practical clothing for children of all ages. Discover playful designs and durable fabrics.
        """)
        st.write("- **Playwear**: Comfortable and durable for active kids.")
        st.write("- **Special Occasion Wear**: Stylish outfits for special events.")
        st.write("- **Accessories**: Fun and practical accessories for kids.")

# Set the title of the app
st.title('Fashion and Retail App')

# Sidebar for category selection
st.sidebar.title('Select Category')
category = st.sidebar.selectbox(
    'Choose a category',
    options=['Men', 'Women', 'Kids']
)

# Display the selected category's content
display_category_content(category)

# Add a footer
st.markdown("""
---
Created with ❤️ by Your Fashion Team
""")
