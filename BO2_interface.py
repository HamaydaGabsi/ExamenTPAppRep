import tkinter as tk
from BO2_server import send_sales_data

class BO2Interface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("BO2 Interface")
        self.pack()

        # Create the 'Send Sales Data' button
        self.send_sales_btn = tk.Button(self)
        self.send_sales_btn["text"] = "Send Sales Data"
        self.send_sales_btn["command"] = self.send_sales_data
        self.send_sales_btn.pack(side="top")

    def send_sales_data(self):
        # Call the send_sales_data() function from BO2_server.py
        send_sales_data()
        print('Sales data sent from BO2')

if __name__ == '__main__':
    root = tk.Tk()
    app = BO2Interface(master=root)
    app.mainloop()
