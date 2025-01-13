import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit 앱 설정
st.title("검색 키워드 관심도 추이 분석 (2004-2025)")

# CSV 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # CSV 파일 읽기
    data = pd.read_csv(uploaded_file)
    
    # 첫 번째 열을 날짜/인덱스로 변환
    data.set_index(data.columns[0], inplace=True)
    data.index = pd.to_datetime(data.index)

    # 데이터 표시
    st.write("업로드된 데이터:")
    st.dataframe(data)

    # 그래프 그리기
    st.write("검색 키워드 관심도 추이:")
    plt.figure(figsize=(14, 8))
    for column in data.columns:
        plt.plot(data.index, data[column], label=column)
    
    plt.title("검색 키워드 관심도 추이 (2004-2025)", fontsize=16)
    plt.xlabel("년도", fontsize=12)
    plt.ylabel("검색 관심도", fontsize=12)
    plt.legend(title="키워드", fontsize=10)
    plt.grid(True)
    
    # Streamlit에 그래프 표시
    st.pyplot(plt)
