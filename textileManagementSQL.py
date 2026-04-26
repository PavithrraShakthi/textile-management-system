import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Goodday@1",
    database="textile_db"
)


cursor = conn.cursor()

# ----------------- FUNCTIONS -----------------

def show_categories():
    cursor.execute("SELECT category_name FROM categories")
    categories = cursor.fetchall()

    print("\nAVAILABLE CATEGORIES")
    print("-" * 40)

    for i, cat in enumerate(categories, start=1):
        print(f"{i}. {cat[0]}")

    return [cat[0] for cat in categories]


def show_products(category_name):
    query = """
    SELECT product_name, price
    FROM products p
    JOIN categories c ON p.category_id = c.category_id
    WHERE c.category_name = %s
    """

    cursor.execute(query, (category_name,))
    products = cursor.fetchall()

    print(f"\n--- {category_name.upper()} ---")
    print("-" * 40)

    for i, (name, price) in enumerate(products, start=1):
        print(f"{i}. {name} - Rs.{price}")

    return products


def buy_products(products):
    total = 0

    choice = int(input("\nEnter product number: "))
    quantity = int(input("Enter quantity: "))

    selected_product = products[choice - 1]
    price = selected_product[1]

    cost = price * quantity
    total += cost

    print(f"\nCost: Rs.{cost}")
    return total


# ----------------- MAIN PROGRAM -----------------

def main():
    grand_total = 0

    while True:
        categories = show_categories()

        try:
            choice = int(input("\nSelect category number: "))
            category_name = categories[choice - 1]
        except:
            print("Invalid choice!")
            continue

        products = show_products(category_name)
        total = buy_products(products)

        grand_total += total

        cont = input("\nDo you want to continue shopping? (y/n): ")
        if cont.lower() != 'y':
            break

    print("\n" + "=" * 40)
    print(f"TOTAL BILL: Rs.{grand_total}")
    print("=" * 40)


# ----------------- RUN -----------------
main()

# Close connection
cursor.close()
conn.close()
