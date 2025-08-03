import streamlit as st
import pandas as pd
import openpyxl as op
import Gfile as gf
import Algo as al

# Cài đặt định dạng trang web
st.set_page_config(page_title="Tra cứu sự cố",layout="wide",initial_sidebar_state="expanded")

# Cài đặt tittle và chế độ chia cột
colm1, colm2=st.columns([5,1],vertical_alignment="bottom")
colm1.title("📊 TRA CỨU SỰ CỐ" )
view_mode=colm2.toggle("🔄 Chế độ chia cột")

# Lựa chọn tình trạng đóng lặp lại
F79=al.initial_info()

#Cấu hình đường dây, tba
select_dz=gf.select_name_dz()
subs=gf.select_tba_1(select_dz)
df = gf.accum(select_dz)

#Chạy chương trình
colm6, colm7=st.columns(2)
if view_mode:
    with colm6:  #TẠI TBA 1 #cột 1
            al.process(subs[0],df,"subs_0")
    with colm7:#TẠI TBA 2 #cột 2
            al.process(subs[1],df,"subs_1")
else:   
    with st.expander(f"{subs[0]}"): #TẠI TBA 1 #cột 1
        al.process(subs[0], df,"subs_0")
    with st.expander(f"{subs[1]}"): #TẠI TBA 2 #cột 2
        al.process(subs[1], df,"subs_1")
# Xem tổng kê
# st.markdown("---")
# xem_tongke=st.checkbox("Xem tổng kê đường dây")
# if xem_tongke: df

# lat=12.47484
# lon=109.28699

# maps_url = f"https://www.google.com/maps?q={lat},{lon}"
# # Nút mở Google Maps
# if st.button("🔍 Loc trên Google Maps"):
#     st.markdown(f"[🗺️ Xem trên bản đồ]({maps_url})", unsafe_allow_html=True)


    









    # col_name=gf.ass_col_name(tba_1)
    # st.header(f"📋{tba_1}")
    # st.markdown("---")
    # dis87_2 = st.number_input(f"🔢 Nhập khoảng cách sự cố F87/2:", min_value=0)
    # dis21_2 = st.number_input(f"🔢 Nhập khoảng cách sự cố F21/2:", min_value=0)
    # result_87 = al.findx(dis87_2, df, "F87", col_name)
    # if result_87:
    #     al.info(df, result_87, "F87")
    # result_21 = al.findx(dis21_2, df, "F21", col_name)
    # if result_21:
    #     al.info(df, result_21, "F21")
