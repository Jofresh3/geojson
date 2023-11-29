import geopandas as gpd
import pandas as pd
import folium
from folium import plugins
from streamlit_folium import folium_static
import streamlit as st

# 배차 데이터 로드
file_path = '배차.csv'
df = pd.read_csv(file_path)

# GeoJSON 파일 로드
geojson_path = 'TL_SCCO_SIG.json'
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
selected_info = st.sidebar.selectbox('표시할 정보 선택', ['총_주문수', '배차 30분이상', '총배달시간 60분이상', '알뜰배차시간', '알뜰픽업시간', '알뜰총배달시간', '알뜰고안시준수율','배차30분비중','배달60분비중'])

# 데이터 병합
merged_data = pd.merge(gdf, filtered_data, how='left', left_on='SIG_CD', right_on='rgn2_cd')

# Folium 지도 생성
m = folium.Map(location=[36.5, 127.5], zoom_start=7, control_scale=True)

# Choropleth를 사용하여 색상 표시
folium.Choropleth(
    geo_data=merged_data,
    name='choropleth',
    data=merged_data,
    columns=['SIG_CD', selected_info],
    key_on='feature.properties.SIG_CD',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name=selected_info,
    highlight=True,  # 마우스 오버 시 하이라이트 효과 추가
    smooth_factor=0.7,  # 폴리곤 간 경계 부드럽게 처리
).add_to(m)

# 행정 경계 안에 평균 데이터값 추가
for idx, row in merged_data.iterrows():
    avg_value = row[selected_info]
    folium.Marker(
        location=[row.geometry.centroid.y, row.geometry.centroid.x],
        icon=folium.DivIcon(html=f'<div style="font-size: 10pt;">{avg_value:.2f}</div>')
    ).add_to(m)

# Folium 지도를 Streamlit에 표시
folium_static(m)
