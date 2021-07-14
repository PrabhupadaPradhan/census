import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
@st.cache()
def load_data():
	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	df.head()
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)
	df.head()
	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)
	df.dropna(inplace=True)
	df.drop(columns='fnlwgt',axis=1,inplace=True)
	return df
census_df = load_data()
if st.checkbox("show raw data"):
    st.subheader("Census Data Set")
    st.dataframe(census_df)
    st.write("The dataframe has ", census_df.shape[0], " rows and ", census_df.shape[1], "columns.")