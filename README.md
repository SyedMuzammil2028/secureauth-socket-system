# SecureAuth - Secure Network-Based User Authentication System

SecureAuth is a Computer Networks project that demonstrates secure user authentication using Python socket programming, FastAPI, SQLite, and a React + TypeScript frontend.

## Features

- Python TCP socket authentication flow
- FastAPI REST backend for the frontend
- SQLite database initialization and migration scripts
- Email OTP verification for registration and email change
- QR/TOTP multi-factor authentication
- Session token creation, expiry checks, and revocation
- Rate limiting and account lockout
- User suspension and soft delete controls
- Audit logging and admin log clearing
- Admin dashboard, user management, session management, and settings
- User profile, sessions, email change, logout, and delete-account dashboard

## Requirements

Install these before running the project:

- Python 3.11 or newer
- Node.js 20.19 or newer, or Node.js 22.13 or newer
- npm
- Git
- Gmail app password or another SMTP account for OTP emails

Check versions on Windows PowerShell:

```powershell
python --version
node --version
npm --version
git --version
```

## Download From GitHub

Clone the repository:

```powershell
git clone https://github.com/SyedMuzammil2028/secureauth-socket-system.git
cd secureauth-socket-system
```

Or download it manually:

1. Open the GitHub repository.
2. Click `Code`.
3. Click `Download ZIP`.
4. Extract the ZIP.
5. Open PowerShell inside the extracted project folder.

If you downloaded ZIP, go to the extracted folder:

```powershell
cd "C:\path\to\authsystemv2"
```

## Project Structure

```text
backend/        FastAPI API, socket server, services, and SQLite scripts
docs/           Project documentation
frontend/       React + TypeScript + Vite frontend
.env.example    Backend environment template
requirements.txt
README.md
```

## Environment Setup

This project does not include real `.env` files. Create them locally from the examples.

Windows PowerShell:

```powershell
Copy-Item .env.example .env
Copy-Item frontend\.env.example frontend\.env
```

Open backend `.env`:

```powershell
notepad .env
```

Update these values:

```text
SECRET_KEY=your_long_random_secret
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_gmail_app_password
SMTP_TIMEOUT_SECONDS=10
ADMIN_USERNAME=admin
ADMIN_PASSWORD=YourStrongPassword@123
```

The frontend `.env` should normally stay as:

```text
VITE_API_BASE_URL=http://127.0.0.1:8000
```

## Backend Setup

Run these commands from the project root.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If virtual environment activation is blocked, run this once:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate the virtual environment again:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Database Setup

Keep the virtual environment activated. Do not deactivate it before running these commands.

```powershell
python -m backend.database.init_db
python -m backend.database.migrate_security_controls
python -m backend.database.create_admin
```

This creates a local SQLite database at:

```text
backend/database/auth_system.db
```

Do not commit or upload this database file.

## Run the Backend

The project uses both a socket server and a FastAPI server. Run them in two separate PowerShell terminals.

### Terminal 1: Socket Server

From the project root:

```powershell
.\.venv\Scripts\Activate.ps1
python -m backend.socket_server.server
```

Expected output:

```text
[SOCKET] Listening on 127.0.0.1:9000
```

Keep this terminal open.

### Terminal 2: FastAPI Server

Open a new PowerShell terminal from the project root:

```powershell
.\.venv\Scripts\Activate.ps1
uvicorn backend.api.main:app --host 127.0.0.1 --port 8000 --reload
```

The backend API will run at:

```text
http://127.0.0.1:8000
```

Keep this terminal open.

## Frontend Setup

Open a third PowerShell terminal from the project root:

```powershell
cd frontend
npm ci
```

If `npm ci` shows vulnerability warnings, that is not automatically a setup failure. Do not run this command unless you intentionally want to upgrade packages and test for breaking changes:

```powershell
npm audit fix --force
```

Now start the frontend:

```powershell
npm run dev
```

The frontend will run at:

```text
http://127.0.0.1:5173
```

## Optional Frontend Build Check

To verify that the frontend builds successfully:

```powershell
cd frontend
npm run build
```

To preview the production build locally:

```powershell
npm run preview
```

## Quick Run Order

You need three terminals running.

```text
Terminal 1:
python -m backend.socket_server.server

Terminal 2:
uvicorn backend.api.main:app --host 127.0.0.1 --port 8000 --reload

Terminal 3:
cd frontend
npm run dev
```

Then open:

```text
http://127.0.0.1:5173
```

## Demo Flow

1. Register a new user.
2. Verify the email OTP.
3. Log in using username/email and password.
4. Scan the QR code in an authenticator app.
5. Enter the TOTP MFA code.
6. Open the user dashboard.
7. Log in as admin using the admin credentials from `.env`.
8. Review users, sessions, logs, locked accounts, and settings.

