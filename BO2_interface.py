import tkinter as tk
from tkinter import ttk
import mysql.connector
from BO2_server import send_sales_data

class BO2Interface(tk.Frame):
    def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.master.title("BO2 Interface")
            self.pack(fill='both', expand=True)

            # Create the Treeview table to display sales data
            self.table_columns = ('Sale ID', 'Product', 'Date')
            self.treeview = ttk.Treeview(self, columns=self.table_columns, show='headings')
            self.treeview.column('Sale ID', width=100, anchor='center')
            self.treeview.column('Product', width=200, anchor='center')
            self.treeview.column('Date', width=120, anchor='center')

           
            self.treeview.heading('Sale ID', text='Sale ID')
            self.treeview.heading('Product', text='Product')
            self.treeview.heading('Date', text='Date')
           
            self.treeview.pack(pady=10)

            # Create the 'Refresh' button
            self.refresh_btn = ttk.Button(self, text="Refresh", command=self.refresh_table)
            self.refresh_btn.pack()

            # Create the 'Send Sales Data' button
            self.send_sales_btn = ttk.Button(self, text="Send Sales Data", command=self.send_sales_data)
            self.send_sales_btn.pack(pady=10)

            # Populate the table with initial data
            self.refresh_table()

    def refresh_table(self):
        # Clear the table
        self.treeview.delete(*self.treeview.get_children())

        # Connect to the BO database
        bo2_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bo2_sales"
        )

        # Fetch the unsynchronized sales data from the BO database
        cursor = bo2_db.cursor()
        query = "SELECT * FROM sales WHERE isSync = 0 ORDER BY sale_date DESC LIMIT 10"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()

        # Populate the table with the sales data
        for row in rows:
            self.treeview.insert("", tk.END, values=row)

        # Close the database connection
        bo2_db.close()

    def send_sales_data(self):
        # Call the send_sales_data() function from BO2_server.py
        send_sales_data()
        self.refresh_table()
        print('Sales data sent from BO2')

if __name__ == '__main__':
    root = tk.Tk()
    app = BO2Interface(master=root)
    app.mainloop()
