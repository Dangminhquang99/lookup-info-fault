import streamlit as st
import pandas as pd
import config as cf

def find_positions(value, data):
    if 'Lũy kế' not in data.columns or data.empty:
        st.error("❌ Dữ liệu không hợp lệ hoặc thiếu cột 'Lũy kế'.")
        return None
    for i in range(len(data) - 1):
        lower = data['Lũy kế'].iloc[i]
        upper = data['Lũy kế'].iloc[i + 1]
        if min(lower, upper) <= value <= max(lower, upper):
            return data['Vị trí'].iloc[i], data['Vị trí'].iloc[i + 1]
    return None

def findx(dis, dataframe, role_name):
    if dis:
        result = find_positions(dis, dataframe)
        if result:
            st.info(f"🔍 Khoảng cách rơ le {role_name} tương đương khoảng cột {result[0]} - {result[1]}.")
        else:
            st.warning("⚠️ Không tìm thấy khoảng phù hợp với giá trị đã nhập.")
        return result
    return None

def info(dataframe, result, role_name):
    if not result:
        st.warning(f"⚠️ Không có dữ liệu kết quả để hiển thị cho {role_name}.")
        return
    if 'VITRI' not in dataframe.columns:
        st.error("❌ File thông tin cột thiếu cột 'VITRI'.")
        return

    v1, v2 = result
    selected_rows = dataframe[dataframe['VITRI'].isin([v1, v2])]
    if selected_rows.empty:
        st.warning("⚠️ Không tìm thấy thông tin tương ứng trong file thông tin.")
    else:
        st.subheader(f"📋 Thông tin chi tiết các cột theo {role_name}:")
        st.table(selected_rows)
