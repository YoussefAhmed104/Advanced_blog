# Advanced_blog

هذا مشروع تطبيق مدونة مبني باستخدام Django. يسمح للمستخدمين بإنشاء، تعديل، وحذف المقالات، بالإضافة إلى إمكانية إضافة تعليقات ومشاركة التدوينات عبر البريد الإلكتروني.

🎯 Features

✅ إضافة، تعديل، وحذف المقالات 📄
✅ نظام تعليقات للمستخدمين 💬
✅ مشاركة التدوينات عبر البريد الإلكتروني 📧
✅ دعم لصفحات مخصصة مثل صفحة تواصل معنا 📞
✅ دعم للـ Pagination لعرض المقالات بشكل منظم 📚
✅ تحسينات للأمان باستخدام CSRF Token 🛡️

🛠️ Tech Stack

Backend: Django 5.0.6 🐍

Database: SQLite (يمكن استبداله بـ PostgreSQL/MySQL) 🗄️

Frontend: HTML, Bootstrap 🎨

Email System: SMTP (Gmail) ✉️

🚀 Installation Guide

1️⃣ Clone the Repository

git clone https://github.com/YoussefAhmed104/Advanced_bloggit

cd YOUR_PROJECT

2️⃣ Create a Virtual Environment & Activate it

python -m venv venv  
source venv/bin/activate  # (Mac/Linux)
venv\Scripts\activate  # (Windows)

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Apply Migrations

python manage.py makemigrations
python manage.py migrate

5️⃣ Create Superuser (اختياري للدخول إلى لوحة الإدارة)

python manage.py createsuperuser

6️⃣ Run the Server

python manage.py runserver

الآن يمكنك الوصول إلى التطبيق عبر المتصفح من خلال:🔗 http://127.0.0.1:8000/

📨 Contact Form Configuration

لإرسال رسائل البريد الإلكتروني، تأكد من إعداد settings.py باستخدام SMTP:

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
DEFAULT_TO_EMAIL = 'your_email@gmail.com'

⚠️ ملاحظة: استخدم App Password لحماية حسابك من جوجل.

📜 License

هذا المشروع مفتوح المصدر، يمكنك تعديله واستخدامه بحرية! 🚀