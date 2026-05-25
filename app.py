
import streamlit as st
import pandas as pd
import plotly.express as px
from scipy import stats

panel = pd.read_csv('panel_data.csv')
region_avg = pd.read_csv('region_data.csv')

st.title('Minimum Wage and Unemployment in Europe')

st.sidebar.header('Filters')
selected_region = st.sidebar.selectbox(
    'Select Region',
    ['All'] + sorted(panel['region'].dropna().unique().tolist())
)
selected_years = st.sidebar.slider(
    'Select Year Range',
    int(panel['year'].min()),
    int(panel['year'].max()),
    (2010, 2023)
)

filtered = panel[
    (panel['year'] >= selected_years[0]) &
    (panel['year'] <= selected_years[1])
]
if selected_region != 'All':
    filtered = filtered[filtered['region'] == selected_region]

st.subheader('Minimum Wage vs Unemployment Rate')
fig1 = px.scatter(filtered, x='min_wage_eur', y='unemployment_rate',
    color='geo', hover_data=['geo', 'year'], trendline='ols')
st.plotly_chart(fig1)

st.subheader('Trends by Region')
fig2 = px.line(region_avg, x='year', y='min_wage_eur', color='region')
st.plotly_chart(fig2)
fig3 = px.line(region_avg, x='year', y='unemployment_rate', color='region')
st.plotly_chart(fig3)
