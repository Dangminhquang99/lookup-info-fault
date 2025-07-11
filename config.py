import streamlit as st
import pandas as pd

#============== Truy xuat file luy ke de tinh toan=======================
def accum():
    tendz_map={
        "Đường dây 273 KrongBuk - 271 Nha Trang":["Krb-nt.xlsx","Tongke_krb.xlsx"],
        "Đường dây 272 Thiên Tân - 271 Cam Ranh":"Dn.xlsx"
        }
    choose_dz=st.selectbox("Hãy chọn đường dây",list(tendz_map.keys()))
    ten_file,ten_file2=tendz_map[choose_dz]
    path_dz=f"data/{ten_file}"
    path_tk=f"data/{ten_file2}"
    df = pd.read_excel(path_dz)
    df2 = pd.read_excel(path_tk)
    return df, df2

#============== Truy xuat file Tong ke theo đường dây=======================
