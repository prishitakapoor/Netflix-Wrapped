#importing the libraries
import altair as alt
import streamlit as st
import pandas as pd
import numpy as np

st.markdown("<h1 style='text-align: center; color: white;'>🎬🍿 Netlix Wrapped! 🍿🎬</h1>",
            unsafe_allow_html=True)

#file upload
uploaded_file = st.file_uploader(label="Upload your ViewingActivity.csv file",type='csv')

if uploaded_file is not None:
    global df
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)


    st.write('Your netflix wrapped will be created with the following data!', df)
    st.markdown("<br>",unsafe_allow_html=True)

    st.markdown("***")

    st.markdown("<h2 style='text-align:center;'>Netflix Wrapped loading ... 🎬</h2>",
                unsafe_allow_html=True)

    st.markdown("***")

    st.markdown("<br>", unsafe_allow_html=True)

    #finding the number of profiles

    st.markdown("<h2 style='text-align:center;'>🎬 How many people use this accout? 🤔</h2>",
                unsafe_allow_html=True)
    n = len(pd.unique(df['Profile Name']))
    col1, col2, col3 = st.beta_columns([1, 2, 1])
    with col1:
        st.write("")
    with col2:
        st.write('No of unique users in this account: ', n)
    with col3:
        st.write("")
    st.markdown("***")

    #who watched the most?

    st.markdown("<h2 style='text-align: center; color: white;'> 🎬 Who spent the most time Watching Netflix? ⌛</h2>",
                unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    df['Duration'] = pd.to_timedelta(df['Duration'])
    df = df[df['Duration'].dt.total_seconds() > 120]
    watch_time_days = df.groupby(by=['Profile Name'])['Duration'].sum().dt.days
    st.bar_chart(watch_time_days)
    x = watch_time_days.index.tolist()[-1]
    col1, col2, col3 = st.beta_columns([1, 3, 1])
    with col1:
        st.write("")
    with col2:
        st.write('🎦 Looks like ', x, ' watches Netflix the most! 📺🍿')
    with col3:
        st.write("")
    st.markdown("***")

    #Which is the most preferred? Movies or Series?

    st.markdown("<h2 style='text-align: center; color: white;'> 🎬 Which content type is preferred the most?</h2>",
                unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    df[['TV Show', 'Season', 'Episode']] = df['Title'].str.split(':', expand=True, n=2)
    df['Content Type'] = df['Season'].apply(lambda x: 'Movie' if x == None else 'Series')
    movie_or_series = df['Content Type'].value_counts()
    st.bar_chart(movie_or_series)
    y = df['Content Type'].value_counts().index.tolist()[0]
    col1, col2, col3 = st.beta_columns([1, 3, 1])
    with col1:
        st.write("")
    with col2:
        st.write('🎦 Looks like you prefer watching ', y, ' the most! 📺🍿')
    with col3:
        st.write("")
    
    st.markdown("***")

    # Top 10 Movies Watched

    df1 = df[df['Content Type'] == 'Movie']
    top10_movies = df1['TV Show'].value_counts(ascending=False)[0:10]
    st.markdown("<h2 style='text-align: center; color: white;'>🎬 Top 10 Movies Watched:</h2>",
                unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.beta_columns([1, 2, 1])
    with col1:
        st.write("")
    with col2:
        st.write(top10_movies)
    with col3:
        st.write("")
    st.markdown("***")

    #Top10 series watched

    df2 = df[df['Content Type'] == 'Series']
    top10_series = df2['TV Show'].value_counts(ascending=False)[0:10]
    st.markdown("<h2 style='text-align: center; color: white;'>🎬 Top 10 Series Watched:</h2>",
                unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.beta_columns([1, 2, 1])
    with col1:
        st.write("")
    with col2:
        st.write(top10_series)
    with col3:
        st.write("")
    st.markdown("***")

    #preprocessing start time coloum

    df[['Date', 'Time']] = df['Start Time'].str.split(' ', expand=True, n=2)
    df[['Hour', 'Min', 'Sec']] = df['Time'].str.split(':', expand=True, n=2)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Year'] = df['Start Time'].dt.year
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.day
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['day_name'] = df['Start Time'].dt.day_name()
    

    #viewing activity on different days of the week

    st.markdown("<h2 style='text-align: center; color: white;'> 🎬 Which day of the week do you netflix the most?</h2>",
                unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    watch_time_week = df["day_name"].value_counts(ascending=False)
    st.bar_chart(watch_time_week)
    k = df["day_name"].value_counts(ascending=False).index.tolist()[0]
    col1, col2, col3 = st.beta_columns([1, 2, 1])
    with col1:
        st.write("")
    with col2:
        st.write('🍿 You watch Netflix the most on', k, '🍿')
    with col3:
        st.write("")
    st.markdown("***")

    #preferred time to watch netflix
    st.markdown("<h2 style='text-align:center'> 🎬 What is your preferred time to watch Netflix?</h2>",
                unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    start_time = df['Hour'].value_counts()
    st.bar_chart(start_time)
    z = df['Hour'].value_counts().index.tolist()[0]
    col1, col2, col3 = st.beta_columns([1, 3, 1])
    with col1:
        st.write("")
    with col2:
        st.write('🍿 You start Netflixing the most at', z, ': 00 hours 🍿')
    with col3:
        st.write("")
    st.markdown("***")
    st.markdown("<h1 style='text-align: center; color: white;'>🎬🍿 Netlix Wrapped! 🍿🎬</h1>",
                unsafe_allow_html=True)
    st.markdown("***")