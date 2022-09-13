# Diabetes-Detection

Diabetes is among the most common chronic diseases in the United States impacting millions of Americans each year.

In this repository, different supervised classification models were fit and tuned on a dataset created from a Behavorial Risk Factor Surveillance System (BRFSS) telephone survey that is collected annually by the CDC and was made available on Kaggle. 

The CDC estimates that 1 in 5 diabetics, and roughly 8 in 10 pre-diabetics are unaware of their risk. Early diagnosis can lead to lifestyle changes and more effective treatment. 

Using this dataset, predictive modeling seeks to assist in early detection. The best model was then used to create a web application using streamlit.

In addition, Tableau was used to create visualizations to help understand the target and feature variables in the dataset.

Models Used: Logistic Regression, Random Forest Classifier, Ada Boost Classifier

Libraries/Tools Used: Jupyter Notebook, Python, Pandas, Sklearn, Pickle, Streamlit, Tableau

Data Source: https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset?select=diabetes_binary_health_indicators_BRFSS2015.csv

Web App: https://vtnoble-diabetes-detection-app-uzoftx.streamlitapp.com/

<<<<<<< HEAD
![Web App Preview](app_screenshot.png?raw=true "Web App Preview")

2022-09-13 Update: Models were tested on a dataset that has a 50/50 split of the target variable.
    * Findings:
        * Accuracy decreased from ~85% to ~76% and recall decreased from ~97% to ~76%. This is likely due to the full dataset being heavily leaned towards the non-diabetic (0 value) for the target variable.
        * While the models performed better on unscaled data with the full dataset, they performed better on the scaled data witht he 50/50 split dataset.
        * A XGBoost model was tested and slightly outperformed the ADABoost model.
    
=======
![Web App Preview](app_screenshot.png?raw=true "Web App Preview") 
>>>>>>> 35c81e7b2fd16a3342f4f1785ab2b10d35c6fb6a
