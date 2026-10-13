# CampusConnect 🎓

A Student Task Management Application built using Python, Streamlit, and SQLite.

## 1. Project Overview

CampusConnect is a student task management application designed to help students organize assignments, manage study sessions, track deadlines, and monitor their academic progress.

The application provides a user-friendly interface for managing tasks, searching records, filtering tasks, viewing progress charts, planning weekly study schedules, and exporting task information to CSV.

## 2. Project Objectives

- Organize assignments and study sessions.
- Track pending and completed tasks.
- Manage task deadlines.
- Search and filter task records.
- Store task information using SQLite.
- Visualize task progress.
- Export task information to CSV.
- Practice Python, OOP, database management, and Git.

## 3. Features

- Add assignments and study sessions.
- View saved tasks.
- Search tasks by title or subject.
- Filter tasks by type and status.
- Edit existing tasks.
- Delete tasks.
- Mark tasks as completed.
- Track completed and pending tasks.
- View task metrics and progress charts.
- Use a weekly study planner.
- Export task information to CSV.
- Store task information in an SQLite database.

Note: Verify that each feature is implemented in the current application before publishing this README.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Web application interface |
| SQLite | Local database |
| Object-Oriented Programming | Classes and inheritance |
| CSV | Exporting task information |
| Git | Version control |
| GitHub | Hosting source code |

## 5. Project Structure

```text
CampusConnect/
│
├── app.py
├── database.py
├── models.py
├── requirements.txt
├── README.md
├── .gitignore
└── campusconnect.db
```

### File Descriptions

- `app.py` — Main Streamlit application.
- `database.py` — Database connection and database operations.
- `models.py` — Task classes and object-oriented programming logic.
- `requirements.txt` — Required Python packages.
- `README.md` — Project documentation.
- `.gitignore` — Files and folders excluded from Git tracking.
- `campusconnect.db` — Local SQLite database, if created by the application.

The database file is normally excluded from GitHub when it contains local or test data.

## 6. Prerequisites

Install the following tools:

- Python
- Visual Studio Code
- Git

Check Python installation:

```bash
python --version
```

Check pip:

```bash
python -m pip --version
```

Check Git:

```bash
git --version
```

## 7. Installation and Setup

### Step 1: Open the Project Folder

Open Visual Studio Code.

Select:

File → Open Folder → CampusConnect

Open a new terminal:

Terminal → New Terminal

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 3: Activate the Virtual Environment

Windows Command Prompt:

```bat
.venv\Scripts\activate.bat
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt or run the Python commands through `.venv\Scripts\python.exe` directly.

### Step 4: Install Dependencies

The `requirements.txt` file should contain:

```text
streamlit
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## 8. Run the Application

Run the following command from the project folder:

```bash
streamlit run app.py
```

Streamlit displays a local URL in the terminal. Open that URL in your browser.

The default address is commonly:

```text
http://localhost:8501
```

Keep the terminal open while the application is running.

To stop the application, press:

```text
Ctrl + C
```

## 9. Application Workflow

1. Start the application.
2. Add an assignment or study session.
3. Enter task details and a due date.
4. View saved tasks.
5. Search and filter tasks.
6. Edit task information.
7. Mark tasks as completed.
8. Review progress metrics and charts.
9. Check the weekly study planner.
10. Export task information to CSV.

## 10. Database

CampusConnect uses SQLite for local data storage.

The database layer supports task-related operations such as:

- Creating task records.
- Reading saved tasks.
- Updating task information.
- Deleting task records.

The application code should initialize the database and required tables when configured to do so.

## 11. Testing

Run the application:

```bash
streamlit run app.py
```

Test the following features in the browser:

- Add a task.
- View the task.
- Search for the task.
- Filter tasks.
- Edit the task.
- Mark the task as completed.
- Verify progress metrics.
- Check the weekly planner.
- Export task data to CSV.
- Delete a temporary test task.

If the project contains automated tests, run the appropriate test command. For example, if `test_database.py` uses pytest and is designed to run safely:

```bash
python -m pip install pytest
python -m pytest
```

Do not run test files until you have reviewed their contents, because a test may insert or modify database records.

## 12. Git Configuration

Check whether Git is initialized:

```bash
git status
```

If Git reports that the folder is not a repository:

```bash
git init
```

Check the status again:

```bash
git status
```

Configure your Git identity if required:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Replace the placeholders with your preferred Git commit name and email.

## 13. Git Ignore Configuration

Create a `.gitignore` file in the project root.

Example contents:

```gitignore
__pycache__/
*.py[cod]
.venv/
venv/
.env
*.db
*.sqlite
*.sqlite3
```

This excludes Python cache files, virtual environments, environment-variable files, and local SQLite database files from future Git tracking.

## 14. Stage and Commit Changes

Review the project files:

```bash
git status
```

Stage the main project files:

```bash
git add app.py database.py models.py README.md requirements.txt .gitignore
```

Check the staged changes:

```bash
git status
```

Create a commit:

```bash
git commit -m "Complete CampusConnect Python project"
```

View the commit history:

```bash
git log --oneline
```

## 15. Upload the Project to GitHub

### Step 1: Create a Repository

1. Open https://github.com/
2. Sign in.
3. Select New repository.
4. Enter `CampusConnect` as the repository name.
5. Add a short project description.
6. Choose Public or Private.
7. If your local project already has a README and commit, create the online repository without initializing another README.
8. Click Create repository.

### Step 2: Connect the Local Repository

Check whether a remote is already configured:

```bash
git remote -v
```

If no remote exists, add your repository URL:

```bash
git remote add origin YOUR_GITHUB_REPOSITORY_URL
```

Replace the placeholder with your actual repository HTTPS URL.

If `origin` already exists, verify that it points to the correct repository rather than adding it again.

### Step 3: Push to GitHub

Check the current branch:

```bash
git branch
```

Rename the current branch to `main` if appropriate:

```bash
git branch -M main
```

Push your commit:

```bash
git push -u origin main
```

Complete any authentication prompts.

If Git reports that the remote contains commits that are missing locally, inspect the histories before proceeding. Do not force-push without understanding the consequences.

## 16. Verify the GitHub Repository

After pushing, refresh the repository page.

Check that the repository contains:

- `app.py`
- `database.py`
- `models.py`
- `requirements.txt`
- `.gitignore`
- `README.md`

Confirm that the README renders correctly.

Do not upload passwords, API keys, personal data, or an unnecessary local database.

## 17. Learning Outcomes

This project provides practical experience with:

- Python programming.
- Object-Oriented Programming.
- Classes and inheritance.
- CRUD operations.
- SQLite database management.
- Streamlit web applications.
- Search and filtering.
- Data visualization.
- CSV file handling.
- Git version control.
- GitHub repository management.

## 18. Future Enhancements

Possible improvements include:

- Student login and authentication.
- Role-based access control.
- Deadline reminders.
- Improved task analytics.
- Online deployment.

These are proposed enhancements, not claims that the features already exist.

## 19. Author

**Bodimalla Archana**

Python Developer | Data Analyst

## 20. License

This project is intended for learning and portfolio demonstration. Add an appropriate open-source license if you decide to distribute the project under specific license terms.