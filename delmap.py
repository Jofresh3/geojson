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
from dotenv import load_dotenv
import json

# GitHub Secrets에서 Google API 키 가져오기
google_api_key_str = st.secrets["GOOGLE_API_KEY"]
google_api_key = json.loads(google_api_key_str)

# Credentials 객체 생성
credentials = Credentials.from_service_account_info(google_api_key, scopes=['https://www.googleapis.com/auth/spreadsheets'])
gc = gspread.authorize(credentials)


# 구글 시트 문서 이름을 사용하여 문서를 열거나 만듭니다.
spreadsheet = gc.open_by_key('155H5Kk4W9vVwN03vHJwUIjRVw563Vx26l1Kd5mPxV-k')

# 'main_raw' 시트를 선택합니다.
worksheet = spreadsheet.worksheet('rawdata>')

# 시트의 데이터를 가져와 DataFrame으로 변환합니다.
data = worksheet.get_all_values()
headers = data[0]
df = pd.DataFrame(data[1:], columns=headers)

# '총_주문수'와 같은 숫자 형식의 열을 숫자로 변환하고 NaN 값을 0으로 채웁니다.
numeric_columns = ['총_주문수', '배차 30분이상', '총배달시간 60분이상', '알뜰배차시간', '알뜰픽업시간', '알뜰총배달시간', '알뜰고안시준수율', '배차30분비중', '배달60분비중']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce').fillna(0)

# GeoJSON 파일 로드
geojson_path = 'streamlit/SIG_KOREA.json'
gdf = gpd.read_file(geojson_path)

# 'gdf'의 'SIG_CD' 열의 데이터 타입을 문자열로 변경
gdf['SIG_CD'] = gdf['SIG_CD'].astype(str)

# 'rgn2_cd' 열의 데이터 타입을 문자열로 변경
df['rgn2_cd'] = df['rgn2_cd'].astype(str)

# 'service_type' 선택을 위한 sidebar
selected_service_type = st.sidebar.selectbox('서비스 타입 선택', df['service_type'].unique())

# 선택된 'service_type'만 필터링
filtered_data = df[df['service_type'] == selected_service_type]

# 정보 선택을 위한 sidebar
selected_info = st.sidebar.selectbox('표시할 정보 선택', numeric_columns)

# 데이터 병합
merged_data = pd.merge(gdf, filtered_data, how='left', left_on='SIG_CD', right_on='rgn2_cd')

# Folium 지도 생성
m = folium.Map(location=[36.5, 127.5], zoom_start=7, control_scale=True)

# Choropleth를 사용하여 색상 표시
choropleth = folium.Choropleth(
    geo_data=merged_data,
    name='choropleth',
    data=merged_data,
    columns=['SIG_CD', selected_info],
    key_on='feature.properties.SIG_CD',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name=selected_info,
    highlight=True,
    smooth_factor=0.7,
).add_to(m)

# 마우스 오버 시 팝업에 정보 추가
choropleth.geojson.add_child(folium.features.GeoJsonTooltip(['SIG_KOR_NM'], labels=False))

# 행정 경계 안에 평균 데이터값 추가
for idx, row in merged_data.iterrows():
    avg_value = row[selected_info]
    folium.Marker(
        location=[row.geometry.centroid.y, row.geometry.centroid.x],
        icon=folium.DivIcon(html=f'<div style="font-size: 10pt;">{avg_value:.2f}</div>')
    ).add_to(m)

# Folium 지도를 Streamlit에 표시
folium_static(m)
