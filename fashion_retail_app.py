import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Sample product data
products = {
    "Men": [
        {"name": "Men's Shirt", "price": 25, "image": "men_shirt.jpg"},
        {"name": "Men's Jeans", "price": 40, "image": "men_jeans.jpg"},
        {"name": "Men's Jacket", "price": 60, "image": "men_jacket.jpg"},
        {"name": "Men's Shoes", "price": 50, "image": "men_shoes.jpg"},
        {"name": "Men's Hat", "price": 15, "image": "men_hat.jpg"}
    ],
    "Women": [
        {"name": "Women's Dress", "price": 30, "image": "women_dress.jpg"},
        {"name": "Women's Skirt", "price": 25, "image": "women_skirt.jpg"},
        {"name": "Women's Jacket", "price": 35, "image": "women_jacket.jpg"},
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
        self.root.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        # Frame for category selection
        self.category_frame = ttk.Frame(self.root, padding="10")
        self.category_frame.pack(side=tk.TOP, fill=tk.X)

        # Category selection
        self.category_var = tk.StringVar(value="Men")
        ttk.Label(self.category_frame, text="Select Category:").pack(side=tk.LEFT, padx=5)
        categories = ["Men", "Women", "Kids"]
        for category in categories:
            ttk.Radiobutton(self.category_frame, text=category, variable=self.category_var, value=category, command=self.update_products).pack(side=tk.LEFT, padx=5)

        # Frame for displaying products
        self.product_frame = ttk.Frame(self.root, padding="10")
        self.product_frame.pack(fill=tk.BOTH, expand=True)

        self.update_products()

    def update_products(self):
        # Clear previous products
        for widget in self.product_frame.winfo_children():
            widget.destroy()

        category = self.category_var.get()
        for idx, product in enumerate(products[category]):
            img = Image.open(product["image"]).resize((150, 150), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            img_label = ttk.Label(self.product_frame, image=img)
            img_label.image = img  # Keep a reference to avoid garbage collection
            img_label.grid(row=idx, column=0, padx=10, pady=10)
            
            ttk.Label(self.product_frame, text=product["name"], font=("Arial", 12)).grid(row=idx, column=1, padx=10, pady=10)
            ttk.Label(self.product_frame, text=f"${product['price']}", font=("Arial", 12)).grid(row=idx, column=2, padx=10, pady=10)
            ttk.Button(self.product_frame, text="Add to Cart", command=lambda p=product: self.add_to_cart(p)).grid(row=idx, column=3, padx=10, pady=10)

    def add_to_cart(self, product):
        # For now, just print the product added
        print(f"Added {product['name']} to cart!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()
