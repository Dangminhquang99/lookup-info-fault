import streamlit as st
import pandas as pd
import Gfile as gf

def find_positions(value, data, col_name):
    if col_name not in data.columns or data.empty:
        st.error(f"❌ Dữ liệu không hợp lệ hoặc thiếu cột '{col_name}'.")
        return None
    for i in range(len(data) - 1):
        lower = data[col_name].iloc[i]
        upper = data[col_name].iloc[i + 1]
        if min(lower, upper) <= value <= max(lower, upper):
            return data['Vị trí'].iloc[i], data['Vị trí'].iloc[i + 1]
    return None

def findx(dis, dataframe, role_name, col_name):
    if dis:
        result = find_positions(dis, dataframe, col_name)
        if result:
            st.info(f"🔍 Khoảng cách rơ le {role_name} tương đương khoảng cột {result[0]} - {result[1]}.")
        else:
            st.warning("⚠️ Không tìm thấy khoảng phù hợp với giá trị đã nhập.")
        return result
    return None


def info(df, result, role_name):
    if not result:
        st.warning(f"⚠️ Không có dữ liệu kết quả để hiển thị cho {role_name}.")
        return
    if 'Vị trí' not in df.columns:
        st.error("❌ File thông tin cột thiếu cột 'Vị trí'.")
        return
    v1, v2 = result
    row_index = df[df['Vị trí']==v1].index[0]
    st.header(f"THÔNG TIN VỊ TRÍ {v1}")
    cong_dung_cot=df.loc[row_index,'Công dụng cột']
    st.write(f"Công dụng cột: {cong_dung_cot}")
    Thu_tu_pha=df.loc[row_index,'Thứ tự pha']
    st.write(f"Thứ tự pha: {Thu_tu_pha}")
    goc_lai=df.loc[row_index,'Góc lái']
    st.write(f"Góc lái: {goc_lai}")
    loai_cot=df.loc[row_index,'Loại cột']
    st.write(f"Loại cột: {loai_cot}")
    chieu_cao_cot=df.loc[row_index,'Chiều cao cột']
    st.write(f"Chiều cao cột: {chieu_cao_cot} m")
    loai_tiep_dia=df.loc[row_index,'Loại tiếp địa']
    st.write(f"Loại tiếp địa: {loai_tiep_dia}")
    loai_day_dan=df.loc[row_index,'Loại dây dẫn']
    st.write(f"Loại dây dẫn: {loai_day_dan}")
    loai_cach_dien=df.loc[row_index,'Loại cách điện']
    st.write(f"Loại cách điện: {loai_cach_dien}")
    loai_cap_quang=df.loc[row_index,'Loại cáp quang']
    st.write(f"Loại cáp quang: {loai_cap_quang}")
    hanh_lang=df.loc[row_index,'Hành lang']
    st.write(f"Hành lang: {hanh_lang}")
