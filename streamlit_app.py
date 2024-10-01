import streamlit as st
import standard  # 성취기준 검색기 모듈
import search2    # 내용체계 검색기 모듈
import SEED8_ver2  # 교사교육과정 및 학급교육과정 개발 도우미 모듈
import edutech    # 에듀테크 사례 검색기 모듈

st.set_page_config(page_title="2022 교사교육과정 및 학급교육과정 개발 도우미", layout="wide")

def main():
    st.sidebar.title("SEED가 준비한 도움들😄")
    menu = [
        "도움 설명서",
        "성취기준 검색기",
        "내용체계 검색기",
        "교사교육과정 및 학급교육과정 개발 도우미",
        "에듀테크 사례 검색기"
    ]
    choice = st.sidebar.selectbox("4가지 선물🎁", menu)

    if choice == "도움 설명서":
        st.subheader("도움 설명서")
        st.write(""" 
        이 웹 애플리케이션은 2022 교사교육과정 및 학급교육과정 개발 도우미와 성취기준 검색기를 제공합니다.
        
        사이드바에서 원하는 기능을 선택하세요:
        - **성취기준 검색기**: 2022 개정 교육과정 성취기준을 검색할 수 있는 기능을 제공합니다.
        - **내용체계 검색기**: 2022 개정 교육과정 내용체계를 검색할 수 있는 기능을 제공합니다.
        - **교사교육과정 및 학급교육과정 개발 도우미**: 2022 개정 교육과정의 교사교육과정과 학급교육과정을 짤 때 드는 막막함을 도와줍니다.
        - **에듀테크 사례 검색기**: 연구대회 자료에 기반한 에듀테크 수업 사례 검색 기능을 제공합니다.
        """)

    elif choice == "성취기준 검색기":
        standard.main()  # 성취기준 검색기 함수 호출

    elif choice == "내용체계 검색기":
        search2.main()  # 내용체계 검색기 함수 호출

    elif choice == "교사교육과정 및 학급교육과정 개발 도우미":
        SEED8_ver2.main()  # 교사교육과정 및 학급교육과정 개발 도우미 함수 호출

    elif choice == "에듀테크 사례 검색기":
        edutech.search_function()  # 에듀테크 사례 검색기 함수 호출
        
if __name__ == '__main__':
    main()




