# 🚀 CampusConnect Deployment Guide

## Phase 1: Database Setup (Neon)
1. Go to [neon.tech](https://neon.tech) and create account
2. Create new project: `campusconnect-db`
3. Copy connection string from Dashboard
4. Save as `DATABASE_URL` in backend environment

## Phase 2: Backend (Render)
1. Go to [render.com](https://render.com)
2. Connect your GitHub repository
3. Create new Web Service
4. Use these settings:
   - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Start Command: `gunicorn core.wsgi:application`
5. Add all environment variables from `.env.example`

## Phase 3: Storage (Cloudflare R2)
1. Create Cloudflare account
2. Go to R2 Storage and create bucket: `campusconnect-media`
3. Generate API tokens with read/write permissions
4. Configure public domain for the bucket

## Phase 4: Frontend (Vercel)
1. Go to [vercel.com](https://vercel.com)
2. Import GitHub repository
3. Set root directory to `frontend/`
4. Add environment variables from `.env.local.example`

## Environment Variables Needed:

### Backend (.env)
```env
SECRET_KEY=generate-a-secure-key
DEBUG=False
DATABASE_URL=neon-connection-string
R2_ACCOUNT_ID=your-account-id
R2_ACCESS_KEY_ID=your-access-key
R2_SECRET_ACCESS_KEY=your-secret-key
R2_BUCKET_NAME=campusconnect-media
R2_PUBLIC_URL=your-public-url
