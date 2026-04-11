FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./
COPY src ./src

RUN uv sync --frozen

ENV PYTHONPATH=/app/src

CMD ["uv", "run", "src/app.py"]