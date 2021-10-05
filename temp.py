# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Understanding Kickstarter Campaigns")

@st.cache
def load_data(nrows = 1000):
    df = pd.read_csv('https://raw.githubusercontent.com/JonathanBechtel/dat-02-22/main/ClassMaterial/Unit3/data/ks2.csv', nrows = 1000)

    return df

section = st.sidebar.radio('Application Section', ['Data Explorer', 
                                                   'Model Explorer'])

nrows = st.sidebar.number_input("Number of Rows to Load",min_value = 1000, max_value = 10000, step = 1000)

df = load_data(nrows)

if section == 'Data Explorer':
        
    x_axis = st.sidebar.selectbox('Choose Your X-Axis Category', df.select_dtypes(include=np.object).columns, index = 6)
    
    y_axis = st.sidebar.selectbox('Choose Your Y-Axis Category', df.select_dtypes(include=np.number).columns, index = 2)
    
    chart_type = st.sidebar.selectbox('Choose Your Chart Type', ['table', 'line', 'bar', 'strip'])
    
    @st.cache
    
    def create_grouping(x_axis, y_axis):
        grouping =  df.groupby(x_axis)[y_axis].mean()
        return grouping
    
    grouping = create_grouping(x_axis, y_axis)
    
    st.write(df)
    
    st.title("Grouped Data")
    
    if chart_type == 'line':
        st.line_chart(grouping)
    elif chart_type == 'table':
        st.write(grouping)
    elif chart_type == 'bar':
        st.bar_chart(grouping)
    else:
        st.plotly_chart(px.strip(df[[x_axis, y_axis]][:100], x = x_axis, y = y_axis))
        
elif section == 'Model Explorer':
    category =  st.sidebar.selectbox('Choose Your Category', df['category'].unique())
    sub_cat =  st.sidebar.selectbox('Choose Your Category', df['main_category'].unique())
    goal = st.sidebar.number_input('Your Fundraising Amount', min_value = 1, max_value = 100000, step = 500, value = 1000)
    
    st.title("Use Our Model For Live Predictions")
    
    sample = pd.DataFrame([[category, subcat, goal]], 
                          columns = ['category', 'main_category', 'goal'])
    
    proba = pipe.predict_proba(sample)[0][1]
    
    st.title(f"Odds of Success: {proba:.2%}")
    
