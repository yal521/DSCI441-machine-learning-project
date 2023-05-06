# DSCI441-machine-learning-project

# Machine Learning Financial Applications: Credit Card Fraud Detection

## Project Description

Machine learning models have already had significant development in engineering and biological applications. However, sometimes their accuracy and security are challenged by the financial industry. At the same time, expensive failure cost and fierce competition provoke advanced machine learning models to be used in stock forecasting, risk prediction, recommendation systems in e-commerce, fraud detection and so on. The NILSON report predicts that huge card fraud losses of $ 49.32 billion will be projected in 2030. In order to have an advanced solution for this problem, the research project will focus on machine learning models used in credit card fraud detection and evaluating the performance of different model constructions. 

### Data Source
Dataset:https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

###  Methodology
(1)Data processing (SMOTE method)

(2)Feature selection and dimensionality reduction to reduce the number of input features before fitting into the model by particle swarm optimization

(3)Building Logistic regression model, LSTM model, and LSTM model with attention mechanism 

(4)Performance Evaluation:making comparison among these three

### Code operating instruction
Code part includes two parts. one is for feature selection and the other one is for model construction and evaluation.

The original dataset it too big to upload in Github so I put them in a google drive folder. Also you can download it by the link (https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). Due to the csv dataset relies on the path from drive folder, if it is difficult for you to run it successfully, I will also offer the google drive folder link (https://drive.google.com/drive/u/0/folders/1tmY-NsNvENfVKvUPPrbgdpx22HjzXQmG). Feel free to download the whole folder in your account and run. If it cannot run successfully, change a little bit about the dataset path in your drive folder, it will run successfully. The results will change a little bit each time you run the code but the overall conclusion is what I get in the report.

First open the code named "DSCI_441_final_project.ipynb" and run code before feature selection part and then refer to the code named "Feature_Selection_PSO.ipynb" to see the results of the feature selection. However it will take long time to get the results. After reading the results of the "Feature_Selection_PSO.ipynb", then going back to "DSCI_441_final_project.ipynb" to run the other part of codes cell by cell.

The structure of "DSCI_441_final_project.ipynb" includes the following parts:

(1) Data Preprocessing (2)Feature Extraction (3)Model Development (4)Model Assessment
These parts is the process for exploring credit card fraud detection

### Demo 

Video Link:https://drive.google.com/drive/u/0/folders/1MMmgeck2T9aaTH4J2KCWwcQnsSwutXzx

Pdf Link:https://drive.google.com/drive/u/0/folders/1MMmgeck2T9aaTH4J2KCWwcQnsSwutXzx

I also upload the pdf in the github repo


### References
https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional

https://arxiv.org/pdf/1811.05320.pdf

https://arxiv.org/pdf/1909.09586.pdf

https://dl.acm.org/doi/pdf/10.1145/3442381.3449989

https://nilsonreport.com/upload/content_promo/NilsonReport_Issue1209.pdf

https://machinelearningmastery.com/a-gentle-introduction-to-particle-swarm-optimization/

https://towardsdatascience.com/smote-fdce2f605729

https://www.bioinf.jku.at/publications/older/2604.pdf

https://www.kdnuggets.com/2021/01/attention-mechanism-deep-learning-explained.html

https://reader.elsevier.com/reader/sd/pii/S092523122100477X?token=45D132B9DF241517DCE3CCD5C8F286FD47B44F266FC3374283113A4EE9884A19DFE9CA6A87CDBF3EF52B6B8B82CA0D72&originRegion=us-east-1&originCreation=20230506001011



