# CRM Microservices Architecture

Bu proje, modern bir CRM (Customer Relationship Management) sisteminin mikroservis mimarisi kullanılarak geliştirilmiş bir örneğidir. Sistem, müşteri yönetimi, satış işlemleri ve kullanıcı kimlik doğrulama gibi temel CRM işlevlerini içeren ayrı mikroservislerden oluşmaktadır.

## 🏗️ Mimari Yapı

Sistem aşağıdaki mikroservislerden oluşmaktadır:

- **API Gateway (5003)**: Tüm isteklerin giriş noktası ve yönlendirme merkezi
- **Customer Service (5001)**: Müşteri yönetimi servisi (MongoDB)
- **Sales Service (5002)**: Satış işlemleri servisi (PostgreSQL)
- **Auth Service (5000)**: Kimlik doğrulama ve yetkilendirme servisi (PostgreSQL)

## 🛠️ Teknolojiler

- **Backend**: Python, Flask
- **Veritabanları**: 
  - MongoDB (Customer Service)
  - PostgreSQL (Sales ve Auth Services)
- **API Dokümantasyonu**: Swagger UI
- **Containerization**: Docker, Docker Compose
- **Kimlik Doğrulama**: JWT (JSON Web Tokens)

## 📋 Özellikler

- Mikroservis mimarisi ile modüler yapı
- Her servis için ayrı veritabanı
- JWT tabanlı kimlik doğrulama
- Swagger UI ile API dokümantasyonu
- Docker containerization
- CORS desteği
- Veritabanı migrasyonları

## 🚀 Başlangıç

### Gereksinimler

- Docker
- Docker Compose

### Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/yourusername/crm-microservices.git
cd crm-microservices
```

2. Docker container'larını başlatın:
```bash
docker compose up --build
```

3. Servisler şu portlarda çalışacaktır:
   - API Gateway: http://localhost:5003
   - Customer Service: http://localhost:5001
   - Sales Service: http://localhost:5002
   - Auth Service: http://localhost:5000

### API Dokümantasyonu

Her servis için Swagger UI dokümantasyonu mevcuttur:
- API Gateway: http://localhost:5003/api/docs
- Customer Service: http://localhost:5001/api/docs
- Sales Service: http://localhost:5002/api/docs
- Auth Service: http://localhost:5000/api/docs

## 🔧 Servis Yapılandırması

### Environment Variables

Her servis için gerekli environment variable'lar:

#### API Gateway
```
FLASK_APP=run.py
FLASK_ENV=development
CUSTOMER_SERVICE_URL=http://customer-service:5001
SALES_SERVICE_URL=http://sales-service:5002
AUTH_SERVICE_URL=http://auth-service:5000
```

#### Customer Service
```
FLASK_APP=run.py
FLASK_ENV=development
MONGODB_URI=mongodb://mongodb:27017/customer-db
```

#### Sales Service
```
FLASK_APP=run.py
FLASK_ENV=development
DATABASE_URL=postgresql://postgres:postgres@postgres:5432/salesdb
```

#### Auth Service
```
FLASK_APP=run.py
FLASK_ENV=development
DATABASE_URL=postgresql://postgres:postgres@postgres:5432/authdb
JWT_SECRET=jwt_secret_key
```

## 📁 Proje Yapısı

```
crm-microservices/
├── api-gateway/
│   ├── app/
│   │   ├── routes/
│   │   ├── config/
│   │   └── __init__.py
│   ├── requirements.txt
│   └── run.py
├── customer-service/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   └── __init__.py
│   ├── requirements.txt
│   └── run.py
├── sales-service/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   └── __init__.py
│   ├── requirements.txt
│   └── run.py
├── auth-service/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   └── __init__.py
│   ├── requirements.txt
│   └── run.py
└── docker-compose.yml
```

## 🔒 Güvenlik

- JWT tabanlı kimlik doğrulama
- CORS politikaları
- Environment variable'lar ile hassas bilgilerin yönetimi
- Veritabanı bağlantılarının güvenli yapılandırması
