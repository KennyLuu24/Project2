from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load data
data = pd.read_csv('superstore_sales.csv')

@app.route('/')
def index():
    # Get unique values for dropdowns
    categories = data['Category'].unique()
    subcategories = data['Sub-Category'].unique()
    regions = data['Region'].unique()
    segments = data['Segment'].unique()
    queries = ['Total Sales and Profit', 'Average Discount by Product', 'Total Sales by Year', 'Profit by Region', 'Products with Negative Profit']  # Example queries
    return render_template('index.html', categories=categories, subcategories=subcategories, regions=regions, segments=segments, queries=queries)

@app.route('/results', methods=['POST'])
def results():
    # Get form data
    category = request.form['category']
    subcategory = request.form['subcategory']
    region = request.form['region']
    segment = request.form['segment']
    query = request.form['query']

    # Filter data
    filtered_data = data[
        (data['Category'] == category) &
        (data['Sub-Category'] == subcategory) &
        (data['Region'] == region) &
        (data['Segment'] == segment)
    ]

    # Perform the query

    if query == 'Total Sales and Profit':
        total_sales = filtered_data['Sales'].sum()
        total_profit = filtered_data['Profit'].sum()
        result = {
            "Total Sales": f"${total_sales:,.2f}",
            "Total Profit": f"${total_profit:,.2f}"
        }

    elif query == 'Average Discount by Product':
        result_df = filtered_data.groupby('Product Name')['Discount'].mean().sort_values(ascending=False).round(2)
        result = result_df.to_dict()

    elif query == 'Total Sales by Year':
        filtered_data['Order Date'] = pd.to_datetime(filtered_data['Order Date'])
        result_df = filtered_data.groupby(filtered_data['Order Date'].dt.year)['Sales'].sum().round(2)
        result = result_df.to_dict()

    elif query == 'Profit by Region':
        result_df = filtered_data.groupby('Region')['Profit'].sum().round(2)
        result = result_df.to_dict()

    elif query == 'Products with Negative Profit':
        result_df = filtered_data[filtered_data['Profit'] < 0][['Product Name', 'Profit']].round(2)
        result = result_df.to_dict(orient='records')
    return render_template('results.html', result=result, query=query)

if __name__ == '__main__':
    app.run(debug=True)
