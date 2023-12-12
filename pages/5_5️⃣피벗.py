import geopandas as gpd
import pandas as pd
import folium
from folium import plugins
from streamlit_folium import folium_static
import streamlit as st
import numpy as np
import gspread
from google.oauth2.service_account import Credentials
import os
import json
import io
import plotly as px

# 파일 업로드
uploaded_file = st.sidebar.file_uploader("apikey 업로드", type=["json"])

if uploaded_file is not None:
    # 업로드된 파일을 읽어서 API 키 업데이트
    api_key_data = json.load(io.StringIO(uploaded_file.getvalue().decode("utf-8")))
    credentials = Credentials.from_service_account_info(api_key_data, scopes=['https://www.googleapis.com/auth/spreadsheets'])
    gc = gspread.authorize(credentials)

# 구글 시트 문서 열기
spreadsheet = gc.open_by_key('155H5Kk4W9vVwN03vHJwUIjRVw563Vx26l1Kd5mPxV-k')
worksheet = spreadsheet.worksheet('main_raw')

# 시트의 데이터를 DataFrame으로 변환
data = worksheet.get_all_values()
headers = data[0]
df = pd.DataFrame(data[1:], columns=headers)

# 스트림릿 앱 시작
st.title('피벗테이블 시각화')

# Sidebar 영역
st.sidebar.title('Options')

# x축 선택
x_axis = st.sidebar.selectbox('X축 선택', df.columns)

# y축 선택 (다중 선택 가능)
y_axes = st.sidebar.multiselect('Y축 선택', df.columns)

# 필터 선택
filter_column = st.sidebar.selectbox('필터 선택', df.columns)
filter_value = st.sidebar.selectbox('필터 상세 선택', df[filter_column].unique())

# 필터링된 데이터 생성
filtered_data = df[df[filter_column] == filter_value]

# 더하기/평균/유니크/카운트
aggfunction = ['sum', 'mean', 'count', 'unique']
agg = st.sidebar.selectbox('함수 선택', aggfunction)

# 각각의 y축에 대해 피벗테이블 생성
pivot_tables = {}
for y_axis in y_axes:
    filtered_data[y_axis] = pd.to_numeric(filtered_data[y_axis], errors='coerce')
    pivot_tables[y_axis] = pd.pivot_table(filtered_data, values=y_axis, index=x_axis, aggfunc=agg)

    # 피벗테이블 출력
    st.subheader(f'Y축: {y_axis}')
    st.dataframe(pivot_tables[y_axis])

    # 플롯 생성
    fig = px.bar(pivot_tables[y_axis], x=pivot_tables[y_axis].index, y=y_axis, labels={y_axis: f'{agg.capitalize()} of {y_axis}'})
    st.plotly_chart(fig)
