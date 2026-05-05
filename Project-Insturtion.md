# Django Development & Git Workflow Assignment

## 🚀 Project Overview
You are tasked with developing a module within a base Django project while adhering to a professional Git workflow. This assignment evaluates your ability to build functional web modules and collaborate effectively in a shared codebase.

---

## 📋 Task Instructions

### 1. Create a New Django App
- Initialize a new app within the project directory.
- Name it appropriately based on your assigned module.
- Register the new app in the `INSTALLED_APPS` section of `Eduport/settings.py`.

### 2. Module Assignments

#### 🎓 ANJALI – Student Module
Build a **Student Management** module with the following requirements:
- **Model**: Create a `Student` entity.
- **Fields**: Store basic details such as `name` and `age`.
- **Display**: Create a webpage to list all registered students.
- **Management**: Add a form/page to register new students.

#### 📚 RABEEH – Course Module
Build a **Course Management** module with the following requirements:
- **Model**: Create a `Course` entity.
- **Fields**: Store basic details such as `title` and `duration`.
- **Display**: Create a webpage to list all available courses.
- **Management**: Add a form/page to create new courses.

### 3. UI Requirements
- **Base Layout**: Implement a common `base.html` layout (shared template).
- **Consistency**: All module pages must inherit from this base layout.
- **Aesthetics**: Keep the UI clean, professional, and responsive.

### 4. Collaboration Requirement
- Both developers must contribute to the same base template.
- Each developer should integrate their own navigation links and sections.
- **Conflict Resolution**: You are responsible for handling and resolving any merge conflicts.

---

## 🛠 GitHub Workflow (MANDATORY)
Strict adherence to the following workflow is required:

1.  **Fork the Repository**: Create your own copy of the main project on GitHub.
2.  **Clone Your Fork**: Download your fork to your local system.
3.  **Connect Upstream**: Link your local repository to the original (upstream) repository.
4.  **Feature Branching**:
    - **Do NOT** work directly on `main` or `development`.
    - Create a new branch for your task (e.g., `feature/student-module`).
5.  **Commit Standards**: Write clear, descriptive, and meaningful commit messages.
6.  **Push to Fork**: Push your feature branch to your GitHub repository.
7.  **Create Pull Request**: Raise a PR targeting the `development` branch of the main repository.

---

## ⚠️ Important Notes
- **Sync Regularly**: Always pull the latest changes from upstream before starting work.
- **Respect Others' Code**: Do not overwrite or delete code written by your partner.
- **Validation**: Ensure your code runs correctly and passes basic tests after merging.

---
*Created for the ZLQ Internship Program.*
