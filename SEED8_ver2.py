import streamlit as st
import pandas as pd

# Load data function
def load_data(file_path, sheet_name):
    return pd.read_excel(file_path, sheet_name=sheet_name).dropna(how='all').fillna('')

def main():
    st.title("2022 교사교육과정 및 학급교육과정 개발 도우미")

    # Load the data
    standards_data = load_data('C:/Users/sohi9/OneDrive - 서울공항초등학교/8. SEED/1조 산출물/data/2022 통합본.xlsx', '성취기준 통합')
    content_data = load_data('C:/Users/sohi9/OneDrive - 서울공항초등학교/8. SEED/1조 산출물/data/2022 통합본.xlsx', '내용체계 통합')

    # Step 1: Subject, Curriculum, and Grade Selection
    st.subheader("1. 시작 (Start)")
    subject = st.selectbox('과목을 선택하세요:', standards_data['과목'].unique())
    category = st.selectbox('교육과정을 선택하세요:', standards_data['교육과정'].unique())
    grade_selection = st.selectbox('학년군을 선택하세요:', standards_data['학년'].unique())

    # Create tabs for Achievement Standards, Content Framework, and Additional Information
    tab1, tab2, tab3 = st.tabs(["1. 성취기준 검색", "2. 내용체계 검색", "3. 추가 정보 입력"])

    # Step 2: Achievement Standards Search
    with tab1:
        st.subheader("성취기준 검색")
        
        # Get relevant achievement standards
        standards = standards_data[
            (standards_data['과목'] == subject) & 
            (standards_data['교육과정'] == category) & 
            (standards_data['학년'] == grade_selection)
        ]

        if not standards.empty:
            st.write("선택한 성취기준:")
            standards['표시'] = standards.apply(lambda x: f"[{x['분류번호']}] {x['성취기준']}", axis=1)
            selected_standards = st.multiselect('성취기준을 선택하세요:', 
                                                  standards['표시'].tolist())
        else:
            st.write("해당 조건에 맞는 성취기준이 없습니다.")
            selected_standards = []

    # Step 3: Content Framework Search
    with tab2:
        st.subheader("내용체계 검색")
        
        # Get relevant content
        content = content_data[
            (content_data['과목'] == subject) & 
            (content_data['교육과정'] == category) & 
            (content_data['학년'] == grade_selection)
        ]

        if not content.empty:
            st.write("선택한 내용체계:")
            selected_content = st.multiselect('내용 요소를 선택하세요:', 
                                               content['내용 요소'].tolist())
        else:
            st.write("해당 조건에 맞는 내용체계가 없습니다.")
            selected_content = []

    # Step 4: Additional Information Input
    with tab3:
        st.subheader("추가 정보 입력")
        disability_type = st.multiselect('수업에 참여하는 학생들의 장애 유형 (최대 3가지)', 
                                          ['지적 장애', '지체 장애', '시각 장애', 
                                           '청각 장애', '정서 및 행동 장애', 
                                           '자폐성 장애', '의사소통 장애', 
                                           '학습 장애', '건강 장애', 
                                           '발달 지체', '간질 장애', '기타 장애'], 
                                          max_selections=3)
        subject_level = st.text_input('교과와 관련한 현재 학습 수행 수준')
        student_response = st.text_input('학생들의 반응 양식 및 표현 양식, 언어 유창성')
        core_concept = st.text_input('교사가 선정한 핵심 개념 또는 핵심개념을 추출할 교육과정 핵심아이디어의 문장')

        if st.button('제출'):
            # Display final summary
            formatted_text = f"""
            과목: {subject}
            교육과정: {category}
            학년군: {grade_selection}
            장애 유형: {', '.join(disability_type)}
            현재 학습 수행 수준: {subject_level}
            학생들의 반응 양식 및 표현 양식: {student_response}
            선택한 성취기준: {', '.join(selected_standards)}
            선택한 내용체계: {', '.join(selected_content)}
            """

            # Show the formatted text
            st.subheader("입력된 정보")
            st.text_area("다음 텍스트를 복사하여 챗봇에 입력하세요:", formatted_text, height=200)
            
            st.write("생성된 텍스트를 Ctrl+C 키로 복사해 다음 페이지로 이동하세요.")
            st.markdown("[ChatGPT 챗봇으로 이동](https://chatgpt.com/g/g-TtbM3264K-gaenyeomgiban-gyoyuggwajeong-seolgye-dijaineo-caesbos-feat-edyutekeu)")
            st.markdown("이동 후 로그인이 필요합니다. 복사한 내용을 챗봇에 검색해주세요.")

if __name__ == "__main__":
    main()
