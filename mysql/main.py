from database import *

mysql = MySQL(user="root", password="123#@*qwe",host="10.93.12.156", port="3306", database_name="phone_info")

data = {
    "brand": "HUAWEI",
    "name": "Hornor V10",
    "serial": "165165sdf",
    "sdk version": 27,
    "CPU": "Kilin 90",
    "GPU": "Mali 1214"
}

mysql.insert(table_name="phone_list", data = data)

mysql.close()
