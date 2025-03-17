# استخدام صورة أساسية لـ Python
FROM python:3.9-slim

# تعيين مجلد العمل
WORKDIR /app

# نسخ ملفات المشروع
COPY . .

# تثبيت التبعيات
RUN pip install --no-cache-dir -r requirements.txt

# تعيين الأمر الافتراضي لتشغيل التطبيق
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8080"]
