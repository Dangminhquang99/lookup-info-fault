import streamlit as st
import pandas as pd
import openpyxl as op



g_map=pd.read_excel("data/mapping.xlsx")                                                    #doc file mapping
tendz_map = pd.Series(g_map['TEN FILE'].values, index=g_map['TEN DZ']).to_dict()            #Anh xa ten duong day -> ten file
tba_map = pd.Series(zip(g_map['TBA1'], g_map['TBA2']), index=g_map['TEN DZ']).to_dict()     #Anh xa ten duong day -> ten TBA 1, TBA2

def select_name_dz():
    select_dz = st.selectbox("📂 Hãy chọn đường dây", list(tendz_map.keys()),index=None,placeholder="Chọn 01 đường dây trong danh sách") or st.stop()
    return select_dz

def select_tba_1(select_dz):
    select_tba = tba_map.get(select_dz,[])
    return select_tba

def accum(select_dz):
    excel_name= tendz_map.get(select_dz,None)
    if not excel_name:
        st.error("❌ Không tìm thấy ánh xạ đúng cho đường dây đã chọn.")
        return None
    path_excel = f"data/{excel_name}"
    try:
        df = pd.read_excel(path_excel)
    except Exception as e:
        st.error(f"❌ Lỗi khi đọc file: {e}")
        return pd.DataFrame()
    return df


# mapping=pd.read_excel("data/mapping.xlsx") #doc file mapping
# tendz_map = pd.Series(mapping['TEN FILE'].values, index=mapping['TEN DZ']).to_dict()            #Anh xa ten duong day -> ten file
# tba_map = pd.Series(zip(mapping['TBA1'], mapping['TBA2']), index=mapping['TEN DZ']).to_dict()   #Anh xa ten duong day -> ten TBA 1, TBA2

# def select_name_dz():
#     select_dz = st.selectbox("📂 Hãy chọn đường dây", list(tendz_map.keys()))
#     return select_dz

# def select_tba_1(select_dz):
#     select_tba = tba_map.get(select_dz,[])
#     return select_tba



# def accum(select_dz):
#     excel_name= tendz_map.get(select_dz,None)
#     if not excel_name:
#         st.erro("❌ Không tìm thấy ánh xạ đúng cho đường dây đã chọn.")
#         return None
#     path_excel = f"data/{excel_name}"
#     try:
#         df = pd.read_excel(path_excel)
#     except Exception as e:
#         st.error(f"❌ Lỗi khi đọc file: {e}")
#         return pd.DataFrame()
#     return df



# Ánh xạ đường dây → file Excel
# tendz_map = {
#     "Đường dây 273 KrongBuk - 271 Nha Trang": "krb-nt.xlsx",
#     "Đường dây 274 Cam Ranh - 274 Nha Trang": "274CR-274NT.xlsx"
#     }


# Ánh xạ đường dây → danh sách các TBA tương ứng
# tba_map = {
#     "Đường dây 273 KrongBuk - 271 Nha Trang": ["Trạm biến áp 220kV KrongBuk","Trạm biến áp 220kV Nha Trang"],
#     "Đường dây 274 Cam Ranh - 274 Nha Trang": ["Trạm biến áp 220kV Cam Ranh","Trạm biến áp 220kV Nha Trang"]
# }
