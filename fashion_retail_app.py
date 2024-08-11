import streamlit as st
from PIL import Image
import os

# Directory containing the images
IMAGE_DIR = 'images'

# Sample product data
products = {
    "Men": [
        {"name": "Men's Shirt", "price": 25, "image": "men_shirt.jpg"},
        {"name": "Men's Jeans", "price": 40, "image": "men_jeans.jpg"},
        {"name": "Men's Jacket", "price": 60, "image": "men_jacket.jpg"},
        {"name": "Men's Shoes", "price": 50, "image": "men_shoes.jpg"},
        {"name": "Men's Hat", "price": 15, "image": "men_hat.jpg"},
        {"name": "Men's Sunglasses", "price": 20, "image": "men_sunglasses.jpg"},
        {"name": "Men's Belt", "price": 30, "image": "men_belt.jpg"},
        {"name": "Men's Scarf", "price": 25, "image": "men_scarf.jpg"},
        {"name": "Men's Gloves", "price": 18, "image": "men_gloves.jpg"},
        {"name": "Men's Watch", "price": 75, "image": "men_watch.jpg"}
    ],
    "Women": [
        {"name": "Women's Dress", "price": 30, "image": "women_dress.jpg"},
        {"name": "Women's Skirt", "price": 25, "image": "women_skirt.jpg"},
        {"name": "Women's Jacket", "price": 35, "image": "women_jacket.jpg"},
        {"name": "Women's Shoes", "price": 45, "image": "women_shoes.jpg"},
        {"name": "Women's Bag", "price": 50, "image": "women_bag.jpg"},
        {"name": "Women's Scarf", "price": 20, "image": "women_scarf.jpg"},
        {"name": "Women's Gloves", "price": 22, "image": "women_gloves.jpg"},
        {"name": "Women's Hat", "price": 18, "image": "women_hat.jpg"},
        {"name": "Women's Jeans", "price": 40, "image": "women_jeans.jpg"},
        {"name": "Women's Belt", "price": 30, "image": "women_belt.jpg"}
    ],
    "Kids": [
        {"name": "Kids' T-Shirt", "price": 15, "image": "kids_tshirt.jpg"},
        {"name": "Kids' Shorts", "price": 20, "image": "kids_shorts.jpg"},
        {"name": "Kids' Jacket", "price": 30, "image": "kids_jacket.jpg"},
        {"name": "Kids' Shoes", "price": 25, "image": "kids_shoes.jpg"},
        {"name": "Kids' Hat", "price": 10, "image": "kids_hat.jpg"},
        {"name": "Kids' Sweater", "price": 28, "image": "kids_sweater.jpg"},
        {"name": "Kids' Jeans", "price": 22, "image": "kids_jeans.jpg"},
        {"name": "Kids' Scarf", "price": 12, "image": "kids_scarf.jpg"},
        {"name": "Kids' Gloves", "price": 15, "image": "kids_gloves.jpg"},
        {"name": "Kids' Boots", "price": 30, "image": "kids_boots.jpg"}
    ]
}

# Function to load image
def load_image(image_name):
    image_path = os.path.join(IMAGE_DIR, image_name)
    image = Image.open(image_path)
    return image

def main():
    st.title("Fashion and Retail Billing App")

    # Sidebar for category selection
    category = st.sidebar.selectbox("Select Category:", ["Men", "Women", "Kids"])

    st.header(f"{category} Products")

    # Display products
    for product in products[category]:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            st.image(load_image(product["image"]), caption=product["name"], use_column_width=True)
        with col2:
            st.subheader(product["name"])
            st.write(f"Price: ${product['price']}")
        with col3:
            if st.button("Add to Cart", key=product["name"]):
                st.write(f"{product['name']} added to cart!")

if __name__ == "__main__":
    main()
