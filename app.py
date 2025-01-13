import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit 앱 제목
st.title("GPT 기반 데이터 분석 및 그래프 추천")

# CSV 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    try:
        # CSV 파일 읽기
        data = pd.read_csv(uploaded_file)
        
        # 데이터 확인
        st.write("### 업로드된 데이터:")
        st.dataframe(data)

        # 데이터 요약
        st.write("### 데이터 요약:")
        st.write(data.describe())

        # 데이터의 기본 정보 확인
        st.write("### 데이터 구조:")
        st.write(f"행 개수: {data.shape[0]}, 열 개수: {data.shape[1]}")

        # 사용자에게 적합한 그래프 추천
        st.write("### GPT 기반 그래프 추천:")
        if data.shape[1] == 2:
            # 2개의 열이 있는 경우: 선 그래프 추천
            st.write("2개의 열이 있으므로 선 그래프를 추천합니다.")
            x_col, y_col = data.columns[0], data.columns[1]
            plt.figure(figsize=(12, 6))
            plt.plot(data[x_col], data[y_col], marker='o', linestyle='-', color='b')
            plt.title(f"{x_col} vs {y_col}", fontsize=16)
            plt.xlabel(x_col, fontsize=12)
            plt.ylabel(y_col, fontsize=12)
            plt.grid(True)
            st.pyplot(plt)
        elif data.shape[1] > 2:
            # 3개 이상의 열이 있는 경우: 히트맵 추천
            st.write("3개 이상의 열이 있으므로 상관 관계 히트맵을 추천합니다.")
            correlation = data.corr()
            plt.figure(figsize=(10, 8))
            sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
            plt.title("Correlation Heatmap", fontsize=16)
            st.pyplot(plt)
        else:
            st.write("데이터 열이 하나뿐입니다. 적합한 그래프를 생성할 수 없습니다.")
    except Exception as e:
        st.error(f"파일 처리 중 오류가 발생했습니다: {e}")
