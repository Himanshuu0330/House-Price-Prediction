# -*- coding: utf-8 -*-
"""appstream.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qkZHPnV4JvQER-kn6mamc7gZlJnlI4kg
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
import streamlit as st
import pickle
df=pd.read_csv("Train.csv")
df=df.drop(['LONGITUDE','LATITUDE','BHK_OR_RK'],axis=1)
df['ADDRESS'] = df['ADDRESS'].apply(lambda x: x.split(',')[-1].lower())
leloc= LabelEncoder()
lepost= LabelEncoder()
leloc.fit(df['ADDRESS'])
lepost.fit(df['POSTED_BY'])
pickled_model = pickle.load(open('modelprice.pkl', 'rb'))

address=df['ADDRESS'].unique()
postby=df['POSTED_BY'].unique()
#POSTED_BY>>	UNDER_CONSTRUCTION>>2	RERA	>>3BHK_NO.>>4		SQUARE_FT>>5	READY_TO_MOVE	>>6RESALE>>7	ADDRESS	>>8
def modelpred(postby,location,undconstru,rera,bhkno,sqft,readytomove,resale):
  keys = ['POSTED_BY', 'UNDER_CONSTRUCTION', 'RERA', 'BHK_NO.', 'SQUARE_FT', 'READY_TO_MOVE', 'RESALE', 'ADDRESS']
  arr={}
  arr['POSTED_BY']=lepost.transform([postby])[0]
  arr['UNDER_CONSTRUCTION']=undconstru
  arr['RERA']=rera
  arr['BHK_NO.']=bhkno
  arr['SQUARE_FT']=sqft
  arr['READY_TO_MOVE']=readytomove
  arr['RESALE']=resale
  arr['ADDRESS']=leloc.transform([location])[0]
  df = pd.DataFrame([arr])
  return pickled_model.predict(df)[0]
  


st.set_page_config(layout="wide")

st.title("HOUSE PRICE PREDICTION")
st.write("This Project is Devoloped for MiniSkill Project of Data Mining Lab ")


col1, col2,col3,col4 = st.tabs(['Sq. Ft.','BHK','Tab 3','Tab 4'])
with col1:
    loci = st.selectbox(" Select Address : ",
                     address)

    sqrft = st.slider('how much sqft ',900, 7000, 10)
with col2:
    postedby=st.selectbox("postedby",postby)
    bhk=int(st.text_input('No of BHK', '2'))
    
with col3:
    undercon = int(st.checkbox("is this Under Construction"))
    rer=int(st.checkbox('AREA project or not '))
  
with col4:
    
  resaler =int(st.checkbox('is it for RESALE '))
  redytomove =int(st.checkbox('is it ready to move '))



if(st.button("Predict Price")):
    

    price=int(modelpred(postedby,loci,undercon,rer, bhk,sqrft,redytomove,resaler))
    st.text("precited selling price in Lacs is: "+str(price))
    #modelpred('Dealer','mumbai',1,1, 4,1780,1,1)

    
  










ft = ""
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/sape94" target="_blank"> by sape94</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)


