import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 앱 제목
st.title("IT 트렌드와 직무 수요 분석")

# CSV 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")

if uploaded_file is not None:
    # 데이터 읽기
    data = pd.read_csv(uploaded_file)
    st.write("업로드된 데이터:")
    st.dataframe(data)

    # 사용자 선택: 분석할 컬럼
    columns = st.multiselect("분석할 컬럼을 선택하세요:", data.columns)

    if columns:
        # 1. IT 트렌드와 직무 수요 변화 그래프
        st.subheader("IT 트렌드와 직무 수요 변화")
        fig, ax = plt.subplots()
        data[columns].plot(ax=ax)
        plt.xlabel("시간")
        plt.ylabel("검색량")
        plt.title("IT 트렌드와 직무 수요 변화")
        st.pyplot(fig)

        # 2. 상관 분석 히트맵
        st.subheader("IT 트렌드와 직무 간 상관 분석")
        # 상관 분석 계산
        correlation_matrix = data[columns].corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
        plt.title("상관 분석 히트맵")
        st.pyplot(fig)
