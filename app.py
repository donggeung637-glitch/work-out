import streamlit as st
import os

st.set_page_config(layout="wide")

# index.html 파일 경로 설정
html_path = os.path.join(os.path.dirname(__file__), "htmls", "index.html")

# HTML 파일 읽기 및 렌더링
if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # height 값을 조절하여 화면 높이에 맞게 설정할 수 있습니다.
    st.components.v1.html(html_content, height=800, scrolling=True)
else:
    st.error("htmls/index.html 파일을 찾을 수 없습니다. 경로를 확인해 주세요.")
