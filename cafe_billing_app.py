import streamlit as st
import pandas as pd

# Sample menu items
menu_items = {
    "Coffee": 30.00 rs,
    "Tea": 25.00 rs,
    "Juice": 135.00 rs,
    "Chocolate shake": 185.00 rs,
    "Sandwich": 175.00 rs,
    "Pudding": 250.00 rs,
    "Pasta": 390.00 rs,
    "Pizza (small)": 250.00 rs,
    "Pizza (medium)": 340.00 rs,
    "Pizza (large)": 450.00 rs,
}

def main():
    st.title("Cafe Billing App")

    st.sidebar.header("Menu")
    # Display the menu items in the sidebar
    for item, price in menu_items.items():
        st.sidebar.write(f"{item}: ${price:.2f}")

    st.sidebar.header("Order")
    # Create a form for the user to input the quantity of each item
    order_form = st.sidebar.form(key='order_form')
    quantities = {}
    for item in menu_items.keys():
        quantity = order_form.number_input(f"Quantity of {item}", min_value=0, key=item)
        quantities[item] = quantity

    submit_button = order_form.form_submit_button("Submit Order")

    if submit_button:
        # Calculate the total bill
        total = sum(menu_items[item] * quantities[item] for item in menu_items)
        st.write("### Order Summary")
        st.write("**Items Ordered:**")
        for item, quantity in quantities.items():
            if quantity > 0:
                st.write(f"{item}: {quantity} @ ${menu_items[item]:.2f} each")

        st.write(f"**Total Bill:** ${total:.2f}")

if __name__ == "__main__":
    main()
