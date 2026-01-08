# Project Title: E-commerce Mini Testing Project

**This project is created by me—a self-trained tester who just got graduated and choose Testing to grow a career with.**

It covered **Manual Testing**, **API Testing**, **API Performance Testing**, and **Automation Testing** with both Selenium and Cypress. I hope this project can show my technical skill and knowledge, as it took a hard time for me to finished it.
### 📝 Project Recap & Motivation
This project was developed to showcase a structured, end-to-end software quality assurance process for an e-commerce application. It demonstrates both manual testing discipline and automated testing using modern tools like **Cypress**, **Selenium**, **Pytest**, and **JMeter** and **Postman**

### 🚀 Features Tested
*   User Authentication (Login, Registration)
*   Product Searching 
*   Shopping Cart Functionality
*   API Endpoints
*   System Performance (Load and Endurance Testing)
*   Comprehensive Bug Reporting

### 🛠️ Tech Stack & Tools
*   **Manual Testing:** Test Plans (.docx), Test Cases (.xlsx)
*   **API Testing:** Postman/Newman, JSON Reports
*   **Performance Testing:** Apache JMeter (.jmx, .jtl, .html reports)
*   **Automation Testing (UI):**
    *   Cypress (JavaScript)
    *   Selenium with Python & Pytest
*   **Reporting:** HTML reports (Mochawesome, pytest-html, Newman)
*   **Visual Studio Code:** 

### 📂 Project Structure Overview
A clean structure helps recruiters understand your organization. You can describe your folders here:

*   **`01_Test_plan/`**: Project scope, strategy, and deliverables.
*   **`02_Test_Cases/`**: Detailed manual and API test scenarios and expected results.
*   **`03_Test_Execution/`**: Results from executing tests (manual and automated).
*   **`04_API_Performance_Testing/`**: JMeter scripts and performance analysis reports.
*   **`05_Automation_Testing/`**: Codebase for UI automation using Cypress and Selenium/Python.
*   **`06_Bug_reports/`**: Logs of defects, screenshots, and summary report.

### ⚙️ Installation & Usage
To run this project locally, follow these steps:

#### Prerequisites
*   Node.js (for Cypress/Newman)
*   Python 3.x (for Selenium/Pytest)
*   JMeter (for Performance Testing)
*   Postman (for API Testing)

#### Running Automation Tests
Use these commands in your terminal:

```bash

# Install Node.js dependencies (Newman & helpers)
# From project root
cd E-commerce Mini Testing project by TDuy

npm install

# Run API tests with Newman and generate HTML report    
cd 03_Test_Execution/API_Test_execution


newman run ./03_Test_Execution/API_Test_Execution/Final_of_Final.json -r cli,htmlextra --reporter-htmlextra-export ./03_Test_Execution/API_Test_Execution/API_Test_Report.html 
#OR 
newman run test:api


# just run simple API Test   
newman run ./03_Test_Execution/API_Test_Execution/Final_of_Final.json
#OR
newman run test:api:simple




# Run JMeter test plan (headless mode)
cd 04_API_Performance_Testing
jmeter -n -t Test_plan.jmx -l results.jtl -e -o ./report




# Run Cypress tests
cd 05_Automation_Testing/Cypress_testing
npm install
npx cypress run
# Merge JSON reports from Cypress
npx mochawesome-merge "cypress/report/mochawesome-report/*.json" > mochawesome.json
# Generate HTML report
npx mochawesome-report-generator mochawesome.json --reportDir cypress/report --inline



# Run Selenium/Python tests
cd 05_Automation_Testing/Selenium_testing
# Create/activate virtual environment if necessary
python -m venv venv
# Activate virtual environment
# Windows
venv\Scripts\Activate.ps1
# macOS / Linux
source venv/bin/activate.bat


# Install dependencies
pip install -r requirements.txt
pytest tests/
# Generate HTML report for Selenium/Python
pytest --html=report_final_all_passed.html --self-contained-html
