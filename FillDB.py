import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='bo2_sales')
cursor = cnx.cursor()

# Execute the query
# query = "CREATE TABLE sales (\
#          id INT AUTO_INCREMENT PRIMARY KEY  ,\
#          product_name VARCHAR(50) NOT NULL,\
#          sale_date DATE NOT NULL,\
#          isSync BOOLEAN NOT NULL DEFAULT FALSE\
#         );"
query =" INSERT INTO sales (product_name, sale_date) VALUES \
        ('Product A', '2023-05-01'), \
        ('Product B', '2023-05-02'), \
        ('Product C', '2023-05-02'), \
        ('Product D', '2023-05-03')"
# query = "ALTER TABLE sales ADD COLUMN isSync BOOLEAN NOT NULL DEFAULT FALSE;"
cursor.execute(query)

# Commit the changes
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()
