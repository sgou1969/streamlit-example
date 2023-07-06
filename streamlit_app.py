# port 3351

import pandas as pd; import streamlit as st

import streamlit.components.v1 as components



def betcalc2(oddx,betAmin,betAmax,oddy,betBmin,betBmax):
 
# with st.spinner('**Please Wait for Results...**'):  
     
  mostprofitAx=mostprofitBx=mostprofitAy=mostprofitBy=0
  mostbetAx=mostbetBx=mostbetAy=mostbetBy=bestchoice=0
  topbet=betdet=fulls=fullsA=fullsB=fA=fB=''
       
 # df = pd.DataFrame(columns=['betA', 'returnA', 'profitA', 'betB', 'returnB', 'profitB','finalprofitA','finalprofitB'])
    
 

def betcalc3(oddx,betAmin,betAmax,oddy,betBmin,betBmax,oddz,betCmin,betCmax):
 
 #with st.spinner('**Please Wssssait for Results...**'):  
     
  mostprofitAx=mostprofitBx=mostprofitAy=mostprofitBy= mostprofitCx=mostprofitCy=0
  mostbetAx=mostbetBx=mostbetAy=mostbetBy= mostbetCx=mostbetCy=bestchoice=0
  topbet=betdet=fulls=fullsA=fullsB=fullsC=fA=fB=fC=''
       
  

with st.form("bet",clear_on_submit=False): 
 
    col1, col2, col3,col4,col5= st.columns([3.5,0.5,3.5,1,3.5])
    
    with col1:   
       oddx = st.number_input('odd betA')
       betAmin = st.number_input('betA minimum', value=3)
       betAmax = st.number_input('betA maximum', value=25)
      
    with col3: 
       oddy = st.number_input('odd betB')
       betBmin = st.number_input('betB minimum', value=2)
       betBmax = st.number_input('betB maximum', value=12)
    
    with col4:
       submitted_check = st.form_submit_button("Calculate")
          
    with col5: 
       oddz = st.number_input('odd betC')
       betCmin = st.number_input('betC minimum', 2)
       betCmax = st.number_input('betC maximum', 12)
         
    
    
    if submitted_check:
      
      if oddz==0:
         
         betcalc2(oddx,betAmin,betAmax,oddy,betBmin,betBmax)
      else:
        
         betcalc3(oddx,betAmin,betAmax,oddy,betBmin,betBmax,oddz,betCmin,betCmax)
        
       
   
