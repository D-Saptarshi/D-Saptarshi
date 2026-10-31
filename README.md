# Saptarshi Das — Quantitative Analyst Portfolio

One-page portfolio site served by Streamlit: hero, about, selected work, journey, toolkit,
an interactive Options Lab (Black-Scholes + binomial pricing with Greeks) and contact.

## Run locally

```bash
./run.sh          # http://localhost:8501
```

## Deploy to Streamlit Community Cloud

1. Push this folder to a **public GitHub repo** (e.g. `saptarshi-portfolio`).
2. Go to <https://share.streamlit.io> → **Create app** → pick the repo, branch `main`, main file `app.py`.
3. Under **Advanced settings**, choose Python 3.12, and set a custom subdomain such as
   `saptarshi-das.streamlit.app`.
4. Deploy. Every `git push` redeploys automatically.

## Structure

| File | Purpose |
|---|---|
| `app.py` | Page content and Options Lab |
| `style.css` | All visual design |
| `quant.py` | Black-Scholes and binomial pricing (numpy only) |
| `.streamlit/config.toml` | Theme and static file serving |
| `static/Saptarshi_Das_CV.pdf` | Downloadable CV — replace to update |
# D-Saptarshi
# D-Saptarshi
