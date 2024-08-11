import streamlit as st
import pandas as pd
from PIL import Image

# Define product details
menu_items = {
    "Coffee": {"price": 3.00, "image": "images/coffee.jpg"},
    "Tea": {"price": 2.50, "image": "images/tea.jpg"},
    "Sandwich": {"price": 5.00, "image": "images/sandwich.jpg"},
    "Cake": {"price": 4.00, "image": "images/cake.jpg"},
    "Juice": {"price": 3.50, "image": "images/juice.jpg"}
}

def main():
    st.title("Cafe Billing System")

    # Display menu with images
    st.sidebar.header("Menu")
    for item, details in menu_items.items():
        img = Image.open(details["image"])
        st.sidebar.image(img, use_column_width=True, caption=item)
        st.sidebar.write(f"{item}: ${details['price']:.2f}")

    st.sidebar.header("Order")
    order_form = st.sidebar.form(key='order_form')
    quantities = {}
    for item, details in menu_items.items():
        quantity = order_form.number_input(f"Quantity of {item}", min_value=0, key=item)
        quantities[item] = quantity

    submit_button = order_form.form_submit_button("Submit Order")

    if submit_button:
        # Calculate the total bill
        total = sum(details["price"] * quantities[item] for item, details in menu_items.items())
        st.write("### Order Summary")
        st.write("**Items Ordered:**")
        for item, quantity in quantities.items():
            if quantity > 0:
                st.write(f"{item}: {quantity} @ ${menu_items[item]['price']:.2f} each")

        st.write(f"**Total Bill:** ${total:.2f}")

if __name__ == "__main__":
    main()
