# port 3351

import pandas as pd; import streamlit as st

import streamlit.components.v1 as components

# oddx=1.55
# oddy=3

# betAmin=2
# betAmax=20

# betBmin=1
# betBmax=12


            
def streamlit_init_conf():
  #---------------------------------------- streamlit ------------------------------------------

  st.set_page_config(
      page_title="Bt",
      page_icon=":wave:",   
      layout="wide",
      initial_sidebar_state="expanded",
  )

 
  #### main page padding ##################

  st.markdown(f""" <style>
    .appview-container .main .block-container{{
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
        }}
 </style> """, unsafe_allow_html=True)

 #### sidebar padding ################## 

  st.markdown("""
  <style>
    .css-1544g2n {
      margin-top: -75px;
    }
  </style>
 """, unsafe_allow_html=True)
  
 ##### horizontal line padding ###########

  s = f"""
    <style>
    hr {{
      margin: 0em 0px ;
      }}
    <style>
    """
  st.markdown(s, unsafe_allow_html=True)  
  
 ###### hide menu and footer #############
 
  hide_streamlit_style = """
              <style>
              #MainMenu {visibility: hidden;}
              footer {visibility: hidden;}
              .css-hi6a2p {padding-top: 0rem;}
              .reportview-container .main .block-container {max-width: 98%;}
              </style>
              """
  st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

 
def betcalc2(oddx,betAmin,betAmax,oddy,betBmin,betBmax):
 
 with st.spinner('**Please Wait for Results...**'):  
     
  mostprofitAx=mostprofitBx=mostprofitAy=mostprofitBy=0
  mostbetAx=mostbetBx=mostbetAy=mostbetBy=bestchoice=0
  topbet=betdet=fulls=fullsA=fullsB=fA=fB=''
       
  df = pd.DataFrame(columns=['betA', 'returnA', 'profitA', 'betB', 'returnB', 'profitB','finalprofitA','finalprofitB'])
    
  for x in range(betAmin*10, (betAmax*10)+1, 1):
    valuex = x / 10.0
   
    returnx=oddx * valuex
    for y in range(betBmin*10, (betBmax*10)+1, 1):
        valuey = y / 10.0
     
        returny=oddy * valuey
        
        if returnx>=valuex+valuey and returny>=valuex+valuey:
            
            if valuex % 10 == 0 and not (str(round(valuex,2)) + ',') in fA:
       
                fA=fA +  str(round(valuex,2)) + ','
                
                fullsA=fullsA + '\nbetA:' + str(round(valuex,2)) + ' returnA:' + str(round(returnx,2)) + ' profitA:' + str(round(returnx-valuex,2)) + " ----" +' betB:' + \
                str(round(valuey,2))+' returnB:' + str(round(returny,2)) + ' profitB:' + str(round(returny-valuey,2)) + \
                    ' ----' + ' finalprofitA:' +  str(round(returnx-valuex-valuey,2)) + ' finalprofitB:' +  str(round(returny-valuex-valuey,2))
           
            if valuex.is_integer() and  valuey.is_integer():
                
                df = df.append({'betA': round(valuex,2), 'returnA': round(returnx,2), 'profitA': round(returnx-valuex,2), 'betB': round(valuey,2), 'returnB': round(returny,2), 'profitB': round(returny-valuey,2),'finalprofitA': round(returnx-valuex-valuey,2),'finalprofitB': round(returny-valuex-valuey,2)}, ignore_index=True)
              
            if returnx-valuex-valuey>mostprofitAx:
                mostprofitAx=returnx-valuex-valuey;mostbetAx=valuex;mostbetBx=valuey;mostprofitBx=returny-valuex-valuey
            if returny-valuex-valuey>mostprofitBy:
                mostprofitBy=returny-valuex-valuey;mostbetAy=valuex;mostbetBy=valuey;mostprofitAy=returnx-valuex-valuey    
        
            betdet=betdet + '\nbetA:' + str(round(valuex,2)) + ' returnA:' + str(round(returnx,2)) + ' profitA:' + str(round(returnx-valuex,2)) + " ----" +' betB:' + \
                 str(round(valuey,2))+' returnB:' + str(round(returny,2)) + ' profitB:' + str(round(returny-valuey,2)) + \
                     ' ----' + ' finalprofitA:' +  str(round(returnx-valuex-valuey,2)) + ' finalprofitB:' +  str(round(returny-valuex-valuey,2))
                  
  df=df.sort_values('finalprofitA', ascending=False)
  
  df1=df.sort_values('finalprofitB')
  
