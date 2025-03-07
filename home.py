import streamlit as st
import leafmap
import folium
import datetime

st.set_page_config(page_title='Homepage', page_icon=':material/home:', layout='wide', initial_sidebar_state='auto',
                   menu_items={'About': 'Developed by:\nAkhilesh Kumar'})

# sidebar options
st.sidebar.write('A website to download AERONET data')
st.sidebar.write('---')

st.sidebar.write('### Input Parameters')
c1, c2 = st.sidebar.columns([0.5, 0.5])
with c1:
    start_date = st.date_input('Start date', min_value=datetime.date(1993, 1, 1), )
with c2:
    end_date = st.date_input('End date', min_value=datetime.date(1993, 1, 1))

level = st.sidebar.selectbox('Data quality', options=[1, 1.5, 2], index=1)


# Main page
m = leafmap.foliumap.Map(center=(32.65, 82.5), zoom=5)
m.to_streamlit()