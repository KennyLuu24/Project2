# Interactive Web Application for Superstore Data Analysis

## Overview
This project is a Flask-based web application designed to analyze the Superstore sales dataset. The application allows users to filter data by Category, Sub-Category, Region, and Segment and perform specific pre-defined queries. It integrates Flask for the backend, Pandas for data processing, and HTML templates for the frontend interface.

## Features
- Interactive HTML form for user input
- Dynamic dropdowns populated from CSV data
- Data filtering based on user-selected fields
- Five pre-defined data analysis queries:
  - Total Sales and Profit
  - Average Discount by Product
  - Total Sales by Year
  - Profit by Region
  - Products with Negative Profit
- Result display page with neatly formatted tables

## Technologies Used
- Python
- Flask
- Pandas
- HTML (Jinja2 templates)

## File Structure
```
Project2_InClass/
├── app.py                  # Flask application
├── TableauSalesData.csv    # Dataset
├── templates/
│   ├── index.html          # Frontend form
│   └── results.html        # Display page
```

## How to Run
1. Install Flask and Pandas:
   ```
   pip install flask pandas
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## License
This project is for educational purposes only.
