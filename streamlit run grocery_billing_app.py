import streamlit as st

# Define the list of grocery items and their prices
items = {
    'Apples': 1.00,
    'Bananas': 0.50,
    'Carrots': 0.30,
    'Milk': 1.20,
    'Bread': 1.50,
    'Eggs': 2.00
}

def main():
    st.title('Grocery Billing App')

    st.write("Welcome to the Grocery Billing App!")
    st.write("Select items and quantities to calculate the total bill.")

    # Initialize the shopping cart
    cart = {}

    # Display items and get user input for quantities
    st.header('Available Items')
    for item, price in items.items():
        quantity = st.number_input(f'{item} - ${price:.2f} per unit', min_value=0, key=item)
        if quantity > 0:
            cart[item] = quantity

    # Calculate and display the total bill
    if cart:
        st.header('Your Cart')
        total = 0
        for item, quantity in cart.items():
            item_total = items[item] * quantity
            total += item_total
            st.write(f"{item}: {quantity} x ${items[item]:.2f} = ${item_total:.2f}")

        st.subheader(f'Total Bill: ${total:.2f}')
    else:
        st.write("Your cart is empty. Please select items.")

if __name__ == "__main__":
    main()
