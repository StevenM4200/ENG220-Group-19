# -*- coding: utf-8 -*-
"""TEST UNIT 3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14KYTGWnpBeigFDU-_zOKlyPqXYKjVnvR
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("CSV Data Visualization App")

# File uploader for CSV
uploaded_file = st.file_uploader("EPI.csv", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    data = pd.read_csv(uploaded_file)

    # Slice the data to only use rows 1 to 6 and columns 3 to 8
    data = data.iloc[1:7, 2:8]  # Rows 1 to 6 (index 1:7) and Columns 3 to 8 (index 2:8)

    st.write("### Data Preview")
    st.dataframe(data)

    # Extract Years (Row 1) and Functions (Rows 2-6)
    years = ["2017", "2018", "2019", "2020", "2021", "2022"]
    f1 = data.iloc[0, :].values
    f2 = data.iloc[1, :].values
    f3 = data.iloc[2, :].values
    f4 = data.iloc[3, :].values
    f5 = data.iloc[4, :].values

    # Dropdown for selecting function to plot
    function = st.selectbox(
        "Select Function",
        ["f1", "f2", "f3", "f4", "f5"]
    )

    # Plot button
    if st.button("Plot Graph"):
        fig, ax = plt.subplots()

        # Select the correct function based on user input
        if function == "f1":
            ax.plot(f1, years, marker='o', label="f1")
            ax.set_title("Function f1 vs Years (Line Plot)")
        elif function == "f2":
            ax.plot(f2, years, marker='o', label="f2")
            ax.set_title("Function f2 vs Years (Line Plot)")
        elif function == "f3":
            ax.plot(f3, years, marker='o', label="f3")
            ax.set_title("Function f3 vs Years (Line Plot)")
        elif function == "f4":
            ax.plot(f4, years, marker='o', label="f4")
            ax.set_title("Function f4 vs Years (Line Plot)")
        elif function == "f5":
            ax.plot(f5, years, marker='o', label="f5")
            ax.set_title("Function f5 vs Years (Line Plot)")

        ax.set_xlabel("Function Value")
        ax.set_ylabel("Year")
        ax.legend()

        st.pyplot(fig)

    st.write("Tip: Ensure the data is in the correct format for meaningful plots.")
else:
    st.info("Please upload a CSV file to get started.")