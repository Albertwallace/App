from turtle import color
from matplotlib.pyplot import yticks
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px
from pyparsing import col  # pip install plotly-express
import streamlit as st  # pip install streamlit
import plotly.graph_objects as go

st.set_page_config(page_title="SWP", page_icon=":bar_chart:", layout="wide")
if 'df' not in st.session_state:
    
    df = pd.DataFrame({"Role":["Dave"],"Man Hours":["Tuesdays"]},columns=["Role","Man Hours"])
    st.session_state['df'] = df
with st.form("my_form"):
    st.write("Inside the form")
    add_role = st.selectbox(
    "Role Type:",
    options=["Dave","Greg","Samantha","Jane","Harold"],
    key = "edit_asset"
    )
    man_hours = st.number_input("Man Hours" ,min_value= 0, value = 0,max_value=1000)
    
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Add role", add_role, "Hours", man_hours)
        this_role = pd.DataFrame({"Role":[add_role],"Man Hours":[str(man_hours)]},columns=["Role","Man Hours"])
        st.session_state.df=pd.concat([st.session_state.df,this_role],axis=0)
st.dataframe(st.session_state.df)

@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

csv = convert_df(st.session_state.df)

st.download_button("Download this as a CSV for you to send to George",csv,"Downloaded SWP.csv",mime='text/csv')