#!/usr/bin/env bash
# Start the portfolio site locally. Usage: ./run.sh [port]
set -euo pipefail

cd "$(dirname "$0")"
PORT="${1:-8501}"

if [ ! -d .venv ]; then
  echo "Creating virtual environment..."
  python3 -m venv .venv
fi
source .venv/bin/activate

# Reinstall only when requirements.txt has changed since the last install.
if [ ! -f .venv/.installed ] || [ requirements.txt -nt .venv/.installed ]; then
  echo "Installing dependencies..."
  pip install -q --upgrade pip
  pip install -q -r requirements.txt
  touch .venv/.installed
fi

echo "Starting site at http://localhost:$PORT  (Ctrl+C to stop)"
streamlit run app.py --server.port "$PORT"
