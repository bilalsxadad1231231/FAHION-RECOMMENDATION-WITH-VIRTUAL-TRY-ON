
# Fashion Recommender with Virtual Try-On: A Streamlit Demo

This project offers an AI-powered fashion experience, allowing users to upload a clothing image, receive recommendations, and perform a virtual try-on. Using ResNet50, the system extracts features from the uploaded image to recommend similar items based on cosine similarity. Selected items can then be visualized on the user using the VITON-HD model for realistic virtual try-on. The entire workflow is wrapped in an interactive Streamlit interface, providing a seamless journey from recommendations to try-on results.

## DEMO IMAGES
![Recommended Dress](https://github.com/bilalsxadad1231231/FAHION-RECOMMENDATION-WITH-VIRTUAL-TRY-ON/blob/main/Pictures/RECOMMEND_DRESS.jpg)

![Virtual Try-On Result](https://github.com/bilalsxadad1231231/FAHION-RECOMMENDATION-WITH-VIRTUAL-TRY-ON/blob/main/Pictures/TRY-ON.jpg)

## Features

- 1 : ResNet50 for Feature Extraction:

The ResNet50 model, a deep convolutional network pre-trained on ImageNet, is used to extract features from clothing images. It converts each clothing item into a 2048-dimensional feature vector, which is then used for comparing and recommending visually similar items based on cosine similarity.
VITON-HD for Virtual Try-On:

- 2 VITON-HD is employed for high-quality virtual try-on, enabling realistic rendering of the selected clothing item on the user’s image. This model uses generative techniques to transfer clothing from a source image onto a target (user) image, creating a seamless try-on experience.

## Dataset

For testing purposes, two dataset options are available:

1. **Zalando-HD Resized Dataset**:  
   You can download the high-quality fashion images resized for easier processing here:  
   [Zalando-HD Resized Dataset](https://www.dropbox.com/s/10bfat0kg4si1bu/zalando-hd-resized.zip?dl=0)

2. **Small Testing Dataset**:  
   If you prefer a smaller dataset for quick testing, use the link below:  
   [Small Testing Dataset](https://drive.google.com/drive/folders/0B8kXrnobEVh9flBkdnNYR3V5dTNKQmFWNURXMUExZ0lFcngxeGI1WkdLT3p5Z1h0OTc2MjQ?resourcekey=0-l_xMCXpXAg7uU5xMZYuKXA)

Both datasets contain a variety of clothing items that can be used to test the recommendation and virtual try-on functionality.

## DEMO IMAGES
![Recommended Dress](https://github.com/bilalsxadad1231231/FAHION-RECOMMENDATION-WITH-VIRTUAL-TRY-ON/blob/main/Pictures/RECOMMEND_DRESS.jpg)

![Virtual Try-On Result](https://github.com/bilalsxadad1231231/FAHION-RECOMMENDATION-WITH-VIRTUAL-TRY-ON/blob/main/Pictures/TRY-ON.jpg)
## Pretrained Networks

If you’d like to use the pretrained weights for the model, they are available for download. You can find the pretrained weights at the following link:  
[Pretrained Networks](https://drive.google.com/drive/folders/0B8kXrnobEVh9fnJHX3lCZzEtd20yUVAtTk5HdWk2OVV0RGl6YXc0NWhMOTlvb1FKX3Z1OUk?resourcekey=0-OIXHrDwCX8ChjypUbJo4fQ&usp=sharing)
