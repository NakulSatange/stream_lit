import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Sample product data
products = {
    "Men": [
        {"name": "Men's T-Shirt", "price": 20, "image": "men_tshirt.jpg"},
        {"name": "Men's Jeans", "price": 40, "image": "men_jeans.jpg"},
        {"name": "Men's Jacket", "price": 60, "image": "men_jacket.jpg"},
        {"name": "Men's Shoes", "price": 50, "image": "men_shoes.jpg"},
        {"name": "Men's Hat", "price": 15, "image": "men_hat.jpg"}
    ],
    "Women": [
        {"name": "Women's Dress", "price": 30, "image": "women_dress.jpg"},
        {"name": "Women's Skirt", "price": 25, "image": "women_skirt.jpg"},
        {"name": "Women's Blouse", "price": 35, "image": "women_blouse.jpg"},
        {"name": "Women's Shoes", "price": 45, "image": "women_shoes.jpg"},
        {"name": "Women's Bag", "price": 50, "image": "women_bag.jpg"}
    ],
    "Kids": [
        {"name": "Kids' T-Shirt", "price": 15, "image": "kids_tshirt.jpg"},
        {"name": "Kids' Shorts", "price": 20, "image": "kids_shorts.jpg"},
        {"name": "Kids' Jacket", "price": 30, "image": "kids_jacket.jpg"},
        {"name": "Kids' Shoes", "price": 25, "image": "kids_shoes.jpg"},
        {"name": "Kids' Hat", "price": 10, "image": "kids_hat.jpg"}
    ]
}

class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fashion and Retail Billing App")

        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.category_var = tk.StringVar(value="Men")
        self.create_widgets()

    def create_widgets(self):
        # Category selection
        ttk.Label(self.frame, text="Select Category:").grid(row=0, column=0, padx=5, pady=5)
        categories = ["Men", "Women", "Kids"]
        for idx, category in enumerate(categories):
            ttk.Radiobutton(self.frame, text=category, variable=self.category_var, value=category, command=self.update_products).grid(row=0, column=idx + 1, padx=5, pady=5)

        # Product display
        self.product_frame = ttk.Frame(self.frame)
        self.product_frame.grid(row=1, column=0, columnspan=4, pady=10)

        self.update_products()

    def update_products(self):
        # Clear previous products
        for widget in self.product_frame.winfo_children():
            widget.destroy()

        category = self.category_var.get()
        for idx, product in enumerate(products[category]):
            img = Image.open(product["image"]).resize((100, 100), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            ttk.Label(self.product_frame, image=img).grid(row=idx, column=0, padx=5, pady=5)
            ttk.Label(self.product_frame, text=product["name"]).grid(row=idx, column=1, padx=5, pady=5)
            ttk.Label(self.product_frame, text=f"${product['price']}").grid(row=idx, column=2, padx=5, pady=5)
            ttk.Button(self.product_frame, text="Add to Cart", command=lambda p=product: self.add_to_cart(p)).grid(row=idx, column=3, padx=5, pady=5)

    def add_to_cart(self, product):
        # Here, you can implement the functionality to add the product to the cart
        print(f"Added {product['name']} to cart!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()
