# Resume Parsing System (Multi-Resume Upload with Database Storage)

## Project Overview
This project is a Resume Parsing System built using Python and Flask.  
It allows users to upload multiple resumes at the same time, extract important information, and store the parsed data locally in a database and an Excel file.

The application runs completely on a local machine and is suitable for academic projects, internship work, and resume screening demonstrations.

---

## Objectives
- Parse multiple resumes simultaneously
- Extract key information such as:
  - Name
  - Email
  - Phone number
  - Skills
  - Education
- Store extracted data locally
- Save results to:
  - SQLite Database
  - Excel file

---

## Tech Stack
- Python
- Flask
- Scikit-learn
- NLP (TF-IDF, Regex)
- SQLite
- Pandas
- HTML, CSS

---




## How It Works
1. User uploads one or more PDF resumes
2. Text is extracted from each resume
3. NLP techniques process the text
4. Important fields are extracted
5. Data is stored in:
   - SQLite database (`resume.db`)
   - Excel file (`resume_data.xlsx`)
6. Each uploaded resume is saved as a separate entry

---

## Installation & Setup

### Clone Repository
```bash
git clone https://github.com/your-username/resume-parser.git
cd resume-parser
Create Virtual Environment
python -m venv venv
venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Run the Application
python app.py
Open browser and visit:

http://127.0.0.1:5000/
Resume Upload
Upload single or multiple PDF resumes

Each resume is parsed individually

Parsed data is automatically saved

Database
Database file: resume.db

Created automatically if not present

Stores parsed resume information locally

Excel Output
File: resume_data.xlsx

Created automatically

Each uploaded resume adds a new row

Features
Multi-resume upload

Automatic database creation

Local data storage

Excel export

Simple web interface

Limitations
Accuracy depends on resume format

Scanned PDFs may not extract text properly

Skill extraction is keyword-based

Future Enhancements
OCR support for scanned resumes

Improved NLP-based skill extraction

Resume ranking and filtering

Admin dashboard

Author
Charu Garg

Conclusion
This project successfully implements a local resume parsing system capable of processing multiple resumes at once and storing the extracted data in both a database and an Excel file.
