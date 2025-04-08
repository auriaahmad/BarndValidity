# School Support Services

A full-stack web application for managing school uniform orders and QR code-based product authentication.

## Project Structure

```
school-support-services/
├── frontend/           # Next.js frontend application
├── backend/           # FastAPI backend application
└── README.md
```

## Features

- Public-facing landing page with company information
- Admin dashboard for product management
- QR code generation and validation system
- Secure authentication system
- Bulk and individual order management

## Setup Instructions

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file with the following variables:
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/school_support
   SECRET_KEY=your_secret_key
   ```

5. Run database migrations:
   ```bash
   alembic upgrade head
   ```

6. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```

## Technology Stack

- Frontend: Next.js, React, Tailwind CSS
- Backend: FastAPI, PostgreSQL
- Authentication: JWT
- QR Code Generation: qrcode
- PDF Generation: reportlab
- Excel Generation: openpyxl

## API Documentation

Once the backend is running, visit `http://localhost:8000/docs` for the Swagger API documentation. 