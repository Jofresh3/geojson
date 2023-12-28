import streamlit as st

@st.cache_data
def calcul(price, total_sales):
    revenue = price * total_sales
    return revenue

def main():
    st.title("매출액 계산기")
    price = st.slider("단가:", 1000, 100000, value=25000)
    total_sales = st.slider("전체 판매 개수:", 1, 10000, value=500)


    # 매출을 천 단위로 포맷하여 출력
    if st.button("매출액 계산"):
        st.write('매출은', calcul(price,total_sales), '원입니다.')

if __name__ == "__main__":
    main()
