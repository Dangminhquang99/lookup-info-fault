import streamlit as st
import pandas as pd
#import openpyxl as op
from config import accum
from Algo import findx, info

st.title("📊 TRA CỨU SỰ CỐ")

df, df2 = accum()

dis87 = st.number_input("🔢 Nhập khoảng cách sự cố F87:", min_value=0)
dis21 = st.number_input("🔢 Nhập khoảng cách sự cố F21:", min_value=0)
submit = st.button("🔍 Tra cứu")

if submit:
    result_87 = findx(dis87, df, "F87")
    if result_87:
        info(df2, result_87, "F87")

    result_21 = findx(dis21, df, "F21")
    if result_21:
        info(df2, result_21, "F21")
