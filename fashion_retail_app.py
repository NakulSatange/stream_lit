import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Sample product data
products = {
    'Men': [
        {'name': 'Leather Jacket', 'price': 120, 'image': 'images/leather_jacket.jpg'},
        {'name': 'Casual Shirt', 'price': 40, 'image': 'images/casual_shirt.jpg'},
        {'name': 'Jeans', 'price': 60, 'image': 'images/jeans.jpg'},
        {'name': 'Sneakers', 'price': 80, 'image': 'images/sneakers.jpg'},
        {'name': 'Suit', 'price': 250, 'image': 'images/suit.jpg'},
        {'name': 'Blazer', 'price': 150, 'image': 'images/blazer.jpg'},
        {'name': 'Chinos', 'price': 70, 'image': 'images/chinos.jpg'},
        {'name': 'Sweater', 'price': 55, 'image': 'images/sweater.jpg'},
        {'name': 'Shorts', 'price': 35, 'image': 'images/shorts.jpg'},
        {'name': 'Boots', 'price': 90, 'image': 'images/boots.jpg'},
    ],
    'Women': [
        {'name': 'Summer Dress', 'price': 60, 'image': 'images/summer_dress.jpg'},
        {'name': 'Winter Coat', 'price': 150, 'image': 'images/winter_coat.jpg'},
        {'name': 'Skirt', 'price': 50, 'image': 'images/skirt.jpg'},
        {'name': 'High Heels', 'price': 70, 'image': 'images/high_heels.jpg'},
        {'name': 'Blouse', 'price': 45, 'image': 'images/blouse.jpg'},
        {'name': 'Cardigan', 'price': 55, 'image': 'images/cardigan.jpg'},
        {'name': 'Jumpsuit', 'price': 85, 'image': 'images/jumpsuit.jpg'},
        {'name': 'Leggings', 'price': 40, 'image': 'images/leggings.jpg'},
        {'name': 'Sunglasses', 'price': 25, 'image': 'images/sunglasses.jpg'},
        {'name': 'Handbag', 'price': 120, 'image': 'images/handbag.jpg'},
    ],
    'Kids': [
        {'name': 'Teddy Bear Hoodie', 'price': 30, 'image': 'images/teddy_bear_hoodie.jpg'},
        {'name': 'School Uniform', 'price': 45, 'image': 'images/school_uniform.jpg'},
        {'name': 'Raincoat', 'price': 40, 'image': 'images/raincoat.jpg'},
        {'name': 'Sneakers', 'price': 35, 'image': 'images/kid_sneakers.jpg'},
        {'name': 'Play Dress', 'price': 25, 'image': 'images/play_dress.jpg'},
        {'name': 'Winter Jacket', 'price': 50, 'image': 'images/winter_jacket.jpg'},
        {'name': 'Pajamas', 'price': 28, 'image': 'images/pajamas.jpg'},
        {'name': 'Backpack', 'price': 38, 'image': 'images/backpack.jpg'},
        {'name': 'Beanie', 'price': 15, 'image': 'images/beanie.jpg'},
        {'name': 'Gloves', 'price': 18, 'image': 'images/gloves.jpg'},
    ]
}

class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Fashion Retail Billing App')
        self.root.geometry('1200x800')
        self.root.resizable(True, True)

        self.cart = []

        # Create Notebook
        self.tab_control = ttk.Notebook(root)
        self.tab_control.add(self.create_tab('Men'), text='Men')
        self.tab_control.add(self.create_tab('Women'), text='Women')
        self.tab_control.add(self.create_tab('Kids'), text='Kids')
        self.tab_control.pack(expand=1, fill='both')

        # Cart and Total Price Section
        self.cart_frame = ttk.Frame(root)
        self.cart_frame.pack(pady=10, padx=10, fill='x')

        self.cart_listbox = tk.Listbox(self.cart_frame, height=10, width=50)
        self.cart_listbox.pack(side='left', fill='y')

        self.scrollbar = tk.Scrollbar(self.cart_frame, orient='vertical', command=self.cart_listbox.yview)
        self.scrollbar.pack(side='right', fill='y')

        self.cart_listbox.config(yscrollcommand=self.scrollbar.set)

        self.total_price_label = tk.Label(root, text='Total Price: $0.00', font=('Arial', 14, 'bold'))
        self.total_price_label.pack(pady=10)

        self.checkout_button = tk.Button(root, text='Checkout', command=self.checkout, font=('Arial', 12, 'bold'))
        self.checkout_button.pack(pady=10)

    def create_tab(self, category):
        frame = ttk.Frame(self.tab_control)
        # Add products to the tab
        for i, product in enumerate(products[category]):
            self.add_product(frame, product, i)
        return frame

    def add_product(self, frame, product, index):
        img = Image.open(product['image'])
        img = img.resize((150, 150), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)

        # Create a frame for each product
        product_frame = ttk.Frame(frame)
        product_frame.grid(row=index // 5, column=index % 5, padx=10, pady=10, sticky='nsew')

        # Product Image
        label_img = tk.Label(product_frame, image=img_tk)
        label_img.image = img_tk  # Keep a reference to avoid garbage collection
        label_img.pack()

        # Product Name and Price
        label_name = tk.Label(product_frame, text=product['name'], font=('Arial', 12, 'bold'))
        label_name.pack()
        label_price = tk.Label(product_frame, text=f'${product["price"]:.2f}', font=('Arial', 10))
        label_price.pack()

        # Add to cart button
        add_button = tk.Button(product_frame, text='Add to Cart', command=lambda p=product: self.add_to_cart(p))
        add_button.pack(pady=5)

    def add_to_cart(self, product):
        self.cart.append(product)
        self.update_cart()

    def update_cart(self):
        self.cart_listbox.delete(0, tk.END)
        total_price = 0
        for product in self.cart:
            self.cart_listbox.insert(tk.END, f'{product["name"]} - ${product["price"]:.2f}')
            total_price += product['price']
        self.total_price_label.config(text=f'Total Price: ${total_price:.2f}')

    def checkout(self):
        if not self.cart:
            tk.messagebox.showinfo('Checkout', 'Your cart is empty!')
            return
        total_price = sum(product['price'] for product in self.cart)
        tk.messagebox.showinfo('Checkout', f'Your total amount is ${total_price:.2f}. Thank you for shopping with us!')
        self.cart.clear()
        self.update_cart()

def main():
    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
