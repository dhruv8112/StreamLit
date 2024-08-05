import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time

#st write use for the print statement

st.write("Hello world")
st.write("Here is Our Demo application")
st.write(pd.DataFrame({

    'First Name':[ 'John','alogue','bob'],
    'Age':[20,50,18]
}))

DataFrame = np.random.randint(10,50)
st.write(DataFrame)

# newDf=pd.DataFrame(np.random.rand(10,50),
#     columns=('Col %d'% i  for i in range(50)))

# st.newDf(newDf.style.highlight_max(axis=0))


newDf = pd.DataFrame(np.random.rand(10, 50), index=('Row %d' % i for i in range(10)), columns=('Col %d' % i for i in range(50)))

# Use st.dataframe to display the styled dataframe
st.dataframe(newDf.style.highlight_max(axis=0)) 

# Chart to display

chart_data=pd.DataFrame(
    np.random.rand(20,4),
    columns=['a','b','c','d']
    )

st.line_chart(chart_data)

map_data=pd.DataFrame(
    np.random.rand(1000,2)/[50,50]+[37,-122],
    columns=['lat','lon']
)

st.map(map_data)

test_data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 15, 25, 30]
})

# Create a Streamlit slider to filter the DataFrame based on the 'y' values
min_y, max_y = st.slider(
    'Select y value range',
    min_value=int(test_data['y'].min()),
    max_value=int(test_data['y'].max()),
    value=(int(test_data['y'].min()), int(test_data['y'].max()))
)

# Filter the DataFrame based on the selected range
filtered_data = test_data[(test_data['y'] >= min_y) & (test_data['y'] <= max_y)]

# Create the Altair line chart with the filtered data
test_chart = alt.Chart(filtered_data).mark_line().encode(
    x='x:O',
    y='y:Q',
    tooltip=[
        alt.Tooltip('x:O', title='X Value'),
        alt.Tooltip('y:Q', title='Y Value')
    ]
).interactive()

# Display the chart in Streamlit
st.altair_chart(test_chart, use_container_width=True)

# Display the filtered DataFrame
st.write(filtered_data)


# Add a slider to the sidebar
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
add_selectbox = st.sidebar.selectbox(
    'Month Date Filter',
    ('Month', 'Year', 'range')
)

# Add a radio button to the sidebar
chosen = st.sidebar.radio(
    'Sorting hat',
    ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
)

multi=st.sidebar.multiselect(
    'Choose country',
    ('India','america','Australia','United States','united kingdom','France','Germany','Serbia','Sri Lanka')
)

add_time=st.sidebar.time_input('Time')

# Create two columns


left_column, right_column = st.columns(4)
# Use the right column
with right_column:
    st.write(f"You are in {chosen} house!")
    
    
latest_iteration = st.empty()
bar = st.progress(0)

#Complete processing Show
st.warning("IT over")
for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)
st.success('IterationCompleted')
st.error('IterationFailed')
st.write('Goood Byr')

