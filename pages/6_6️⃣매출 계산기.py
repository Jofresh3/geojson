import streamlit as st
import locale

# 로케일 설정 (한국의 경우 'ko_KR'을 사용)
locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')

def main():
    st.title("매출 계산기")
    price = st.slider("객단가:", 1000, 100000, value=25000)
    total_sales = st.slider("전체 판매 개수:", 1, 10000, value=500)

    revenue = price * total_sales

    # 매출을 천 단위로 포맷하여 출력
    formatted_revenue = locale.format_string("%d", revenue, grouping=True)
    st.write('매출은', formatted_revenue, '원입니다.')

if __name__ == "__main__":
    main()
