import streamlit as st

# Configure the page
st.set_page_config(
    page_title='Translasi Aksara Jawa',
    layout='wide'
)

st.title("Javanese Manuscript Translation")

# Create columns for layout
col1, col2, col3 = st.columns(3)

# Initialize session states for segmented results and translation if not already set
if "segmented_text" not in st.session_state:
    st.session_state.segmented_text = ""
if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

# Input column
with col1:
    aksara = st.text_area("Input Manuscript")
    submit = st.button("Submit")

# Process segmentation when "Submit" is clicked
if submit:
    # Here we would add segmentation logic. For demonstration, we just use the input text.
    st.session_state.segmented_text = aksara  # Store in session state

# Display segmented results
if st.session_state.segmented_text:
    with col2:
        st.write("Segmentation Results")
        st.markdown(
            f"""
            <div style="
                display: inline-block;
                width: 100%;
                border: 1px solid #ddd;
                padding: 10px;
                border-radius: 5px;
                background-color: #f9f9f9;
                word-wrap: break-word;
            ">
                {st.session_state.segmented_text}
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Add a button for translation under segmented results
        st.write()
        translasi = st.button("Translate")

        # Process translation when "Translate" is clicked
        if translasi:
            # Here you would use your model for translation.
            # For now, we'll set a placeholder translation.
            st.session_state.translated_text = st.session_state.segmented_text

# Display translation results
if st.session_state.translated_text:
    with col3:
        st.write("Translation Results")
        st.markdown(
            f"""
            <div style="
                display: inline-block;
                width: 100%;
                border: 1px solid #ddd;
                padding: 10px;
                border-radius: 5px;
                background-color: #f9f9f9;
                word-wrap: break-word;
            ">
                {st.session_state.translated_text}
            </div>
            """,
            unsafe_allow_html=True
        )
