import tkinter as tk
from tkinter import ttk, messagebox

# Sample Inventory
inventory = {
    "Apples": {"price": 2.5, "stock": 50},
    "Bananas": {"price": 1.2, "stock": 100},
    "Milk": {"price": 3.0, "stock": 30},
    "Bread": {"price": 2.0, "stock": 20},
}

# Cart to hold selected items
cart = {}


# Function to add item to cart
def add_to_cart():
    selected_item = item_var.get()
    quantity = int(quantity_var.get())

    if selected_item not in inventory:
        messagebox.showerror("Error", "Item not found!")
        return

    if inventory[selected_item]["stock"] < quantity:
        messagebox.showerror("Error", "Insufficient stock!")
        return

    # Update cart and inventory
    if selected_item in cart:
        cart[selected_item] += quantity
    else:
        cart[selected_item] = quantity

    inventory[selected_item]["stock"] -= quantity
    update_cart()
    update_inventory()


# Function to remove item from cart
def remove_from_cart():
    selected_item = cart_var.get()
    if selected_item not in cart:
        messagebox.showerror("Error", "Item not in cart!")
        return

    # Restore stock and remove from cart
    inventory[selected_item]["stock"] += cart[selected_item]
    del cart[selected_item]
    update_cart()
    update_inventory()


# Function to update cart view
def update_cart():
    cart_list.delete(0, tk.END)
    for item, quantity in cart.items():
        price = inventory[item]["price"]
        cart_list.insert(tk.END, f"{item} - {quantity} x ${price:.2f}")


# Function to update inventory view
def update_inventory():
    inventory_list.delete(0, tk.END)
    for item, details in inventory.items():
        inventory_list.insert(tk.END, f"{item} - ${details['price']:.2f} - {details['stock']} left")


# Function to calculate total bill
def calculate_total():
    total = sum(inventory[item]["price"] * quantity for item, quantity in cart.items())
    messagebox.showinfo("Total Bill", f"Total Amount: ${total:.2f}")


# Create main window
root = tk.Tk()
root.title("Grocery Store POS System")
root.geometry("600x600")

# Inventory Section
tk.Label(root, text="Inventory").grid(row=0, column=0, padx=10, pady=10)
inventory_list = tk.Listbox(root, width=40)
inventory_list.grid(row=1, column=0, padx=10, pady=10)
update_inventory()

# Add to Cart Section
tk.Label(root, text="Add to Cart").grid(row=0, column=1, padx=10, pady=10)
item_var = tk.StringVar()
quantity_var = tk.StringVar(value="1")
tk.Entry(root, textvariable=item_var, width=20).grid(row=1, column=1, padx=10)
tk.Entry(root, textvariable=quantity_var, width=5).grid(row=1, column=2, padx=10)
tk.Button(root, text="Add", command=add_to_cart).grid(row=1, column=3, padx=10)

# Cart Section
tk.Label(root, text="Cart").grid(row=2, column=0, padx=10, pady=10)
cart_list = tk.Listbox(root, width=40)
cart_list.grid(row=3, column=0, padx=10, pady=10)
cart_var = tk.StringVar()
tk.Entry(root, textvariable=cart_var, width=20).grid(row=4, column=0, padx=10)
tk.Button(root, text="Remove", command=remove_from_cart).grid(row=4, column=1, padx=10)

# Billing Section
tk.Button(root, text="Calculate Total", command=calculate_total).grid(row=5, column=0, padx=10, pady=10)

# Run the app
root.mainloop()
