import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 앱 제목
st.title("IT 트렌드와 직무 수요 분석 (여러 파일 업로드 지원)")

# 여러 파일 업로드
uploaded_files = st.file_uploader("CSV 파일들을 업로드하세요", type="csv", accept_multiple_files=True)

if uploaded_files:
    # 여러 파일을 읽어서 하나의 데이터프레임으로 결합
    dataframes = []
    for uploaded_file in uploaded_files:
        df = pd.read_csv(uploaded_file)
        df['파일명'] = uploaded_file.name  # 파일명을 데이터프레임에 추가
        dataframes.append(df)
    
    # 데이터프레임 합치기
    combined_data = pd.concat(dataframes)
    st.write("업로드된 데이터:")
    st.dataframe(combined_data)

    # 사용자 선택: 분석할 컬럼
    columns = st.multiselect("분석할 컬럼을 선택하세요:", combined_data.columns)

    if columns:
        # 1. IT 트렌드와 직무 수요 변화 그래프
        st.subheader("IT 트렌드와 직무 수요 변화")
        fig, ax = plt.subplots()
        combined_data.groupby('파일명')[columns].mean().plot(ax=ax)  # 파일별 평균을 사용
        plt.xlabel("파일")
        plt.ylabel("검색량 (평균)")
        plt.title("IT 트렌드와 직무 수요 변화 (파일별)")
        st.pyplot(fig)

        # 2. 상관 분석 히트맵
        st.subheader("IT 트렌드와 직무 간 상관 분석")
        # 상관 분석 계산
        correlation_matrix = combined_data[columns].corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
        plt.title("상관 분석 히트맵")
        st.pyplot(fig)
