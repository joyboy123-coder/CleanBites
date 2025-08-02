# 🍽️ CleanBites ETL Pipeline

A comprehensive ETL (Extract, Transform, Load) pipeline for processing food delivery data and loading it into Snowflake data warehouse.

<p align="center">
  <img src="images/thumbnail/thumbnail_image.png" alt="Clean Bites Thumbnail" style="width:100%; max-width:700px; border-radius: 8px;"/>
</p>

<p align="center">
  <em>100,000 rows cleaned, transformed, and loaded — unstoppable ETL victory with pandas 🐼 and Snowflake ❄️ magic!</em>
</p>

---

## 📋 Project Overview

CleanBites is a data engineering project that processes raw food delivery data through a robust ETL pipeline. The project extracts data from CSV files, applies data cleaning and transformation rules, and loads the processed data into Snowflake for analytics and reporting.

## 🏗️ Architecture

```
📁 CleanBites/
├── 📁 data/                    # Data files
│   ├── raw_data.csv           # Original dataset
│   └── cleaned_data.csv       # Processed dataset
├── 📁 etl_python/             # ETL modules
│   ├── extract.py             # Data extraction logic
│   ├── transform.py           # Data transformation & cleaning
│   └── load.py                # Snowflake data loading
├── 📁 images/                 # Project screenshots & visuals
├── etl_pipeline.py            # Main pipeline orchestrator
├── sql_queries.sql            # Sample analytics queries
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## 🚀 Features

### 📥 **Extract Module**
- Reads raw CSV data from local files
- Handles file path resolution dynamically
- Comprehensive error handling and logging
- Supports various data formats

### 🔄 **Transform Module**
- **Customer Data Cleaning**: Removes special characters, normalizes names
- **Email Anonymization**: Generates random email addresses for privacy
- **Date Processing**: Converts and formats order dates
- **Delivery Time Enhancement**: Fills missing delivery times with realistic values
- **Order Amount Standardization**: Fixes formatting issues
- **Status Normalization**: Standardizes delivery status values
- **Column Standardization**: Converts all column names to uppercase

### 📤 **Load Module**
- **Snowflake Integration**: Secure connection to Snowflake data warehouse
- **Environment Variable Management**: Secure credential handling
- **Auto Table Creation**: Automatically creates tables if they don't exist
- **Bulk Data Loading**: Efficient pandas-to-Snowflake data transfer
- **Comprehensive Logging**: Detailed operation tracking

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.7+
- Snowflake account and credentials
- Required Python packages (see requirements.txt)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd CleanBites
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**
   Create a `.env` file in the project root with your Snowflake credentials:
   ```env
   SNOWFLAKE_USER=your_username
   SNOWFLAKE_PASSWORD=your_password
   SNOWFLAKE_ACCOUNT=your_account
   SNOWFLAKE_WAREHOUSE=your_warehouse
   SNOWFLAKE_DATABASE=your_database
   SNOWFLAKE_SCHEMA=your_schema
   SNOWFLAKE_ROLE=your_role
   SNOWFLAKE_TABLE=your_table_name
   ```

4. **Data Preparation**
   - Place your raw CSV data file in the `data/` directory
   - Ensure the file is named `raw_data.csv`

## 🚀 Usage

### Running the ETL Pipeline

```bash
python etl_pipeline.py
```

The pipeline will:
1. Extract data from `data/raw_data.csv`
2. Apply all transformation rules
3. Load cleaned data into Snowflake
4. Generate detailed logs in `log_file.log`

## 📝 Logging

The pipeline generates comprehensive logs in `log_file.log` including:
- Extraction progress and errors
- Transformation steps and data quality metrics
- Loading status and row counts
- Error handling and debugging information

### Sample Analytics Queries

The project includes `sql_queries.sql` with sample analytics queries:

- 🍽️ Food item order frequency analysis
- 💰 Highest order amounts
- ⏱️ Delivery time analysis
- 📊 Order ranking and top performers
- 🔍 Data quality checks

## 📊 Data Schema

The processed data includes the following columns:

| Column | Type | Description |
|--------|------|-------------|
| CUSTOMER_NAME | String | Cleaned customer names |
| EMAIL | String | Anonymized email addresses |
| ORDER_DATE | Date | Standardized order dates |
| DELIVERY_TIME_MINS | Integer | Delivery time in minutes |
| ORDER_AMOUNT | Float | Standardized order amounts |
| REGION | String | Customer region |
| DELIVERY_STATUS | String | Normalized delivery status |
| FOOD_ITEM | String | Food item names |
| PLATFORM | String | Platform where food will got ordered by |


## 🔧 Customization

### Adding New Transformations
Edit `etl_python/transform.py` to add new data cleaning rules:

```python
# Example: Add new column transformation
df['NEW_COLUMN'] = df['EXISTING_COLUMN'].apply(your_transformation_function)
```

### Modifying Data Sources
Update `etl_pipeline.py` to change data source paths or add new extraction methods.

### Extending Analytics
Add new queries to `sql_queries.sql` for additional business insights.


---

**Happy Data Engineering! 🚀**