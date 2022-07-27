#Loading Necessary Libraries
import pickle
import pandas as pd
import streamlit as st



carsDF = pd.read_csv('CarPricePredictor/Cars_CSV') #Reading the cleaned CSV file.
model = pickle.load(open('CarPricePredictor/XGBModelFinal.pkl', 'rb')) #Loading the Model
st.set_page_config(page_title='Car Price Predictior - Mitesh Soni', page_icon='car.png') #Standard settings for WebApp

def WebApp(): #Function 
    st.image('CarPricePredictor/car.png',width=500) #Setting up the Image
    st.sidebar.title('CAR PRICE PREDICTOR') #Setting the Title
    st.sidebar.write(" ") #Formatting Spaces.
    
    #----Setting up of Selectboxes and Slider-----
    
    Companyname = st.sidebar.selectbox(
        "Please Select Car's Company",
        ([i for i in carsDF.Companyname.unique()]))
    if Companyname:
        Name = st.sidebar.selectbox(
            "Please Select Car's Name/ Model",
            ([i for i in  carsDF.Name.unique() if str(i).startswith(Companyname)]))
    Transmission = st.sidebar.selectbox(
        "Please Select Location",
        ([i for i in carsDF.Transmission.unique()]))
    Fuel = st.sidebar.selectbox(
        "Please Select Fuel Type",
        ([i for i in carsDF.Fuel.unique()]))
    Owner = st.sidebar.selectbox(
        "Owner?",
        ([i for i in carsDF.Owner.unique()]))
    Seller_Type = st.sidebar.selectbox(
        "Seller_Type?",
        ([i for i in carsDF.Seller_Type.unique()]))
    Km_Driven = st.sidebar.text_input(
        "Km_Driven?",00)
    Year = st.sidebar.slider("Year of Purchase",1990,2022,1990) #Slider

    submit = st.sidebar.button('Submit') #Submit Button
    output = model.predict(pd.DataFrame([[Name,Year,Km_Driven,Fuel,Seller_Type,Transmission,Owner,Companyname]],columns=["Name","Year","Km_Driven","Fuel","Seller_Type","Transmission","Owner","Companyname"])) #Model's Prediction
    prediction = round(output[0]/100000,2) #Rounding of the Prediction.

    if submit: #On Click Effects.
        st.balloons()
        st.info('The Searched Car is Good to Sell around {} Lakh Rupees'.format(prediction)) #Prediction Display 

if __name__ == '__main__':
    WebApp() #Calling of Function


