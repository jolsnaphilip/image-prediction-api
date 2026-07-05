# Image Prediction API

## Project Overview

This project is an Image Prediction API built using **Python**, **FastAPI**, and **TensorFlow**.

The API accepts an image uploaded by the user and predicts the object present in the image using the pre-trained **MobileNetV2** model. The prediction is returned in **JSON** format.

---

# Objective

The objective of this project is to create a REST API that can classify images and return the prediction to the user.

---

# Technologies Used

* Python
* FastAPI
* TensorFlow
* MobileNetV2 (Pre-trained Model)
* Pillow
* NumPy
* Uvicorn

---

# Project Structure

```text
image-prediction-api/
│── app.py
│── requirements.txt
└── README.md
```

---

# How the Project Works

### Step 1: Upload an Image

The user uploads an image through the `/predict` API endpoint.

Examples:

* Cat
* Dog
* Car
* Laptop
* Banana

---

### Step 2: Read the Image

The uploaded image is read using the Pillow library.

---

### Step 3: Resize the Image

The image is resized to **224 × 224 pixels**, which is the required input size for the MobileNetV2 model.

---

### Step 4: Predict the Image

The image is converted into a NumPy array, preprocessed, and passed to the pre-trained MobileNetV2 model.

The model predicts the object present in the image.

---

### Step 5: Return the Result

The API returns the prediction in JSON format.

Example:

```json
{
  "prediction": "tabby"
}
```

---

# API Endpoints

## Home

**GET /**

Returns a message indicating that the API is running.

Example Response:

```json
{
  "message": "Image Prediction API is running!"
}
```

---

## Predict Image

**POST /predict**

Uploads an image and returns the predicted object.

Example Response:

```json
{
  "prediction": "golden_retriever"
}
```

---

# Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

# Run the Project

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Open the automatically generated API documentation:

```text
http://127.0.0.1:8000/docs
```

From this page you can upload an image and test the API directly in your browser.

---

# Deployment

This project can be deployed on **Render**.

### Steps

1. Push the project to GitHub.
2. Create a new Web Service on Render.
3. Connect your GitHub repository.
4. Use the following settings:

**Build Command**

```text
pip install -r requirements.txt
```

**Start Command**

```text
uvicorn app:app --host 0.0.0.0 --port 10000
```

5. Deploy the application.

After deployment, Render provides a public URL that can be used to access the API from anywhere.

---

# Sample Output

```json
{
  "prediction": "tabby"
}
```

---

# What I Learned

* What an API is.
* How FastAPI creates API endpoints.
* How to upload images through an API.
* How a pre-trained machine learning model performs image classification.
* How to return predictions in JSON format.
* How to test APIs using the FastAPI Swagger UI.
* How to deploy a FastAPI application on Render.

---

# Future Improvements

* Show prediction confidence scores.
* Support multiple image uploads.
* Train a custom image classification model.
* Add a web interface for uploading images.
* Support more image formats.

---

# Conclusion

This project demonstrates how to build an Image Prediction API using FastAPI and TensorFlow. The API receives an image, processes it with the MobileNetV2 pre-trained model, predicts the object in the image, and returns the result in JSON format. It also includes automatic API documentation through FastAPI and can be deployed on Render for public access.
