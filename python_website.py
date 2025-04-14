import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

st.title("Simple data dashboard")

upload_data = st.file_uploader("Choose a file to upload", type='csv')

if upload_data is not None:
    data_frame = pd.read_csv(upload_data)

    st.subheader("Data Preview")
    st.write(data_frame.head())

    st.subheader("Data Summary")
    st.write(data_frame.describe())

    st.subheader("Filter Data")
    columns = data_frame.columns.tolist()
    selected_columns = st.selectbox("Select column to filter by", columns)
    unique_value = data_frame[selected_columns].unique()
    selected_value = st.selectbox("Select Value", unique_value)

    filtered_df = data_frame[data_frame[selected_columns] == selected_value ]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column) [y_column])   
else:
    st.write("Waiting for file to be upload...")