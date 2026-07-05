import torch
import torchvision.transforms as transforms
from torchvision.models import mobilenet_v2, MobileNet_V2_Weights
from PIL import Image
import gradio as gr

# Load model
weights = MobileNet_V2_Weights.DEFAULT
model = mobilenet_v2(weights=weights)
model.eval()

# Transform
preprocess = weights.transforms()

# Prediction function
def predict(image):
    image = preprocess(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(image)
        predicted = outputs.argmax(1).item()

    label = weights.meta["categories"][predicted]
    return label

# UI
demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Image Prediction API"
)

demo.launch()