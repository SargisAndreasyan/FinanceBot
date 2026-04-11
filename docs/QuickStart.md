

## ⚡ Install dependencies

```bash
uv sync
```



## ▶️ Run bot

```bash
python src/app.py
```

## 🐳 Docker (optional)

### Build image

```bash
docker build -t finance-bot .
```

### Run container

```bash
docker run --name finance-bot --env-file .env finance-bot
```
