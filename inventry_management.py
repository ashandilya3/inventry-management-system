import sqlite3

# Connect/Create database
conn = sqlite3.connect('inventory.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL
            )''')
conn.commit()

def add_product(name, quantity):
    c.execute("INSERT INTO products (name, quantity) VALUES (?, ?)", (name, quantity))
    conn.commit()
    print(f"Product '{name}' added with quantity {quantity}.")

def update_product(name, quantity):
    c.execute("UPDATE products SET quantity = ? WHERE name = ?", (quantity, name))
    conn.commit()
    print(f"Product '{name}' updated to quantity {quantity}.")

def delete_product(name):
    c.execute("DELETE FROM products WHERE name = ?", (name,))
    conn.commit()
    print(f"Product '{name}' deleted.")

def view_inventory():
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    if products:
        print("\nCurrent Inventory:")
        for prod in products:
            print(f"ID: {prod[0]}, Name: {prod[1]}, Quantity: {prod[2]}")
    else:
        print("Inventory is empty.")

def main():
    while True:
        print("\n1. Add Product\n2. Update Product\n3. Delete Product\n4. View Inventory\n5. Exit")
        choice = input("Choose option: ")
        
        if choice == '1':
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            add_product(name, quantity)
        elif choice == '2':
            name = input("Enter product name to update: ")
            quantity = int(input("Enter new quantity: "))
            update_product(name, quantity)
        elif choice == '3':
            name = input("Enter product name to delete: ")
            delete_product(name)
        elif choice == '4':
            view_inventory()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
