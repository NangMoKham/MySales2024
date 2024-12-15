import pandas as pd
import streamlit as st
import plotly.express as px
st.set_page_config(page_title = "My Sales Dashboard",page_icon=':bar_chart:',layout='wide')
df = pd.read_csv('all_df 2.csv')
st.sidebar.header('Please Filter Here: ')
product = st.sidebar.multiselect(
    "Select Product: ",
    options = df['Product'].unique(),
    default = df['Product'].unique()[:5])
city = st.sidebar.multiselect(
    "Select City: ",
    options = df['City'].unique(),
    default = df['City'].unique()[:5])
month = st.sidebar.multiselect(
    "Select Month: ",
    options = df['Month'].unique(),
    default = df['Month'].unique()[:5])
st.title(':bar_chart: Sales Dashborad for 2019')
st.markdown('##')
tsum = df['Total'].sum()
pno = df['Product'].nunique()
left_col, right_col = st.columns(2)
with left_col:
    st.subheader('Total Sales')
    st.subheader(f'US $ {tsum}')
with right_col:
    st.subheader('Number of Products')
    st.subheader(f' {pno}')
df_select = df.query('City == @city and Month == @month and Product == @product')
sales_by_product = df_select.groupby('Product')['Total'].sum()
fig_sales_by_product = px.bar(
    sales_by_product,
    x = sales_by_product.values,
    y = sales_by_product.index,
    orientation = 'h',
    title = 'sales_by_product')
a, b, c = st.columns(3)
a.plotly_chart(fig_sales_by_product, use_container_width = True)

fig_sales_by_city = px.pie(df_select, values='Total', names='City', title='Sale by City')
b.plotly_chart(fig_sales_by_city, use_container_width = True)

sales_by_month = df_select.groupby('Month')['Total'].sum().sort_values()
fig_sales_by_month = px.bar(
    sales_by_month,
    x = sales_by_month.values,
    y = sales_by_month.index,
    orientation = 'h',
    title = 'sales_by_month')
c.plotly_chart(fig_sales_by_month, use_container_width = True)

d, e = st.columns(2)
fig_line_sales_by_month = px.line(
    df_select,
    x = sales_by_month.values,
    y = sales_by_month.index,
    title = 'Sale by Month')
d.plotly_chart(fig_line_sales_by_month, use_container_width = True)

fig_total_QuantityOrdered = px.scatter(
    df,
    x = 'Total',
    y = 'QutantityOrdered',
    title = 'Sale total amount')
e.plotly_chart(fig_total_QuantityOrdered, use_container_width = True)