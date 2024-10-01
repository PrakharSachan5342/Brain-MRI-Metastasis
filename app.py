import streamlit as st
import requests
from PIL import Image
import io

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #1E90FF;
        margin-bottom: 20px;
    }
    .description {
        text-align: center;
        font-size: 18px;
        color: #555555;
        margin-bottom: 30px;
    }
    .uploader {
        display: flex;
        justify-content: center;
        margin: 20px 0;
    }
    .footer {
        text-align: center;
        font-size: 12px;
        color: #aaaaaa;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app title
st.markdown('<p class="title">Brain MRI Metastasis Segmentation</p>', unsafe_allow_html=True)

# Description
st.markdown('<p class="description">Upload a Brain MRI image (PNG, JPG, JPEG) for segmentation. The model will process the image and display the results.</p>', unsafe_allow_html=True)

# Upload MRI image
uploaded_file = st.file_uploader("Upload Brain MRI Image", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded MRI Image', use_column_width=True)
    
    # Save the uploaded image temporarily
    temp_file_path = "temp_image" + uploaded_file.name
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Send the image to the FastAPI backend for segmentation
    with st.spinner("Processing..."):
        files = {'file': open(temp_file_path, 'rb')}
        response = requests.post("http://127.0.0.1:8000/predict/", files=files)
        
        # Check the response status
        if response.status_code == 200:
            st.image(response.content, caption='Segmented Image', use_column_width=True)
            # Provide a download link for the processed image
            st.download_button("Download Segmented Image", data=response.content, file_name='segmented_image.png', key='download_button')
        else:
            st.error("Error processing the image. Please try again.")

# Clear temporary file after processing
if uploaded_file is not None:
    import os
    os.remove(temp_file_path)

# Footer
st.markdown('<p class="footer">© 2024 Brain MRI Segmentation. All rights reserved.</p>', unsafe_allow_html=True)

# Additional styling and spacing
st.markdown("<br>", unsafe_allow_html=True)
