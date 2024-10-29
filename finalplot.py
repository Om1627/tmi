import pandas as pd
import numpy as np
import plotly.express as px

# Load the Excel file with monthly data for drug sales
excel_file = 'drug_salt_monthly_data.xlsx'
excel_sheets = pd.ExcelFile(excel_file)

# Combine all sheets into a single DataFrame
sales_data = pd.DataFrame()

for sheet_name in excel_sheets.sheet_names:
    df = excel_sheets.parse(sheet_name)
    df['month'] = sheet_name  # Add a 'month' column based on the sheet name
    sales_data = pd.concat([sales_data, df], ignore_index=True)

# Convert the 'month' column to a datetime format for proper sorting on the x-axis
sales_data['month'] = pd.to_datetime(sales_data['month'], format='%Y-%m')

# Plot a scatter plot with plotly express, using 'Qty' as y-axis and 'month' as x-axis
fig = px.scatter(
    sales_data,
    x='month',
    y='Qty',
   
    hover_data={'DrugSalt': True, 'month': False},
    title="Monthly Drug Sales (Quantity vs. Month)",
    labels={'Qty': 'Quantity Sold', 'month': 'Month'},
)

# Update layout for better readability
fig.update_traces(marker=dict(size=8, opacity=0.6))
fig.update_layout(
    xaxis_title="Month",
    yaxis_title="Quantity Sold",
    xaxis=dict(tickformat="%Y-%m", tickangle=45),
    height=600,
)

fig.show()
