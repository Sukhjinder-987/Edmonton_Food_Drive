import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# Load the dataset with a specified encoding
data = pd.read_csv('Cleaned_food_drive_data.csv', encoding='latin1')

# Page 1: Dashboard
def dashboard():
    st.image('Logo.PNG', use_column_width=True)

    st.subheader("💡 Abstract:")

    inspiration = '''
    The Edmonton Food Drive Project....Talk about the Project here and lessons learned
    '''

    st.write(inspiration)

    st.subheader("👨🏻‍💻 What our Project Does?")

    what_it_does = '''
    Your project description goes here.
    '''

    st.write(what_it_does)


# Page 2: Exploratory Data Analysis (EDA)
def exploratory_data_analysis():
    st.title("Exploratory Data Analysis")
    # Rename columns for clarity
    data_cleaned = data.rename(columns={
        'Drop Off Location for year 2024': 'Location',
        'Stake for year 2024': 'Stake',
        '# of Adult Volunteers for year 2024': '# of Adult Volunteers',
        '# of Youth Volunteers for year 2024': '# of Youth Volunteers',
        'Donation Bags Collected for the year 2024': 'Donation Bags Collected',
        'COMBINED STAKES': 'Ward',
        'Time to Complete (min) for year 2024': 'Time to Complete (min)',
        'Completed More Than One Route for year 2024': 'Completed More Than One Route',
        'How many routes did you complete? for year 2024': 'Routes Completed',
        'Doors in Route for the year 2024': 'Doors in Route',
        'Comment Sentiments for year 2024': 'Comment Sentiments',
        'Comments or Feedback for year 2024': 'Comments or Feedback'
    })

    # Visualize the distribution of numerical features using Plotly
    fig = px.histogram(data_cleaned, x='# of Adult Volunteers', nbins=20, labels={'# of Adult Volunteers': 'Adult Volunteers'})
    st.plotly_chart(fig)

    fig = px.histogram(data_cleaned, x='# of Youth Volunteers', nbins=20, labels={'# of Youth Volunteers': 'Youth Volunteers'})
    st.plotly_chart(fig)

    fig = px.histogram(data_cleaned, x='Donation Bags Collected', nbins=20, labels={'Donation Bags Collected': 'Donation Bags Collected'})
    st.plotly_chart(fig)

    fig = px.histogram(data_cleaned, x='Time to Complete (min)', nbins=20, labels={'Time to Complete (min)': 'Time to Complete'})
    st.plotly_chart(fig)

    fig = px.histogram(data_cleaned, x='Comment Sentiments', nbins=20, labels={'Comment Sentiments': 'Comment Sentiments'})
    st.plotly_chart(fig)

# Page 3: Machine Learning Modeling
def machine_learning_modeling():
    st.title("Machine Learning Modeling")
    st.write("Enter the details to predict donation bags:")

    # Input fields for user to enter data
    completed_routes = st.slider("Completed More Than One Route", 0, 1, 0)
    routes_completed = st.slider("Routes Completed", 1, 10, 5)
    time_spent = st.slider("Time Spent (minutes)", 10, 300, 60)
    adult_volunteers = st.slider("Number of Adult Volunteers", 1, 50, 10)
    doors_in_route = st.slider("Number of Doors in Route", 10, 500, 100)
    youth_volunteers = st.slider("Number of Youth Volunteers", 1, 50, 10)
    comment_sentiments = st.slider("Comment Sentiments", 0, 2, 1)

    # Predict button
    if st.button("Predict"):
        # Load the trained model
        model = joblib.load('random_forest_classifier_model.pkl')

        # Prepare input data for prediction
        input_data = [[completed_routes, routes_completed, time_spent, adult_volunteers, doors_in_route, youth_volunteers, comment_sentiments]]

        # Make prediction
        prediction = model.predict(input_data)

        # Display the prediction
        st.success(f"Predicted Comment Sentiments: {prediction[0]}")

        # You can add additional information or actions based on the prediction if needed
# Page 4: Neighbourhood Mapping
# Read geospatial data
#geodata = pd.read_csv("Location_data_updated.csv")

#def neighbourhood_mapping():
#    st.title("Neighbourhood Mapping")

    # Get user input for neighborhood
#    user_neighbourhood = st.text_input("Enter the neighborhood:")

    # Check if user provided input
#    if user_neighbourhood:
        # Filter the dataset based on the user input
#        filtered_data = geodata[geodata['Neighbourhood'] == user_neighbourhood]

        # Check if the filtered data is empty, if so, return a message indicating no data found
#        if filtered_data.empty:
#            st.write("No data found for the specified neighborhood.")
#        else:
            # Create the map using the filtered data
#            fig = px.scatter_mapbox(filtered_data,
#                                    lat='Latitude',
#                                    lon='Longitude',
#                                    hover_name='Neighbourhood',
#                                    zoom=12)

            # Update map layout to use OpenStreetMap style
#            fig.update_layout(mapbox_style='open-street-map')

            # Show the map
#            st.plotly_chart(fig)
#    else:
#        st.write("Please enter a neighborhood to generate the map.")






# Page 5: Data Collection
def data_collection():
    st.title("Data Collection")
    st.write("Please fill out the Google form to contribute to our Food Drive!")
    google_form_url = "https://forms.gle/Sif2hH3zV5fG2Q7P8"#YOUR_GOOGLE_FORM_URL_HERE
    st.markdown(f"[Fill out the form]({google_form_url})")

# Main App Logic
def main():
    st.sidebar.title("Food Drive App")
    app_page = st.sidebar.radio("Select a Page", ["Dashboard", "EDA", "ML Modeling", "Data Collection"])

    if app_page == "Dashboard":
        dashboard()
    elif app_page == "EDA":
        exploratory_data_analysis()
    elif app_page == "ML Modeling":
        machine_learning_modeling()
    #elif app_page == "Neighbourhood Mapping":
     #   neighbourhood_mapping()
    elif app_page == "Data Collection":
        data_collection()

if __name__ == "__main__":
    main()
