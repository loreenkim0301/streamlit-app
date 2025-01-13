import streamlit as st
import pandas as pd

# Streamlit 앱 제목
st.title("CSV 업로드 및 프롬프트 기반 데이터 분석")

# CSV 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    try:
        # CSV 파일 읽기
        data = pd.read_csv(uploaded_file)
        
        # 데이터 표시
        st.write("### 업로드된 데이터:")
        st.dataframe(data)

        # 프롬프트 입력
        st.write("### 프롬프트 입력")
        prompt = st.text_area(
            "데이터 분석을 요청할 프롬프트를 입력하세요.",
            placeholder="예: '2020년 이후 데이터 필터링' 또는 'AI기획의 평균값 계산'",
        )

        # 분석 결과 생성 버튼
        if st.button("분석 실행"):
            try:
                # 프롬프트 처리 및 분석
                if "필터링" in prompt:
                    # 예: "2020년 이후 데이터 필터링"
                    year = int(prompt.split("년")[0].strip())
                    if "이후" in prompt:
                        filtered_data = data[data[data.columns[0]] >= year]
                        st.write(f"### {year}년 이후 데이터 필터링 결과:")
                        st.dataframe(filtered_data)
                    elif "이전" in prompt:
                        filtered_data = data[data[data.columns[0]] < year]
                        st.write(f"### {year}년 이전 데이터 필터링 결과:")
                        st.dataframe(filtered_data)
                    else:
                        st.error("올바른 필터링 조건을 입력하세요 (이후/이전).")
                
                elif "평균값" in prompt:
                    # 특정 컬럼의 평균값 계산
                    column_name = prompt.split("의")[0].strip()
                    if column_name in data.columns:
                        mean_value = data[column_name].mean()
                        st.write(f"### '{column_name}'의 평균값: {mean_value}")
                    else:
                        st.error(f"컬럼 '{column_name}'을(를) 찾을 수 없습니다.")

                elif "최대값" in prompt:
                    # 특정 컬럼의 최대값 계산
                    column_name = prompt.split("의")[0].strip()
                    if column_name in data.columns:
                        max_value = data[column_name].max()
                        st.write(f"### '{column_name}'의 최대값: {max_value}")
                    else:
                        st.error(f"컬럼 '{column_name}'을(를) 찾을 수 없습니다.")

                elif "최소값" in prompt:
                    # 특정 컬럼의 최소값 계산
                    column_name = prompt.split("의")[0].strip()
                    if column_name in data.columns:
                        min_value = data[column_name].min()
                        st.write(f"### '{column_name}'의 최소값: {min_value}")
                    else:
                        st.error(f"컬럼 '{column_name}'을(를) 찾을 수 없습니다.")

                else:
                    st.error("지원하지 않는 분석 요청입니다. 필터링, 평균값, 최대값 또는 최소값을 요청하세요.")

            except Exception as e:
                st.error(f"분석 중 오류가 발생했습니다: {e}")
    except Exception as e:
        st.error(f"파일을 처리할 수 없습니다: {e}")
else:
    st.info("CSV 파일을 업로드해주세요.")
