import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit 앱 제목
st.title("GPT 프롬프트 기반 데이터 시각화")

# CSV 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    try:
        # CSV 파일 읽기
        data = pd.read_csv(uploaded_file)

        # 데이터 구조 확인 및 처리
        if data.shape[0] == 0 or data.shape[1] < 2:
            st.error("CSV 파일에 데이터가 없거나 올바른 형식이 아닙니다.")
        else:
            # 첫 번째 열을 날짜로 변환
            data.rename(columns={data.columns[0]: "Date"}, inplace=True)
            data["Date"] = pd.to_datetime(data["Date"], errors='coerce')  # 날짜 변환

            # 날짜 변환 실패한 데이터 제거
            data = data.dropna(subset=["Date"])
            data.set_index("Date", inplace=True)

            # 데이터 표시
            st.write("업로드된 데이터:")
            st.dataframe(data)

            # 프롬프트 입력
            st.write("### GPT 프롬프트 입력")
            prompt = st.text_area("데이터를 필터링하거나 시각화할 프롬프트를 입력하세요.",
                                  placeholder="예: '2020년 이후 데이터만 보여줘' 또는 'AI기획과 AI사업 키워드 그래프를 그려줘'")

            # 프롬프트 처리
            if st.button("결과 생성"):
                if "이후" in prompt:
                    try:
                        year = int(prompt.split("년")[0].strip())  # 연도 추출
                        filtered_data = data[data.index.year >= year]
                        st.write(f"필터링된 데이터 (기준: {year}년 이후):")
                        st.dataframe(filtered_data)
                    except ValueError:
                        st.error("올바른 연도를 입력해주세요. 예: '2020년 이후'")

                elif "그래프" in prompt:
                    keywords = [word.strip() for word in prompt.split("그래프를 그려줘")[0].split("와")]
                    keywords = [kw for kw in keywords if kw in data.columns]  # 데이터에 존재하는 키워드만 선택

                    if keywords:
                        st.write(f"선택된 키워드: {', '.join(keywords)}")
                        plt.figure(figsize=(14, 8))
                        for column in keywords:
                            plt.plot(data.index, data[column], label=column)

                        plt.title("검색 키워드 관심도 추이 (필터링된 키워드)", fontsize=16)
                        plt.xlabel("년도", fontsize=12)
                        plt.ylabel("검색 관심도", fontsize=12)
                        plt.legend(title="키워드", fontsize=10)
                        plt.grid(True)
                        st.pyplot(plt)
                    else:
                        st.error("프롬프트에 유효한 키워드가 포함되어 있지 않습니다.")
                else:
                    st.warning("프롬프트를 이해할 수 없습니다. '이후' 또는 '그래프'와 같은 명령을 포함해주세요.")
    except Exception as e:
        st.error(f"파일 처리 중 오류가 발생했습니다: {e}")
