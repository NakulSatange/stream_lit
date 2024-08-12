import streamlit as st

# Define product data with image paths for 10 sections each for men, women, and kids
products = {
    "Men": [
        {"name": "Men's Shirt", "price": 30, "image": "images/mens_shirt.jpg"},
        {"name": "Men's Jeans", "price": 50, "image": "images/mens_jeans.jpg"},
        # Add more products here
    ],
    "Women": [
        {"name": "Women's Dress", "price": 60, "image": "images/womens_dress.jpg"},
        {"name": "Women's Skirt", "price": 40, "image": "images/womens_skirt.jpg"},
        # Add more products here
    ],
    "Kids": [
        {"name": "Kids T-Shirt", "price": 20, "image": "images/kids_tshirt.jpg"},
        {"name": "Kids Shorts", "price": 25, "image": "images/kids_shorts.jpg"},
        # Add more products here
    ]
}

# Define the sections (10 sections per category)
sections = {
    "Men": [f"Section {i}" for i in range(1, 11)],
    "Women": [f"Section {i}" for i in range(1, 11)],
    "Kids": [f"Section {i}" for i in range(1, 11)]
}

# Function to display products for a specific section
def display_products(category, section):
    st.header(f"{category} - {section} Products")
    
    # Filter products based on the section if needed (dummy filter here for demonstration)
    section_products = [p for p in products[category] if section in p['name']]
    
    selected_products = st.multiselect("Select Products", [p['name'] for p in section_products])
    
    total_price = 0
    for product in section_products:
        if product['name'] in selected_products:
            st.image(product['image'], width=150)
            st.write(f"**{product['name']}** - ${product['price']}")
            total_price += product['price']
    
    st.write(f"**Total Price: ${total_price}**")

# Streamlit app
def main():
    st.title("Fashion Product Billing App")
    
    category = st.sidebar.selectbox("Choose a category", ["Men", "Women", "Kids"])
    section = st.sidebar.selectbox("Choose a section", sections[category])
    
    display_products(category, section)

if __name__ == "__main__":
    main()
