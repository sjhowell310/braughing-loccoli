#!/usr/bin/env bash
set -e

echo "🚀 Starting backend (FastAPI + Uvicorn)..."
python3 --version
uv run python --version
cd backend
uv venv
uv sync

source .venv/bin/activate
uv run uvicorn app.main:app --host 0.0.0.0 --port 9002 --reload &

echo "🌐 Starting frontend (Vite)..."
cd ../frontend
npm run dev -- --host 0.0.0.0

wait
