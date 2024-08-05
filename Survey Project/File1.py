import pandas as pd
import streamlit as st
import plotly.express as px

# Function to load data
def load_data():
    file_read = pd.read_csv('D:/INTERNSHIP/StreamLit/Starbucks satisfactory survey.csv')
    return file_read

# Load data
data = load_data()

# Sidebar for filter options
st.sidebar.header('Filter Designation')
selected_status = st.sidebar.multiselect(
    'Select Designation',
    options=data['Designation'].unique(),
    default=None
)

# Filter data based on selection, or show all data if no selection
if selected_status:
    filtered_data = data[data['Designation'].isin(selected_status)]
else:
    filtered_data = data


# Display the filtered dataset
st.header('Filtered Survey Data')
st.write(filtered_data)

selected_genders = st.sidebar.multiselect(
    'Select Gender',
    options=data['Gender'].unique(),
    default=data['Gender'].unique()  # Default to all genders
)
if selected_genders:
    filtered_data = filtered_data[filtered_data['Gender'].isin(selected_genders)]

# Create a pie chart for the filtered data using Plotly
st.header('Status Distribution Pie Chart')
count_data = filtered_data['Designation'].value_counts().reset_index()
count_data.columns = ['Status', 'Count']

# Plotly pie chart
fig = px.pie(count_data, values='Count', names='Status', title='Status Distribution')
# Display the pie chart
st.plotly_chart(fig)

# Calculate average values for each relevant column
avg_quality = filtered_data['Quality Rate'].mean()
avg_price_range = filtered_data['Price Range Reviews'].mean()
avg_marketing = filtered_data['Marketing Reviews'].mean()
avg_interior = filtered_data['Interior and ambious'].mean()
avg_wifi = filtered_data['Wifi Service'].mean()

# Create a DataFrame for the average values
avg_data = pd.DataFrame({
    'Category': ['Quality Rate', 'Price Range Reviews', 'Marketing Reviews', 'Interior and ambious', 'Wifi Service'],
    'Average': [avg_quality, avg_price_range, avg_marketing, avg_interior, avg_wifi]
})

# Create a bar chart for the average values
st.header('Average Ratings Bar Chart')
fig_avg = px.bar(avg_data, 
                 x='Category', 
                 y='Average', 
                 title='Average Ratings of Different Categories', 
                 labels={'Average': 'Average Rating'}, 
                 color='Category',  # Color bars based on the category
                 color_discrete_sequence=px.colors.qualitative.Plotly)

# Display the bar chart
st.plotly_chart(fig_avg)
Count_gender = filtered_data['Gender'].value_counts().reset_index()
Count_gender.columns = ['Gender', 'Count']

# Create a pie chart for gender distribution
fig_gender = px.pie(Count_gender, values='Count', names='Gender', title='Gender Distribution')
# Display the pie chart
st.plotly_chart(fig_gender)

