import streamlit as st

# Sample data for products
products = {
    "Men": [
        {"name": "Leather Jacket", "price": "$120", "image": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQJDNGgIxiRmlygjdq5XjVX8QlP91EW3cFKETJSrEWS2oMunVQxiZSCCiR6ouwx"},
        {"name": "Casual Shirt", "price": "$30", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjbYXQ63uJC3KQQQlhG2qIZ9tOCzKMsQGa-ROrjHqKXzjnF22s6sJKJfjIkLJw"},
        {"name": "Running Shoes", "price": "$75", "image": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRO7ewirsejNF26IGHhuAPk2hmcOdQLzIPCTI6azswGwFeYyx0_GjoWdgffhsWv"},
        {"name": "Jeans", "price": "$50", "image": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRQfT-yLWHup2RT7gUPVK1uUwQKWcthuuEF4rjMEkGKNUVe3Rg0mstmRdNRggVS"},
        {"name": "Wool Sweater", "price": "$60", "image": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQB_eMql1tECrptezm5FMsTSpgDhuzpKqVvqxf64PHQHAPMxEXOF58O2jPTt_jl"},
        {"name": "Shorts", "price": "$25", "image": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRyUX2a4LGMGDQJVcn5vivETIakrjQ_XFTFZ7YI2b5bTN_hCKRd4y34COLHwuBi"},
        {"name": "Dress Shirt", "price": "$40", "image": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRRkuv00dDdL_pok91RrN5mAvWOHp2d6iPOLsDQlbuVEN3zPZHN31JhR_kN9_8-"},
        {"name": "Blazer", "price": "$150", "image": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRVsdgW_9_zgx6yh1HM75ESblB7BTHZu_a1kec8lEThujl8uPa3cHW6BfGiE3ZP"},
        {"name": "Boots", "price": "$85", "image": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcS9dz-dR5aQ4L5Emc09f64t-4ej-chnFRn7xZNKifSzItNTC3GARYtnskKer1KL"},
        {"name": "Sweatpants", "price": "$35", "image": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQrpvNyZ9d7VuXicUr6r_fGDGcfz7d_twBb76igjsnbNV4VxYM2wkWsBmIvj3qB"},
    ],
    "Women": [
        {"name": "Summer Dress", "price": "$80", "image": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSjc5vpJn_x3LJSo3U6nZ5LDVPJrdtZSVa6T9HZHwQJuR4ZCMDJShCuFs87uL8t"},
        {"name": "High Heels", "price": "$60", "image": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcS7f0Of9rzqnLhcDJP14gEuCvjP78Po6PiW_bYVL6cvORTuUcSkgS1GfK45jqaM"},
        {"name": "Oversized Ts", "price": "$45", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSbfkfEJcB0uRdO_xHUtIPBVdN-QPgPtWpk5w9eaDhaXn2NkaqD4Vz8B7pqk2_"},
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
