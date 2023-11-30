# Student Performance Indicator with MLOPs

The "Student Performance Indicator with MLOps" project is a machine learning application designed to help educational institutions and educators assess and predict student academic performance. It includes data collection, preprocessing, and the development of machine learning models to forecast student outcomes. The project highlights the implementation of MLOps for Continous integration and Continous deployment (CI/CD) using GitHub Actions for model updates and features a user-friendly web application that offers performance predictions. This end-to-end solution promotes academic success and scalability while being hosted on Azure Cloud. It demonstrates the integration of machine learning and operational excellence in an educational context.


## Features

- Take User Input from the Web interface (Rest API).
- Performs preprocessing on the raw data through data pipelines.
- Pass the processed data to the ML model for Prediction.
- Display the Predictions to the User on the Web page.

## Getting Started

### Prerequisites

- Python 3.10 
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SinghJagpreet096/Studentperformanceindicator-with-mlops
   cd Studentperformanceindicator-with-mlops
   ```

2. (Optional) Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies from requirements.txt:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Start the Flask application:

```bash
python application.py
```

2. Open your web browser and navigate to http://127.0.0.1:5000 to access the web interface.

3. Enter details in the Web interface to get the Predictions.

### Usage
- Enter details in the Given drop-down and text fields.
- Click the Submit button to get the prediction.

### Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow the guidelines in CONTRIBUTING.md.

### License
This project is licensed under the MIT License - see the LICENSE file for details.




