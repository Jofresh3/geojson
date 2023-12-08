import streamlit as st

st.set_page_config(page_title="데이터를 활용한 세일즈고도화", page_icon='👨‍🔧')

st.markdown("### 👨‍🔧 데이터를 활용한 세일즈고도화 by [DQ](https://delivery-quality.streamlit.app/)")

st.image("https://plus.unsplash.com/premium_photo-1661508333411-0246522ee003?q=80&w=1632&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")

st.info("Original Course Repository on [Github](https://github.com/Jofresh3/geojson)")

st.markdown("---")


st.markdown("""
## 📄 Contents

##### <a href="배달품질" target='_self'>배달품질</a>
##### <a href="뭘넣으면좋을까" target='_self'>page2</a>

---

## 👨‍🎓 Others

####

##### 👥 HI guys

# 무지개색 스타일링 함수
def rainbow_text(text):
    colors = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF', '#4B0082', '#8B00FF']
    return ''.join([f'<span style="color:{color};">{char}</span>' for char, color in zip(text, colors)])

# 메인 메시지
main_message = "이곳은 데이터를 활용한 웹페이지입니다. 데이터의 힘으로 더 나은 인사이트를 찾고, 즐겁게 데이터를 탐험하는 여정에 함께 참여해보세요."

# 무지개색 스타일링 적용
styled_message = rainbow_text(main_message)

# Streamlit에 무지개색 텍스트 표시
st.markdown(styled_message, unsafe_allow_html=True)

st.error("To see 2023 streamlit ressources see this [link](https://streamlit.io/).")


""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
