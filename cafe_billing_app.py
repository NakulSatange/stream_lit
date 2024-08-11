import streamlit as st
import pandas as pd

# Sample menu items
menu_items = {
    "Coffee": 3.00,
    "Tea": 2.50,
    "Sandwich": 5.00,
    "Cake": 4.00,
    "Juice": 3.50
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
