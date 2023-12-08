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

## 👨‍🎓 Taking the course

####

##### 👥 2023 Cohort

* **Start**: 16 January 2023 (Monday) at 18:00 CET
* **Registration link**: https://airtable.com/shr6oVXeQvSI5HuWD
* Subscribe to our [public Google Calendar](https://calendar.google.com/calendar/?cid=ZXIxcjA1M3ZlYjJpcXU0dTFmaG02MzVxMG9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ) (it works from Desktop only)
* [Cohort folder](cohorts/2023/) with homeworks and deadlines""", unsafe_allow_html=True)

st.error("2023 Cohort ended in the 18th May of 2023. To see 2023 cohort ressources see this [link](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/cohorts/2023).")

st.markdown("""
##### 👨‍🔧 Self-paced mode

All the materials of the course are freely available, so that you can take the course at your own pace

* Follow the suggested syllabus (see below) week by week
* You don't need to fill in the registration form. Just start watching the videos and join Slack
* Check [FAQ](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?usp=sharing) if you have problems
* If you can't find a solution to your problem in FAQ, ask for help in Slack

---

### 📓 Prerequisites

To get the most out of this course, you should feel comfortable with coding and command line
and know the basics of SQL. Prior experience with Python will be helpful, but you can pick
Python relatively fast if you have experience with other programming languages.

Prior experience with data engineering is not required.

---


""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
