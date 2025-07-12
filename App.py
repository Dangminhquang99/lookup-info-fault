import streamlit as st
import pandas as pd
import openpyxl as op
import Gfile as gf
import Algo as al

#Cài đặt định dạng trang web
st.set_page_config(page_title="Tra cứu sự cố",layout="wide",initial_sidebar_state="expanded")
st.title("📊 TRA CỨU SỰ CỐ" )

#Cấu hình đường dây
select_dz=gf.select_name_dz()
tba_0, tba_1=gf.select_tba_1(select_dz)
df = gf.accum(select_dz)
col1, col2=st.columns(2)
with col1:  #TẠI TBA 1 #cột 1
    col_name=gf.ass_col_name(tba_0)
    st.header(f"-----------{tba_0}----------")
    st.markdown("---")
    dis87_1 = st.number_input(f"🔢 Nhập khoảng cách sự cố F87/1:", min_value=0)
    dis21_1 = st.number_input(f"🔢 Nhập khoảng cách sự cố F21/1:", min_value=0)
    result_87 = al.findx(dis87_1, df, "F87", col_name)
    if result_87:
        al.info(df, result_87, "F87")
    result_21 = al.findx(dis21_1, df, "F21", col_name)
    if result_21:
        al.info(df, result_21, "F21")
        
with col2:#TẠI TBA 2 #cột 2
    col_name=gf.ass_col_name(tba_1)
    st.header(f"-----------{tba_1}-----------")
    st.markdown("---")
    dis87_2 = st.number_input(f"🔢 Nhập khoảng cách sự cố F87/2:", min_value=0)
    dis21_2 = st.number_input(f"🔢 Nhập khoảng cách sự cố F21/2:", min_value=0)
    result_87 = al.findx(dis87_2, df, "F87", col_name)
    if result_87:
        al.info(df, result_87, "F87")
    result_21 = al.findx(dis21_2, df, "F21", col_name)
    if result_21:
        al.info(df, result_21, "F21")
