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
import io
import math
print(os.getcwd())


uploaded_file = st.sidebar.file_uploader("apikey 업로드", type=["json"])

if uploaded_file is not None:
    # 업로드된 파일을 읽어서 API 키 업데이트
    api_key_data = json.load(io.StringIO(uploaded_file.getvalue().decode("utf-8")))
    credentials = Credentials.from_service_account_info(api_key_data, scopes=['https://www.googleapis.com/auth/spreadsheets'])
    gc = gspread.authorize(credentials)
#credentials = Credentials.from_service_account_file('/Users/chjo/Desktop/python_practice/크롤링/woowahan_google_key.json', scopes=['https://www.googleapis.com/auth/spreadsheets'])
#gc = gspread.authorize(uploaded_file)
#혼자 사용할꺼라면 apikey를 그냥 파일로 가져와서 하면 더 편함!! 위에 주석처리된것 이용하면됨.


# 구글 시트 문서 이름을 사용하여 문서를 열거나 만듭니다.
spreadsheet = gc.open_by_key('155H5Kk4W9vVwN03vHJwUIjRVw563Vx26l1Kd5mPxV-k')

# 'main_raw' 시트를 선택합니다.
worksheet = spreadsheet.worksheet('시트15')

# 시트의 데이터를 가져와 DataFrame으로 변환합니다.
data = worksheet.get_all_values()
headers = data[0]
df = pd.DataFrame(data[1:], columns=headers)

# '총_주문수'와 같은 숫자 형식의 열을 숫자로 변환하고 NaN 값을 0으로 채웁니다.
numeric_columns = ['OD 도입율','알뜰배달 도입율']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce').fillna(0)

# GeoJSON 파일 로드
geojson_path = 'SIG_KOREA.json'
gdf = gpd.read_file(geojson_path)

# 'gdf'의 'SIG_CD' 열의 데이터 타입을 문자열로 변경
gdf['SIG_CD'] = gdf['SIG_CD'].astype(str)

# 'rgn2_cd' 열의 데이터 타입을 문자열로 변경
df['rgn2_cd'] = df['rgn2_cd'].astype(str)

# 'rgn1_nm' 선택을 위한 sidebar
# 전체도 할수 있도록 수정
selected_rgn1_nm = st.sidebar.selectbox('rgn1 선택', ['전체'] + list(df['rgn1_nm'].unique()))

# 선택된 'rgn1_nm'만 필터링
filtered_data = df if selected_rgn1_nm == '전체' else df[df['rgn1_nm'] == selected_rgn1_nm]

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

# TOP5 표시를 위한 코드 추가
st.subheader(f'{selected_rgn1_nm} 서비스 타입 - {selected_info} TOP 5 지역',divider='rainbow')
top5_data = filtered_data.groupby(['rgn1_nm', 'rgn2_nm'])[selected_info].sum().nlargest(5).reset_index()
if not top5_data.empty:
    top5_data_table = top5_data.rename(columns={'rgn2_nm': '지역', selected_info: f'{selected_info} 합계'})
    st.table(top5_data_table)
else:
    st.warning("데이터가 없습니다.")

# Folium 지도를 Streamlit에 표시
st.subheader("지도로 상세 확인",divider='rainbow')
folium_static(m)
st.markdown("""

---

### 📓TIP

확인하고 싶은 정보를 [표시할 정보 선택]에서 선택합니다.

* OD 도입율 = OD 이용업주수 / 전체 업주수
* 알뜰배달 도입율 = 알뜰배달 이용업주수 / 전체 업주수

#### 위의 전체 업주수는 가입 가능 지역의 <span style="color:red; font-weight:bold;">전체 업주수</span>입니다.

---


""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
