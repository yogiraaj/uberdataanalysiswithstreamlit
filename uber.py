from typing import Any

import streamlit as st
import pandas as pd
import preprocessor
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("Uber Data Analyzer")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    fact_table = preprocessor.preprocessor(data)
    st.dataframe(fact_table)

    vendor_id: list | Any = fact_table['VendorID'].unique().tolist()
    vendor_id.sort()
    vendor_id.insert(0, "Overall")

    selected_vendor_id = st.sidebar.selectbox("Show Analysis", vendor_id)

    if st.sidebar.button("Start Analysis"):

        if selected_vendor_id == "Overall":

            total_amount_sum = fact_table['total_amount'].sum()
            avg_fare_amt = fact_table['fare_amount'].mean()
            avg_trip_distance = fact_table['trip_distance_id'].mean()

            st.subheader("Analysis Results (Overall)")
            st.text(f"Total of Total Amount: {total_amount_sum}")
            st.text(f"Average Fare Amount: {avg_fare_amt}")
            st.text(f"Average Trip Distance: {avg_trip_distance}")

            st.subheader("Distribution of Vendor IDs (Overall)")
            plt.figure(figsize=(10, 6))
            sns.countplot(x='VendorID', data=fact_table)
            plt.title('Distribution of Vendor IDs')
            st.pyplot(plt.gcf())

            st.subheader("Passenger Count Distribution (Overall)")
            plt.figure(figsize=(10, 6))
            sns.countplot(x='passenger_count_id', data=fact_table, palette="viridis", order=[1, 2, 3, 4, 5])
            plt.title('Passenger Count Distribution')
            st.pyplot(plt.gcf())

            st.subheader("Distribution of Rate Code IDs (Overall)")
            plt.figure(figsize=(10, 6))
            sns.countplot(x='rate_code_id', data=fact_table, palette="viridis", order=[1, 2, 3, 4, 5])
            plt.title('Distribution of Rate Code IDs')
            st.pyplot(plt.gcf())

            st.subheader("Distribution of Payment Types (Overall)")
            plt.figure(figsize=(10, 6))
            sns.countplot(x='payment_type_id', data=fact_table.replace({'payment_type_id': {0: 'Credit card', 1: 'Cash', 2: 'No charge', 3: 'Dispute'}}), palette="viridis")
            plt.title('Distribution of Payment Types')
            st.pyplot(plt.gcf())

            data.rename(columns={'pickup_latitude': 'latitude', 'pickup_longitude': 'longitude'},
                        inplace=True)

            st.subheader("Pickup Locations on Map (Overall)")
            st.map(data[['latitude', 'longitude']])

        else:

            subset_data = fact_table[fact_table['VendorID'] == selected_vendor_id]

            total_amount_sum = subset_data['total_amount'].sum()
            avg_fare_amt = subset_data['fare_amount'].mean()
            avg_trip_distance = subset_data['trip_distance_id'].mean()

            st.subheader(f"Analysis Results for VendorID: {selected_vendor_id}")
            st.text(f"Total of Total Amount: {total_amount_sum}")
            st.text(f"Average Fare Amount: {avg_fare_amt}")
            st.text(f"Average Trip Distance: {avg_trip_distance}")

            st.subheader(f"Distribution of Vendor ID {selected_vendor_id}")
            plt.figure(figsize=(10, 6))
            sns.countplot(x='VendorID', data=subset_data)
            plt.title(f'Distribution of Vendor ID {selected_vendor_id}')
            st.pyplot(plt.gcf())

            st.subheader(f"Passenger Count Distribution for Vendor ID {selected_vendor_id}")
            plt.figure(figsize=(10, 6))
            sns.countplot(x='passenger_count_id', data=subset_data, palette="viridis", order=[1, 2, 3, 4, 5])
            plt.title(f'Passenger Count Distribution for Vendor ID {selected_vendor_id}')
            st.pyplot(plt.gcf())

            st.subheader(f"Distribution of Rate Code IDs for Vendor ID {selected_vendor_id}")
            plt.figure(figsize=(10, 6))
            sns.countplot(x='rate_code_id', data=subset_data, palette="viridis", order=[1, 2, 3, 4, 5])
            plt.title(f'Distribution of Rate Code IDs for Vendor ID {selected_vendor_id}')
            st.pyplot(plt.gcf())

            st.subheader(f"Distribution of Payment Types for Vendor ID {selected_vendor_id}")
            plt.figure(figsize=(10, 6))
            sns.countplot(x='payment_type_id', data=subset_data.replace({'payment_type_id': {0: 'Credit card', 1: 'Cash', 2: 'No charge', 3: 'Dispute'}}), palette="viridis")
            plt.title(f'Distribution of Payment Types for Vendor ID {selected_vendor_id}')
            st.pyplot(plt.gcf())

            data.rename(columns={'pickup_latitude': 'latitude', 'pickup_longitude': 'longitude'},
                        inplace=True)

            st.subheader("Pickup Locations on Map (Overall)")
            st.map(data[['latitude', 'longitude']])





