# Resume Parsing System (Local & Multi-Resume Support)

## 📌 Overview
This project is a **local Resume Parsing System** developed using **Python and Flask**.  
It allows users to upload **multiple resumes at the same time**, automatically extracts important information, and stores the results in both a **SQLite database** and an **Excel file**.

The system runs completely **offline on a local machine** and demonstrates practical use of **NLP-based text extraction**.

---

## 🎯 Objectives
- Parse **multiple resumes simultaneously**
- Extract key details:
  - Name
  - Email
  - Phone number
  - Skills
  - Education
- Save parsed data:
  - Into a **SQLite database**
  - Into an **Excel (.xlsx) file**
- Run the application **locally**

---

## 🛠 Technologies Used
- Python  
- Flask  
- SQLite  
- Pandas  
- PDF Parsing Libraries  
- HTML / CSS  

---

## ⚙️ Setup Instructions

### 1️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
2️⃣ Install Required Packages
pip install -r requirements.txt

3️⃣ Run the Application
python app.py

4️⃣ Access the App

Open your browser and go to:

http://127.0.0.1:5000/

🚀 How the System Works

User uploads one or multiple PDF resumes

Each resume is parsed automatically

The system extracts:

Candidate name

Email address

Phone number

Skills

Education details

The extracted information is:

Inserted into a SQLite database

Appended as a new row in an Excel file

Each resume is stored independently, without overwriting previous entries.

🗄 Database Behavior

Database file is created automatically on first run

Each uploaded resume creates a new record

Data persists even after restarting the application

📊 Excel File Behavior

Excel file is created automatically if not present

Each resume adds a new row

Useful for quick review and reporting

✅ Key Features

✔ Multiple resume upload
✔ Automatic data extraction
✔ SQLite database storage
✔ Excel export
✔ Runs locally
✔ Simple and clean interface

🔮 Future Improvements

Resume category prediction

Job role recommendation

Resume ranking system

Admin dashboard

CSV export option

👩‍💻 Author

Charu Garg


