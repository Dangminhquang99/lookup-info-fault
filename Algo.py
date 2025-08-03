import streamlit as st
import pandas as pd
import Gfile as gf

def initial_info():
    TimeF=st.text_input("🔢 Thời gian sự cố",placeholder="00:00:00 ngày 01/01/2025")
    F79 = st.radio(
    "### **Tình trạng đóng lặp lại:**",[":green[Thành công] :white_check_mark:", ":red[Không thành công] :x:"],index=None, horizontal=True)
    return F79



def find_positions(value, data,role_name,subs_no):
    lower=0     #Khoi tao lower bang 0
    result=None #Khoi tao result bang None nham tranh gop loi

    if 'Chiều dài' not in data.columns or data.empty:
        st.error(f"❌ Dữ liệu không hợp lệ hoặc thiếu cột 'Chiều dài'")
        return None
    if subs_no=="subs_0":
        for i in range(len(data)-1):
            lower=data['Chiều dài'].iloc[i]+lower
            upper=lower+data['Chiều dài'].iloc[i+1]
            if value==lower:        #Neu value bang lower
                result = data['Vị trí'].iloc[i-1],data['Vị trí'].iloc[i], data['Vị trí'].iloc[i + 1]  
            elif min(lower, upper) < value <= max(lower, upper):
                result = data['Vị trí'].iloc[i], data['Vị trí'].iloc[i + 1]

    if subs_no=="subs_1":           #TBA so 1
        for i in range(len(data)-1,-1,-1):
            lower=data['Chiều dài'].iloc[i]+lower
            upper=lower+data['Chiều dài'].iloc[i-1]
            if value==lower and i!=len(data)-1:
                result = data['Vị trí'].iloc[i-1],data['Vị trí'].iloc[i], data['Vị trí'].iloc[i + 1]   
            elif min(lower, upper) < value <= max(lower, upper):
                result = data['Vị trí'].iloc[i - 1],data['Vị trí'].iloc[i]
        
                
    if value:
        if not result:
            st.warning(f"⚠️ Không tìm thấy khoảng phù hợp với giá trị đã nhập, hãy đảm bảo rằng giá trị nằm trong phạm vi chiều dài của đường dây! ")
        elif len(result)==2:
            st.info(f"🔍 Khoảng cách rơ le {role_name} tương đương khoảng cột {result[0]} - {result[1]}.")
        elif len(result)==3:
            st.info(f"🔍 Khoảng cách rơ le {role_name} tương đương khoảng cột {result[0]} - {result[1]} - {result[2]}.")          
        return result
    return None


def info(df, result, role_name):
    if not result:
        st.warning(f"⚠️ Không có dữ liệu kết quả để hiển thị cho {role_name}.")
        return
    if 'Vị trí' not in df.columns:
        st.error("❌ File thông tin cột thiếu cột 'Vị trí'.")
        return
    get_col=df.query("`Vị trí` in @result")[['Vị trí','Khoảng cột', 'Công dụng cột','Thứ tự pha','Chiều dài']]
    st.write(get_col.T)

def process(subs, df, subs_no):
    st.header(f"📋{subs}")
    st.write(f" 🔍***Tổng chiều dài đường dây: {df['Chiều dài'].sum()} m***")
    st.markdown("---")
    dis87_2 = st.number_input(f"🔢 Nhập khoảng cách sự cố F87/{subs}:", min_value=0,step=500)
    dis21_2 = st.number_input(f"🔢 Nhập khoảng cách sự cố F21/{subs}:", min_value=0,step=500)
    result_87 = find_positions(dis87_2, df, "F87", subs_no)
    if result_87:
        info(df, result_87, "F87")
        directions (df, result_87)
    result_21 = find_positions(dis21_2, df, "F21", subs_no)
    if result_21:
        info(df, result_21, "F21")
        directions (df, result_21)
    return


 
def directions (df, result):
    if result:
        lat=df.query("`Vị trí` in @result")['Latitude']
        lon=df.query("`Vị trí` in @result")['Longtitude']
        maps_url_0 = f"https://www.google.com/maps?q={lat.iloc[0]},{lon.iloc[0]}"
        st.markdown(f"[🗺️ Xem trên bản đồ: VT {result[0]}]({maps_url_0})", unsafe_allow_html=True)
        maps_url_1 = f"https://www.google.com/maps?q={lat.iloc[1]},{lon.iloc[1]}"
        st.markdown(f"[🗺️ Xem trên bản đồ: VT {result[1]}]({maps_url_1})", unsafe_allow_html=True)
    return None
    

    # row_index = df[df['Vị trí']==v1].index[0]





     
 # def findx(dis, dataframe, role_name, col_name):
