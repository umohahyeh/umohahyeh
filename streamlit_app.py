import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("🎈 Streamlit 요소 데모 페이지")

st.markdown("이 페이지는 Streamlit의 다양한 요소들을 보여줍니다. 각 요소의 사용법을 확인하세요!")

# 텍스트 요소들
st.header("1. 텍스트 요소들")
st.subheader("제목과 부제목")
st.text("일반 텍스트입니다.")
st.markdown("**마크다운** 텍스트입니다. *이탤릭*과 `코드`도 지원합니다.")
st.latex(r"E = mc^2")  # 수식 예시

# 입력 위젯들
st.header("2. 입력 위젯들")

# 버튼
if st.button("클릭하세요"):
    st.success("버튼이 클릭되었습니다!")

# 체크박스
agree = st.checkbox("동의합니다")
if agree:
    st.write("동의하셨습니다!")

# 라디오 버튼
option = st.radio("선택하세요:", ["옵션 1", "옵션 2", "옵션 3"])
st.write(f"선택된 옵션: {option}")

# 셀렉트박스
select = st.selectbox("드롭다운 선택:", ["항목 1", "항목 2", "항목 3"])
st.write(f"선택된 항목: {select}")

# 멀티셀렉트
multi = st.multiselect("여러 항목 선택:", ["A", "B", "C", "D"])
st.write(f"선택된 항목들: {multi}")

# 슬라이더
age = st.slider("나이를 선택하세요:", 0, 100, 25)
st.write(f"선택된 나이: {age}")

# 텍스트 입력
name = st.text_input("이름을 입력하세요:")
st.write(f"입력된 이름: {name}")

# 텍스트 영역
message = st.text_area("메시지를 입력하세요:")
st.write(f"입력된 메시지: {message}")

# 숫자 입력
number = st.number_input("숫자를 입력하세요:", min_value=0.0, max_value=100.0, value=50.0)
st.write(f"입력된 숫자: {number}")

# 날짜 입력
date = st.date_input("날짜를 선택하세요:")
st.write(f"선택된 날짜: {date}")

# 파일 업로더
uploaded_file = st.file_uploader("파일을 업로드하세요:")
if uploaded_file is not None:
    st.write("파일이 업로드되었습니다:", uploaded_file.name)

# 출력 요소들
st.header("3. 출력 요소들")

# 데이터프레임
st.subheader("데이터프레임")
df = pd.DataFrame({
    '이름': ['Alice', 'Bob', 'Charlie'],
    '나이': [25, 30, 35],
    '점수': [85, 90, 95]
})
st.dataframe(df)

# 테이블
st.subheader("테이블")
st.table(df)

# JSON
st.subheader("JSON")
st.json({"이름": "Alice", "나이": 25, "점수": 85})

# 메트릭
st.subheader("메트릭")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("온도", "70 °F", "1.2 °F")
with col2:
    st.metric("바람", "9 mph", "-8%")
with col3:
    st.metric("습도", "86%", "4%")

# 프로그레스 바
st.subheader("프로그레스 바")
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)

# 스피너
st.subheader("스피너")
with st.spinner("로딩 중..."):
    import time
    time.sleep(1)
st.success("완료되었습니다!")

# 차트
st.header("4. 차트")
st.subheader("라인 차트")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

st.subheader("바 차트")
st.bar_chart(chart_data)

st.subheader("에어리어 차트")
st.area_chart(chart_data)

# Matplotlib 차트
st.subheader("Matplotlib 차트")
fig, ax = plt.subplots()
ax.plot(chart_data['A'], label='A')
ax.plot(chart_data['B'], label='B')
ax.plot(chart_data['C'], label='C')
ax.legend()
st.pyplot(fig)

# 레이아웃
st.header("5. 레이아웃")

# 사이드바
with st.sidebar:
    st.header("사이드바")
    st.write("이것은 사이드바입니다.")

# 컬럼
st.subheader("컬럼")
col1, col2 = st.columns(2)
with col1:
    st.write("왼쪽 컬럼")
with col2:
    st.write("오른쪽 컬럼")

# 익스팬더
with st.expander("더보기"):
    st.write("이것은 익스팬더 내부입니다.")

# 컨테이너
st.subheader("컨테이너")
container = st.container()
container.write("컨테이너 내부입니다.")

# 미디어
st.header("6. 미디어")
st.subheader("이미지")
st.image("https://www.streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", caption="Streamlit 로고")

st.subheader("오디오")
# 오디오 파일이 없으므로 생략 또는 예시
st.write("오디오 예시: 실제 파일을 업로드하거나 URL을 사용할 수 있습니다.")

st.subheader("비디오")
# 비디오 파일이 없으므로 생략 또는 예시
st.write("비디오 예시: 실제 파일을 업로드하거나 URL을 사용할 수 있습니다.")

st.markdown("---")
st.write("이 데모는 Streamlit의 기본 요소들을 보여줍니다. 더 자세한 정보는 [Streamlit 문서](https://docs.streamlit.io/)를 참고하세요!")
