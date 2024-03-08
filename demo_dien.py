import tkinter as tk
from define import *

def submit():
    device_name = device_name_entry.get()
    maintenance_type = maintenance_type_var.get()
    maintenance_date = maintenance_date_entry.get()
    
    # Thực hiện xử lý dữ liệu ở đây, ví dụ: in ra các giá trị đã nhập
    print("Device Name:", device_name)
    print("Maintenance Type:", maintenance_type)
    print("Maintenance Date:", maintenance_date)

# Tạo cửa sổ
root = tk.Tk()
root.title("Maintenance Management")

#Chieu cao va chieu rong
root.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH,WINDOW_HEIGHT,WINDOW_POSITION_RIGHT,WINDOW_POSITION_DOWN))

# Tạo và định dạng giao diện
device_name_label = tk.Label(root, text="Device Name:")
device_name_label.grid(row=0, column=0, padx=10, pady=5)
device_name_entry = tk.Entry(root)
device_name_entry.grid(row=0, column=1, padx=10, pady=5)

maintenance_type_label = tk.Label(root, text="Maintenance Type:")
maintenance_type_label.grid(row=1, column=0, padx=10, pady=5)
maintenance_type_var = tk.StringVar(root)
maintenance_type_var.set("Scheduled")  # Thiết lập giá trị mặc định
maintenance_type_dropdown = tk.OptionMenu(root, maintenance_type_var, "Scheduled", "Emergency")
maintenance_type_dropdown.grid(row=1, column=1, padx=10, pady=5)

maintenance_date_label = tk.Label(root, text="Maintenance Date:")
maintenance_date_label.grid(row=2, column=0, padx=10, pady=5)
maintenance_date_entry = tk.Entry(root)
maintenance_date_entry.grid(row=2, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Chạy ứng dụng
root.mainloop()