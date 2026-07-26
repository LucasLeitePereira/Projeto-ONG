# Superação VD — NGO Management System

A web platform for the **Superação da Violência Doméstica (Superação VD)** NGO, focused on supporting victims of domestic violence through volunteer networks and legal assistance.

Built as a college project and deployed to production using Docker and Render.

---

## About the Project

Superação VD operates by connecting domestic violence victims with volunteer professionals — law students (interns), lawyers, and law graduates. The system manages volunteer registrations, victim records, and service appointments.

The platform includes:
- A public-facing website with information about the NGO, news, and volunteer program details
- Registration forms for victims and three types of volunteers
- A REST API backend for data management

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.11 + Django 4.2 |
| REST API | Django REST Framework |
| Database | PostgreSQL (production) / SQLite (development) |
| Static files | Whitenoise |
| Web server | Gunicorn |
| Containerization | Docker + Docker Compose |
| Deployment | Render |
| Environment config | python-decouple |

---

## Features

### Public Website
- Home page with NGO mission, about section, and news
- Volunteer program information (intern, lawyer, graduate)
- Victim registration form
- 3 news article pages

### REST API
| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/voluntarios/adicionar/estagiario/` | Register a law student intern |
| POST | `/api/voluntarios/adicionar/advogado/` | Register a lawyer |
| POST | `/api/voluntarios/adicionar/bacharel/` | Register a law graduate |
| POST | `/api/vitimas/adicionar/` | Register a victim |
| POST | `/api/atendimentos/adicionar/` | Register a service appointment |

### Admin Panel
Available at `/admin/` — full Django admin interface for managing all records.

---

## Data Models

```
Voluntario (base volunteer)
├── Estagiario (law student intern) — with availability schedule
├── Advogado (lawyer) — with OAB registration number
└── Bacharel (law graduate) — with degree course

Vitima (victim)

Atendimento (service appointment)
└── links Vitima ↔ Estagiario
```

---

## Getting Started

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/marcelocataldo/ProjetoONG.git
   cd ProjetoONG
   ```

2. **Create your environment file**
   ```bash
   cp .env.Example .env
   ```
   Fill in the values in `.env` (see [Environment Variables](#environment-variables) below).

3. **Run with Docker Compose**
   ```bash
   docker compose up --build
   ```

4. **Access the app**
   - Website: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

5. **Create a superuser** (optional, for admin access)
   ```bash
   docker compose exec web python manage.py createsuperuser
   ```

---

## Environment Variables

Copy `.env.Example` to `.env` and fill in the values:

| Variable | Description | Example |
|---|---|---|
| `SECRET_KEY` | Django secret key — generate at [djecrety.ir](https://djecrety.ir/) | `your-secret-key-here` |
| `DEBUG` | Debug mode — `True` for dev, `False` for production | `False` |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hostnames | `localhost,127.0.0.1` |
| `DATABASE_URL` | Database connection URL | `sqlite:///db.sqlite3` |

> In production (Render), these are set directly in the dashboard — never commit `.env` to Git.

---

## Deployment (Render)

1. Push your code to GitHub
2. Create a new **Web Service** on [render.com](https://render.com) connected to this repository
3. Set **Environment** to `Docker`
4. Add a **PostgreSQL** database — Render fills `DATABASE_URL` automatically
5. Set the following environment variables in the Render dashboard:

   | Variable | Value |
   |---|---|
   | `SECRET_KEY` | Your generated secret key |
   | `DEBUG` | `False` |
   | `ALLOWED_HOSTS` | `your-service-name.onrender.com` |

On every push to the `production` branch, Render will automatically rebuild and redeploy.

---

## Project Structure

```
ProjetoONG/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.Example
└── back-end/
    ├── manage.py
    ├── entrypoint.sh          # Runs migrations + starts Gunicorn
    ├── server/                # Django project settings & URLs
    ├── core/                  # Public website views, templates & static files
    ├── voluntarios/           # Volunteer models, views & API endpoints
    ├── vitimas/               # Victim models, views & API endpoints
    └── atendimentos/          # Service appointment models & endpoints
```

---

## License

This project was developed as a college assignment. All rights reserved.
