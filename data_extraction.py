import os
import pandas as pd
import re
import streamlit as st




def get_meta_title(text):
  for i in text.split("\n"):
    if len(i)>20:
      return i
def get_meta_desc(text):
  for i in text.split("\n")[2:]:
    if len(i)>30:
      return i


st.title("Data Extraction System")



file_name=st.file_uploader("Upload the File", type=["xlsx"])



# col1,col2,col3,col4,col5=st.columns(5)

# with col3:
if st.button("Submit"):
    if file_name is not None:
        df=pd.read_excel(file_name)

    df["meta_title"]=df["Unnamed: 2"].apply(lambda x:get_meta_title(x))
    df["meta_desc"]=df["Unnamed: 2"].apply(lambda x:get_meta_desc(x))

    df["meta_title"]=df["meta_title"].apply(lambda x:re.sub("\*\*Meta Title:\*\*","",x))
    df["meta_title"]=df["meta_title"].apply(lambda x:x.strip())



    df["meta_desc"]=df["meta_desc"].apply(lambda x:re.sub("\*\*Meta Description:\*\*","",x))
    df["meta_desc"]=df["meta_desc"].apply(lambda x:x.strip())
    st.write(df)
