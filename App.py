import streamlit as st
import pandas as pd
import config as cf
from config import accum
import Algo as al
from Algo import find_positions
from Algo import findx
from Algo import info
#==========title=================================
st.title("📊 TRA CỨU SỰ CỐ")
#============Nhập giá trị khoảng cách====================
dis87 = st.number_input("🔢 Nhập khoảng cách sự cố F87:", min_value=0)
dis21 = st.number_input("🔢 Nhập khoảng cách sự cố F21:", min_value=0)
submit=st.button("submit")
if submit:
      df, df2 = accum()
      result=findx(dis87,df,"F87")
      info(df2,result, "F87")
      result=findx(dis21,df,"F21")
      info(df2,result,"F21")




# # =================Tìm và hiển thị kết quả F87=================================
# if dis21:
#     result21 = find_positions(dis21, df)
#     if result21:
#         st.info(f"🔍 Khoảng cách rơ le F21 tương đương khoảng cột {result21[0]} - {result21[1]}.")
#     else:
#         st.warning("⚠️ Không tìm thấy khoảng phù hợp với giá trị đã nhập.")












# Tracuu=st.button("Submit")

# try:
#     if Tracuu:
#         # Kiểm tra cột cần thiết
#         if 'Lũy kế' not in df.columns:
#             st.error("❌ File phải chứa cột 'Lũy kế'.")
#         else:
#             # Thêm cột vị trí nếu chưa có
#             if 'Vị trí' not in df.columns:
#                 df['Vị trí'] = df.index

#             def find_positions(value, data):
#                 for i in range(len(data) - 1):
#                     lower = data['Lũy kế'].iloc[i]
#                     upper = data['Lũy kế'].iloc[i + 1]
#                     if min(lower, upper) <= value <= max(lower, upper):
#                         return data['Vị trí'].iloc[i], data['Vị trí'].iloc[i + 1]
#                 return None

#             # Tìm và hiển thị kết quả F87
#             if dis87:
#                 result87 = find_positions(dis87, df)
#                 if result87:
#                     st.info(f"🔍 Khoảng cách rơ le F87 tương đương khoảng cột {result87[0]} - {result87[1]}.")
#                 else:
#                     st.warning("⚠️ Không tìm thấy khoảng phù hợp với giá trị đã nhập.")
#             # Tìm và hiển thị kết quả F21
#             if dis21:
#                 result21 = find_positions(dis21, df)
#                 if result21:
#                     st.info(f"🔍 Khoảng cách rơ le F21 tương đương khoảng cột {result21[0]} - {result21[1]}.")
#                 else:
#                     st.warning("⚠️ Không tìm thấy khoảng phù hợp với giá trị đã nhập.")
      
#         df_info = pd.read_excel("data/Tke_krb.xlsx")
#                 #Thong tin vi tri theo F87
#         if 'VITRI' not in df_info.columns:
#              st.error("❌ File thông tin cột thiếu cột 'VITRI'.")
#         else:
#             # Lọc ra thông tin của 2 vị trí
#             v1, v2 = result87  # ví dụ: 247, 248
#             selected_rows = df_info[df_info['VITRI'].isin([v1, v2])]
#             if selected_rows.empty:
#                 st.warning("⚠️ Không tìm thấy thông tin tương ứng trong file thông tin.")
#             else:
#                 st.subheader("📋 Thông tin chi tiết các cột theo F87:")
#                 st.table(selected_rows)
                
# #         #Thong tin vi tri theo F21
# #         if 'VITRI' not in df_info.columns:
# #              st.error("❌ File thông tin cột thiếu cột 'VITRI'.")
# #         else:
# #             # Lọc ra thông tin của 2 vị trí
# #             v1, v2 = result21  # ví dụ: 247, 248
# #             selected_rows = df_info[df_info['VITRI'].isin([v1, v2])]
# #             if selected_rows.empty:
# #                 st.warning("⚠️ Không tìm thấy thông tin tương ứng trong file thông tin.")
# #             else:
# #         #         st.subheader("📋 Thông tin chi tiết các cột theo F21:")
# #         #         st.table(selected_rows)                   
# except Exception as e:
#         st.error(f"❌ Lỗi khi đọc file: {e}")


















