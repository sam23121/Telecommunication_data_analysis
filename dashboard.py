import streamlit as st
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
import sys
import os
sys.path.append(os.path.abspath(os.path.join('../')))

st.set_page_config(page_title="Telecom Data Analysis", layout="wide")



def loadData():
    print("loading started ")
    dataframe = pd.read_csv(r"C:\Users\sam\Desktop\Telecommunication_data_analysis\data\cleaned_data.csv")
    dataframe2 = pd.read_csv(r"C:\Users\sam\Desktop\Telecommunication_data_analysis\data\all_scores.csv")
    dataframe3 = pd.read_csv(r"C:\Users\sam\Desktop\Telecommunication_data_analysis\data\Experience_data.csv")
    print("loading completed")
    return dataframe, dataframe2, dataframe3

dataframe, dataframe2, dataframe3 =  loadData()
def selectUseroverview():
    userview1 = "Dataframe"
    st.markdown(f"## {userview1}")
    st.write(dataframe.sample(100))
    userview2 = "Top Handset Type"
    st.markdown(f"## {userview2}")
    topHandSet = pd.DataFrame(dataframe['Handset Type'].value_counts().head(10))
    topHandName = topHandSet.index

    fig = px.bar( topHandSet,x=topHandName,  y='Handset Type')
    st.plotly_chart(fig)
    userview3 = "Top Handset Manufacturer"
    st.markdown(f"## {userview3}")
    topManufacture =  pd.DataFrame(dataframe['Handset Manufacturer'].value_counts().head(3))
    manu = topManufacture.index

    fig = px.bar( topManufacture,x=manu,  y='Handset Manufacturer')
    st.plotly_chart(fig)





    return 
  

def UserEngagement():
    engage = "User Engagement analysis"

    re_dataframe=dataframe.rename(columns = {'Total DL (Bytes)' : 'totalDL','Total UL (Bytes)' : 'totalUL','Dur. (ms)' : 'dur','MSISDN/Number':'msisdn','Last Location Name':'location','Handset Manufacturer':'manufacturer','Handset Type':'handset'})

    sum_column = re_dataframe["totalUL"] + re_dataframe["totalDL"]


    google = re_dataframe['Google DL (Bytes)']+ re_dataframe['Google UL (Bytes)']
    email = re_dataframe['Email DL (Bytes)']+ re_dataframe['Email UL (Bytes)']
    gaming = re_dataframe['Gaming DL (Bytes)']+ re_dataframe['Gaming UL (Bytes)']
    youtube = re_dataframe['Youtube DL (Bytes)']+ re_dataframe['Youtube UL (Bytes)']
    netflix = re_dataframe['Netflix DL (Bytes)']+ re_dataframe['Netflix UL (Bytes)']
    social = re_dataframe['Social Media DL (Bytes)']+ re_dataframe['Social Media UL (Bytes)']

    re_dataframe['google']=google
    re_dataframe['email']=email
    re_dataframe['gaming']=gaming
    re_dataframe['youtube']=youtube
    re_dataframe['netflix']=netflix
    re_dataframe['social']=social

    DataFrame=re_dataframe[['msisdn', 'google','email','gaming','youtube','netflix','social']]
    DataFrame["totalData"] = sum_column
    DataFrame.groupby('msisdn')['totalData'].sum()


    sumApplicationsDF = DataFrame.groupby('msisdn')[['google','youtube','netflix','social','email','gaming']].sum()
    argestApps=sumApplicationsDF[['google','youtube','netflix','social','email','gaming']].sum().nlargest(10)
    userviewre = "relationship between each application the total DL+UL data"
    st.markdown(f"## {userviewre}")
    
    fig = px.bar(argestApps,x=argestApps.index , y=argestApps.values)
    st.plotly_chart(fig)

    corr_df = DataFrame[['email','gaming','youtube','social','netflix']].corr(method ='pearson').corr()
    
    print(corr_df)
    userviewcor = "Correlation Analysis"
    st.markdown(f"## {userviewcor}")
    fig = px.imshow(corr_df)
    st.plotly_chart(fig)
    return 
def ExperienceAnalytics():
    exper = "Experience Analytics"
    userviewre = "top ten device with the highest throughput"
    st.markdown(f"## {userviewre}")   
    avg_tp = dataframe3.groupby('Handset Type').agg({'AVG_TP': 'mean'}).sort_values(by=['AVG_TP'], ascending=False).head(10)
    argestApps=avg_tp[['AVG_TP']].sum().nlargest(10)
    fig = px.bar(argestApps,x=argestApps.index , y=argestApps.values)
    st.plotly_chart(fig)
    return 

def SatisfactionAnalysis():
    sat = "Satisfaction Analysis"
    userviewre = "most satisfied customers"
    st.markdown(f"## {userviewre}")
    dataframe2['Handset Type'] = dataframe['Handset Type']
    topcust = dataframe2.groupby('Handset Type').agg({'experience_score': 'max'}).sort_values(by=['experience_score'], ascending = False).head(10)
    
    fig = px.bar(topcust,x=topcust.index , y=topcust.values)
    st.plotly_chart(fig)
    return 


st.sidebar.title("Telecom-Data-Analysis")
option = st.sidebar.selectbox('select result',('User Overview',
'User Engagement analysis',' Experience Analytics','Satisfaction Analysis'))
if option =='User Overview':
    selectUseroverview()
elif option == 'User Engagement analysis':
    UserEngagement()
elif option == 'Experience Analytics':
    ExperienceAnalytics()
elif option == 'Satisfaction Analysis':
    SatisfactionAnalysis()


