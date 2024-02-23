import csv
import pandas as pd

# อ่านไฟล์ CSV และนำเข้าเป็น DataFrame
df = pd.read_csv('testScrip.csv')

product_codes = df["รหัสสินค้า"]
product_model = df["Meta : model"]
df["Meta : model"] = df["รหัสสินค้า"]
df.to_csv("NewtestScrip.csv", index=False)
# print(product_codes)
# # สร้าง Dictionary ที่เก็บ Order Code และ Model ที่จะนำเข้าใน DataFrame
# data_to_add = []
#
# # วนลูปผ่านแถวใน DataFrame และเก็บข้อมูลเข้า Dictionary
# for index, row in df.iterrows():
#     order_code = row['รหัสสินค้า']
#     model = row['Meta : model']
#     data_to_add.append({'รหัสสินค้า': order_code, 'Meta : model': model})
#
#     # หยุดการวนลูปหากมีข้อมูลใน Dictionary มากกว่าหรือเท่ากับ 10 แถว
#     if len(data_to_add) >= 10:
#         break
#
# # เพิ่มข้อมูลใน Dictionary เข้าไปใน DataFrame
# df = df.append(data_to_add, ignore_index=True)
#
# # พิมพ์ DataFrame ที่มีข้อมูลใหม่
# print(df)
