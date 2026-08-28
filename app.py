import streamlit as st

from utils.file_loader import load_file
from operations.pandas_operations.remove_duplicates import remove_duplicates 
from operations.pandas_operations.preview_first_rows import preview_first_rows
from operations.pandas_operations.shape import shape

# Page configuration
st.set_page_config(
    page_title="DataLab",
    page_icon="📊",
    layout="wide"
)

st.title("📊 DataLab")
st.write("Data Science Analysis Portal")

# File upload
uploaded_file = st.file_uploader(
    "Upload your CSV or Excel file",
    type=["csv", "xlsx", "xls"]
)

# Process uploaded file
if uploaded_file is not None:

    try:

        df = load_file(uploaded_file)

        st.success("File loaded successfully!")

        st.write("### Dataset Preview")

        st.dataframe(
            df,
            use_container_width=True
        )


        # Pandas operations
        st.write("### Pandas Operations")


        # Remove duplicates
        if st.button("Remove Duplicates"):

            result_df = remove_duplicates(df)

            st.write("### Result")

            st.dataframe(result_df, use_container_width=True)

        # Preview First Rows
        if st.button("Preview First Rows"):
            result_df = preview_first_rows(df)
            st.write("### Result")
            st.dataframe(result_df, use_container_width=True)

        # Preview Shape of Table
        if st.button("Preview Shape of Data"):
            result_df = shape(df)
            st.write("### Result")
            st.write(result_df)


    except Exception as e:
        st.exception(e)

