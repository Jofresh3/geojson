
import streamlit as st


def main():
    st.title("streamlit Button widget")
    price = st.slider("객단가:",1000,100000,value=25000)
    total_sales = st.slider("전체 판매 개수:",1,1000,value=500)

    revenue = price * total_sales

    st.write('매출은',revenue,'원입니다.')

if __name__ == "__main__":
    main()
