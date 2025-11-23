# Project-1-CSE
# Faculty Data CRUD Manager

## 1. Overview
This project is a simple desktop application developed using Python, Tkinter, and SQLite.  
The application allows users to store, view, update, and delete faculty details.  
It is designed to demonstrate basic CRUD operations with a clean and easy-to-use interface.

The purpose of this project is to implement:
- GUI development using Tkinter  
- Database handling using SQLite  
- Modular programming  
- Basic input validation  
- Simple data management features  

---

## 2. Features
- Add new faculty records  
- Display all stored records in a table  
- Select any row to load the data for editing  
- Update selected faculty details  
- Delete selected records  
- Error messages for invalid inputs  
- Success messages for add, update, and delete actions  
- Structured and modular code  
- Persistent data using SQLite database  

---

## 3. Technologies / Tools Used
- **Python 3**  
- **Tkinter** (Graphical User Interface)  
- **SQLite** (Database)  
- **VS Code** (Code editor)  
- **Git & GitHub** (Version control & hosting)  

---

## 4. Steps to Install & Run the Project

### Step 1: Install Python
Download Python 3 from the official website and install it.

### Step 2: Download or Clone the Repository
git clone https://github.com/NiyatiSethi/Project-1-CSE.git

### Step 3: Open in VS Code
- Open the project folder  
- Ensure Python extension is installed  

### Step 4: Run the Project
Open the terminal and run:
python main.py

- The Faculty Manager GUI will open.

---

## 5. Instructions for Testing

### ✔ Test 1: Add Faculty  
1. Enter all the details  
2. Click **Add Faculty**  
3. A new row should appear in the table  
4. A success message should be shown

### ✔ Test 2: Select a Row  
- Click on any row in the table  
- All fields should automatically fill with the selected row’s data

### ✔ Test 3: Update Record  
1. Select a row  
2. Change any detail  
3. Click **Update Faculty**  
4. The table should update the row  
5. A success message should appear

### ✔ Test 4: Delete Record  
1. Select a row  
2. Click **Delete Faculty**  
3. The row should disappear  
4. A success message should appear

### ✔ Test 5: Validation  
Try submitting:
- Empty fields  
- Non-numeric experience  
- Name with numbers  

You should see meaningful error messages.

---

## 6. Screenshots
All screenshots related to the project are available in the **/screenshots** folder:

- Home screen  
- Add faculty  
- Update faculty  
- Delete faculty  
- Validation message  
- Project structure  
- Database file  

---

## 7. Database
The project uses an SQLite database (`faculty.db`).  
The table is automatically created when the program runs.

Fields:
- id  
- name  
- department  
- qualification  
- experience  

---

## 8. Author
This project is created as part of a Computer Science course project focused on CRUD operations, GUI development, and basic database handling.

- Niyati Sethi
  25BCE10997