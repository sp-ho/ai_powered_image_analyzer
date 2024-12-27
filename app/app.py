import os
import io
import streamlit as st
from PIL import Image
from dotenv import load_dotenv
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

# read the content of .env file
load_dotenv()

try:
    VISION_KEY = os.environ['VISION_KEY']
    VISION_ENDPOINT = os.environ['VISION_ENDPOINT']
except:
    print('Missing required env variables')
    exit()

# use image analysis client
client = ImageAnalysisClient(
    endpoint=VISION_ENDPOINT,
    credential=AzureKeyCredential(VISION_KEY)
)

# set up the title of the web page
st.title('Computer Vision with Streamlit')

# set up a form for image upload indicating the label and image types
uploadedFile = st.file_uploader('Choose image', type=['jpg', 'jpeg', 'png'])

# display the uploaded image
if uploadedFile:
    image = Image.open(uploadedFile)
    st.image(image, caption='Uploaded image')

    # pre-process the image
    imageBytes = io.BytesIO()
    image.save(imageBytes, format=image.format)
    imageBytes = imageBytes.getvalue()

    # create a button for analyzing the uploaded image
    if st.button('Analyze image'):
        try:
            # tell azure api what we want in the result
            visual_features = [
                VisualFeatures.TAGS,
                VisualFeatures.CAPTION,
                VisualFeatures.DENSE_CAPTIONS
            ]

            # make api call
            result = client.analyze(
                image_data=imageBytes,
                visual_features=visual_features
            )

            # display the caption result
            if result.caption:
                st.write("Caption:")
                st.write(f'{result.caption.text}')
                st.write(f'{result.caption.confidence:.4f}') # 4 decimal places

            # display the description
            if len(result.dense_captions.list) > 0:
                st.write("Dense Captions:")
                st.dataframe(result.dense_captions.list)

            # display the tags
            if len(result.tags.list) > 0:
                st.write("Tags")
                st.dataframe(result.tags.list)
        except Exception as e:
            st.error(f'There was an error when analyzing the image {e}')
