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
git clone https://github.com/dilarademirhan/crm-microservices-architecture.git
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

- API Gateway: http://localhost:5003/api/docs

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
