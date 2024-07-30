# 📊 Nomina Import Tool

## 🔎 Overview
This project is a Python-based tool designed to import and process employee data (nomina) from various Excel files into specific database tables. It's tailored for handling different types of employee data such as administrative staff, technical staff, post-paid service staff, and more.

## ✨ Features
- Imports data from multiple Excel files with different structures
- Supports various data types and performs necessary conversions
- Configurable import settings for each data type
- Database integration for storing processed data
- Error handling and reporting

## 🛠️ Requirements
- Python 3.x
- openpyxl
- SQLAlchemy
- pymssql
- python-dotenv

## 🚀 Setup
1. Clone the repository:
   ```
   git clone https://github.com/RicardoR-M/nomina-import-tool.git
   cd nomina-import-tool
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the root directory and add your database connection string:
   ```
   DB_CONN=your_database_connection_string
   ```

4. Prepare your Excel files:
   Place your nomina Excel files in the `./nominas/` directory with the following names:
   - `tec.xlsx` (for technical agents)
   - `adm.xlsx` (for administrative agents)
   - `post.xlsx` (for postpago agents)
   - `at.xlsx` (for AT agents)
   - `mesa.xlsx` (for mesa validaciones agents)
   - `contseg.xlsx` (for seguimiento control agents)

## 📋 Usage
Run the main script to import all nomina data:

```
python importa.py
```

This script will process all Excel files and import the data into the respective database tables.

## ⚙️ Configuration
The import process for each type of nomina is configured in separate files in the `config/` directory:

- `adm.py`: Administrative agents configuration
- `tec.py`: Technical agents configuration
- `post.py`: Postpago agents configuration
- `at.py`: AT agents configuration
- `mesa_val.py`: Mesa validaciones agents configuration
- `cont_seg.py`: Seguimiento control agents configuration

Each configuration file defines the database name, table name, Excel sheet details, and column mappings.

## 🔧 Customization
To add a new type of nomina or modify existing ones:

1. Create a new configuration file in the `config/` directory.
2. Define the necessary variables and column mappings.
3. Import the new configuration in `importa.py`.
4. Add a new `importa_informe()` call in the `__main__` section of `importa.py`.

# ⚠️ Error Handling
The script will raise `ValueError` if required columns are not found in the Excel files. Make sure your Excel files match the expected structure defined in the configuration files.

## 📄 License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).