import streamlit as st

st.set_page_config(page_title="데이터를 활용한 세일즈고도화", page_icon='👨‍🔧')

st.markdown("### 👨‍🔧 데이터를 활용한 세일즈고도화 by [DQ](https://delivery-quality.streamlit.app/)")



st.image("https://plus.unsplash.com/premium_photo-1661508333411-0246522ee003?q=80&w=1632&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")

st.info("Original Course Repository on [Github](https://github.com/Jofresh3/geojson)")

st.markdown("---")


st.markdown("""
## 👥 HI guys
#### 이곳은 데이터를 활용한 웹페이지입니다. 데이터의 힘으로 더 나은 인사이트를 찾고, 즐겁게 데이터를 탐험하는 여정에 함께 참여해보세요.
---

## 📄 Contents

##### <a href="배달품질" target='_self'>배달품질</a>
* 상품(배민/배라), 지역별 배달품질 현황 확인
##### <a href="OD 도입율" target='_self'>OD 도입율</a>
* OD, STOD 도입율 확인
##### <a href="외식업자료" target='_self'>외식업자료</a>
* 통계청 외식업 통계 자료 확인
##### <a href="시장매력도" target='_self'>시장매력도</a>
##### <a href="피벗" target='_self'>피벗</a>
* 피벗테이블로 원하는 정보 바로 확인하기!
---

## 👨‍🎓 How to use
st.info("사용방법 👀[MOVE HERE▼](https://wiki.woowa.in/pages/viewpage.action?pageId=911253907)")






""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
