
# Brain MRI Metastasis Segmentation

## Project Overview
The **Brain MRI Metastasis Segmentation** application is designed to assist in the identification and segmentation of brain metastases from MRI images. This application utilizes **FastAPI** for the backend and **Streamlit** for the frontend, providing a user-friendly interface for uploading MRI images and receiving segmented results.

## Features
- Upload Brain MRI images in PNG, JPG, or JPEG format.
- Process images using a segmentation model (currently a placeholder).
- Display uploaded and segmented images.
- Download segmented images for further analysis.
- User-friendly interface with loading indicators and error messages.

## Technologies Used
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Image Processing**: OpenCV, PIL
- **Python Packages**: numpy, requests

## Prerequisites
Ensure you have the following installed on your machine:
- Python 3.7 or later
- pip (Python package installer)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/PrakharSachan5342/Brain-MRI-Metastasis.git
   cd Brain-MRI-Metastasis
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
1. Start the FastAPI backend:
   ```bash
   uvicorn main:app --reload
   ```

2. In another terminal, start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. Open your browser and navigate to `http://localhost:8501` to access the application.

## Usage
1. Upload a Brain MRI image by dragging and dropping it into the designated area or clicking "Browse files".
2. The application will process the image and display the segmented result.
3. You can download the segmented image for further analysis.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
Thank you to the contributors and libraries that made this project possible.

## Contact
For questions or feedback, please reach out to:
- **Name**: Prakhar Sachan
- **Email**: [your-email@example.com]
