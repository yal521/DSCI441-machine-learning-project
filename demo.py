#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 05:03:08 2023

@author: yangliu
"""

import streamlit as st
from PIL import Image

# Load the image from a file
image1 = Image.open("/Users/yangliu/Desktop/DSCI441/GitHub_DSCI441_final_project/DSCI441-machine-learning-project/DSCI441_demo/data1.png")
image2 = Image.open("/Users/yangliu/Desktop/DSCI441/GitHub_DSCI441_final_project/DSCI441-machine-learning-project/DSCI441_demo/data2.png")
image3 = Image.open("/Users/yangliu/Desktop/DSCI441/GitHub_DSCI441_final_project/DSCI441-machine-learning-project/DSCI441_demo/Plot Before SMOTE.png")
image4 = Image.open("/Users/yangliu/Desktop/DSCI441/GitHub_DSCI441_final_project/DSCI441-machine-learning-project/DSCI441_demo/Plot After SMOTE.png")
image5 = Image.open("/Users/yangliu/Desktop/DSCI441/GitHub_DSCI441_final_project/DSCI441-machine-learning-project/DSCI441_demo/PSO results.png")
image6 = Image.open("/Users/yangliu/Desktop/DSCI441/GitHub_DSCI441_final_project/DSCI441-machine-learning-project/DSCI441_demo/LSTM_model.png")
image7 = Image.open("/Users/yangliu/Desktop/DSCI441/GitHub_DSCI441_final_project/DSCI441-machine-learning-project/DSCI441_demo/Loss for LSTM.png")
image8 = Image.open("/Users/yangliu/Desktop/DSCI441/GitHub_DSCI441_final_project/DSCI441-machine-learning-project/DSCI441_demo/Accuracy for LSTM.png")
image9 = Image.open("/Users/yangliu/Desktop/DSCI441/GitHub_DSCI441_final_project/DSCI441-machine-learning-project/DSCI441_demo/Confusion matrix for LSTM.png")
image10 = Image.open("/Users/yangliu/Desktop/DSCI441/GitHub_DSCI441_final_project/DSCI441-machine-learning-project/DSCI441_demo/LSTM_Attention_model.png")
image11 = Image.open("/Users/yangliu/Desktop/DSCI441/GitHub_DSCI441_final_project/DSCI441-machine-learning-project/DSCI441_demo/Loss for LSTM_Attention.png")
image12 = Image.open("/Users/yangliu/Desktop/DSCI441/GitHub_DSCI441_final_project/DSCI441-machine-learning-project/DSCI441_demo/Accuracy for LSTM_Attention.png")
image13 = Image.open("/Users/yangliu/Desktop/DSCI441/GitHub_DSCI441_final_project/DSCI441-machine-learning-project/DSCI441_demo/Confusion matrix for LSTM_Attention.png")
image14 = Image.open("/Users/yangliu/Desktop/DSCI441/GitHub_DSCI441_final_project/DSCI441-machine-learning-project/DSCI441_demo/Comparison_three_models.png")


# Display the image in Streamlit
st.write("Visualizations of Machine Learning Model Comparison for Credit Card Fraud Detection")


st.write("Dataset")
st.image(image1, caption="Credit Card Fraud Detection Dataset-part1")
st.image(image2, caption="Credit Card Fraud Detection Dataset-part2")

st.write("Data Preprocessing (data augmentation): SMOTE(Synthetic Minority Oversampling Technique)")
st.image(image3, caption="Data Preprocessing-Before SMOTE")
st.image(image4, caption="Data Preprocessing-After SMOTE")


st.write("Feature Selection : PSO(Particle Swarm Optimization) results")
st.image(image5, caption="Feature Selection-PSO results")


st.write("Model Construction and Evaluation : LSTM & LSTM_Attention")
st.write("Model Structure")
st.image(image6, caption="LSTM Model")
st.image(image10, caption="LSTM_Attention Model")
st.write("Loss Comparison")
st.image(image7, caption="Loss for LSTM")
st.image(image11, caption="Loss for LSTM_Attention")
st.write("Accuracy Comparison")
st.image(image8, caption="Accuracy for LSTM")
st.image(image12, caption="Accuracy for LSTM_Attention")
st.write("Confusion Matrix Comparison")
st.image(image9, caption="LSTM Model")
st.image(image13, caption="LSTM_Attention Model")


st.write("Comparison of Three Models")
st.image(image14,caption="Model Comparison Results")


