import streamlit as st


def main():
    st.title("매출 계산기")
    price = st.slider("객단가:", 1000, 100000, value=25000)
    total_sales = st.slider("주문수:", 1, 10000, value=500)

    revenue = price * total_sales


    st.write('매출은',revenue, '원입니다.')

if __name__ == "__main__":
    main()
