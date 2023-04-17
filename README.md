# DSCI441-machine-learning-project

# Machine Learning Financial Applications: Credit Card Fraud Detection

## Project Description

Machine learning models have already had significant development in engineering and biological applications. However, sometimes their accuracy and security are challenged by the financial industry. At the same time, expensive failure cost and fierce competition provoke advanced machine learning models to be used in stock forecasting, risk prediction, recommendation systems in e-commerce, fraud detection and so on. Recent years, graph-based data, with its adaptability, flexibility and agility, seems ideal for the complexity and flexibility of financial markets and applications because it can simulate realistic transactions better compared with other formats of data. In this research, we will focus on machine learning models used in credit card fraud detection and evaluating the performance of different model constructions.

### Data Source
Dataset:https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

###  Methodology
(1)Data processing (SMOTE method)

(2)Feature selection and dimensionality reduction to reduce the number of input features before fitting into the model by particle swarm optimization

(3)LSTM model with attention mechanism 

(4)Performance Evaluation

### Code operating instruction
Code part includes two parts. one is for feature selection and the other one is for model construction and evaluation.

First open the code named "DSCI_441_final_project.ipynb" and run the first four cells and then refer to the code named "swarm_feature_selection.ipynb" to see the results of the feature selection. However it will take long time to get the results. After reading the results of the "swarm_feature_selection.ipynb", then going back to "DSCI_441_final_project.ipynb" to run the other part of codes cell by cell.

The structure of "DSCI_441_final_project.ipynb" includes the following parts:

(1) Data Preprocessing (2)Feature Extraction (3)Model Development (4)Model Assessment
These parts is the process for exploring credit card fraud detection



### References
https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional

https://arxiv.org/pdf/1811.05320.pdf

https://arxiv.org/pdf/1909.09586.pdf

https://dl.acm.org/doi/pdf/10.1145/3442381.3449989