#  print ('betA:' + str(round(valuex,2)),'returnA:' + str(round(returnx,2)),'profitA:' + str(round(returnx-valuex,2)),"----",'betB:' + \
#                str(round(valuey,2)), 'returnB:' + str(round(returny,2)),'profitB:' + str(round(returny-valuey,2)), \
#                    '----', 'finalprofitA:' +  str(round(returnx-valuex-valuey,2)), 'finalprofitB:' +  str(round(returny-valuex-valuey,2)))
  dftxt=''
  for index, row in df.iterrows():
    if row['betA']<10: 
        newbetA= str(row['betA']) + '0' 
    else:
        newbetA= round(row['betA'],1) 
    if row['betB']<10: 
        newbetB= str(row['betB']) + '0' 
    else:
        newbetB= round(row['betB'],1) 
                
    
    dftxt=dftxt + 'betA:    ' + str(newbetA) + '    betB:   ' +  str(newbetB) + '\tfinalprofitA:' + str(round(row['finalprofitA'],2)) + '     finalprofitB:' + str(round(row['finalprofitB'],2)) + "\t ---- "   \
                + ' ** returnA:' + str(round(row['returnA'],2)) + '     profitA:' + str(round(row['profitA'],2)) + \
                    '  ----  ' + '     returnB:' +  str(round(row['returnB'],2)) + '      profitB:' +  str(round(row['profitB'],2)) + '\n'

  dftxt1=''
  for index, row in df1.iterrows():
    if row['betA']<10: 
        newbetA= str(row['betA']) + '0' 
    else:
        newbetA= round(row['betA'],1) 
    if row['betB']<10: 
        newbetB= str(row['betB']) + '0' 
    else:
        newbetB= round(row['betB'],1) 
                
    
    dftxt1=dftxt1 + 'betA:    ' + str(newbetA) + '    betB:   ' +  str(newbetB) + '\tfinalprofitA:' + str(round(row['finalprofitA'],2)) + '     finalprofitB:' + str(round(row['finalprofitB'],2)) + "\t ---- "   \
                + ' ** returnA:' + str(round(row['returnA'],2)) + '     profitA:' + str(round(row['profitA'],2)) + \
                    '  ----  ' + '     returnB:' +  str(round(row['returnB'],2)) + '      profitB:' +  str(round(row['profitB'],2)) + '\n'

  
  topbet='\nmostbetA: *** ' + str(round(mostbetAx,2)) + ' *** finalprofitA:' + str(round(mostprofitAx,2)) + ' lessbetB: *** ' + str(round(mostbetBx,2)) + ' *** finalprofitB:' + str(round(mostprofitBx,2)) + \
                    ' ( ' + 'mostbetB:' +  str(round(mostbetBy,2)) + ' finalprofitB:' +  str(round(mostprofitBy,2)) + ' lessbetA:' + str(round(mostbetAy,2)) + ' finalprofitA:' + str(round(mostprofitAy,2)) + ' )'

  outtxt= dftxt + '\n'  + dftxt1 + '\n' + topbet +  '\n' + fullsA  + '\n'  + '\n' +  '\n' + betdet
  #st.write(outtxt)
  dtxt=f'''<textarea id="textareabox" name="textareabox1" style="background-color:#f5fab1; " spellcheck="false" rows="400" cols="220">{outtxt}</textarea>'''
  components.html(dtxt, height=6000) ;   st.markdown('---') 
  
