# dependencies
from sklearn.ensemble import AdaBoostClassifier
import streamlit as st
import pandas as pd

# load AdaBoostClassifer model we created in jupyter notebook
model = AdaBoostClassifier
model.load_model('Model/model.json')

# cache for faster loading
@st.cache

# define a function to predict whether a new user is not diabetic (0) or prediabetic or diabetic (1)
def predict(HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income):

    # Predicting diabetes
    if HighBP == 'Yes':
        HighBP = 1
    elif HighBP == 'No':
        HighBP = 0

    if HighChol == 'Yes':
        HighChol = 1
    elif HighChol == 'No':
        HighChol = 0

    if CholCheck == 'Yes':
        CholCheck = 1
    elif CholCheck == 'No':
        CholCheck = 0

    if Smoker == 'Yes':
        Smoker = 1
    elif Smoker == 'No':
        Smoker = 0

    if Stroke == 'Yes':
        Stroke = 1
    elif Stroke == 'No':
        Stroke = 0

    if HeartDiseaseorAttack == 'Yes':
        HeartDiseaseorAttack = 1
    elif HeartDiseaseorAttack == 'No':
        HeartDiseaseorAttack = 0

    if PhysActivity == 'Yes':
        PhysActivity = 1
    elif PhysActivity == 'No':
        PhysActivity = 0

    if Fruits == 'Yes':
        Fruits = 1
    elif Fruits == 'No':
        Fruits = 0

    if Veggies == 'Yes':
        Veggies = 1
    elif Veggies == 'No':
        Veggies = 0
    
    if HvyAlcoholConsump == 'Yes':
        HvyAlcoholConsump = 1
    elif HvyAlcoholConsump == 'No':
        HvyAlcoholConsump = 0

    if AnyHealthcare == 'Yes':
        AnyHealthcare = 1
    elif AnyHealthcare == 'No':
        AnyHealthcare = 0

    if NoDocbcCost == 'Yes':
        NoDocbcCost = 1
    elif NoDocbcCost == 'No':
        NoDocbcCost = 0

    if GenHlth == 'Excellent':
        GenHlth = 1
    elif GenHlth == 'Very Good':
        GenHlth = 2
    elif GenHlth == 'Good':
        GenHlth = 3
    elif GenHlth == 'Fair':
        GenHlth = 4
    elif GenHlth == 'Poor':
        GenHlth = 5

    if DiffWalk == 'Yes':
        DiffWalk = 1
    if DiffWalk == 'No':
        DiffWalk = 0

    if Sex == 'Male':
        Sex = 1
    if Sex == 'Female':
        Sex = 0

    if Age >= 18 and Age <= 24:
        Age = 1
    elif Age >= 25 and Age <= 29:
        Age = 2
    elif Age >= 30 and Age <= 34:
        Age = 3
    elif Age >= 35 and Age <= 39:
        Age = 4
    elif Age >= 40 and Age <= 44:
        Age = 5
    elif Age >= 45 and Age <= 49:
        Age = 5
    elif Age >= 50 and Age <= 54:
        Age = 7
    elif Age >= 55 and Age <= 59:
        Age = 8
    elif Age >= 60 and Age <= 64:
        Age = 9
    elif Age >= 65 and Age <= 69:
        Age = 10
    elif Age >= 70 and Age <= 74:
        Age = 11
    elif Age >= 75 and Age <= 79:
        Age = 12
    elif Age >= 80:
        Age = 13

    if Education == 'Never attended school or only kindergarden':
        Education = 1
    elif Education == 'Elementary School':
        Education = 2
    elif Education == 'Middle School':
        Education = 3
    elif Education == 'High School':
        Education = 4
    elif Education == 'College (Did Not Finish)':
        Education = 5
    elif Education == 'College (4 Years or more)':
        Education = 6

    if Income < 10000:
        Income = 1
    elif Income < 16250:
        Income = 2
    elif Income < 22500:
        Income = 3
    elif Income < 28750:
        Income = 4
    elif Income < 35000:
        Income = 5
    elif Income < 55000:
        Income = 6
    elif Income < 75000:
        Income = 7
    elif Income >= 75000:
        Income = 8

    prediction = model.predict(pd.DataFrame([[HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income]]))
    return prediction

# Build the streamlit app
# Give basic title, image, and prompt to user
st.title('Diabetes Predictor')
st.image("""https://res.cloudinary.com/grohealth/image/upload/c_fill,f_auto,fl_lossy,h_650,q_auto,w_1085/v1581695681/DCUK/Content/causes-of-diabetes.png""")
st.header('If you are 18 or older, please answer the following survey questions:')

# Define user inputs
HighBP = st.selectbox('Do you have High Blood Pressure?', ['Yes', 'No'])
HighChol = st.selectbox('Do you have High Cholesterol?', ['Yes', 'No'])
CholCheck = st.selectbox('Have you had a Cholestoral Check in the last 5 years?', ['Yes', 'No'])
BMI = st.number_input('Enter your approximate BMI (between 1 and 99):', min_value=1.0, max_value=99.0, value=1.0)
Smoker = st.selectbox('Have you smoked at least 100 cigarettes in your life?', ['Yes', 'No'])
Stroke = st.selectbox('Have you ever been told you had a stroke?', ['Yes', 'No'])
HeartDiseaseorAttack = st.selectbox('Do you have coronary heart disease of myocardial infarction?', ['Yes', 'No'])
PhysActivity = st.selectbox('Have you had physical activity in past 30 days (not including job)?', ['Yes', 'No'])
Fruits = st.selectbox('Do you consume fruit at least once a day?', ['Yes', 'No'])
Veggies = st.selectbox('Do you consume vegetables at least once a day?', ['Yes', 'No'])
HvyAlcoholConsump = st.selectbox('Are you a heavy drinker by the following criteria? Adult Male over 14 drinks per week. Adult Female over 7 drinks per week:', ['Yes', 'No'])
AnyHealthcare = st.selectbox('Do you have any kind of health care coverage?', ['Yes', 'No'])
NoDocbcCost = st.selectbox('Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?', ['Yes', 'No'])
GenHlth = st.selectbox('Rate your general health:', ['Excellent', 'Very Good', 'Good', 'Fair', 'Poor'])
MentHlth = st.number_input('Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good? (between 10 and 30):', min_value=0.0, max_value=30.0, value=0.0)
PhysHlth = st.number_input('Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? (between 10 and 30):', min_value=0.0, max_value=30.0, value=0.0)
DiffWalk = st.selectbox('Do you have serious difficulty walking or climbing stairs?', ['Yes', 'No'])
Sex = st.selectbox('What is your biological gender?', ['Male', 'Female'])
Age = st.number_input('What is your age:', min_value=18.0, max_value=150.0, value=18.0)
Education = st.selectbox('What is your highest completed education?', ['Never attended school or only kindergarden', 'Elementary School', 'Middle School', 'High School', 'College (Did Not Finish)', 'College (4 Years or more)'])
Income = st.number_input('What is your income:', min_value=0.0, max_value=100000000.0, value=0.0)

if st.button('Predict Diabetes'):
    diabetes = predict(HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income)
    if diabetes == 0:
        st.success(f'The model says you are not diabetic.')
    elif diabetes == 1:
        st.success(f'The model says you are prediabetic or diabetic.')