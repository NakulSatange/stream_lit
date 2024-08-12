import streamlit as st
from PIL import Image

# Sample data for products
products = {
    'Men': [
        {'name': 'Leather Shoes', 'price': 100, 'image': 'images/men1.jpg'},
        {'name': 'Denim Jacket', 'price': 120, 'image': 'images/men2.jpg'},
        {'name': 'Formal Shirt', 'price': 70, 'image': 'images/men3.jpg'},
        {'name': 'Chinos', 'price': 60, 'image': 'images/men4.jpg'},
        {'name': 'Winter Coat', 'price': 200, 'image': 'images/men5.jpg'},
        {'name': 'Sneakers', 'price': 90, 'image': 'images/men6.jpg'},
        {'name': 'Casual Trousers', 'price': 55, 'image': 'images/men7.jpg'},
        {'name': 'Sweater', 'price': 65, 'image': 'images/men8.jpg'},
        {'name': 'Leather Belt', 'price': 30, 'image': 'images/men9.jpg'},
        {'name': 'Sports Jacket', 'price': 110, 'image': 'images/men10.jpg'}
    ],
    'Women': [
        {'name': 'Summer Dress', 'price': 80, 'image': 'images/women1.jpg'},
        {'name': 'High Heels', 'price': 90, 'image': 'images/women2.jpg'},
        {'name': 'Blouse', 'price': 50, 'image': 'images/women3.jpg'},
        {'name': 'Skirt', 'price': 45, 'image': 'images/women4.jpg'},
        {'name': 'Winter Jacket', 'price': 150, 'image': 'images/women5.jpg'},
        {'name': 'Handbag', 'price': 130, 'image': 'images/women6.jpg'},
        {'name': 'Cardigan', 'price': 55, 'image': 'images/women7.jpg'},
        {'name': 'Leggings', 'price': 40, 'image': 'images/women8.jpg'},
        {'name': 'Sunglasses', 'price': 75, 'image': 'images/women9.jpg'},
        {'name': 'Scarf', 'price': 25, 'image': 'images/women10.jpg'}
    ],
    'Kids': [
        {'name': 'T-Shirt', 'price': 20, 'image': 'images/kids1.jpg'},
        {'name': 'Shorts', 'price': 25, 'image': 'images/kids2.jpg'},
        {'name': 'Jacket', 'price': 45, 'image': 'images/kids3.jpg'},
        {'name': 'Sneakers', 'price': 30, 'image': 'images/kids4.jpg'},
        {'name': 'Dress', 'price': 35, 'image': 'images/kids5.jpg'},
        {'name': 'Sweater', 'price': 28, 'image': 'images/kids6.jpg'},
        {'name': 'Hat', 'price': 15, 'image': 'images/kids7.jpg'},
        {'name': 'Gloves', 'price': 12, 'image': 'images/kids8.jpg'},
        {'name': 'Leggings', 'price': 22, 'image': 'images/kids9.jpg'},
        {'name': 'Raincoat', 'price': 40, 'image': 'images/kids10.jpg'}
    ]
}

def display_products(category):
    st.subheader(f"{category} Products")
    for product in products[category]:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.image(product['image'], use_column_width=True)
        with col2:
            st.write(f"**{product['name']}**")
            st.write(f"Price: ${product['price']}")
            if st.button(f"Add {product['name']} to Cart", key=product['name']):
                st.session_state.cart.append(product)
                st.success(f"{product['name']} added to cart")

def main():
    st.title("Fashion Billing App")
    st.sidebar.title("Categories")
    
    # Sidebar category selection
    category = st.sidebar.selectbox("Select Category", ['Men', 'Women', 'Kids'])
    
    # Display products based on selected category
    display_products(category)
    
    # Display Cart
    if 'cart' not in st.session_state:
        st.session_state.cart = []

    if st.button("Show Cart"):
        st.subheader("Cart")
        if st.session_state.cart:
            total_price = 0
            for item in st.session_state.cart:
                st.write(f"{item['name']} - ${item['price']}")
                total_price += item['price']
            st.write(f"**Total Price: ${total_price}**")
        else:
            st.write("Your cart is empty.")

if __name__ == "__main__":
    main()
