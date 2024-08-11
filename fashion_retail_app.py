import streamlit as st

# Sample data for the fashion categories
fashion_data = {
    'Men': [
        {'name': 'Elegant Suit', 'price': '$299', 'image': 'https://via.placeholder.com/300x200?text=Men+Suit'},
        {'name': 'Casual Shirt', 'price': '$49', 'image': 'https://via.placeholder.com/300x200?text=Casual+Shirt'},
        {'name': 'Leather Jacket', 'price': '$199', 'image': 'https://via.placeholder.com/300x200?text=Leather+Jacket'}
    ],
    'Women': [
        {'name': 'Evening Gown', 'price': '$399', 'image': 'https://via.placeholder.com/300x200?text=Evening+Gown'},
        {'name': 'Summer Dress', 'price': '$79', 'image': 'https://via.placeholder.com/300x200?text=Summer+Dress'},
        {'name': 'Trendy Handbag', 'price': '$129', 'image': 'https://via.placeholder.com/300x200?text=Handbag'}
    ],
    'Kids': [
        {'name': 'Playful T-Shirt', 'price': '$29', 'image': 'https://via.placeholder.com/300x200?text=Kids+T-Shirt'},
        {'name': 'Cute Dress', 'price': '$59', 'image': 'https://via.placeholder.com/300x200?text=Kids+Dress'},
        {'name': 'Comfy Sneakers', 'price': '$89', 'image': 'https://via.placeholder.com/300x200?text=Kids+Sneakers'}
    ]
}

# Function to display fashion items
def display_fashion_items(category):
    st.header(f'{category} Fashion')
    items = fashion_data.get(category, [])
    
    for item in items:
        st.image(item['image'], caption=item['name'], use_column_width=True)
        st.write(f"**{item['name']}** - {item['price']}")
        st.write("---")

# Streamlit app layout
def main():
    st.title('Fashion and Retail App')
    
    st.sidebar.title('Select Category')
    category = st.sidebar.selectbox(
        'Choose a category',
        options=['Men', 'Women', 'Kids']
    )
    
    display_fashion_items(category)
    
    st.markdown("""
    ---
    Created with ❤️ by Your Fashion Team
    """)

if __name__ == "__main__":
    main()
