import streamlit as st
from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt
from featurize_cloth import recommend  
from load_network_setup import gmm, alias, seg, opt
from utils import test

# Paths for images and files
predefined_image_path = r"datasets\test\image\07445_00.jpg"  # Path to the image shown in the sidebar
recommended_clothes_file = "recommend_clothes.txt"  # Text file to store recommended clothes paths
generated_images_dir = r"results\test"  # Directory where the generated images are stored

predefined_image_name = "07445_00.jpg"  # Predefined image name
test_pairs_file = r"datasets\test_pairs.txt"  # Path to store the image pairs

# Function to write image pairs to a text file
def save_image_pairs(selected_images, predefined_image, file_path):
    with open(file_path, 'w') as file:  # Open file in append mode
        for img_path in selected_images:
            # Extract the image name from the full path
            image_name = os.path.basename(img_path)
            # Write the predefined image and selected image as a pair
            file.write(f"{predefined_image} {image_name}\n")
            
            
# Initialize session state for selected images
if 'selected_images_paths' not in st.session_state:
    st.session_state.selected_images_paths = []

# Function to load image paths from a text file
def load_image_paths(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]
    return []

# Function to display images with checkboxes for selection, 3 images per row
def display_images_with_checkboxes(image_paths, num_columns=3):
    selected_images = []
    
    # Create a layout with `num_columns` columns
    cols = st.columns(num_columns)
    
    for i, img_path in enumerate(image_paths):
        # Open and display image
        img = Image.open(img_path)
        
        # Use modulo to place images in the respective column
        with cols[i % num_columns]:
            st.image(img, caption=f"Image {i+1}", use_column_width=True)
            # Use the image path as part of the key to ensure uniqueness
            if st.checkbox(f"Select Image {i+1}", key=f"select_{img_path}"):
                selected_images.append(img_path)
    
    return selected_images


# Streamlit App Layout
st.sidebar.title("Cloth Virtual Try-On")
predefined_image = Image.open(predefined_image_path)
st.sidebar.image(predefined_image, caption="Predefined Cloth Image", use_column_width=True)

# Upload option in the sidebar for cloth image
uploaded_image = st.sidebar.file_uploader("Upload a cloth image", type=["jpg", "png", "jpeg"])

# Recommend Dress button in the sidebar
if st.sidebar.button("Recommend Dress"):
    if uploaded_image:
        # Save the uploaded image to a temporary file
        uploaded_image_path = 'uploaded_image.jpg'
        with open(uploaded_image_path, 'wb') as file:
            file.write(uploaded_image.read())

        # Call the recommend function
        recommend()
        st.sidebar.success("Dress recommendation generated! Check Tab 1 for options.")
    else:
        st.sidebar.error("Please upload an image to recommend a dress.")

# Try on button in the sidebar
if st.sidebar.button("Try on"):
    if st.session_state.selected_images_paths:
        # Call the test function with the selected image paths        
        # Save image pairs to the test_pairs.txt file
        save_image_pairs(st.session_state.selected_images_paths, predefined_image_name, test_pairs_file)
        
        test(opt, seg, gmm, alias)
        
        st.sidebar.success("Images generated! Check Tab 2.")
        st.sidebar.success(f"Image pairs saved to {test_pairs_file}")
    else:
        st.sidebar.error("Please select clothes first.")

# Main Tabs
tab1, tab2 = st.tabs(["Recommended Clothes", "Generated Images"])

# Tab 1: Display recommended clothes with checkboxes for selection
with tab1:
    st.header("Recommended Clothes")
    
    # Load recommended clothes paths from the text file
    recommended_clothes = load_image_paths(recommended_clothes_file)
    
    if recommended_clothes:
        # Display images with checkboxes
        selected_clothes = display_images_with_checkboxes(recommended_clothes, num_columns=3)
        
        # Store the paths of selected clothes in session state
        st.session_state.selected_images_paths = selected_clothes
        # Inform about the selected images
        if selected_clothes:
            st.success(f"You have selected {len(selected_clothes)} clothes.")
    else:
        st.info("Upload an image and click 'Recommend Dress' to see recommendations.")

# Tab 2: Display generated images
with tab2:
    st.header("Generated Images")
    
    # Check if the directory for generated images exists
    if os.path.exists(generated_images_dir):
        generated_image_paths = [os.path.join(generated_images_dir, img) for img in os.listdir(generated_images_dir)]
        
        if generated_image_paths:
            display_images_with_checkboxes(generated_image_paths, num_columns=3)  # Optionally, use checkboxes for generated images too
        else:
            st.info("No generated images found yet.")
    else:
        st.info("Run the model first to generate images.")
