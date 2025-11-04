#!/usr/bin/env bash
set -e

echo "🚧 Starting environment setup..."

ls

# --- Frontend ---
if [ -d "frontend/" ]; then
  echo "📦 Installing frontend dependencies..."
  cd frontend
  if [ -f "package.json" ]; then
    npm install
  else
    echo "⚠️  No package.json found in frontend/"
  fi
  cd 
else
  echo "⚠️  No frontend/ directory found — skipping frontend setup."
fi

# --- Backend ---
if [ -d "backend/" ]; then
  echo "🐍 Setting up backend dependencies..."
  cd backend

  if command -v uv &> /dev/null; then
    if [ -f "pyproject.toml" ]; then
      echo "🔧 Using uv to sync Python dependencies..."
      uv venv
      source .venv/bin/activate
      uv sync --active
    elif [ -f "requirements.txt" ]; then
      echo "📄 Installing dependencies from requirements.txt..."
      pip install -r requirements.txt
    else
      echo "⚠️  No pyproject.toml or requirements.txt found in backend/"
    fi
  else
    echo "⚠️  uv not found — falling back to pip."
    pip install fastapi uvicorn
  fi

  cd 
else
  echo "⚠️  No backend/ directory found — skipping backend setup."
fi

# --- Environment Summary ---
echo ""
echo "✅ Setup complete!"
echo "🧱 Node version: $(node -v)"
echo "🐍 Python version: $(python3 --version)"
echo "⚙️  uv version: $(uv --version || echo 'uv not found')"
echo ""
