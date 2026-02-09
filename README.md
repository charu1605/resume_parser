📌 Project Overview

This project is a Resume Parsing System built using Python, Flask, NLP, and Machine Learning.
It allows users to upload multiple resumes at the same time, automatically extract key information, and store the parsed data locally in both a SQLite database and an Excel file.

The system is designed to run entirely on a local machine, making it suitable for academic projects, internships, and offline use.

🎯 Objectives

Parse multiple resumes simultaneously

Extract important information such as:

Name

Email

Phone number

Skills

Education

Store extracted data locally

SQLite database (resume.db)

Excel file (resume_data.xlsx)

Provide a simple web interface for resume upload

🛠️ Tech Stack

Programming Language: Python

Web Framework: Flask

NLP & ML:

Scikit-learn

TF-IDF Vectorizer

Random Forest Classifier

PDF Processing: pdfminer.six / PyMuPDF

Database: SQLite

Data Export: Pandas (Excel)

Frontend: HTML, CSS

📂 Project Structure
ResumeParser/
│
├── app.py                     # Main Flask application
├── resume.db                  # SQLite database (auto-created)
├── resume_data.xlsx           # Excel file (auto-created)
├── rf_classifier_job_recommendation.pkl
├── tfidf_vectorizer_job_recommendation.pkl
│
├── templates/
│   └── resume.html             # Resume upload UI
│
├── static/
│   └── style.css               # Optional styling
│
├── requirements.txt
└── README.md

⚙️ How It Works

User uploads one or multiple resumes through the web interface

Resume text is extracted from PDF files

NLP techniques are used to clean and process text

Important details are parsed using regex and ML models

Parsed data is:

Stored in SQLite database

Appended to Excel file

Each resume is processed individually, even when uploaded together

🚀 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/resume-parser.git
cd resume-parser

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Application
python app.py


Open browser and visit:

http://127.0.0.1:5000/

📥 Uploading Resumes

Upload single or multiple PDF resumes

Supported format: .pdf

Each resume is:

Parsed

Saved in database

Added as a new row in Excel

🗄️ Database Details

Database file: resume.db

Automatically created using init_db()

Stores parsed resume information in structured format

No manual database setup required

📊 Excel Output

File: resume_data.xlsx

Automatically created on first upload

New resumes append new rows

Useful for:

Analysis

Reporting

Sharing data

✅ Features

✔ Multi-resume upload

✔ Automatic database creation

✔ Local storage (no cloud dependency)

✔ Excel export

✔ Simple UI

✔ Fully offline execution

⚠️ Limitations

Parsing accuracy depends on resume format

Scanned PDFs may require OCR for better results

Skill extraction is keyword-based

🔮 Future Enhancements

Add OCR support for scanned resumes

Improve skill extraction using advanced NLP

Resume ranking & recommendation

Admin dashboard for analytics

CSV export option

👤 Author

Charu Garg
Data Science | Machine Learning | Python

⭐ Final Note

This project fulfills the objective of building a local, multi-resume parsing system with database storage and is suitable for:

Academic submissions

Internship projects

Resume screening demos
