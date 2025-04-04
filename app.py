import torch
import gradio as gr
from torchvision import transforms
from PIL import Image
from torchvision.models import convnext_base
import requests

# Load pre-trained ConvNeXt model
model = convnext_base(weights="DEFAULT")
model.eval()  # Set to evaluation mode

# ImageNet class labels (download directly as text)
LABELS_URL = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
response = requests.get(LABELS_URL)
labels = response.text.split("\n")

# Image preprocessing
def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0)  # Add batch dimension

# Prediction function
def predict(image):
    image = preprocess_image(image)
    with torch.no_grad():
        outputs = model(image)
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
        top5_prob, top5_catid = torch.topk(probabilities, 5)
    return {labels[catid]: float(prob) for prob, catid in zip(top5_prob, top5_catid)}

# Gradio UI
demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=5),
    title="ConvNeXt Image Classifier",
    description="Upload an image and let ConvNeXt predict what's in it!"
)

demo.launch()
