import streamlit as st
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

# Streamlit 앱 제목 설정
st.title("Google 시트 데이터 스트림릿으로 불러오기")

# GitHub Secrets에서 Google API 키 가져오기
google_api_key_str = st.secrets["GOOGLE_API_KEY"]
google_api_key = json.loads(google_api_key_str)

# Credentials 객체 생성
credentials = Credentials.from_service_account_info(google_api_key, scopes=['https://www.googleapis.com/auth/spreadsheets'])
gc = gspread.authorize(credentials)

# 구글 시트 문서 이름을 사용하여 문서를 열거나 만듭니다.
spreadsheet = gc.open_by_key('155H5Kk4W9vVwN03vHJwUIjRVw563Vx26l1Kd5mPxV-k')

# 'main_raw' 시트를 선택합니다.
worksheet = spreadsheet.worksheet('rawdata')

# 시트의 데이터를 가져와 DataFrame으로 변환합니다.
data = worksheet.get_all_values()
headers = data[0]
df = pd.DataFrame(data[1:], columns=headers)

# 불러온 데이터를 출력합니다.
st.write("불러온 데이터:", df)
