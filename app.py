import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit 앱 헤더
st.title("데이터 시각화 앱")
st.subheader("업로드된 데이터를 분석하고 시각화합니다.")

# 데이터 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요.", type=["csv"])

if uploaded_file is not None:
    # 데이터 로드
    data = pd.read_csv(uploaded_file)
    
    # 데이터 미리보기
    st.write("데이터 프리뷰:")
    st.dataframe(data.head())
    
    # 컬럼 선택
    x_column = st.selectbox("X축 컬럼 선택", data.columns)
    y_column = st.selectbox("Y축 컬럼 선택", data.columns)

    # 그래프 유형 선택
    chart_type = st.selectbox("그래프 유형 선택", ["Scatter Plot", "Line Plot", "Bar Plot", "Histogram"])
    
    # 그래프 생성
    st.write("선택한 데이터 시각화 결과:")

    if chart_type == "Scatter Plot":
        fig, ax = plt.subplots()
        sns.scatterplot(x=data[x_column], y=data[y_column], ax=ax)
        ax.set_title("Scatter Plot")
        st.pyplot(fig)
        
    elif chart_type == "Line Plot":
        fig, ax = plt.subplots()
        sns.lineplot(x=data[x_column], y=data[y_column], ax=ax)
        ax.set_title("Line Plot")
        st.pyplot(fig)
        
    elif chart_type == "Bar Plot":
        fig, ax = plt.subplots()
        sns.barplot(x=data[x_column], y=data[y_column], ax=ax)
        ax.set_title("Bar Plot")
        st.pyplot(fig)
        
    elif chart_type == "Histogram":
        fig, ax = plt.subplots()
        sns.histplot(data[x_column], kde=True, ax=ax)
        ax.set_title("Histogram")
        st.pyplot(fig)
else:
    st.write("CSV 파일을 업로드하세요.")
