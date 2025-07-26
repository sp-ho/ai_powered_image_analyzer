# AI-Powered Image Analyzer

A Streamlit-based web application that utilizes Azure's Computer Vision API to analyze uploaded images and provide captions, dense captions, and tags.

## Features

- **Image Upload**: Upload images in JPG, JPEG, or PNG format.
- **Image Analysis**: Analyze uploaded images using Azure's Computer Vision API.
- **Captions**: Get a descriptive caption for the uploaded image.
- **Dense Captions**: View detailed dense captions for various regions of the image.
- **Tags**: Receive a list of relevant tags for the image.

## Prerequisites

Before running this application, ensure you have the following:

1. Python installed on your machine.
2. An Azure account with access to the Azure Computer Vision service.
3. Environment variables for your Azure Vision Key and Endpoint.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sp-ho/ai_powered_image_analyzer.git
cd <repository-folder>
```

### 2. Install Dependencies

Install the required Python libraries:
```bash
pip install -r requirements.txt
```

The requirements.txt file should include:

- streamlit
- azure-ai-vision
- python-dotenv
- Pillow

### 3. Set Up Environment Variables

Create a .env file in the project root directory and add your Azure Computer Vision credentials:

```bash
VISION_KEY=<Your Azure Vision Key>
VISION_ENDPOINT=<Your Azure Vision Endpoint>
```

### 4. Run the Application Locally

Run the Streamlit app:

```bash
streamlit run app.py
```

## Usage

1. Launch the application in your browser after starting Streamlit.
2. Upload an image using the Choose image button.
3. Click the Analyze image button to analyze the uploaded image.
4. View the results, including captions, dense captions, and tags, displayed on the page.

## Error Handling

If there is an error during the image analysis, the application will display an appropriate error message.

## Deployment

1. Build the Docker Image

```bash
docker build -t <dockerhub-username>/<image-name>:<tag> .
```

2. Push the Docker Image to Docker Hub

```bash
docker push <dockerhub-username>/<image-name>:<tag>
```

3. Deploy the Image to Azure Container App

- The application is deployed using Azure Container Apps, showcasing a seamless integration of cloud-based AI services.
- Azure Container App is configured to automatically pull the latest image from Docker Hub when a new version is available.
- No manual action is needed on the Azure portal unless you need to troubleshoot or update configuration settings.
- For details on deploying your own version, refer to [Azure Container Apps documentation](https://learn.microsoft.com/en-us/azure/container-apps/).
