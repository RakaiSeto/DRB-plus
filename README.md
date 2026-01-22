# <App Name>

Internal application built using the ***DRB+ Stack***.

This repository follows a standardized, opinionated setup to keep development fast, predictable, and boring (in the good way).

---

## What is the *DRB+ Stack*?

The ***DRB+ Stack*** is our internal default stack for building applications.

### Core
- **Django** — backend & API
- **React** — frontend
- **Bun** — runtime & package manager

### Plus (+)
- **PostgreSQL** — default database
- **TanStack Query** — server-state management
- **TanStack Router** — type-safe routing
- **TanStack Form** — form management
- **Tailwind CSS** — styling

All projects assume these choices by default.  
We do not re-debate the stack per app.

---

## Core Principles

- API-first architecture
- Clear separation of concerns
- Opinionated defaults > flexibility
- Fewer decisions, more shipping

If something feels clever, it’s probably not aligned with this stack.

---

## Requirements

- Bun
- Python 3.x
- PostgreSQL

---

## Project Structure

```txt
.
├── backend/              # Django API
│   ├── app/
│   ├── services/
│   ├── domains/
│   └── manage.py
│
├── frontend/             # React app
│   ├── dist/
│   ├── src/
│   │   ├── routes/       # TanStack Router routes
│   │   ├── api/          # API clients
│   │   ├── components/
│   │   └── main.tsx
│   └── bun.lockb
│
└── README.md
```

---

## Local Development

This project follows the ***DRB+ Stack*** and assumes a split backend/frontend setup.

---

### Backend — Django (API)

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Create environment variables files in backend folder:
```bash
cp .env.example .env
```

Run server:
```bash
python manage.py migrate
python manage.py runserver
```

Backend will be available at:

```bash
http://localhost:8000
```

Notes:
- Django is API-only
- All schema changes must go through migrations
- Do not use SQLite in production

---

### Frontend — React + Bun

```bash
cd frontend
bun install
bun run dev
```

Frontend will be available at:

```bash
http://localhost:5173
```

Notes:
- Bun is mandatory
- Do not use npm or yarn
- bun.lockb is the source of truth

---

# Project Conventions

This document defines **coding, configuration, and runtime conventions** for all internal apps using this template.  
The goal is boring consistency, zero magic, and fast onboarding.

---

## 1. Configuration Convention (Environment Variables)

### Principle
**All configuration comes from environment variables.**  
No `.env` parsing inside the app. No config libraries. No surprises.

- Django reads env **directly** via `os.getenv`

---

### Environment Variable Naming

Rules:
- Use `UPPER_SNAKE_CASE`
- One concern = one prefix
- Be explicit, never clever

Examples:

```txt
DEBUG=true
SECRET_KEY=super-secret-key

DB_NAME=app_db
DB_USER=app_user
DB_PASSWORD=app_password
DB_HOST=localhost
DB_PORT=5432

FRONTEND_PUBLIC_API_BASE_URL=http://localhost:8000
```

### Django (backend/config/settings.py)
```python
import os

DEBUG = os.getenv("DEBUG", "false").lower() == "true"

SECRET_KEY = os.getenv("SECRET_KEY")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}
```

Rules:
- No defaults for secrets
- App should fail fast if critical env is missing
- Do not import dotenv or similar libraries

---

## 2. Backend Conventions (Django)
### Project Structure
```txt
backend/
├── config/          # settings, urls, wsgi, asgi
│   └── settings.py
├── domains/         # business domains (DDD-lite)
│   ├── users/
│   ├── payments/
│   └── reports/
├── services/        # cross-domain logic
├── manage.py
```

### Domains
- One domain = one bounded context
- Domains own:
    - models
    - selectors (read logic)
    - services (write logic)
- Avoid fat views, avoid god services


## 3. Frontend Conventions (Bun + React)
### Project Structure
```txt
frontend/
├── src/
│   ├── routes/        # TanStack Router routes (file-based or declarative)
│   ├── api/           # API clients, fetchers
│   ├── components/    # reusable UI components
│   ├── lib/           # helpers, utils
│   └── main.tsx
└── bun.lockb
```

### Routing (TanStack Router)
Rules:
- All navigation goes through TanStack Router
- No React Router
- Route = screen, not component soup
- Data loading happens in route loaders when possible


