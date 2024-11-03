import sqlite3

# connection to DB (or creating if not exist))
connection = sqlite3.connect('shop.db')

try:
    print("Connected to the database successfully!")
    cursor = connection.cursor()

    # 1. creation categories table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT NOT NULL
        )
    ''')

    # 2. creation products table with foreign key 'categories'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(category_id)
        )
    ''')
    print("Tables created successfully!")

    # 3. insertion data into categories table
    cursor.execute("INSERT INTO categories (category_name) VALUES ('Electronics')")
    cursor.execute("INSERT INTO categories (category_name) VALUES ('Clothing')")
    cursor.execute("INSERT INTO categories (category_name) VALUES ('Home Appliances')")

    # 4. insertion data into  products table
    cursor.execute(
        "INSERT INTO products (product_name, description, price, category_id) VALUES ('Smartphone', 'Latest model smartphone with 128GB storage', 599.99, 1)")
    cursor.execute(
        "INSERT INTO products (product_name, description, price, category_id) VALUES ('T-Shirt', 'Cotton t-shirt with logo', 19.99, 2)")
    cursor.execute(
        "INSERT INTO products (product_name, description, price, category_id) VALUES ('Blender', '500W kitchen blender', 49.99, 3)")
    cursor.execute(
        "INSERT INTO products (product_name, description, price, category_id) VALUES ('Laptop', 'High-performance laptop with 16GB RAM', 999.99, 1)")
    cursor.execute(
        "INSERT INTO products (product_name, description, price, category_id) VALUES ('Jeans', 'Denim jeans for casual wear', 49.99, 2)")

    # saving changes in BD
    connection.commit()
    print("Data inserted successfully!")

    # 5. executing JOIN-request for getting products and categories
    cursor.execute('''
        SELECT products.product_name, products.description, products.price, categories.category_name
        FROM products
        JOIN categories ON products.category_id = categories.category_id
    ''')

    # get and print results
    records = cursor.fetchall()
    print("Products and their categories:")
    for row in records:
        print(f"Product: {row[0]}, Description: {row[1]}, Price: {row[2]}, Category: {row[3]}")

except (Exception, sqlite3.Error) as error:
    print("Error while connecting to SQLite", error)

finally:
    # connection closing
    if connection:
        cursor.close()
        connection.close()
        print("SQLite connection is closed")