#  print('\n' + topbet + '\n' + fullsA  + '\n'  + '\n' + dftxt + '\n' + betdet)

#  f = open("./data/bets.txt", "w")
#  f.write('\n' + topbet + '\n' + fullsA  + '\n'  + '\n' + dftxt + '\n' + betdet)



def betcalc3(oddx,betAmin,betAmax,oddy,betBmin,betBmax,oddz,betCmin,betCmax):
 
 with st.spinner('**Please Wssssait for Results...**'):  
     
  mostprofitAx=mostprofitBx=mostprofitAy=mostprofitBy= mostprofitCx=mostprofitCy=0
  mostbetAx=mostbetBx=mostbetAy=mostbetBy= mostbetCx=mostbetCy=bestchoice=0
  topbet=betdet=fulls=fullsA=fullsB=fullsC=fA=fB=fC=''
       
  df = pd.DataFrame(columns=['betA', 'returnA', 'profitA', 'betB', 'returnB', 'profitB','betC', 'returnC', 'profitC','finalprofitA','finalprofitB','finalprofitC'])
 
  for x in range(betAmin*10, (betAmax*10)+1, 1):
    valuex = x / 10.0
   
    returnx=oddx * valuex
    
    for y in range(betBmin*10, (betBmax*10)+1, 1):
      valuey = y / 10.0
     
      returny=oddy * valuey
      
      for z in range(betCmin*10, (betCmax*10)+1, 1):
        valuez = z / 10.0
     
        returnz=oddz * valuez
        
        if returnx>=valuex+valuey+valuez and returny>=valuex+valuey+valuez and returnz>=valuex+valuey+valuez:
           
         
            if valuex.is_integer() and  valuey.is_integer() and  valuez.is_integer():
                
                df = df.append({'betA': round(valuex,2), 'returnA': round(returnx,2), 'profitA': round(returnx-valuex,2), 'betB': round(valuey,2), 'returnB': round(returny,2), 'profitB': round(returny-valuey,2), 'betC': round(valuez,2), 'returnC': round(returnz,2), 'profitC': round(returnz-valuez,2),'finalprofitA': round(returnx-valuex-valuey-valuez,2),'finalprofitB': round(returny-valuex-valuey-valuez,2),'finalprofitC': round(returnz-valuex-valuey-valuez,2)}, ignore_index=True)
                  
 
  df=df.sort_values('finalprofitA', ascending=False)
 
  dftxt=''
  for index, row in df.iterrows():
    if row['betA']<10: 
        newbetA= str(row['betA']) + '0' 
    else:
        newbetA= round(row['betA'],1) 
    if row['betB']<10: 
        newbetB= str(row['betB']) + '0' 
    else:
        newbetB= round(row['betB'],1) 
    if row['betC']<10: 
        newbetC= str(row['betC']) + '0' 
    else:
        newbetC= round(row['betC'],1) 
                    
    
    dftxt=dftxt + 'betA:** \t' + str(newbetA) + '\t** \tbetB:** \t' +  str(newbetB) + '\t** \tbetC:** \t' +  str(newbetC) + ' \t** profitA:' + str(round(row['profitA'],2)) + " ---- "   \
                 + ' profitB:' + str(round(row['profitB'],2)) + " ---- "   \
                   + ' profitC:' + str(round(row['profitC'],2)) + \
                     '  ----  ' + ' finalprofitA:' +  str(round(row['finalprofitA'],2)) + '      finalprofitB:' +  str(round(row['finalprofitB'],2)) + '      finalprofitC:' +  str(round(row['finalprofitC'],2)) + '\n'

  dtxt=f'''<textarea id="textareabox" name="textareabox1" style="background-color:#f5fab1; " spellcheck="false" rows="400" cols="220">{dftxt}</textarea>'''
  components.html(dtxt, height=6000) ;   st.markdown('---') 
  
#  print('\n' + dftxt + '\n')

 # f = open("./data/bets.txt", "w")
 # f.write( '\n' + dftxt + '\n')


 
streamlit_init_conf()



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
        
       
   
