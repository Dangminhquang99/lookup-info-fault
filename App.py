import streamlit as st
import pandas as pd
import openpyxl as op
import Gfile as gf
import Algo as al

# Cài đặt định dạng trang web
st.set_page_config(page_title="Tra cứu sự cố",layout="wide",initial_sidebar_state="expanded")

# Cài đặt tittle và chế độ chia cột

cola, colb=st.columns([5,1])
with cola:
    st.title("📊 TRA CỨU SỰ CỐ" )
with colb:
    view_mode = st.toggle("🔄 Chế độ chia cột")
    
#Cấu hình đường dây, tba
select_dz=gf.select_name_dz()
subs_0, subs_1=gf.select_tba_1(select_dz)
df = gf.accum(select_dz)

#Chạy chương trình
col1, col2=st.columns(2)
st.sidebar.selectbox("Hãy chọn công việc",["Tra cứu thông tin sự cố", "Tra cứu thông tin đường dây"])
if view_mode:
    with col1:  #TẠI TBA 1 #cột 1
        al.process(subs_0,df)
    with col2:#TẠI TBA 2 #cột 2
        al.process(subs_1,df)    
else:
    with st.expander(f"{subs_0}"): #TẠI TBA 1 #cột 1
        al.process(subs_0, df)
    with st.expander(f"{subs_1}"): #TẠI TBA 2 #cột 2
        al.process(subs_1, df)

#Xem tổng kê
st.markdown("---")
xem_tongke=st.checkbox("Xem tổng kê đường dây")
if xem_tongke: df
