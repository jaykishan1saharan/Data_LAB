import streamlit as st

from utils.file_loader import load_file
from operations.pandas_operations.remove_duplicates import remove_duplicates

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

            st.dataframe(
                result_df,
                use_container_width=True
            )


    except Exception as e:

        st.error(
            f"Error loading file: {e}"
        )