## Important Security Notes

Do not upload these files or folders to GitHub:

```text
.env
frontend/.env
backend/database/auth_system.db
__pycache__/
*.pyc
.pytest_cache/
venv/
.venv/
frontend/node_modules/
frontend/dist/
*.zip
*.log
*.tmp
*.bak
```

The repository should include these safe files:

```text
.env.example
frontend/.env.example
.gitignore
requirements.txt
README.md
backend/
docs/
frontend/
frontend/package.json
frontend/package-lock.json
```

## Troubleshooting

If OTP emails are not received:

- Check `SMTP_EMAIL` and `SMTP_PASSWORD` in `.env`.
- Use an app password, not your normal email password.
- Check spam/junk folders.
- Make sure the FastAPI server and socket server are both running.

If frontend API calls fail:

- Confirm FastAPI is running on `http://127.0.0.1:8000`.
- Confirm `frontend/.env` has `VITE_API_BASE_URL=http://127.0.0.1:8000`.
- Restart the frontend after editing `.env` files.

If database errors occur:

- Delete the local `backend/database/auth_system.db` file.
- Run the database setup commands again.
## Deploy On Render

This repository includes `render.yaml`, so you can deploy both services from the Render Dashboard using a Blueprint.

### Recommended Render Architecture

```text
secureauth-api       Render Web Service, Python/FastAPI
secureauth-frontend  Render Static Site, React/Vite
```

The frontend talks to the backend through `VITE_API_BASE_URL`.

### Option 1: Deploy With render.yaml Blueprint

1. Push this repository to GitHub.
2. Open Render Dashboard.
3. Click `New`.
4. Select `Blueprint`.
5. Connect this GitHub repository.
6. Select the `main` branch.
7. Render will detect `render.yaml`.
8. Before deploying, add required secret values when Render asks for them:

```text
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_gmail_app_password
SMTP_TIMEOUT_SECONDS=10
ADMIN_USERNAME=admin
ADMIN_PASSWORD=YourStrongPassword@123
```

The blueprint creates:

```text
Backend URL:  https://secureauth-api.onrender.com
Frontend URL: https://secureauth-frontend.onrender.com
```

If Render gives different URLs, update these environment variables in Render:

Backend service:

```text
CORS_ORIGINS=https://your-frontend-url.onrender.com
```

Frontend static site:

```text
VITE_API_BASE_URL=https://your-backend-url.onrender.com
```

Then redeploy both services.

### Option 2: Manual Render Setup

#### Backend Web Service

Create a new Render `Web Service`.

Use these settings:

```text
Runtime: Python 3
Branch: main
Build Command: pip install -r requirements.txt
Start Command: python -m backend.database.init_db && python -m backend.database.migrate_security_controls && python -m backend.database.create_admin && uvicorn backend.api.main:app --host 0.0.0.0 --port $PORT
```

Add environment variables:

```text
APP_ENV=production
DB_PATH=backend/database/auth_system.db
CORS_ORIGINS=https://your-frontend-url.onrender.com
SECRET_KEY=your_long_random_secret
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_gmail_app_password
SMTP_TIMEOUT_SECONDS=10
ADMIN_USERNAME=admin
ADMIN_PASSWORD=YourStrongPassword@123
EMAIL_OTP_EXPIRY_MINUTES=5
MFA_TEMP_EXPIRY_MINUTES=5
NONCE_EXPIRY_MINUTES=2
SESSION_EXPIRY_HOURS=12
MAX_FAILED_ATTEMPTS=5
LOCKOUT_MINUTES=10
RATE_LIMIT_WINDOW_SECONDS=60
RATE_LIMIT_MAX_REQUESTS=10
```

#### Frontend Static Site

Create a new Render `Static Site`.

Use these settings:

```text
Branch: main
Root Directory: frontend
Build Command: npm install --include=optional && npm install --no-save @rollup/rollup-linux-x64-gnu@4.60.2 && npm run build
Publish Directory: dist
```

Add environment variable:

```text
VITE_API_BASE_URL=https://your-backend-url.onrender.com
```

For React Router routes, add this rewrite rule in Render Static Site settings:

```text
Source: /*
Destination: /index.html
Action: Rewrite
```

### Render Notes

- Render's free web services can sleep when inactive, so the first request after inactivity can be slow.
- This project uses SQLite for the course demo. On Render, SQLite data may reset after redeploys/restarts unless you attach persistent storage or migrate to a managed database.
- The standalone TCP socket server is not exposed as a public Render TCP service. The deployed frontend uses FastAPI routes, and those routes call the socket authentication logic internally.
- Never put real SMTP passwords in GitHub. Add them only in Render environment variables.






Backend health check URL:

```text
https://secureauth-api.onrender.com/health
```