#     if dis:
#         result = find_positions(dis, dataframe, col_name)
#         if result:
#             st.info(f"🔍 Khoảng cách rơ le {role_name} tương đương khoảng cột {result[0]} - {result[1]}.")
#         else:
#             st.warning("⚠️ Không tìm thấy khoảng phù hợp với giá trị đã nhập.")
#         return result
#     return None

# def findx(dis, dataframe, role_name):
#     if dis:
#         result = find_positions(dis, dataframe)
#         if result:
#             st.info(f"🔍 Khoảng cách rơ le {role_name} tương đương khoảng cột {result[0]} - {result[1]}.")
#         else:
#             st.warning("⚠️ Không tìm thấy khoảng phù hợp với giá trị đã nhập.")
#         return result
#     return None    
     
# def process(subs, df):
#     col_name=gf.ass_col_name(subs)
#     st.header(f"📋{subs}")
#     st.markdown("---")
#     dis87_2 = st.number_input(f"🔢 Nhập khoảng cách sự cố F87/{subs}:", min_value=0)
#     dis21_2 = st.number_input(f"🔢 Nhập khoảng cách sự cố F21/{subs}:", min_value=0)
#     result_87 = findx(dis87_2, df, "F87", col_name)
#     if result_87:
#         info(df, result_87, "F87")
#     result_21 = findx(dis21_2, df, "F21", col_name)
#     if result_21:
#         info(df, result_21, "F21") 
 
# def find_positions(value, data, col_name):
#     if col_name not in data.columns or data.empty:
#         st.error(f"❌ Dữ liệu không hợp lệ hoặc thiếu cột '{col_name}'.")
#         return None
#     for i in range(len(data) - 1):
#         lower = data[col_name].iloc[i]
#         upper = data[col_name].iloc[i + 1]
#         if min(lower, upper) <= value <= max(lower, upper):
#             return data['Vị trí'].iloc[i], data['Vị trí'].iloc[i + 1]
#     return None        
    # row_index = df[df['Vị trí']==v1].index[0]
    # st.header(f"THÔNG TIN VỊ TRÍ {v1}")
    # cong_dung_cot=df.loc[row_index,'Công dụng cột']
    # st.write(f"Công dụng cột: {cong_dung_cot}")
    # Thu_tu_pha=df.loc[row_index,'Thứ tự pha']
    # st.write(f"Thứ tự pha: {Thu_tu_pha}")
    # goc_lai=df.loc[row_index,'Góc lái']
    # st.write(f"Góc lái: {goc_lai}")
    # loai_cot=df.loc[row_index,'Loại cột']
    # st.write(f"Loại cột: {loai_cot}")
    # chieu_cao_cot=df.loc[row_index,'Chiều cao cột']
    # st.write(f"Chiều cao cột: {chieu_cao_cot} m")
    # loai_tiep_dia=df.loc[row_index,'Loại tiếp địa']
    # st.write(f"Loại tiếp địa: {loai_tiep_dia}")
    # loai_day_dan=df.loc[row_index,'Loại dây dẫn']
    # st.write(f"Loại dây dẫn: {loai_day_dan}")
    # loai_cach_dien=df.loc[row_index,'Loại cách điện']
    # st.write(f"Loại cách điện: {loai_cach_dien}")
    # loai_cap_quang=df.loc[row_index,'Loại cáp quang']
    # st.write(f"Loại cáp quang: {loai_cap_quang}")
    # hanh_lang=df.loc[row_index,'Hành lang']
    # st.write(f"Hành lang: {hanh_lang}")
    
    
    
    
    # st.write(df.loc[df[df['Vị trí']==v1].index,'TTP'])
    # st.write(df.loc[151,'TTP'])
     # st.write(f"Vị trí {v1}")
    # index=df[df['Vị trí']==v1].index
    # index=df[df['Vị trí']==v1].index
    
    
    
    # selected_rows = dataframe[dataframe['Vị trí'].isin([v1, v2])]
    # if selected_rows.empty:
    #     st.warning("⚠️ Không tìm thấy thông tin tương ứng trong file thông tin.")
    # else:
    #     st.subheader(f"📋 Thông tin chi tiết các cột theo {role_name}:")
    #     st.table(selected_rows)
    # return v1, v2


# def info(dataframe, result, role_name):
#     if not result:
#         st.warning(f"⚠️ Không có dữ liệu kết quả để hiển thị cho {role_name}.")
#         return
#     if 'Vị trí' not in dataframe.columns:
#         st.error("❌ File thông tin cột thiếu cột 'Vị trí'.")
#         return
#     v1, v2 = result
#     selected_rows = dataframe[dataframe['Vị trí'].isin([v1, v2])]
#     if selected_rows.empty:
#         st.warning("⚠️ Không tìm thấy thông tin tương ứng trong file thông tin.")
#     else:
#         st.subheader(f"📋 Thông tin chi tiết các cột theo {role_name}:")
#         st.table(selected_rows)

