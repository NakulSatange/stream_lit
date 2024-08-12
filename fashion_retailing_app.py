import streamlit as st

# Sample product data
products = [
    {
        "name": "T-shirt",
        "category": "Men",
        "description": "A comfortable cotton T-shirt.",
        "image": "https://example.com/men_tshirt.jpg"  # Replace with a valid image URL or path
    },
    {
        "name": "Dress",
        "category": "Women",
        "description": "A stylish summer dress.",
        "image": "https://example.com/women_dress.jpg"  # Replace with a valid image URL or path
    },
    {
        "name": "Jeans",
        "category": "Men",
        "description": "Classic blue jeans.",
        "image": "https://example.com/men_jeans.jpg"  # Replace with a valid image URL or path
    },
    {
        "name": "Skirt",
        "category": "Women",
        "description": "A knee-length skirt.",
        "image": "https://example.com/women_skirt.jpg"  # Replace with a valid image URL or path
    },
    {
        "name": "Kids T-shirt",
        "category": "Kids",
        "description": "A playful T-shirt for kids.",
        "image": "https://example.com/kids_tshirt.jpg"  # Replace with a valid image URL or path
    },
    {
        "name": "Kids Shorts",
        "category": "Kids",
        "description": "Comfortable shorts for kids.",
        "image": "https://example.com/kids_shorts.jpg"  # Replace with a valid image URL or path
    },
]

# App title
st.title("Fashion Brand Product Search")

# Filter options
st.sidebar.header("Filter Options")
category_filter = st.sidebar.selectbox("Select Category", ["All", "Men", "Women", "Kids"])

# Search bar
search_query = st.text_input("Search for a product")

# Filter products based on the selected category
if category_filter != "All":
    filtered_products = [product for product in products if product["category"] == category_filter]
else:
    filtered_products = products

# Display the results
if search_query:
    search_results = [product for product in filtered_products if search_query.lower() in product["name"].lower()]
else:
    search_results = filtered_products

if search_results:
    for product in search_results:
        st.subheader(product["name"])
        st.image(product["image"], width=250)
        st.text(product["description"])
else:
    st.write("No products found.")

# Run the Streamlit app with: streamlit run <script_name>.py
