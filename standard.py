import streamlit as st
import pandas as pd
import re

# Load the achievement standards data
def load_data(file_path, sheet_name):
    return pd.read_excel(file_path, sheet_name=sheet_name).dropna(how='all').fillna('')

def main():
    st.title("성취기준 검색기")

    # Load the standards data
    standards_data = load_data('data/2022 통합본.xlsx', '성취기준 통합')

    # Search method selection
    search_method = st.sidebar.selectbox("검색 방법 선택", ["조건으로 검색", "내용으로 검색"])

    if search_method == "조건으로 검색":
        st.sidebar.subheader("조건 선택")
        subject = st.sidebar.selectbox('과목을 선택하세요:', standards_data['과목'].unique())
        category = st.sidebar.selectbox('교육과정을 선택하세요:', standards_data['교육과정'].unique())
        grade_selection = st.sidebar.selectbox('학년군을 선택하세요:', standards_data['학년'].unique())

        # Search button for standards selection
        if st.sidebar.button('성취기준 검색'):
            # Filter the standards data based on user selection
            filtered_standards = standards_data[
                (standards_data['과목'] == subject) & 
                (standards_data['교육과정'] == category) & 
                (standards_data['학년'] == grade_selection)
            ]

            if not filtered_standards.empty:
                st.subheader("검색 결과")
                filtered_standards['표시'] = filtered_standards.apply(lambda x: f"[{x['분류번호']}] {x['성취기준']}", axis=1)
                st.table(filtered_standards[['분류번호', '성취기준']])  # Show relevant columns
            else:
                st.write("해당 조건에 맞는 성취기준이 없습니다.")

    elif search_method == "내용으로 검색":
        st.subheader("내용으로 검색")
        
        # Initialize search_term in session_state
        if 'search_term' not in st.session_state:
            st.session_state.search_term = ""

        # Text input for search term
        st.session_state.search_term = st.text_input("검색어를 입력하세요 (두 글자 이상)", value=st.session_state.search_term)

        # Search button for content search
        if st.button('내용 검색'):
            if st.session_state.search_term and len(st.session_state.search_term) >= 2:
                # Normalize the search term by removing spaces
                normalized_search_term = re.sub(r'\s+', '', st.session_state.search_term)

                # Define a function to remove spaces from '성취기준' column and search
                def search_in_standard(standard, term):
                    return re.search(term, re.sub(r'\s+', '', standard), re.IGNORECASE)

                # Filter data that contains the normalized search term
                search_results = standards_data[standards_data['성취기준'].apply(lambda x: bool(search_in_standard(x, normalized_search_term)))]

                # Display search results in the main area
                st.write(f"'{st.session_state.search_term}' 검색 결과")
                if not search_results.empty:
                    # Display the table with larger text
                    st.markdown("""
                    <style>
                    .big-font {
                        font-size:20px !important;
                    }
                    </style>
                    """, unsafe_allow_html=True)
                    
                    st.dataframe(search_results[['분류번호', '성취기준']], width=1000, height=600)
                else:
                    st.write("검색 결과가 없습니다.")
            else:
                st.write("검색어를 두 글자 이상 입력해주세요.")

if __name__ == "__main__":
    main()

