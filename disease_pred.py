import streamlit as st
import openai
import os
import pandas as pd
import pickle
from streamlit_option_menu import option_menu
#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
# reading the dataframes
df=pd.read_csv("dataset.csv")
df2=pd.read_csv("Symptom-severity.csv")
df3=pd.read_csv("symptom_Description.csv")
df4=pd.read_csv("symptom_precaution.csv")
# loading the saved model
disease_model=pickle.load(open('C:/Users/FRANK/Desktop/Disease prediction system/disease_pred.sav','rb'))
# loading the standardisation technique
standardised_data=pickle.load(open('C:/Users/FRANK/Desktop/Disease prediction system/standard_scaler (1).pkl','rb'))

with st.sidebar:
	selected=option_menu("DISEASE PREDICTION SYSTEM",
			['Disease Prediction','Disease Precaution','Disease Description','Medical Assistant'],default_index=0)



if(selected=='Disease Prediction'):
    
	st.title("MULTIPLE DISEASE PREDICTION")
	col1,col2=st.columns(2)
    
	#user input as dictionary
	user_input={}
	
	#Function to encode the data
	def remove_space_between_words(df):
		for col in df.columns:
			if df[col].dtype == 'object':
				df[col] = df[col].str.strip().str.replace(" ", "_")
		return df
	df = remove_space_between_words(df)
	def encode_symptoms(df, df2):
		for i in df2.index:
			symptom = df2["Symptom"][i]
			weight = df2["weight"][i]
			df = df.replace(symptom, weight)

		# Replace missing values with 0
		df = df.fillna(0)

		# Additional hardcoded replacements
		df = df.replace("foul_smell_of_urine", 5)
		df = df.replace("dischromic__patches", 6)
		df = df.replace("spotting__urination", 6)
    
		return df
	
	
		
	with col1:
		user_input["Symptom_1"]=st.selectbox("Symptom 1",['']+list(df2['Symptom']))

	with col2:                
		user_input["Symptom_2"]=st.selectbox("Symptom 2",['']+list(df2['Symptom']))
	
	with col1:
		user_input["Symptom_3"]=st.selectbox("Symptom 3",['']+list(df2['Symptom']))
	
	with col2:
		user_input["Symptom_4"]=st.selectbox("Symptom 4",['']+list(df2['Symptom']))
	
	with col1:
		user_input["Symptom_5"]=st.selectbox("Symptom 5",['']+list(df2['Symptom']))
	
	with col2:
		user_input["Symptom_6"]=st.selectbox("Symptom 6",['']+list(df2['Symptom']))
	
	with col1:
		user_input["Symptom_7"]=st.selectbox("Symptom 7",['']+list(df2['Symptom']))
	
	with col2:
		user_input["Symptom_8"]=st.selectbox("Symptom 8",['']+list(df2['Symptom']))
	
	with col1:
		user_input["Symptom_9"]=st.selectbox("Symptom 9",['']+list(df2['Symptom']))
	
	with col2:
		user_input["Symptom_10"]=st.selectbox("Symptom 10",['']+list(df2['Symptom']))
	
	with col1:
		user_input["Symptom_11"]=st.selectbox("Symptom 11",['']+list(df2['Symptom']))
	
	with col2:
		user_input["Symptom_12"]=st.selectbox("Symptom 12",['']+list(df2['Symptom']))
	
	with col1:
		user_input["Symptom_13"]=st.selectbox("Symptom 13",['']+list(df2['Symptom']))

	with col2:	
		user_input["Symptom_14"]=st.selectbox("Symptom 14",['']+list(df2['Symptom']))

	with col1:	
		user_input["Symptom_15"]=st.selectbox("Symptom 15",['']+list(df2['Symptom']))
	
	with col2:
		user_input["Symptom_16"]=st.selectbox("Symptom 16",['']+list(df2['Symptom']))
	
	with col1:
		user_input["Symptom_17"]=st.selectbox("Symptom 17",['']+list(df2['Symptom']))
	
	
	
	
	  
	if st.button("PREDICT DISEASE"):
		user_input_df=pd.DataFrame([user_input])

		#Replace the empty string with 0
		user_input_df=user_input_df.replace("",0)
		st.write(user_input_df)
	
		encoded_input = encode_symptoms(user_input_df, df2)
		st.write(encoded_input)

		final_input=standardised_data.transform(encoded_input)
		prediction = disease_model.predict(final_input)
		st.success(f"Predicted Disease: {prediction}")

	st.write(df)
	
	
	


 

if(selected=='Disease Precaution'):
    st.title("DISEASE PRECAUTION")
    st.write(df4)
   
if(selected=='Disease Description'):
    st.title("DISEASE DESCRIPTION")
    st.write(df3)
   
if(selected=='Medical Assistant'):
	st.header("MEDICAL ASSISTANT")
	import os
	import openai

	
	reviews=st.text_area("Copy Paste any customer symptoms")
	button= st.button("Autogenerate Response")

   