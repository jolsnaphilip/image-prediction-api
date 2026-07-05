from fastapi import FastAPI, UploadFile, File
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions,
)

app = FastAPI(title="Image Prediction API")

# Load the pre-trained model once when the app starts
model = MobileNetV2(weights="imagenet")


@app.get("/")
def home():
    return {"message": "Image Prediction API is running!"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Open uploaded image
    image = Image.open(file.file).convert("RGB")

    # Resize image for the model
    image = image.resize((224, 224))

    # Convert image to array
    image_array = np.array(image)

    # Add batch dimension
    image_array = np.expand_dims(image_array, axis=0)

    # Preprocess for MobileNetV2
    image_array = preprocess_input(image_array)

    # Predict
    prediction = model.predict(image_array)

    # Decode prediction
    label = decode_predictions(prediction, top=1)[0][0][1]

    return {
        "prediction": label
    }