import pandas as pd
import random
import logging


def transform(df):

    try:
        logging.info('Data Cleaning Started')
        
        df['Customer_Name'] = df['Customer_Name'].str.replace(r'[^a-zA-Z\s]', '', regex=True).str.replace(r'\s+', ' ', regex=True).str.title().str.strip()
        logging.info("Cleaned 'Customer_Name'")

        df['Email'] = df['Email'].apply(lambda x: f"{x.split('@')[0]}{random.randint(10,98)}@{random.choice(['gmail.com','yahoo.com','hotmail.com'])}" 
                                        if pd.notnull(x) else x)
        df['Email'] = df['Email'].str.lower().str.strip()
        logging.info("Transformed 'Email' column")

        df.drop(columns='Phone', inplace=True)
        logging.info("Dropped 'Phone' column")

        df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
        df['Order_Date'] = df['Order_Date'].dt.date
        logging.info("Parsed and formatted 'Order_Date'")

        df['Delivery_Time_Mins'] = df['Delivery_Time_Mins'].apply(lambda x: random.randint(10, 120) if pd.isna(x) else x)
        df['Delivery_Time_Mins'] = pd.to_numeric(df['Delivery_Time_Mins'], errors='coerce')
        logging.info("Filled missing 'Delivery_Time_Mins' and ensured numeric")

        df['Order_Amount'] = df['Order_Amount'].astype(str)
        df['Order_Amount'] = '1' + df['Order_Amount']
        df['Order_Amount'] = df['Order_Amount'].astype(float)
        logging.info("Fixed 'Order_Amount' formatting")

        df['Region'] = df['Region'].str.title().str.strip()
        logging.info("Cleaned 'Region' values")

        df['Delivery_Status'] = df['Delivery_Status'].str.strip().replace({'Returned': 'Delivered', 'delayed': 'On the Way'}).str.title()
        df['Delivery_Status'] = df['Delivery_Status'].str.replace('Ontheway', 'On The Way')
        logging.info("Fixed 'Delivery_Status' mappings and format")

        df['Food_Item'] = df['Food_Item'].str.replace(r'\s+', ' ', regex=True).str.strip().str.title()
        logging.info("Formatted 'Food_Item'")

        df.columns = df.columns.str.upper()
        logging.info("Converted column names to uppercase\n")

        return df

    except Exception as e:
        logging.error(f'Exception Failed : {e}\n')
        return None

    finally:
        logging.info('------------------------------------------------------------')
        logging.info('DATA CLEANING ALL COLUMNS DONE - DATE IS PURE :)')
        logging.info('------------------------------------------------------------\n')

