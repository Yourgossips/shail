import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Excel Data Visualization Tool")
    st.write("Upload an Excel file and select columns to generate graphs.")
    
    uploaded_file = st.file_uploader("Upload Excel file", type=["xls", "xlsx"])
    
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write("### Data Preview")
        st.dataframe(df.head())
        
        # Select columns for visualization
        columns = df.columns.tolist()
        selected_columns = st.multiselect("Select columns to visualize", columns)
        
        if selected_columns:
            for col in selected_columns:
                st.write(f"## {col} Visualization")
                if pd.api.types.is_numeric_dtype(df[col]):
                    fig, ax = plt.subplots()
                    df[col].hist(ax=ax, bins=20, edgecolor='black')
                    ax.set_title(f"Histogram of {col}")
                    ax.set_xlabel(col)
                    ax.set_ylabel("Frequency")
                    st.pyplot(fig)
                else:
                    fig, ax = plt.subplots()
                    df[col].value_counts().plot(kind='bar', ax=ax)
                    ax.set_title(f"Bar Chart of {col}")
                    ax.set_xlabel(col)
                    ax.set_ylabel("Count")
                    st.pyplot(fig)

if __name__ == "__main__":
    main()
