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
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
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
