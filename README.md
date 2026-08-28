# 📊 DataLab

DataLab is a Python-based Data Science Analysis Portal built with **Streamlit** and **Pandas**.

It allows users to upload CSV or Excel datasets and perform different data analysis and data-cleaning operations through a simple web interface.

## 🚀 Live Demo

🌐 **Live Application:**  
https://datalabonline.streamlit.app/

## 📌 Features

### 📂 File Handling
- Upload CSV files
- Upload XLSX files
- Upload XLS files
- Preview uploaded datasets

### 🐼 Pandas Operations

Currently available:
- Remove Duplicate Rows
- Preview First Rows
- Preview Dataset Shape

More Pandas operations will be added progressively.

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **NumPy**
- **OpenPyXL**
- **XLRD**

## 📁 Project Structure

```text
DataLab/
│
├── .streamlit/
│   └── config.toml
│
├── data/
├── operations/
│   └── pandas_operations/
├── utils/
│   └── file_loader.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/jaykishan1saharan/Data_LAB.git
```

### 2. Navigate to the Project

```bash
cd Data_LAB
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open locally at:

```text
http://localhost:8501
```

## 📊 How It Works

```text
Upload Dataset
      ↓
Load CSV / Excel File
      ↓
Preview Dataset
      ↓
Select Pandas Operation
      ↓
Process Data
      ↓
Display Result
```

## 🧪 Sample Dataset

A dirty dataset is used during development and testing to demonstrate real-world data-cleaning operations.

The dataset contains examples of:

- Missing values
- Duplicate records
- Invalid values
- Incorrect data types
- Inconsistent categorical values
- Invalid dates
- Negative numeric values

## 🔮 Future Plans

DataLab will gradually be expanded with more Data Science functionality.

### Data Inspection
- Preview first/last rows
- Dataset shape
- Dataset information
- Data types
- Statistical summary
- Unique values
- Value counts

### Data Cleaning
- Handle missing values
- Remove unnecessary columns
- Rename columns
- Convert data types
- Clean strings
- Handle invalid values
- Detect outliers

### Data Analysis
- Filtering
- Sorting
- Mathematical operations
- Statistical analysis
- GroupBy
- Aggregation
- Correlation analysis

### Data Visualization
- Bar charts
- Line charts
- Histograms
- Scatter plots
- Box plots
- Pie charts
- Correlation heatmaps

### Export
- Download cleaned CSV
- Download cleaned Excel
- Download analysis results

## 🎯 Project Goal

The goal of DataLab is to create a simple platform where users can upload a dataset and perform common **Data Science, Data Cleaning, Data Analysis, and Visualization operations** without having to manually write Pandas code for every task.

## 👨‍💻 Author

**Jaykishan Saharan**

Built as a Data Science mini project using Python and Streamlit.

---

⭐ If you find this project useful, consider giving it a star!
