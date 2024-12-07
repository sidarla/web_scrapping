import streamlit as st
import pandas as pd
from datetime import time


# Custom CSS to change font size of the title
st.markdown(
    """
    <style>
    .big-font {
        font-size:50px !important;
        font-weight: bold;
        color: #fff;  
        font-family:'bree serif';
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Using custom class in markdown to change title font size
st.sidebar.markdown('<p class="big-font">Welcome to Red Bus</p>', unsafe_allow_html=True)



st.markdown(
    """
    <style>
    .big-font {
        font-size:25px !important;
        font-weight: bolder;
        color: #fff; 
        font-family:'Monoton';
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Using custom class in markdown to change title font size


st.sidebar.markdown('<p class="big-font">Home</p>', unsafe_allow_html=True)
Select_state=st.sidebar.selectbox("# Select the State",["Telangana","Andhra Pradesh","Assam","Chandiaghar","Punjab",""],index=5)
if st.sidebar.button("Submit State"):
    st.write(f"You selected the Bus is: {Select_state}")
    

st.markdown(
    """
    <style>
    /* Change background color of the sidebar */
    [data-testid="stSidebar"] {
        background-color:#e3093c;
        color:#fff;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)


# Main Page


st.markdown(
    """
    <style>
    .custom-title {
        color: #e3093c;  /* Red color */
        font-size: 40px;
        font-family: 'playfair display';
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(f'<h1 class="custom-title">{Select_state} Bus Booking System</h1>', unsafe_allow_html=True)


 
route=st.selectbox("Select the Route",['Khammam to Hyderabad','Hyderabad to Vijayawada','Hyderabad to Vijayawada','Vijayawada to Hyderabad','Kakinada to Visakhapatnam','Bangalore to Tirupati','Tirupati to Bangalore','Tezpur to Guwahati','Guwahati to Tezpur','Delhi to Chandigarh'])
#unique_routes = df['route_name'].unique()

#route = st.selectbox("Select the Route", unique_routes)





# Select Seat Type
seat_type = st.selectbox("Select the Seat Type", ["Sleeper", "Seater"])

# Select AC Type
bus_type1 = st.selectbox("Select the AC Type", ["A/C", "NON A/C"])

# Select Ratings
rating_filter = st.slider("Select Ratings",min_value=1,max_value=5)



# Starting Time Filter
time_filter = st.time_input("select Arrival time:",time(0, 0))



# Bus Fare Range
#fare_range = st.number_input("Enter the Bus Fare Range",min_value=100,max_value=1000,step=100)
min_value, max_value = st.slider(
    "Select a Price range", 
    min_value=200, 
    max_value=2000, 
    value=(200, 400),  # default range
    step=100
)





# Inject custom CSS for button styling
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #e0073a; /* Green background */
        color: white;             /* White text */
        padding: 10px 24px;       /* Add padding */
        text-align: center;       /* Center the text */
        text-decoration: none;    /* Remove underline */
        display: inline-block;    /* Make it inline */
        font-size: 16px;          /* Font size */
        margin: 4px 2px;          /* Add some margin */
        cursor: pointer;          /* Cursor on hover */
        border-radius: 12px;
        border-width:2px;
        border-color:#fff;      /* Rounded corners */
    }

    div.stButton > button:hover {
        background-color: #fff;
        color:#000; /* Darker shade of green on hover */
    }
    </style>
    """, unsafe_allow_html=True)

# Create the button
if st.button('Click Me'):
    if Select_state=="Telangana":
        data =pd.read_csv(r"C:/Users/Dell/OneDrive/Desktop/scraping/telanganabuses2.csv")
        
    elif Select_state=="Andhra Pradesh":
        data =pd.read_csv(r"C:/Users/Dell/OneDrive/Desktop/scraping/andhrabuses4.csv")
    elif Select_state=="Assam":
        data =pd.read_csv(r"C:/Users/Dell/OneDrive/Desktop/scraping/assam_buses2.csv")
    elif Select_state=="Chandiaghar":
        data =pd.read_csv(r"C:/Users/Dell/OneDrive/Desktop/scraping/chandiarhbuses2.csv")
      


    df = pd.DataFrame(data) 
    filtered_df = df[df['route_name'] == route]
    filtered_df = filtered_df[filtered_df['bustype'] == bus_type1]

    filtered_df=filtered_df[filtered_df['star_rating']<=rating_filter]

    df['hour'] = filtered_df['duparting_time'].str[:2].astype(int)  # Extract hour from the time string
    filtered_df = filtered_df[df['hour'] >= time_filter.hour]
        
    filtered_df = filtered_df[(filtered_df['Price'] >= min_value) & (filtered_df['Price'] <= max_value)]
    st.dataframe(filtered_df)
    
