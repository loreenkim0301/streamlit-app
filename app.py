import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 앱 제목
st.title("IT 트렌드와 직무 수요 분석")

# CSV 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")

if uploaded_file is not None:
    # 업로드된 데이터 읽기
    data = pd.read_csv(uploaded_file)
    st.write("업로드된 데이터:")
    st.dataframe(data)

    # 사용자 선택
    columns = st.multiselect("분석할 컬럼을 선택하세요:", data.columns)
    if columns:
        # 선택된 컬럼으로 그래프 생성
        st.line_chart(data[columns])
