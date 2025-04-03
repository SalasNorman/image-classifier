import torch
import torchvision.transforms as transforms
import gradio as gr
from PIL import Image
import torch.nn.functional as F
from model import SimpleCNN

# Load model
model = SimpleCNN()
model.load_state_dict(torch.load("model.pth", map_location=torch.device('cpu')))
model.eval()

# Define labels (CIFAR-10 classes)
classes = ["airplane", "automobile", "bird", "cat", "deer", 
           "dog", "frog", "horse", "ship", "truck"]

# Define image preprocessing
transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

def classify_image(image):
    image = transform(image).unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        output = model(image)
        probabilities = F.softmax(output, dim=1)
        confidence, predicted_class = torch.max(probabilities, 1)
    return {classes[predicted_class.item()]: float(confidence)}

# Create Gradio interface
iface = gr.Interface(fn=classify_image, 
                     inputs=gr.Image(type="pil"), 
                     outputs=gr.Label(),
                     title="Image Classifier",
                     description="Upload an image and get classification results.")

iface.launch()
