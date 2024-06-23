import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Set Streamlit page configuration
st.set_page_config(
    page_title="Amazon Sales Report",
    layout="wide"
)

# Load the dataset
df = pd.read_csv("E:/Slash InternShip/Amazon Sale Report.csv")
df.set_index('index', inplace=True)

# Sidebar for user input
st.sidebar.header("Filters")
top_n_dates = st.sidebar.slider("Number of Top Dates", 10, 50, 30)

# First Visual: Top 30 Dates with Highest Order Counts
st.subheader('Top Dates with Highest Order Counts')
top_dates = df['Date'].value_counts().nlargest(top_n_dates)
top_dates = top_dates.sort_index()
plt.figure(figsize=(14, 4))
sns.barplot(x=top_dates.index, y=top_dates.values, palette='viridis')
plt.xticks(rotation=90)
plt.title(f'Top {top_n_dates} Dates with Highest Order Counts')
plt.xlabel('Date')
plt.ylabel('Order Count')
st.pyplot(plt.gcf())

# Second Visual: Distribution of Order Status
st.subheader('Distribution of Order Status')
status_order = df['Status'].value_counts().index
plt.figure(figsize=(8, 4))
sns.countplot(y='Status', data=df, order=status_order)
plt.title('Distribution of Order Status')
st.pyplot(plt.gcf())

# Third Visual: Distribution of Fulfilment
st.subheader('Distribution of Fulfilment')
fulfilment_counts = df['Fulfilment'].value_counts()
fulfilment_df = fulfilment_counts.reset_index()
fulfilment_df.columns = ['Fulfilment', 'Count']
plt.figure(figsize=(8, 4))
sns.barplot(x='Fulfilment', y='Count', data=fulfilment_df, palette='pastel')
plt.title('Distribution of Fulfilment')
plt.xlabel('Fulfilment')
plt.ylabel('Count')
st.pyplot(plt.gcf())

# Fourth Visual: Distribution of Category
st.subheader('Distribution of Category')
category_order = df['Category'].value_counts().index
plt.figure(figsize=(8, 4))
sns.countplot(y='Category', data=df, order=category_order)
plt.title('Distribution of Category')
st.pyplot(plt.gcf())

# Fifth Visual: Histogram of Shipping States
st.subheader('Histogram of Shipping States')
fig = px.histogram(df, x='ship-state')
st.plotly_chart(fig)

# Sixth Visual: Highest Amount per Month
st.subheader('Highest Amount per Month')
max_amounts = df.groupby('Month')['Amount'].max().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=max_amounts, x='Month', y='Amount', palette='viridis')
plt.title('Highest Amount per Month')
plt.xlabel('Month')
plt.ylabel('Amount')
st.pyplot(plt.gcf())

# Run the Streamlit app using the following command in your terminal:
# streamlit run your_script_name.py 
