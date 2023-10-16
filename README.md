# Project: Destination Insights (GDI)

This project automates the data retrieval process from the Destination Insights website using Selenium and Python. It enables users to gather essential information regarding travel demand for various countries and categories, facilitating data-driven decisions in the travel industry.
[Destination Insights](https://destinationinsights.withgoogle.com/intl/en_ALL/)

## Table of Contents

- [Prerequisites](#prerequisites)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Python (3.7 or higher)
- [Chromedriver](https://chromedriver.chromium.org/downloads)
- Required Python packages listed in `requirements.txt`

# Features
- **Automated Data Retrieval:** Utilizes Selenium to automate the process of gathering travel demand data.
- **Country Comparison:** Allows users to compare travel demands between different countries.
- **Data Categorization:** Provides options to analyze demand data based on categories like air travel and accommodation.
- **Flexible Date Range:** Supports dynamic date range selection, allowing users to analyze data for specific time periods.
- **Robust Error Handling:** Implements error handling mechanisms to ensure smooth execution even in the face of unexpected errors.

# Technologies Used
- **Python:** Scripting language used for automation and data processing.
- **Selenium:** Automation framework used for web scraping tasks.
- **Markdown:** Documentation format used for clarity and simplicity.

## Getting Started

To get started with Destination Insights, follow these steps:

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/IngAamira/Destination_Insights.git
   ```
2. **Create a Virtual Environment:**
   ```sh
   python3 -m venv env
   ```
3. **Activate the Virtual Environment:**
   ```sh
    source env/bin/activate
   ```
4. **Install Required Packages:**
   ```sh
    pip3 install -r requirements.txt
   ``` 
5. **Download and Configure Chromedriver:**
- Download [Chromedriver](https://chromedriver.chromium.org/downloads) and place the executable in the "./chromedriver/" directory.
6. **Run the Main Script:**
   ```sh
    python3 main.py
   ``` 

## Contributing

Contributions are welcome! Please feel free to open issues and pull requests. For major changes, please discuss them in advance.

## License

This project is licensed under the [Open Source](https://opensource.org/licenses/).