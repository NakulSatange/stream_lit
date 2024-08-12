import streamlit as st

# Sample data for products
products = {
    "Men": [
        {"name": "Leather Jacket", "price": "$120", "image": "https://via.placeholder.com/150?text=Leather+Jacket"},
        {"name": "Casual Shirt", "price": "$30", "image": "https://via.placeholder.com/150?text=Casual+Shirt"},
        {"name": "Running Shoes", "price": "$75", "image": "https://via.placeholder.com/150?text=Running+Shoes"},
        {"name": "Jeans", "price": "$50", "image": "https://via.placeholder.com/150?text=Jeans"},
        {"name": "Wool Sweater", "price": "$60", "image": "https://via.placeholder.com/150?text=Wool+Sweater"},
        {"name": "Shorts", "price": "$25", "image": "https://via.placeholder.com/150?text=Shorts"},
        {"name": "Dress Shirt", "price": "$40", "image": "https://via.placeholder.com/150?text=Dress+Shirt"},
        {"name": "Blazer", "price": "$150", "image": "https://via.placeholder.com/150?text=Blazer"},
        {"name": "Boots", "price": "$85", "image": "https://via.placeholder.com/150?text=Boots"},
        {"name": "Sweatpants", "price": "$35", "image": "https://via.placeholder.com/150?text=Sweatpants"},
    ],
    "Women": [
        {"name": "Summer Dress", "price": "$80", "image": "https://via.placeholder.com/150?text=Summer+Dress"},
        {"name": "High Heels", "price": "$60", "image": "https://via.placeholder.com/150?text=High+Heels"},
        {"name": "Blouse", "price": "$45", "image": "https://via.placeholder.com/150?text=Blouse"},
        {"name": "Skirt", "price": "$35", "image": "https://via.placeholder.com/150?text=Skirt"},
        {"name": "Cardigan", "price": "$50", "image": "https://via.placeholder.com/150?text=Cardigan"},
        {"name": "Leggings", "price": "$40", "image": "https://via.placeholder.com/150?text=Leggings"},
        {"name": "Coat", "price": "$120", "image": "https://via.placeholder.com/150?text=Coat"},
        {"name": "Tank Top", "price": "$20", "image": "https://via.placeholder.com/150?text=Tank+Top"},
        {"name": "Sweater Dress", "price": "$70", "image": "https://via.placeholder.com/150?text=Sweater+Dress"},
        {"name": "Chinos", "price": "$55", "image": "https://via.placeholder.com/150?text=Chinos"},
    ],
    "Kids": [
        {"name": "T-Shirt", "price": "$15", "image": "https://via.placeholder.com/150?text=T-Shirt"},
        {"name": "Jeans", "price": "$25", "image": "https://via.placeholder.com/150?text=Jeans"},
        {"name": "Sweater", "price": "$20", "image": "https://via.placeholder.com/150?text=Sweater"},
        {"name": "Jacket", "price": "$40", "image": "https://via.placeholder.com/150?text=Jacket"},
        {"name": "Shorts", "price": "$18", "image": "https://via.placeholder.com/150?text=Shorts"},
        {"name": "Sneakers", "price": "$30", "image": "https://via.placeholder.com/150?text=Sneakers"},
        {"name": "Dress", "price": "$25", "image": "https://via.placeholder.com/150?text=Dress"},
        {"name": "Overalls", "price": "$28", "image": "https://via.placeholder.com/150?text=Overalls"},
        {"name": "Cap", "price": "$10", "image": "https://via.placeholder.com/150?text=Cap"},
        {"name": "Raincoat", "price": "$35", "image": "https://via.placeholder.com/150?text=Raincoat"},
    ]
}

def display_products(category):
    st.subheader(f"{category} Products")
    for product in products[category]:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(product["image"], caption=product["name"], width=150)
        with col2:
            st.write(f"**Name:** {product['name']}")
            st.write(f"**Price:** {product['price']}")
        st.write("")

def main():
    st.title("Fashion and Retail App")

    # Sidebar for category selection
    category = st.sidebar.selectbox(
        "Select Category",
        ["Men", "Women", "Kids"]
    )

    # Display products based on selected category
    display_products(category)

if __name__ == "__main__":
    main()
