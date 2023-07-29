from selenium import webdriver;from selenium.webdriver.common.keys import Keys;import time
from selenium.webdriver.common.proxy import Proxy, ProxyType;from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait;from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from datetime import datetime
import pandas as pd
import webbrowser;import base64;import hashlib
import requests;import time; import os;import json

fitnearbets=bets5_25=bets10_5=bet10=bet25_1=bet1_0=curdbet=curd1bet=curd2bet= curd3bet=curd4bet=curd5bet=curd6bet=curd7bet=''



def readpage_1_0():

 try:

    global fitnearbets; global bet5_25; global bet10_5; global bet10; global bet25_1
    element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(., '1 - 0.001%')]")))

    element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, '1 - 0.001%')))
    print(element.get_attribute("outerHTML"))
    element.click()
   
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Κουπόνια')))
    time.sleep(4)

    content = driver.page_source

    bets=leagname=gametype=profit=''
    for x in content.split('div'):
       
        if 'gameBlock_dateTime' in x:
            bets=bets + '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n' + 'BetType: ' + leagname + 'Date: ' + str(x).split('"><')[1].replace('span>','').replace('span>','').replace('</<',' - ') + '\n' + profit + '\n'
       
        if 'ScopeID' in x:
            bets=bets +  'Teams: ' + str(x).split('ScopeID')[-1].replace('/a>','').strip('>') + '\n' + gametype + '\n'
       
        if 'gameBlock_type' in x:
            gametype='Choices: ' + str(x).split('">')[1] #+ '\n'
        
        if 'img alt' in x and not '/i>' in x:
            bets=bets + 'BetSite: ' +str(x).split('img alt')[1].split(' ')[0] + '    '
       
        if 'img alt' in x and  '/i>' in x:
            leagname=   str(x).split('/i>')[1] + '\n'    
            
        if 'betButton_quote' in x:
            bets=bets + 'BetOdd: ' + str(x).split('">')[1] + '\n'
       
        if 'Κέρδος</span>' in x:
            profit=str(x).split('"">')[1]
        
    bets=bets.strip('BetSite: ="Ποδόσφαιρο"')
    bets=bets.split('="Ποδόσφαιρο"')[0].replace('</','').replace(' - /','').replace('<<','').replace('102>','').replace('span','').replace('"','').replace('--  --','').replace('Κέρδος>','Profit:').replace('!','').replace('103>','').replace('101>','').replace('><','').replace('a><','').replace('301','').replace('h2','').replace('=','').replace('<-- -->','').replace('<br>',' ')
    bets=bets.replace('<-- ---- -->','')
    
    curd=str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0] + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd1=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 1) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd2=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 2) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd3=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 3) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    
    if len(curd1)==4:
        curd1='0' + curd1 
    if len(curd2)==4:
        curd2='0' + curd2     
    if len(curd3)==4:
        curd3='0' + curd3    
               
   
    nearbets=''
    for y in bets.split('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'):
      for z in y.split('\n'):  
        if 'Date' in z and curd in y or curd1 in y or curd2 in y or curd3 in y:
            nearbets=nearbets + y + '\n---------------------------------------------------\n'
            break
   
    fitnearbets=fitnearbets.strip('BetSite: ') +'---------------------Bets < 1% -----------------------------\n\n'
    for k in nearbets.split('\n'):
        if 'Teams' in k and '>' in k :
            fitnearbets=fitnearbets + 'Teams: ' + k.split('>')[-1] + '\n'
        else:
            fitnearbets=fitnearbets + k + '\n'    
    
    bet1_0=bets
    
    # f = open("./data/betsel.txt", "w",encoding="utf-8")
    
    # f.write(datetime.now().strftime('%d-%m-%Y %H:%M:%S')  + '\n\n' + fitnearbets + '\n\n\n'   \
    #       + '---------------------Bets > 10% -----------------------------\n\n' + bet10 \
    #         + '\n\n---------------------Bets 10 - 5%------------------------------\n\n' + bet10_5  \
    #         + '\n\n---------------------Bets 5 - 2.5%------------------------------\n\n' + bet5_25  \
    #          + '\n\n---------------------Bets 2.5 - 1%------------------------------\n\n' + bet25_1 \
    #              + '\n\n---------------------Bets < 1%------------------------------\n\n' + bet1_0 )
    # f.close()


 except Exception as ex: 
     print(ex)
     print(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in 1_0!\n' + str(ex))
     e = open("./data/exceptions.txt", "a",encoding="utf-8")
     e.write(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in 1_0 !\n')
     e.close()



def readpage_25_1():

 try:

    global fitnearbets; global bet5_25; global bet10_5; global bet10; global bet25_1; global curdbet; global curd1bet; global curd2bet; global curd3bet; global curd4bet; global curd5bet; global curd6bet; global curd7bet
    element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(., '2.5% - 1%')]")))

    element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, '2.5% - 1%')))
    print(element.get_attribute("outerHTML"))
    element.click()
 
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Κουπόνια')))
    time.sleep(4)

    content = driver.page_source

    bets=leagname=gametype=profit=''
    for x in content.split('div'):
       
        if 'gameBlock_dateTime' in x:
            bets=bets + '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n' + 'BetType: ' + leagname + 'Date: ' + str(x).split('"><')[1].replace('span>','').replace('span>','').replace('</<',' - ') + '\n' + profit + '\n'
       
        if 'ScopeID' in x:
            bets=bets +  'Teams: ' + str(x).split('ScopeID')[-1].replace('/a>','').strip('>') + '\n' + gametype + '\n'
       
        if 'gameBlock_type' in x:
            gametype='Choices: ' + str(x).split('">')[1] #+ '\n'
        
        if 'img alt' in x and not '/i>' in x:
            bets=bets + 'BetSite: ' +str(x).split('img alt')[1].split(' ')[0] + '    '
       
        if 'img alt' in x and  '/i>' in x:
            leagname=   str(x).split('/i>')[1] + '\n'    
            
        if 'betButton_quote' in x:
            bets=bets + 'BetOdd: ' + str(x).split('">')[1] + '\n'
       
        if 'Κέρδος</span>' in x:
            profit=str(x).split('"">')[1]
        
    bets=bets.strip('BetSite: ="Ποδόσφαιρο"')
    bets=bets.split('="Ποδόσφαιρο"')[0].replace('</','').replace(' - /','').replace('<<','').replace('102>','').replace('span','').replace('"','').replace('--  --','').replace('Κέρδος>','Profit:').replace('!','').replace('103>','').replace('101>','').replace('><','').replace('a><','').replace('301','').replace('h2','').replace('=','').replace('<-- -->','').replace('<br>',' ')
    bets=bets.replace('<-- ---- -->','')
    
    curd=str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0] + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd1=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 1) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd2=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 2) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd3=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 3) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    
    if len(curd1)==4:
        curd1='0' + curd1 
    if len(curd2)==4:
        curd2='0' + curd2     
    if len(curd3)==4:
        curd3='0' + curd3    
               
   
    nearbets=''
    for y in bets.split('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'):
      for z in y.split('\n'):  
        if 'Date' in z and curd in y or curd1 in y or curd2 in y or curd3 in y:

            if curd in y:
                curdbet=curdbet + y + '\n'
            elif curd1 in y:
                curd1bet=curd1bet + y + '\n'
            elif curd2 in y:
                curd2bet=curd2bet + y + '\n'
            elif curd3 in y:
                curd3bet=curd3bet + y + '\n'
           
            nearbets=nearbets + y + '\n---------------------------------------------------\n'
            break
   
    fitnearbets=fitnearbets.strip('BetSite: ') +'---------------------Bets 2.5 - 1% -----------------------------\n\n'
    for k in nearbets.split('\n'):
        if 'Teams' in k and '>' in k :
            fitnearbets=fitnearbets + 'Teams: ' + k.split('>')[-1] + '\n'
        else:
            fitnearbets=fitnearbets + k + '\n'    
    
    bet25_1=bets
    
    f = open("./data/betsel.txt", "w",encoding="utf-8")
    
    f.write(datetime.now().strftime('%d-%m-%Y %H:%M:%S')  + '\n\n' + fitnearbets + '\n\n\n'   \
          + '---------------------Bets > 10% -----------------------------\n\n' + bet10 \
            + '\n\n---------------------Bets 10 - 5%------------------------------\n\n' + bet10_5  \
            + '\n\n---------------------Bets 5 - 2.5%------------------------------\n\n' + bet5_25  \
             + '\n\n---------------------Bets 2.5 - 1%------------------------------\n\n' + bet25_1)# \
               #  + '\n\n---------------------Bets < 1%------------------------------\n\n' + bet1_0 )
    f.close()
   
   
    # open file in read mode
    with open(r"./data/allbets.txt", 'r' ,encoding="utf-8") as fp:
        for count, line in enumerate(fp):
            pass
    fp.close()
    print('Total Lines', count + 1)

    if count>1000000:
         f = open("./data/allbets.txt", "w",encoding="utf-8")
    else:
         f = open("./data/allbets.txt", "a",encoding="utf-8")

    f.write(datetime.now().strftime('%d-%m-%Y %H:%M:%S')  + '\n' + fitnearbets + '\n' + '\n' + bet10  + '\n' + bet10_5  + '\n' + bet5_25 + '\n' + bet25_1)
    f.close()
   

    f = open("./data/betselbydate.txt", "w",encoding="utf-8")
    
    f.write(datetime.now().strftime('%d-%m-%Y %H:%M:%S')  + '\n\n' + curdbet + '\n\n'   \
        + curd1bet + '\n\n'  + curd2bet + '\n\n'  + curd3bet + '\n\n'  + curd4bet + '\n\n'  + curd5bet + '\n\n'  + curd6bet + '\n\n'  + curd7bet + '\n\n') 
    f.close()

 except Exception as ex: 
     print(ex)
     print(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in 25_1!')
     e = open("./data/exceptions.txt", "a",encoding="utf-8")
     e.write(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in 25_1 !\n' + str(ex) + '\n')
     e.close()



def readpage_5_25():
 
 try:

    global fitnearbets; global bet5_25; global bet10_5; global bet10; global bet25_1; global curdbet; global curd1bet; global curd2bet; global curd3bet; global curd4bet; global curd5bet; global curd6bet; global curd7bet
    element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(., '5% - 2.5%')]")))

    element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, '5% - 2.5%')))
    print(element.get_attribute("outerHTML"))
    element.click()
   
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Κουπόνια')))
    time.sleep(4)

    content = driver.page_source

    bets=leagname=gametype=profit=''
    for x in content.split('div'):
       
        if 'gameBlock_dateTime' in x:
            bets=bets + '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n' + 'BetType: ' + leagname + 'Date: ' + str(x).split('"><')[1].replace('span>','').replace('span>','').replace('</<',' - ') + '\n' + profit + '\n'
       
        if 'ScopeID' in x:
            bets=bets +  'Teams: ' + str(x).split('ScopeID')[-1].replace('/a>','').strip('>') + '\n' + gametype + '\n'
       
        if 'gameBlock_type' in x:
            gametype='Choices: ' + str(x).split('">')[1] #+'\n'
        
        if 'img alt' in x and not '/i>' in x:
            bets=bets + 'BetSite: ' +str(x).split('img alt')[1].split(' ')[0] + '    '
       
        if 'img alt' in x and  '/i>' in x:
            leagname=   str(x).split('/i>')[1] + '\n'    
            
        if 'betButton_quote' in x:
            bets=bets + 'BetOdd: ' + str(x).split('">')[1] + '\n'
       
        if 'Κέρδος</span>' in x:
            profit=str(x).split('"">')[1]
        
    bets=bets.strip('BetSite: ="Ποδόσφαιρο"')
    bets=bets.split('="Ποδόσφαιρο"')[0].replace('</','').replace(' - /','').replace('<<','').replace('102>','').replace('span','').replace('"','').replace('--  --','').replace('Κέρδος>','Profit:').replace('!','').replace('103>','').replace('101>','').replace('><','').replace('a><','').replace('301','').replace('h2','').replace('=','').replace('<-- -->','').replace('<br>',' ')
    bets=bets.replace('<-- ---- -->','')
    
    curd=str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0] + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd1=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 1) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd2=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 2) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd3=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 3) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd4=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 4) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd5=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 5) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd6=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 6) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd7=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 7) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 

    if len(curd1)==4:
        curd1='0' + curd1 
    if len(curd2)==4:
        curd2='0' + curd2     
    if len(curd3)==4:
        curd3='0' + curd3    
    if len(curd4)==4:
        curd4='0' + curd4   
    if len(curd5)==4:
        curd5='0' + curd5 
    if len(curd6)==4:
        curd6='0' + curd6   
    if len(curd7)==4:
        curd7='0' + curd7         
    
    nearbets=''
    for y in bets.split('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'):
      for z in y.split('\n'):  
        if 'Date' in z and curd in y or curd1 in y or curd2 in y or curd3 in y or curd4 in y or curd5 in y or curd6 in y or curd7 in y :
          
            if curd in y:
                curdbet=curdbet + y + '\n'
            elif curd1 in y:
                curd1bet=curd1bet + y + '\n'
            elif curd2 in y:
                curd2bet=curd2bet + y + '\n'
            elif curd3 in y:
                curd3bet=curd3bet + y + '\n'
            elif curd4 in y:
                curd4bet=curd4bet + y + '\n'
            elif curd5 in y:
                curd5bet=curd5bet + y + '\n'
            elif curd6 in y:
                curd6bet=curd6bet + y + '\n'
            elif curd7 in y:
                curd7bet=curd7bet + y + '\n'


            nearbets=nearbets + y + '\n---------------------------------------------------\n'
            break
   
    fitnearbets=fitnearbets.strip('BetSite: ') +'---------------------Bets 5 - 2.5% -----------------------------\n\n'
    for k in nearbets.split('\n'):
        if 'Teams' in k and '>' in k :
            fitnearbets=fitnearbets + 'Teams: ' + k.split('>')[-1] + '\n'
        else:
            fitnearbets=fitnearbets + k + '\n'    
    
    bet5_25=bets
  
 except Exception as ex: 
     print(ex)
     print(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in 5_25!')
     e = open("./data/exceptions.txt", "a",encoding="utf-8")
     e.write(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in 5_25 !\n' + str(ex) + '\n')
     e.close()  



def readpage_10_5():

 try:

    global fitnearbets; global bet10_5; global bet5_25; global bet10;global bet25_1; global curdbet; global curd1bet; global curd2bet; global curd3bet; global curd4bet; global curd5bet; global curd6bet; global curd7bet
    element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(., '10% - 5%')]")))
   
    element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, '10% - 5%')))
    print(element.get_attribute("outerHTML"))
    element.click()
   
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Κουπόνια')))
    time.sleep(4)

    content = driver.page_source

    bets=leagname=gametype=profit=''
    for x in content.split('div'):
       
        if 'gameBlock_dateTime' in x:
            bets=bets + '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n' + 'BetType: ' + leagname + 'Date: ' + str(x).split('"><')[1].replace('span>','').replace('span>','').replace('</<',' - ') + '\n' + profit + '\n'
       
        if 'ScopeID' in x:
            bets=bets +  'Teams: ' + str(x).split('ScopeID')[-1].replace('/a>','').strip('>') + '\n' + gametype + '\n'
       
        if 'gameBlock_type' in x:
            gametype='Choices: ' + str(x).split('">')[1]  #'\n'
        
        if 'img alt' in x and not '/i>' in x:
            bets=bets + 'BetSite: ' +str(x).split('img alt')[1].split(' ')[0] + '    '
       
        if 'img alt' in x and  '/i>' in x:
            leagname=   str(x).split('/i>')[1] + '\n'    
            
        if 'betButton_quote' in x:
            bets=bets + 'BetOdd: ' + str(x).split('">')[1] + '\n'
       
        if 'Κέρδος</span>' in x:
            profit=str(x).split('"">')[1]
        
    bets=bets.strip('BetSite: ="Ποδόσφαιρο"')
    bets=bets.split('="Ποδόσφαιρο"')[0].replace('</','').replace(' - /','').replace('<<','').replace('102>','').replace('span','').replace('"','').replace('--  --','').replace('Κέρδος>','Profit:').replace('!','').replace('103>','').replace('101>','').replace('><','').replace('a><','').replace('301','').replace('h2','').replace('=','').replace('<-- -->','').replace('<br>',' ')
    bets=bets.replace('<-- ---- -->','')
    
    nearbets=''
    curd=str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0] + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd1=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 1) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd2=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 2) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd3=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 3) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd4=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 4) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd5=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 5) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd6=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 6) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd7=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 7) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 

    if len(curd1)==4:
        curd1='0' + curd1 
    if len(curd2)==4:
        curd2='0' + curd2     
    if len(curd3)==4:
        curd3='0' + curd3    
    if len(curd4)==4:
        curd4='0' + curd4   
    if len(curd5)==4:
        curd5='0' + curd5 
    if len(curd6)==4:
        curd6='0' + curd6   
    if len(curd7)==4:
        curd7='0' + curd7         
    
    nearbets=''
    for y in bets.split('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'):
      for z in y.split('\n'):  
        if 'Date' in z and curd in y or curd1 in y or curd2 in y or curd3 in y or curd4 in y or curd5 in y or curd6 in y or curd7 in y :
          
            if curd in y:
                curdbet=curdbet + y + '\n'
            elif curd1 in y:
                curd1bet=curd1bet + y + '\n'
            elif curd2 in y:
                curd2bet=curd2bet + y + '\n'
            elif curd3 in y:
                curd3bet=curd3bet + y + '\n'
            elif curd4 in y:
                curd4bet=curd4bet + y + '\n'
            elif curd5 in y:
                curd5bet=curd5bet + y + '\n'
            elif curd6 in y:
                curd6bet=curd6bet + y + '\n'
            elif curd7 in y:
                curd7bet=curd7bet + y + '\n'

            nearbets=nearbets + y + '\n---------------------------------------------------\n'
            break
   
    fitnearbets=fitnearbets.strip('BetSite: ') +'---------------------Bets 10 - 5% -----------------------------\n\n'
    for k in nearbets.split('\n'):
        if 'Teams' in k and '>' in k :
            fitnearbets=fitnearbets + 'Teams: ' + k.split('>')[-1] + '\n'
        else:
            fitnearbets=fitnearbets + k + '\n'     

    bet10_5=bets
   
 except Exception as ex: 
     print(ex)
     print(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in 10_5!')
     e = open("./data/exceptions.txt", "a",encoding="utf-8")
     e.write(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in 10_5 !\n')
     e.close()  



def readpage_10():
 
 try:

    global fitnearbets; global bet10_5; global bet5_25; global bet10;global bet25_1; global curdbet; global curd1bet; global curd2bet; global curd3bet; global curd4bet; global curd5bet; global curd6bet; global curd7bet
    element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(., '10+%')]")))

    element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, '10+%')))
    print(element.get_attribute("outerHTML"))
    element.click()
   
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Κουπόνια')))
    time.sleep(4)

    #driver.set_window_position(-10000, 0)
 
    content = driver.page_source

    bets=leagname=gametype=profit=''
    for x in content.split('div'):
       
        if 'gameBlock_dateTime' in x:
            bets=bets + '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n' + 'BetType: ' + leagname + 'Date: ' + str(x).split('"><')[1].replace('span>','').replace('span>','').replace('</<',' - ') + '\n' + profit + '\n'
       
        if 'ScopeID' in x:
            bets=bets +  'Teams: ' + str(x).split('ScopeID')[-1].replace('/a>','').strip('>') + '\n' + gametype + '\n'
       
        if 'gameBlock_type' in x:
            gametype='Choices: ' + str(x).split('">')[1]  #'\n'
        
        if 'img alt' in x and not '/i>' in x:
            bets=bets + 'BetSite: ' +str(x).split('img alt')[1].split(' ')[0] + '    '
       
        if 'img alt' in x and  '/i>' in x:
            leagname=   str(x).split('/i>')[1] + '\n'    
            
        if 'betButton_quote' in x:
            bets=bets + 'BetOdd: ' + str(x).split('">')[1] + '\n'
       
        if 'Κέρδος</span>' in x:
            profit=str(x).split('"">')[1]
        
    bets=bets.strip('BetSite: ="Ποδόσφαιρο"')
    bets=bets.split('="Ποδόσφαιρο"')[0].replace('</','').replace(' - /','').replace('<<','').replace('102>','').replace('span','').replace('"','').replace('--  --','').replace('Κέρδος>','Profit:').replace('!','').replace('103>','').replace('101>','').replace('><','').replace('a><','').replace('301','').replace('h2','').replace('=','').replace('<-- -->','').replace('<br>',' ')
    bets=bets.replace('<-- ---- -->','')
    
    nearbets=fitnearbets=''
    curd=str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0] + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd1=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 1) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd2=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 2) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd3=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 3) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd4=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 4) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd5=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 5) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd6=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 6) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 
    curd7=str(int(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[0]) + 7) + '/' + str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split('-')[1] 

    if len(curd1)==4:
        curd1='0' + curd1 
    if len(curd2)==4:
        curd2='0' + curd2     
    if len(curd3)==4:
        curd3='0' + curd3    
    if len(curd4)==4:
        curd4='0' + curd4   
    if len(curd5)==4:
        curd5='0' + curd5 
    if len(curd6)==4:
        curd6='0' + curd6   
    if len(curd7)==4:
        curd7='0' + curd7         
    
    nearbets=''
    for y in bets.split('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'):
      for z in y.split('\n'):  
        if 'Date' in z and curd in y or curd1 in y or curd2 in y or curd3 in y or curd4 in y or curd5 in y or curd6 in y or curd7 in y :
            if curd in y:
                curdbet=curdbet + y + '\n'
            elif curd1 in y:
                curd1bet=curd1bet + y + '\n'
            elif curd2 in y:
                curd2bet=curd2bet + y + '\n'
            elif curd3 in y:
                curd3bet=curd3bet + y + '\n'
            elif curd4 in y:
                curd4bet=curd4bet + y + '\n'
            elif curd5 in y:
                curd5bet=curd5bet + y + '\n'
            elif curd6 in y:
                curd6bet=curd6bet + y + '\n'
            elif curd7 in y:
                curd7bet=curd7bet + y + '\n'

            nearbets=nearbets + y + '\n---------------------------------------------------\n'
            break

    fitnearbets=fitnearbets.strip('BetSite: ') +'---------------------Bets more than 10% -----------------------------\n\n'
    for k in nearbets.split('\n'):
        if 'Teams' in k and '>' in k :
            fitnearbets=fitnearbets + 'Teams: ' + k.split('>')[-1] + '\n'
        else:
            fitnearbets=fitnearbets + k + '\n'     

    bet10=bets
   
 except Exception as ex: 
     print(ex)
     print(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in >10!\n' + str(ex) +'\n')
     e = open("./data/exceptions.txt", "a",encoding="utf-8")
     e.write(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in >10 !\n')
     e.close()  


 
def betcalc2light(oddx,betAmin,betAmax,oddy,betBmin,betBmax):
 
 try:
     
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
                
                df = pd.concat([df, pd.DataFrame([{'betA': round(valuex,2), 'returnA': round(returnx,2), 'profitA': round(returnx-valuex,2), 'betB': round(valuey,2), 'returnB': round(returny,2), 'profitB': round(returny-valuey,2),'finalprofitA': round(returnx-valuex-valuey,2),'finalprofitB': round(returny-valuex-valuey,2)}])], ignore_index=True)
            
            if returnx-valuex-valuey>mostprofitAx:
                mostprofitAx=returnx-valuex-valuey;mostbetAx=valuex;mostbetBx=valuey;mostprofitBx=returny-valuex-valuey
            if returny-valuex-valuey>mostprofitBy:
                mostprofitBy=returny-valuex-valuey;mostbetAy=valuex;mostbetBy=valuey;mostprofitAy=returnx-valuex-valuey    
        
            betdet=betdet + '\nbetA:' + str(round(valuex,2)) + ' returnA:' + str(round(returnx,2)) + ' profitA:' + str(round(returnx-valuex,2)) + " ----" +' betB:' + \
                 str(round(valuey,2))+' returnB:' + str(round(returny,2)) + ' profitB:' + str(round(returny-valuey,2)) + \
                     ' ----' + ' finalprofitA:' +  str(round(returnx-valuex-valuey,2)) + ' finalprofitB:' +  str(round(returny-valuex-valuey,2))
                  
  df=df.sort_values('finalprofitA', ascending=False)
  
  df1=df.sort_values('finalprofitB')
 
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
                
    
    dftxt=dftxt + 'betA:    ' + str(newbetA) + '    betB:   ' +  str(newbetB) + '\tfinalprofitA:' + str(round(row['finalprofitA'],2)) + '     finalprofitB:' + str(round(row['finalprofitB'],2)) + '\n' # "\t ---- "   \
 
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

  
  return dftxt

 except:
     print(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in betcalc2light !')
     e = open("./data/exceptions.txt", "a",encoding="utf-8")
     e.write(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in betcalc2light !\n')
     e.close()  



def betcalc3light(oddx,betAmin,betAmax,oddy,betBmin,betBmax,oddz,betCmin,betCmax):

 try:
     
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
                
                 df = pd.concat([df, pd.DataFrame([{'betA': round(valuex,2), 'returnA': round(returnx,2), 'profitA': round(returnx-valuex,2), 'betB': round(valuey,2), 'returnB': round(returny,2), 'profitB': round(returny-valuey,2), 'betC': round(valuez,2), 'returnC': round(returnz,2), 'profitC': round(returnz-valuez,2),'finalprofitA': round(returnx-valuex-valuey-valuez,2),'finalprofitB': round(returny-valuex-valuey-valuez,2),'finalprofitC': round(returnz-valuex-valuey-valuez,2)}])], ignore_index=True)  
 
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
                    
    
    dftxt=dftxt + 'betA:** \t' + str(newbetA) + '\t** \tbetB:** \t' +  str(newbetB) + '\t** \tbetC:** \t' +   str(newbetC) + \
                     '  ----  ' + ' finalprofitA:' +  str(round(row['finalprofitA'],2)) + '      finalprofitB:' +  str(round(row['finalprofitB'],2)) + '      finalprofitC:' +  str(round(row['finalprofitC'],2)) + '\n'
  
  return dftxt

 except:
     print(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in betcalc3light !')
     e = open("./data/exceptions.txt", "a",encoding="utf-8")
     e.write(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in betcalc3light !\n')
     e.close()  



def download_from_github(file_path):

 try:

    repo_owner = "sgou1969"
    repo_name = "streamlit-example"
    branch = "master"
  
    url = f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/{branch}/{file_path}"
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print("File downloaded successfully.")
    else:
        print("File download failed.")

 except:
     print(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in download_from_github !')
     e = open("./data/exceptions.txt", "a",encoding="utf-8")
     e.write(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in download_from_github !\n')
     e.close()  



def delete_from_github(file_path):

 try:

    repo_owner = "sgou1969"
    repo_name = "streamlit-example"
    branch = "master"
    token = "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"

    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
   
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        existing_file = response.json()
        current_sha = existing_file["sha"]
        print(f"File '{file_path}' already exists on GitHub. Deleting...")

        delete_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}?sha={current_sha}"
        delete_payload = {
            "message": "Delete file",
            "sha": current_sha
        }
        delete_response = requests.delete(delete_url, headers=headers, json=delete_payload)
        if delete_response.status_code != 200:
            print(f"Failed to delete file '{file_path}'. Error: {delete_response.text}")
        else:
            print("File deleted successfully!")
 
 except:
     print(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in delete_from_github !')
     e = open("./data/exceptions.txt", "a",encoding="utf-8")
     e.write(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in delete_from_github !\n')
     e.close()



def upload_to_github(file_path):

 try:

    githubAPIURL = "https://api.github.com/repos/sgou1969/streamlit-example/contents/" + file_path
    githubToken = "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"

    with open(file_path, "rb") as f:
        encodedData = base64.b64encode(f.read())
        headers = {
            "Authorization": f'''Bearer {githubToken}''',
            "Content-type": "application/vnd.github+json"
        }
        data = {
            "message": "My commit message",
            "content": encodedData.decode("utf-8"),
        }
        r = requests.put(githubAPIURL, headers=headers, json=data)
        if r.status_code == 201:
            print('file uploaded successfully!') 

 except:
     print(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in upload_to_github !')
     e = open("./data/exceptions.txt", "a",encoding="utf-8")
     e.write(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in upload_to_github !\n')
     e.close()



def send_slack_message(payload):
    f = open("./data/wb.txt", "r",  encoding="utf8")
    txtfile=f.read()
    f.close()
    #webhook='https://hooks.slack.com/services/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'
    webhook='https://hooks.slack.com/services/' + str(txtfile).strip('\n').strip('S').replace('@@','')#'https://hooks.slack.com/services/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'
    return requests.post(webhook, json.dumps(payload))



def fileexport():

 try:
             
        f = open("./data/betsel.txt", "r",  encoding="utf8")
        txtfile=f.read().replace('.gr','')
        f.close()
      
        f = open("./data/betselbydate.txt", "r",  encoding="utf8")
        txtfilebydate=f.read().replace('.gr','')
        f.close()

        pr = open("./data/prevdropbetsellit.txt", "r",  encoding="utf8")
        prevfile=pr.read()
        pr.close()
 
        try:
            os.remove("./data/playedbets.txt") 
            os.remove("./data/ignorebets.txt") 
        except:
            flag=1    
        
        download_from_github("data/playedbets.txt")
        download_from_github("data/ignorebets.txt")
        download_from_github("data/wb.txt")

        time.sleep(1)
        f = open("./data/playedbets.txt", "r",  encoding="utf8")
        txtplayed=f.read()
        f.close()
        
        f = open("./data/playedbetsall.txt", "r",  encoding="utf8")
        newalltxt=str(f).replace("<_io.TextIOWrapper name='./data/playedbetsall.txt' mode='r' encoding='utf8'>",'')
        f.close()
        for p in txtplayed.split("\n\n"):
             if p.strip().strip('\n')!='' and str(p).replace(' ','').replace('\n','') not in newalltxt.replace(' ','').replace('\n',''):
                newalltxt=newalltxt + p + '\n\n'
        f = open("./data/playedbetsall.txt", "w",encoding="utf-8")
        f.write(newalltxt)
        f.close()

        f = open("./data/ignorebets.txt", "r",  encoding="utf8")
        txtplayed=txtplayed + f.read().replace('\n\n\n\n','\n\n').replace('\n\n\n','\n\n')
        f.close()

        played=[]
        for b in txtplayed.split("\n\n"):
             played.append(b)
      

        txtout=gre5='';betnew=1;stoix=fon=sport=betss=nov=betsh=bwin=bet365=inter=allsites=nopenaltytxt=''
        nopenalty=['Bwin','SportingBet']
      
      ##############################################################
      
        for x in txtfile.split('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')[0].split('---------------------------------------------------'):
        
         try: 
          
          betnew=1  

          if not 'ScopeCode' in x:

            if 'Stoiximan' in x:
                stoix=stoix + x  + '\n'
            if 'Fonbet' in x:
                fon=fon + x  + '\n'
            if 'SportingBet' in x:
                sport=sport + x  + '\n'      
            if 'Betsson' in x:
                betss=betss + x  + '\n'
            if 'Bwin' in x:
                bwin=bwin + x  + '\n'
            if 'Novibet' in x:
                nov=nov + x  + '\n'
            if 'Bet365' in x:
                bet365=bet365 + x  + '\n'
            if 'wetten' in x:
                inter=inter + x  + '\n'
            if 'BetShop' in x or 'Betshop' in x:
                betsh=betsh + x  + '\n'   

          allsites= '@@@@@@@@@@@@@@ Stoiximan @@@@@@@@@@@@@@\n\n' + stoix + '@@@@@@@@@@@@@@ Fonbet @@@@@@@@@@@@@@\n\n' + fon + '@@@@@@@@@@@@@@ SportingBet @@@@@@@@@@@@@@\n\n' + sport + '@@@@@@@@@@@@@@ Betsson @@@@@@@@@@@@@@\n\n' + betss + '@@@@@@@@@@@@@@ Bwin @@@@@@@@@@@@@@\n\n' + bwin + '@@@@@@@@@@@@@@ Novibet @@@@@@@@@@@@@@\n\n' + nov + '@@@@@@@@@@@@@@ Bet365 @@@@@@@@@@@@@@\n\n' + bet365 + '@@@@@@@@@@@@@@ Interwetten @@@@@@@@@@@@@@\n\n'+ inter + '@@@@@@@@@@@@@@ BetShop @@@@@@@@@@@@@@\n\n' +  betsh

          for p in played:
          
            if not 'Bets > 10%' in x:
             newx=x.replace('BetType: ','').replace('Date: ','').replace('Profit: ','').replace('Teams: ','').replace('Choices: ','').replace('BetSite: ','').replace('BetOdd: ','')
           
             if p.strip()!='' and str(p).replace(' ','').replace('\n','') in newx.replace(' ','').replace('\n',''):
                betnew=0;break
    
          if betnew==1:
           
           site1=site2=site3=odd1=odd2=odd3=proflow=''
          
           
           for y in x.split('\n'):

                if 'Profit' in y:
                   prof=y.split(':')[-1].replace('%','').strip()
                   if float(prof)>5:
                      gre5=gre5 + x.strip() +'\n\n'
                   if float(prof)>=2:
                      proflow='2'
                   if float(prof)<1.5:
                      proflow='1'
                      break
            
                if 'BetSite' in y :
                  
                   if site1=='':
                        site1=y.split('BetOdd')[0].split(':')[-1].strip()
                        odd1=y.split('BetOdd')[-1].split(':')[-1].strip()
                   elif site2=='':
                        site2=y.split('BetOdd')[0].split(':')[-1].strip()
                        odd2=y.split('BetOdd')[-1].split(':')[-1].strip()
                   elif site3=='':
                        site3=y.split('BetOdd')[0].split(':')[-1].strip()
                        odd3=y.split('BetOdd')[-1].split(':')[-1].strip()
        
           wsite1=wsite2=wsite3=wodd1=wodd2=wodd3='' 
            
           if proflow=='' or proflow=='2':

            if site3=='':
                if  float(odd1)> float(odd2):
                    wsite1=site2;wsite2=site1;wodd1=odd2;wodd2=odd1
                else:
                    wsite1=site1;wsite2=site2;wodd1=odd1;wodd2=odd2

                dftxt=betcalc2light(float(wodd1),3,25,float(wodd2),2,15)
            
            else:
                siteall=[site1,site2,site3]
                oddall=[odd1,odd2,odd3];c1=c2=c3=4
            
                if  float(odd1)>= float(odd2) and float(odd1)>= float(odd3):
                    wsite3=site1;wodd3=odd1
                    c3=0
                elif  float(odd2)>= float(odd1) and float(odd2)>= float(odd3):
                    wsite3=site2;wodd3=odd2
                    c3=1
                elif  float(odd3)>= float(odd1) and float(odd3)>= float(odd2):
                    wsite3=site3;wodd3=odd3 
                    c3=2

                if  float(odd1)<= float(odd2) and float(odd1)<= float(odd3):
                    wsite1=site1;wodd1=odd1
                    c1=0
                elif  float(odd2)<= float(odd1) and float(odd2)<= float(odd3):
                    wsite1=site2;wodd1=odd2
                    c1=1
                elif  float(odd3)<= float(odd1) and float(odd3)<= float(odd2):
                    wsite1=site3;wodd1=odd3 
                    c1=2
                
                for i in range(3):
                    if i!=c1 and i!=c3:
                        c2=i

                    
                wsite2=siteall[c2];wodd2=oddall[c2]       

                dftxt=betcalc3light(float(wodd1),3,20,float(wodd2),2,12,float(wodd3),2,10)

            if site3=='': 
                    if wsite1 not in nopenalty and wsite2 not in nopenalty:
                        nopenaltytxt=nopenaltytxt + str(x) +'\n\n' + wsite1 + '(' + wodd1 + ') * ' + wsite2 + '(' + wodd2 + ')' +  '\n-----------------------------------------------------------------------------\n' + str(dftxt) + '\n\n'     
                    
                    txtout=txtout + str(x) +'\n\n' + wsite1 + '(' + wodd1 + ') * ' + wsite2 + '(' + wodd2 + ')' +  '\n-----------------------------------------------------------------------------\n' + str(dftxt) + '\n\n'
            else:
                    if wsite1 not in nopenalty and wsite2 not in nopenalty and wsite3 not in nopenalty:
                        nopenaltytxt=nopenaltytxt + str(x) +'\n\n******      ' + wsite1 + '(' + wodd1 + ')     ******      ' + wsite2 + '(' + wodd2 + ')     ******      ' + wsite3 + '(' + wodd3 + ')     ******  ' + '  ******\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------\n' + str(dftxt) + '\n\n'  
                    
                    txtout=txtout + str(x) +'\n\n******      ' + wsite1 + '(' + wodd1 + ')     ******      ' + wsite2 + '(' + wodd2 + ')     ******      ' + wsite3 + '(' + wodd3 + ')     ******  ' + '  ******\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------\n' + str(dftxt) + '\n\n'  

         except:
             print('exception in odd calculation! ' + str(odd1) + ' ' + str(odd2) + ' ' + str(odd3))
     
        f = open("./data/betsellit.txt", "w",encoding="utf-8")
        f.write(txtout)
        f.close()
        
        f = open("./data/sitesbet.txt", "w",encoding="utf-8")
        f.write(allsites)
        f.close()

        txtout=txtout.replace('-----------------------------', '----------').replace('---------------------','----------').replace('Date: ','').replace('Profit: ','') \
            .replace('Teams: ','').replace('Choices: ','').replace('BetSite: ','').replace('BetOdd: ','').replace('betA:    ','A:').replace(':** ','*').replace(' ** ','*')
        txtout=txtout.replace('betB:   ','B:').replace('betC:   ','C:').replace('finalprofitA:','*pA:').replace('\t',' ').replace('  ----   ',' - ') \
                .replace('finalprofitB:','pB:').replace('finalprofitC:','pC:').replace('     *      ','*').replace(' * ','*').replace('* ','*') \
                .replace('     ',' ').replace('    ',' ').replace('\n\n\n\n','\n\n').replace('\n\n\n','\n\n').replace('Bets more than','>') \
                .replace('Bets 5 - 2.5% --------------------Bets 2.5 - 1%','Bets 5 - 2.5% ---------\n---------Bets 2.5 - 1%').replace(' ** ','*')
        
        nopenaltytxt=nopenaltytxt.replace('-----------------------------', '----------').replace('---------------------','----------').replace('Date: ','').replace('Profit: ','') \
            .replace('Teams: ','').replace('Choices: ','').replace('BetSite: ','').replace('BetOdd: ','').replace('betA:    ','A:').replace(':** ','*').replace(' ** ','*')
        nopenaltytxt=nopenaltytxt.replace('betB:   ','B:').replace('betC:   ','C:').replace('finalprofitA:','*pA:').replace('\t',' ').replace('  ----   ',' - ') \
                .replace('finalprofitB:','pB:').replace('finalprofitC:','pC:').replace('     *      ','*').replace(' * ','*').replace('* ','*') \
                .replace('     ',' ').replace('    ',' ').replace('\n\n\n\n','\n\n').replace('\n\n\n','\n\n').replace('Bets more than','>') \
                .replace('Bets 5 - 2.5% --------------------Bets 2.5 - 1%','Bets 5 - 2.5% ---------\n---------Bets 2.5 - 1%').replace(' ** ','*')
        

        f = open("./data/dropbetsellit.txt", "w",encoding="utf-8")
        f.write(txtout.replace('BetType: ',''))
        f.close()

        f = open("./data/bet_no_penalty.txt", "w",encoding="utf-8")
        f.write(nopenaltytxt)
        f.close()

        diffs=''
        for d in txtout.split('BetType: '):
           if d.split('\n\n---')[0].strip().strip('\n') not in prevfile:
              if 'Bwin' not in d and 'Sporting' not in d:  
                for y in d.split('\n'):
                 if '%' in y and not '----' in y:
                   try:
                     prof=y.split(':')[-1].replace('%','').strip()
                   except:
                     prof='1'  
                   if float(prof)>=2:
                     diffs=diffs + d.split('\n\n---')[0] + '\n\n'
                     break
        
        if diffs!='' and 'A:' in diffs:
          if str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')).split(':')[0] in diffs:  
            dict={"text":  diffs}
          else:
            dict={"text": str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + '\n' + diffs}
          
          send_slack_message(dict)
        

        f = open("./data/prevdropbetsellit.txt", "w",encoding="utf-8")
        f.write(txtout.replace('BetType: ',''))
        f.close()

     ###############################################################

        txtout=''
        for x in txtfilebydate.split('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')[0].split('\n\n'):
        
         try: 
          
          betnew=1  

        
          for p in played:
          
            if not 'Bets > 10%' in x:
             newx=x.replace('BetType: ','').replace('Date: ','').replace('Profit: ','').replace('Teams: ','').replace('Choices: ','').replace('BetSite: ','').replace('BetOdd: ','')
           
             if p.strip()!='' and str(p).replace(' ','').replace('\n','') in newx.replace(' ','').replace('\n',''):
                betnew=0;break
    
          if betnew==1 and len(x)>30:
           
           site1=site2=site3=odd1=odd2=odd3=proflow=''
          
           
           for y in x.split('\n'):

                if 'Profit' in y:
                   prof=y.split(':')[-1].replace('%','').strip()
                   if float(prof)<1.4:
                      proflow='1'
                      break
            
                if 'BetSite' in y :
                  
                   if site1=='':
                        site1=y.split('BetOdd')[0].split(':')[-1].strip()
                        odd1=y.split('BetOdd')[-1].split(':')[-1].strip()
                   elif site2=='':
                        site2=y.split('BetOdd')[0].split(':')[-1].strip()
                        odd2=y.split('BetOdd')[-1].split(':')[-1].strip()
                   elif site3=='':
                        site3=y.split('BetOdd')[0].split(':')[-1].strip()
                        odd3=y.split('BetOdd')[-1].split(':')[-1].strip()
        
           wsite1=wsite2=wsite3=wodd1=wodd2=wodd3='' 
            
           if proflow=='':

            if site3=='':
                if  float(odd1)> float(odd2):
                    wsite1=site2;wsite2=site1;wodd1=odd2;wodd2=odd1
                else:
                    wsite1=site1;wsite2=site2;wodd1=odd1;wodd2=odd2

                dftxt=betcalc2light(float(wodd1),3,25,float(wodd2),2,15)
            
            else:
                siteall=[site1,site2,site3]
                oddall=[odd1,odd2,odd3];c1=c2=c3=4
            
                if  float(odd1)>= float(odd2) and float(odd1)>= float(odd3):
                    wsite3=site1;wodd3=odd1
                    c3=0
                elif  float(odd2)>= float(odd1) and float(odd2)>= float(odd3):
                    wsite3=site2;wodd3=odd2
                    c3=1
                elif  float(odd3)>= float(odd1) and float(odd3)>= float(odd2):
                    wsite3=site3;wodd3=odd3 
                    c3=2

                if  float(odd1)<= float(odd2) and float(odd1)<= float(odd3):
                    wsite1=site1;wodd1=odd1
                    c1=0
                elif  float(odd2)<= float(odd1) and float(odd2)<= float(odd3):
                    wsite1=site2;wodd1=odd2
                    c1=1
                elif  float(odd3)<= float(odd1) and float(odd3)<= float(odd2):
                    wsite1=site3;wodd1=odd3 
                    c1=2
                
                for i in range(3):
                    if i!=c1 and i!=c3:
                        c2=i

                    
                wsite2=siteall[c2];wodd2=oddall[c2]       

                dftxt=betcalc3light(float(wodd1),3,20,float(wodd2),2,12,float(wodd3),2,10)

            if site3=='':    
                    txtout=txtout + str(x) +'\n\n' + wsite1 + '(' + wodd1 + ') * ' + wsite2 + '(' + wodd2 + ')' +  '\n-----------------------------------------------------------------------------\n' + str(dftxt) + '\n\n'
            else:
                    txtout=txtout + str(x) +'\n\n******      ' + wsite1 + '(' + wodd1 + ')     ******      ' + wsite2 + '(' + wodd2 + ')     ******      ' + wsite3 + '(' + wodd3 + ')     ******  ' + '  ******\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------\n' + str(dftxt) + '\n\n'  

         except:
             print('exception in odd calculation! ' + str(odd1) + ' ' + str(odd2) + ' ' + str(odd3))
     

        txtout=txtout.replace('-----------------------------', '----------').replace('---------------------','----------').replace('Date: ','').replace('Profit: ','') \
            .replace('Teams: ','').replace('Choices: ','').replace('BetSite: ','').replace('BetOdd: ','').replace('betA:    ','A:').replace(':** ','*').replace(' ** ','*')
        txtout=txtout.replace('betB:   ','B:').replace('betC:   ','C:').replace('finalprofitA:','*pA:').replace('\t',' ').replace('  ----   ',' - ') \
                .replace('finalprofitB:','pB:').replace('finalprofitC:','pC:').replace('     *      ','*').replace(' * ','*').replace('* ','*') \
                .replace('     ',' ').replace('    ',' ').replace('\n\n\n\n','\n\n').replace('\n\n\n','\n\n').replace('Bets more than','>') \
                .replace('Bets 5 - 2.5% --------------------Bets 2.5 - 1%','Bets 5 - 2.5% ---------\n---------Bets 2.5 - 1%').replace(' ** ','*')
        
       
        f = open("./data/dropbetsellitbydate.txt", "w",encoding="utf-8")
        f.write(txtout.replace('BetType: ',''))
        f.close()

      
     ###############################################################

 except:
     print(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in fileexport !')
     e = open("./data/exceptions.txt", "a",encoding="utf-8")
     e.write(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in fileexport !\n')
     e.close()



#################################################################################### 

# fileexport()   
#dict={"text": str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + '\n\n' }
#send_slack_message(dict)
####################################################################################

driver = webdriver.Chrome()
    
driver.get("https://www.oddssafari.gr/sure-bets")

wait = WebDriverWait(driver, 60)

c=0
            
while True:

 try:

    readpage_10()
    readpage_10_5()
    readpage_5_25()
    readpage_25_1()
    #readpage_1_0()
    
    fileexport()
   
    file_path = "data/dropbetsellit.txt"
    file_path1 = "data/exceptions.txt"
    file_path2 = "data/playedbetsall.txt"
    file_path3 = "data/betsel.txt"
    file_path4 = "data/sitesbet.txt"
    file_path5 = "data/dropbetsellitbydate.txt"
    file_path6 ="./data/bet_no_penalty.txt"
    
    delete_from_github(file_path)
    upload_to_github(file_path)
  
    delete_from_github(file_path1)
    upload_to_github(file_path1)
 
    delete_from_github(file_path2)
    upload_to_github(file_path2)
   
    delete_from_github(file_path3)
    upload_to_github(file_path3)
   
    delete_from_github(file_path4)
    upload_to_github(file_path4)
 
    delete_from_github(file_path5)
    upload_to_github(file_path5)
    
    delete_from_github(file_path6)
    upload_to_github(file_path6)

    curdbet=curd1bet=curd2bet= curd3bet=curd4bet=curd5bet=curd6bet=curd7bet=''
    c=c+1
    
    print("runing times: " + str(c))

 except Exception as ex: 
     print(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in startup !')
     e = open("./data/exceptions.txt", "a",encoding="utf-8")
     e.write(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' error in startup !\n' + str(ex) + '\n')
     e.close()

#driver.quit()
#print("finish!!!!")