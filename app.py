import streamlit as st
import dbhelper
from dbhelper import DB
import plotly.graph_objs as go
db = DB()
st.set_page_config(page_title='flight_App')
st.sidebar.title("Flight option")
user_input = st.sidebar.selectbox('Menu', [1,2, 'Analytic'])
if user_input == 1:
    st.title('option 1')
elif user_input == 2:
    st.title('option 2')
    city = db.fetch_city()
    col1, col2 = st.columns(2)

    with col1:
        source = st.selectbox('Source', sorted(city))
    with col2:
        destination = st.selectbox('Destination', sorted(city))
    if st.button('Search'):
        results = db.fetch_all_flights(source, destination)
        st.dataframe(results)
else:
    # ---------------pie chart airline count---------
    st.title('option 3')
    df = db.fetch_pie_data()
    custom_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22']
    fig = go.Figure(data=[
        go.Pie(labels=df['Airline'], values=df['Count'], textinfo='value', hole=0.1, hoverinfo='label+percent',
               marker=dict(colors=custom_colors), hoverlabel=dict(font=dict(color='#251abd', size=16)))
    ])

    fig.update_layout(
        legend=dict(
            font=dict(
                color='Purple', size=14
        )))

    fig.update_traces(textfont_size=18)
    st.header('Bar chart')
    st.plotly_chart(fig, use_container_width=True)

    # ----------bar chart busy airport---------
    df = db.fetch_busy_airport()
    fig = go.Figure(data=[
        go.Bar(x=df['Airline'], y=df['Count'], text=df['Count'])
    ])
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside', marker_color='rgb(32, 214, 172)',
                      marker_line_color='rgb(71, 18, 44)', marker_line_width=1.5
                      )
    st.header('Pie chart')
    st.plotly_chart(fig, use_container_width=True)

    # ------------line chart daily flight---------
    df = db.fetch_daily_flight()
    fig = go.Figure(data=[go.Scatter(x=df['Date'], y=df['No. of Flight'], mode='lines+markers',
                                     line=dict(color='firebrick'))
                          ])

    st.header('Line chart ')
    fig.update_traces(marker=dict(size=10))
    fig.update_layout(title='Daily Flight Count', xaxis_title='Dates', yaxis_title='No. of Flight')
    st.plotly_chart(fig, use_container_width=True)



