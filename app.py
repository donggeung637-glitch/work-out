import streamlit as st
from pathlib import Path

# 1. 페이지 기본 설정 (넓은 화면 레이아웃 및 타이틀 지정)
st.set_page_config(
    page_title="FIT-EVO : 개인 맞춤형 피트니스 AI 보조",
    page_icon="🏋️‍♂️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. index.html 파일 경로 설정
HTML_PATH = Path(__file__).resolve().parent / "htmls" / "index.html"

# 3. HTML 파일 읽기 및 Streamlit 컴포넌트로 렌더링
try:
    if HTML_PATH.exists():
        with open(HTML_PATH, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # HTML 앱을 전체 화면 크기 감안하여 렌더링 (스크롤 허용)
        st.components.v1.html(html_content, height=1200, scrolling=True)
    else:
        st.error("⚠️ HTML 파일을 찾을 수 없습니다.")
        st.info(f"프로젝트 폴더 안에 `htmls/index.html` 파일이 올바르게 위치해 있는지 확인해 주세요.\n(현재 탐색 경로: `{HTML_PATH}`)")

except Exception as e:
    st.error("⚠️ 애플리케이션을 불러오는 중 오류가 발생했습니다.")
    st.code(str(e))