# Krb=st.sidebar.button("Đường dây 273 KrongBuk - 271 Nha Trang")
# DN=st.sidebar.button("Đường dây 272 Thiên Tân - 271 Cam Ranh")
# st.selectbox("Chọn đường dây:",["Đường dây 273 KrongBuk - 271 Nha Trang","Đường dây 272 Thiên Tân - 271 Cam Ranh"])
# st.form_submit_button("Submit")
# Tenfile = tendz_map[chondz]
# Duong_dan=f"data/{Tenfile}"


# Thuat toan
# try:
#     if Tracuu:
#         #Doc du lieu tu file exel
#         df = pd.read_excel("data/krb-nt.xlsx")
#         # Kiểm tra cột cần thiết
#         if 'Lũy kế' not in df.columns:
#             st.error("❌ File phải chứa cột 'Lũy kế'.")
#         else:
#             # Thêm cột vị trí nếu chưa có
#             if 'Vị trí' not in df.columns:
#                 df['Vị trí'] = df.index

#             def find_positions(value, data):
#                 for i in range(len(data) - 1):
#                     lower = data['Lũy kế'].iloc[i]
#                     upper = data['Lũy kế'].iloc[i + 1]
#                     if min(lower, upper) <= value <= max(lower, upper):
#                         return data['Vị trí'].iloc[i], data['Vị trí'].iloc[i + 1]
#                 return None

#             # Tìm và hiển thị kết quả F87
#             if dis87:
#                 result87 = find_positions(dis87, df)
#                 if result87:
#                     st.info(f"🔍 Khoảng cách rơ le F87 tương đương khoảng cột {result87[0]} - {result87[1]}.")
#                 else:
#                     st.warning("⚠️ Không tìm thấy khoảng phù hợp với giá trị đã nhập.")
#             # Tìm và hiển thị kết quả F21
#             if dis21:
#                 result21 = find_positions(dis21, df)
#                 if result21:
#                     st.info(f"🔍 Khoảng cách rơ le F21 tương đương khoảng cột {result21[0]} - {result21[1]}.")
#                 else:
#                     st.warning("⚠️ Không tìm thấy khoảng phù hợp với giá trị đã nhập.")
      
#         df_info = pd.read_excel("data/Tke_krb.xlsx")
        
#         #Thong tin vi tri theo F87
#         if 'VITRI' not in df_info.columns:
#              st.error("❌ File thông tin cột thiếu cột 'VITRI'.")
#         else:
#             # Lọc ra thông tin của 2 vị trí
#             v1, v2 = result87  # ví dụ: 247, 248
#             selected_rows = df_info[df_info['VITRI'].isin([v1, v2])]
#             if selected_rows.empty:
#                 st.warning("⚠️ Không tìm thấy thông tin tương ứng trong file thông tin.")
#             else:
#                 st.subheader("📋 Thông tin chi tiết các cột theo F87:")
#                 st.table(selected_rows)
                
#         #Thong tin vi tri theo F21
#         if 'VITRI' not in df_info.columns:
#              st.error("❌ File thông tin cột thiếu cột 'VITRI'.")
#         else:
#             # Lọc ra thông tin của 2 vị trí
#             v1, v2 = result21  # ví dụ: 247, 248
#             selected_rows = df_info[df_info['VITRI'].isin([v1, v2])]
#             if selected_rows.empty:
#                 st.warning("⚠️ Không tìm thấy thông tin tương ứng trong file thông tin.")
#             else:
#                 st.subheader("📋 Thông tin chi tiết các cột theo F21:")
#                 st.table(selected_rows)                   
# except Exception as e:
#         st.error(f"❌ Lỗi khi đọc file: {e}")
    
   
