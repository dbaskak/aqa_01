# create table ща categories

"""
CREATE TABLE IF NOT EXISTS categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL
);
"""

# create table of products and foreign key categories

"""
CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    description TEXT,
    price NUMERIC(10, 2) NOT NULL,
    category_id INTEGER REFERENCES categories(category_id)
);
"""

# insertion data into categories table
"""
INSERT INTO categories (category_name) 
VALUES 
('Electronics'), 
('Clothing'), 
('Home Appliances');
"""
# insertion data into products table
"""
INSERT INTO products (product_name, description, price, category_id) 
VALUES 
('Smartphone', 'Latest model smartphone with 128GB storage', 599.99, 1),
('T-Shirt', 'Cotton t-shirt with logo', 19.99, 2),
('Blender', '500W kitchen blender', 49.99, 3),
('Laptop', 'High-performance laptop with 16GB RAM', 999.99, 1),
('Jeans', 'Denim jeans for casual wear', 49.99, 2);
"""

# JOIN request for getting information from tables products and categories
"""
SELECT products.product_name, products.description, products.price, categories.category_name
FROM products
JOIN categories ON products.category_id = categories.category_id;
"""