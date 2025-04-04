# **Image Classifier**  
This project uses a pre-trained **ConvNeXt** model on **ImageNet** to classify images using a **Gradio** interface. You can upload an image, and the model will predict the top 5 categories.

## **Files in this Repo**:
- **`app.py`**: Python script for running the image classifier.
- **`requirements.txt`**: Dependency file listing the necessary Python libraries.

## **Deploy to Locally**:

### **1. Clone the repository**:
```bash
git clone https://github.com/YOUR_USERNAME/image-classifier.git
cd image-classifier
```

### **2. Install dependencies**:
```bash
pip install -r requirements.txt
```

### **3. Run the app**:
```bash
python app.py
```

This will launch the Gradio interface locally. Now, you can upload images to see predictions.

## **Deploy to Hugging Face Spaces**:

1. Go to [Hugging Face Spaces](https://huggingface.co/spaces).
2. Create a new Space with the **Gradio** template.
3. Push your repository to the Space.
4. Hugging Face Spaces will automatically install the dependencies from **`requirements.txt`** and run **`app.py`**.

## **Deploy to GitHub Codespaces**:

To run this app in **GitHub Codespaces**, follow these steps:

1. From this **GitHub repository page**, click the **green "Code" button**.
2. Select **"Codespaces"** from the dropdown and then click the **"+"** button to create a new Codespace.
3. Wait for the setup to complete. It may take a few minutes.
   - (Note: If you're using a mobile device, switch to the desktop site to properly view and use Codespaces.)
4. Once the Codespace is ready, the environment will automatically install the dependencies from **`requirements.txt`**.  
   - If you encounter an error about missing dependencies, run the following command in the terminal:
     ```bash
     pip install -r requirements.txt
     ```

5. Once everything is set up, run the app:
   ```bash
   python app.py
   ```

   After running the app, a pop-up window will appear asking you to **"open in browser"**. Click the button, and it will redirect to a new browser tab where you can interact with the app.

---

## **License**:
MIT License - see the [LICENSE](LICENSE) file for details.

---

### **Key Points**:
- The setup in **GitHub Codespaces** will automatically install the required dependencies from **`requirements.txt`**.
- If there is an error about missing dependencies, manually run `pip install -r requirements.txt`.
- Once you run **`python app.py`**, make sure to click the **"open in browser"** pop-up to access the app in your browser.
