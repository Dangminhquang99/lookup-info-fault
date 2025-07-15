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
    get_col=df.query("`Vị trí` in @result")[['Vị trí', 'Công dụng cột','Thứ tự pha','Loại cột','Chiều cao cột','Loại dây dẫn','Loại cáp quang','Loại tiếp địa','Loại cách điện','Hành lang']]
    st.write(get_col.T)
 

def process(subs, df):
    col_name=gf.ass_col_name(subs)
    st.header(f"📋{subs}")
    st.markdown("---")
    dis87_2 = st.number_input(f"🔢 Nhập khoảng cách sự cố F87/{subs}:", min_value=0)
    dis21_2 = st.number_input(f"🔢 Nhập khoảng cách sự cố F21/{subs}:", min_value=0)
    result_87 = findx(dis87_2, df, "F87", col_name)
    if result_87:
        info(df, result_87, "F87")
    result_21 = findx(dis21_2, df, "F21", col_name)
    if result_21:
        info(df, result_21, "F21")
