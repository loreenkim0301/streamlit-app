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
        # CSV 파일 읽기 (구분자 자동 감지)
        try:
            data = pd.read_csv(uploaded_file, sep=None, engine="python")  # 구분자 자동 감지
        except Exception:
            data = pd.read_csv(uploaded_file)  # 기본 구분자 ',' 사용

        # 데이터 확인
        st.write("### 업로드된 데이터:")
        st.dataframe(data)

        # 데이터 요약
        st.w
