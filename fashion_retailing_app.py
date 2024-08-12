import streamlit as st

# Define product data with image paths
products = {
    "Men": [
        {"name": "Men's Shirt", "price": 30, "image": "images/mens_shirt.jpg"},
        {"name": "Men's Jeans", "price": 50, "image": "images/mens_jeans.jpg"},
        {"name": "Men's Jacket", "price": 80, "image": "images/mens_jacket.jpg"},
        {"name": "Men's Shoes", "price": 60, "image": "images/mens_shoes.jpg"},
        {"name": "Men's Tie", "price": 25, "image": "images/mens_tie.jpg"},
        {"name": "Men's Shorts", "price": 35, "image": "images/mens_shorts.jpg"},
        {"name": "Men's Socks", "price": 10, "image": "images/mens_socks.jpg"},
        {"name": "Men's Cap", "price": 20, "image": "images/mens_cap.jpg"},
        {"name": "Men's Belt", "price": 40, "image": "images/mens_belt.jpg"},
        {"name": "Men's Sweater", "price": 45, "image": "images/mens_sweater.jpg"}
    ],
    "Women": [
        {"name": "Women's Dress", "price": 60, "image": "images/womens_dress.jpg"},
        {"name": "Women's Skirt", "price": 40, "image": "images/womens_skirt.jpg"},
        {"name": "Women's Blouse", "price": 35, "image": "images/womens_blouse.jpg"},
        {"name": "Women's Jacket", "price": 70, "image": "images/womens_jacket.jpg"},
        {"name": "Women's Shoes", "price": 55, "image": "images/womens_shoes.jpg"},
        {"name": "Women's Scarf", "price": 25, "image": "images/womens_scarf.jpg"},
        {"name": "Women's Purse", "price": 80, "image": "images/womens_purse.jpg"},
        {"name": "Women's Gloves", "price": 15, "image": "images/womens_gloves.jpg"},
        {"name": "Women's Hat", "price": 30, "image": "images/womens_hat.jpg"},
        {"name": "Women's Tights", "price": 20, "image": "images/womens_tights.jpg"}
    ],
    "Kids": [
        {"name": "Kids T-Shirt", "price": 20, "image": "images/kids_tshirt.jpg"},
        {"name": "Kids Shorts", "price": 25, "image": "images/kids_shorts.jpg"},
        {"name": "Kids Jacket", "price": 45, "image": "images/kids_jacket.jpg"},
        {"name": "Kids Shoes", "price": 30, "image": "images/kids_shoes.jpg"},
        {"name": "Kids Dress", "price": 40, "image": "images/kids_dress.jpg"},
        {"name": "Kids Hat", "price": 15, "image": "images/kids_hat.jpg"},
        {"name": "Kids Socks", "price": 10, "image": "images/kids_socks.jpg"},
        {"name": "Kids Gloves", "price": 12, "image": "images/kids_gloves.jpg"},
        {"name": "Kids Sweater", "price": 35, "image": "images/kids_sweater.jpg"},
        {"name": "Kids Backpack", "price": 50, "image": "images/kids_backpack.jpg"}
    ]
}

# Function to display products
def display_products(category):
    st.header(f"{category} Products")
    selected_products = st.multiselect("Select Products", [p['name'] for p in products[category]])
    
    total_price = 0
    for product in products[category]:
        if product['name'] in selected_products:
            st.image(product['image'], width=150)
            st.write(f"**{product['name']}** - ${product['price']}")
            total_price += product['price']
    
    st.write(f"**Total Price: ${total_price}**")

# Streamlit app
def main():
    st.title("Fashion Product Billing App")
    
    category = st.sidebar.selectbox("Choose a category", ["Men", "Women", "Kids"])
    
    display_products(category)

if __name__ == "__main__":
    main()
