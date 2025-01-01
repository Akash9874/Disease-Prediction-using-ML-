Genomic Disease Prediction Using Machine Learning and Flask

This repository contains a web-based application for predicting diseases based on genomic data. The project leverages machine learning for making predictions and utilizes Flask, HTML, and CSS to create an interactive and user-friendly web interface.

Features

Machine Learning Integration: A robust machine learning model is used to analyze genomic data and predict potential diseases.

User-Friendly Interface: Built with Flask, HTML, and CSS for seamless user interaction.

File Upload Capability: Users can upload genomic data files (e.g., FASTA or CSV) for analysis.

Interactive Output: Disease predictions are displayed clearly on the web page.

Technologies Used

Backend: Flask (Python)

Frontend: HTML, CSS, and JavaScript

Machine Learning: TensorFlow

Installation

Clone the repository:

git clone https://github.com/Akash9874/genomic-disease-prediction.git

Navigate to the project directory:

cd genomic-disease-prediction

Install the required dependencies:

pip install -r requirements.txt

Run the Flask application:

python app.py

Open your browser and visit:

http://127.0.0.1:5000/

How to Use

Upload a genomic data file (e.g., FASTA or CSV).

Click the "Predict" button.

View the predicted diseases on the results page.

Screenshot

Below is a screenshot of the web application:
![Screenshot 2025-01-01 214429](https://github.com/user-attachments/assets/4f40f303-43a4-46eb-98c2-e7e60b6f24bf)

![Screenshot 2025-01-01 214436](https://github.com/user-attachments/assets/fbe6d8b3-7e16-4d56-bb1e-e2da3769131f)



Folder Structure

├── app.py                 # Main Flask application
├── templates/             # HTML files
├── static/                # CSS, JavaScript, and images
├── models/                # Machine learning models
├── uploads/               # Uploaded files
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

Dataset

This project uses the Predict the Genetic Disorders Dataset from Kaggle.

Future Enhancements

Adding support for additional genomic data formats.

Improving prediction accuracy by training on more extensive datasets.

Implementing authentication and user management features.

Contributing

Contributions are welcome! Please fork this repository and create a pull request for any enhancements or bug fixes.
