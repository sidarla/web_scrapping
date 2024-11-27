# web_scrapping

Problem Statement:

The "Redbus Data Scraping and Filtering with Streamlit Application" aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.

Business Use Cases:

The solution can be applied to various business scenarios including:

Travel Aggregators: Providing real-time bus schedules and seat availability for customers.

Market Analysis: Analyzing travel patterns and preferences for market research.

Customer Service: Enhancing user experience by offering customized travel options based on data insights.

Competitor Analysis: Comparing pricing and service levels with competitors.

Approach:

Data Scraping:

Use Selenium to automate the extraction of Redbus data including routes, schedules, prices, and seat availability.

Data Storage:

Store the scraped data in a SQL database.

Streamlit Application:

Develop a Streamlit application to display and filter the scraped data.
Implement various filters such as bustype, route, price range, star rating, availability.

Data Analysis/Filtering using Streamlit:

Use SQL queries to retrieve and filter data based on user inputs.
Use Streamlit to allow users to interact with and filter the data through the application.

Results:

You should aim to:

Successfully scrape a minimum of 10 Government State Bus Transport data from Redbus website using Selenium. Also include the private bus information for the selected routes.
Store the data in a structured SQL database.
Develop an interactive Streamlit application for data filtering.
Ensure the application is user-friendly and efficient.

Technical Tags:

Web Scraping
Selenium
Streamlit
SQL
Data Analysis
Python
Interactive Application



Data Set:

Source: Data will be scraped from the Redbus website.

Link- https://www.redbus.in/

Format: The scraped data will be stored in a SQL database.

Required Fields: Bus routes Link,Bus route Name, Bus name, Bus Type(Sleeper/Seater),  Departing Time, Duration, Reaching_Time, Star-rating, Price, Seat_availability.

Data Set Requirements & Explanation:

The scraped dataset for this project should contain detailed information about bus services available on Redbus, covering various aspects critical to travelers and service providers. Here is a breakdown of the fields required:

Bus Routes Name: 
This field captures the start and end locations of each bus journey, providing crucial information about the routes serviced.

Bus Routes Link: Link for all the route details.

Bus Name: The name of the bus or the service provider, which helps in identifying the specific operator.

Bus Type (Sleeper/Seater/AC/Non-AC): This field specifies whether the bus is a sleeper or seater type, indicating the seating arrangements and comfort level offered.

Departing Time: The scheduled departure time of the bus, essential for planning travel schedules.

Duration: The total duration of the journey from the departure point to the destination, helping passengers estimate travel time.

Reaching Time: The expected arrival time at the destination, allowing for better planning of onward travel or activities.

Star Rating: A rating provided by passengers, indicating the quality of service based on factors such as comfort, punctuality, and staff behavior.

Price: The cost of the ticket for the journey, which can vary based on factors like bus type and demand.

Seat Availability: The number of seats available at the time of data scraping, giving real-time insight into the occupancy levels.

