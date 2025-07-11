import streamlit as st
import pandas as pd
import config as cf


#==============Hàm tìm giá trị==============
def find_positions(value, data):
    for i in range(len(data) - 1):
        lower = data['Lũy kế'].iloc[i]
        upper = data['Lũy kế'].iloc[i + 1]
        if min(lower, upper) <= value <= max(lower, upper):
            return data['Vị trí'].iloc[i], data['Vị trí'].iloc[i + 1]
    return None

#=================Tìm và hiển thị kết quả F87=================================
def findx (dis,dataframe,role_name):
    if dis:
        result = find_positions(dis, dataframe)
        if result:
            st.info(f"🔍 Khoảng cách rơ le {role_name} tương đương khoảng cột {result[0]} - {result[1]}.")
        else:
            st.warning("⚠️ Không tìm thấy khoảng phù hợp với giá trị đã nhập.")
    return result
            
#=================Tìm thông tin vị trí tương ứng====================================
def info (dataframe, result,role_name):
    if 'VITRI' not in dataframe.columns:
        st.error("❌ File thông tin cột thiếu cột 'VITRI'.")
    else:
        v1, v2 = result  #Gán biến result[1,2] sang biến v1, v2 
        selected_rows = dataframe[dataframe['VITRI'].isin([v1, v2])] #hàm isin giữ lại hàng chứa giá trị v1, v2. So sanh v1 v2 với giá trị ở cột VITRI, nếu trùng thì là true, không thì sẽ là false
        if selected_rows.empty:
            st.warning("⚠️ Không tìm thấy thông tin tương ứng trong file thông tin.")
        else:
            st.subheader(f"📋 Thông tin chi tiết các cột theo {role_name}:")
            st.table(selected_rows)
            
            
            
            
            
            
            
        

      
#         # df_info = pd.read_excel("data/Tke_krb.xlsx")
#         #         #Thong tin vi tri theo F87
        # if 'VITRI' not in df_info.columns:
#         #      st.error("❌ File thông tin cột thiếu cột 'VITRI'.")
#         # else:
#         #     # Lọc ra thông tin của 2 vị trí
#         #     v1, v2 = result87  # ví dụ: 247, 248
#         #     selected_rows = df_info[df_info['VITRI'].isin([v1, v2])]
#         #     if selected_rows.empty:
#         #         st.warning("⚠️ Không tìm thấy thông tin tương ứng trong file thông tin.")
#         #     else:
#         #         st.subheader("📋 Thông tin chi tiết các cột theo F87:")
#         #         st.table(selected_rows)
                
#         # #Thong tin vi tri theo F21
#         # if 'VITRI' not in df_info.columns:
#         #      st.error("❌ File thông tin cột thiếu cột 'VITRI'.")
#         # else:
#         #     # Lọc ra thông tin của 2 vị trí
#         #     v1, v2 = result21  # ví dụ: 247, 248
#         #     selected_rows = df_info[df_info['VITRI'].isin([v1, v2])]
#         #     if selected_rows.empty:
#         #         st.warning("⚠️ Không tìm thấy thông tin tương ứng trong file thông tin.")
#         #     else:
#         #         st.subheader("📋 Thông tin chi tiết các cột theo F21:")
#         #         st.table(selected_rows)                   
# except Exception as e:
#         st.error(f"❌ Lỗi khi đọc file: {e}")