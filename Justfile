# Install deps (uv sync)
install:
    uv sync

# Run in dev mode (python)
dev:
    uv run python src/app.py

# Build docker image
build:
    docker build -t finance-bot .

run:
    docker rm -f finance-bot || true
    docker run --rm --name finance-bot --env-file .env finance-bot

run-dev:
    docker rm -f finance-bot || true
    docker build -t finance-bot .
    docker run -d --name finance-bot --env-file .env finance-bot
    docker logs -f finance-bot


# View logs
logs:
    docker logs -f finance-bot

# Stop container
stop:
    docker stop finance-bot

# Remove container
clean:
    docker rm -f finance-bot || true

# Full reset
reset:
    just clean
    docker rmi finance-bot || true