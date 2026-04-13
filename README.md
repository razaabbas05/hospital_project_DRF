🏥 Hospital Management System API (Django REST Framework)

A backend API built using Django and Django REST Framework (DRF) for managing hospital operations like patients, doctors, and appointments.
This project provides CRUD functionality and structured APIs for healthcare management systems.

🚀 Features
👨‍⚕️ Patient Management (Create, Read, Update, Delete)
🩺 Doctor Management
📅 Appointment Booking System
📡 RESTful API design using DRF
🗄️ SQLite database (default, can be switched to PostgreSQL/MySQL)
🛠️ Tech Stack
Python 🐍
Django 🌐
Django REST Framework ⚡
SQLite (default DB)
📂 Project Structure
hospital_project/
│
├── manage.py
├── hospital_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── patients/        # Patient management app

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/razaabbas05/hospital_project_DRF.git
cd hospital_project_DRF
2️⃣ Create virtual environment
python -m venv venv

Activate it:

Windows:

venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate
5️⃣ Start server
python manage.py runserver
📡 API Endpoints (Example)
Endpoint	Method	Description
/api/patients/	GET, POST	Manage patients
/api/patients/id/	GET, PUT, DELETE	Single patient
/api/appointments/	GET, POST	Manage appointments
📌 Future Improvements
📱 React frontend integration
📧 Email notifications for appointments
☁️ Deployment on AWS/Render

👨‍💻 Author

Raza Abbas
📧 razaabbassomerville@gmail.com

🎓 B.Tech, Delhi Technical Campus
