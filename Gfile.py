import streamlit as st
import pandas as pd
import openpyxl as op

# Ánh xạ đường dây → file Excel
tendz_map = {
    "Đường dây 273 KrongBuk - 271 Nha Trang": "krb-nt.xlsx",
    "Đường dây 272 Thiên Tân - 271 Cam Ranh": "dn-nt.xlsx"
    }

# Ánh xạ đường dây → danh sách các TBA tương ứng
tba_map = {
    "Đường dây 273 KrongBuk - 271 Nha Trang": [
        "Trạm biến áp 220kV Nha Trang",
        "Trạm biến áp 220kV KrongBuk"
    ],
    "Đường dây 272 Thiên Tân - 271 Cam Ranh": [
        "Trạm biến áp 220kV Cam Ranh",
        "Trạm biến áp 220kV Thiên Tân"
    ]
}
#Ánh xạ tba đến lũy kế ==========================================================
tba_to_column= {
    "Trạm biến áp 220kV Nha Trang":"Lũy kế",
    "Trạm biến áp 220kV Cam Ranh":"Lũy kế",
    "Trạm biến áp 220kV KrongBuk": "Lũy kế 1",
    "Trạm biến áp 220kV Thiên Tân":"Lũy kế 1"
}

# Chọn đường dây=================================================================
def select_name_dz():
    select_dz = st.selectbox("📂 Hãy chọn đường dây", list(tendz_map.keys()))
    return select_dz

def select_tba_1(select_dz):
    select_tba = tba_map.get(select_dz,[])
    return select_tba

def ass_col_name(select_tba):
    col_name=tba_to_column.get(select_tba, None)
    return col_name

def accum(select_dz):
    excel_name= tendz_map.get(select_dz,None)
    if not excel_name:
        st.erro("❌ Không tìm thấy ánh xạ đúng cho đường dây đã chọn.")
        return None
    path_excel = f"data/{excel_name}"
    try:
        df = pd.read_excel(path_excel)
    except Exception as e:
        st.error(f"❌ Lỗi khi đọc file: {e}")
        return pd.DataFrame()
    return df
