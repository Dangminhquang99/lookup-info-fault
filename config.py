import streamlit as st
import pandas as pd

#============== Truy xuất file lũy kế để tính toán =======================
def accum():
    tendz_map = {
        "Đường dây 273 KrongBuk - 271 Nha Trang": ["krb-nt.xlsx", "Tongke_krb.xlsx"],
        "Đường dây 272 Thiên Tân - 271 Cam Ranh": ["dn-nt.xlsx", "Tongke_dn.xlsx"]
    }

    choose_dz = st.selectbox("📂 Hãy chọn đường dây", list(tendz_map.keys()))
    ten_file, ten_file2 = tendz_map.get(choose_dz, [None, None])

    if not ten_file or not ten_file2:
        st.error("❌ Không tìm thấy ánh xạ đúng cho đường dây đã chọn.")
        return pd.DataFrame(), pd.DataFrame()

    path_dz = f"data/{ten_file}"
    path_tk = f"data/{ten_file2}"

    try:
        df = pd.read_excel(path_dz)
        df2 = pd.read_excel(path_tk)
    except Exception as e:
        st.error(f"❌ Lỗi khi đọc file: {e}")
        return pd.DataFrame(), pd.DataFrame()

    return df, df2
