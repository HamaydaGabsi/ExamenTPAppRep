import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='bo2_sales')
cursor = cnx.cursor()


# Execute the query
# query= "CREATE TABLE sales (\
#          id INT AUTO_INCREMENT PRIMARY KEY  ,\
#          product_name VARCHAR(50) NOT NULL,\
#          sale_date DATE NOT NULL,\
#          bo_id VARCHAR(50) NOT NULL \
#         );"
# queries.push( "CREATE TABLE sales (\
#          id INT AUTO_INCREMENT PRIMARY KEY  ,\
#          product_name VARCHAR(50) NOT NULL,\
#          sale_date DATE NOT NULL,\
#          isSync BOOLEAN NOT NULL DEFAULT FALSE\
#         );")
# queries.push(" INSERT INTO sales (product_name, sale_date) VALUES \
#         ('Product A', '2023-05-01'), \
#         ('Product B', '2023-05-02'), \
#         ('Product C', '2023-05-02'), \
#         ('Product D', '2023-05-03')")
query =(" INSERT INTO sales (product_name, sale_date) VALUES \
        ('Product 1', '2023-05-01'), \
        ('Product 2', '2023-05-02'), \
        ('Product 3', '2023-05-02'), \
        ('Product 4', '2023-05-03')")
# queries.push("ALTER TABLE sales ADD COLUMN isSync BOOLEAN NOT NULL DEFAULT FALSE;")
# queries.push( "CREATE TRIGGER sync_sales\
#           AFTER UPDATE ON sales\
#           FOR EACH ROW\
#           BEGIN\
#             IF NEW.isSync = TRUE THEN\
#             SET NEW.isSync = FALSE;\
#           END IF;\
#         END;")
# query="DELIMITER //\
#       CREATE TRIGGER set_sync_false BEFORE UPDATE ON sales\
#       FOR EACH ROW\
#       BEGIN\
#         IF NEW.product_name <> OLD.product_name OR NEW.sale_date <> OLD.sale_date THEN\
#               SET NEW.isSync = 0;\
#           END IF;\
#       END//\
#       DELIMITER ;"


print(query)
cursor.execute(query)


# Commit the changes
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()
