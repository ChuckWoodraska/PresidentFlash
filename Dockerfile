FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
COPY src/ src/
COPY templates/ templates/

RUN pip install .

# Initialize the database during build
RUN python src/init_db.py

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
