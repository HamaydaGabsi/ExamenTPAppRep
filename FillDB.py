import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='ho1_sales')
cursor = cnx.cursor()

# Execute the query
# query = "CREATE TABLE sales (\
#          id INT PRIMARY KEY,\
#          product_name VARCHAR(50) NOT NULL,\
#          sale_date DATE NOT NULL\
#         );"
query =" INSERT INTO sales (id, product_name, sale_date) VALUES \
        (1, 'Product A', '2023-05-01'), \
        (2, 'Product B', '2023-05-02'), \
        (3, 'Product C', '2023-05-02'), \
        (4, 'Product A', '2023-05-03')"
cursor.execute(query)

# Commit the changes
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()
# APP_PORT=3000
# DB_HOST=localhost
# DB_PORT=3306
# DB_TYPE=mysql
# DB_USERNAME=root
# DB_PASSWORD=
# DB_NAME=cv_nest
