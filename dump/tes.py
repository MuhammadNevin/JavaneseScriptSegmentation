import streamlit as st

# Configure the page
st.set_page_config(
    page_title='Translasi Aksara Jawa',
    layout='wide'
)

st.title("Javanese Manuscript Translation")

# # Create columns for layout
# col1, col2, col3 = st.columns(3)

# # Initialize session states for segmented results and translation if not already set bbbbbbbbbbbbbbb
# if "segmented_text" not in st.session_state:
#     st.session_state.segmented_text = ""
# if "translated_text" not in st.session_state:
#     st.session_state.translated_text = ""