# Django resmi Python görüntüsünü kullan
FROM python:3.12.2

# Çalışma dizinini belirt
WORKDIR /code

# Gerekli Python paketlerini yükle
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını görüntüye ekle
COPY . /code/

# Giriş komutunu belirt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
