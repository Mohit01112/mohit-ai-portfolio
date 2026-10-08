# Mohit Jadhav - Stark-Net 3D Portfolio (Flask)

## Run locally
    pip install -r requirements.txt
    python app.py        # http://localhost:5000

## Edit content
All content lives in `portfolio.json` (projects, links, phone, honors). Empty `live` = no Live button.
`"verified": false` links point to a GitHub repo search - replace with the exact repo/demo URLs.

## Deploy (Render / Railway / Heroku)
Push to GitHub -> New Web Service on Render -> it reads `render.yaml`.
Start command: `gunicorn app:app --bind 0.0.0.0:$PORT`. Health check: `/healthz`.
