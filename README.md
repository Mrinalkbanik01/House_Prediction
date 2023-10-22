# House Prediction System

This web application allows users to predict house prices based on various input parameters.Basically an ML Model is created after performing a lot of Feature Engineering , EDA and Featue Selection on a large dataset.The ML model is then pickeled and is used by the flask server to fetch the correct price

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

These instructions will help you set up and run the House Prediction System on your local machine for development and testing purposes.

### Prerequisites

Before you begin, make sure you have the following software installed:

- [Python](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/house-prediction-system.git
Change to the project directory:

bash
Copy code
cd house-prediction-system
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS and Linux:

bash
Copy code
source venv/bin/activate
Install Python dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Start the Flask application:

bash
Copy code
python app.py
Access the application in your web browser at http://127.0.0.1:5000.

Use the application to predict house prices by providing the required input parameters.
