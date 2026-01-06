# President Flashcards

A simple Dockerized Python web application that quizzes you on US Presidents.

## Features

- Randomly selects a US President.
- Asks one of three types of questions:
  - What number president were they?
  - What years were they president?
  - Which president oversaw a specific legislation/act?
- Multiple choice format.
- Data stored in a SQLite database.

## Running Version

Link: https://chuck.rocks/president-flash

## Running with Docker

1. Build the image:
   ```bash
   docker build -t president-flash .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 president-flash
   ```

3. Open your browser to `http://localhost:8000`.

## Development

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Initialize the database:
   ```bash
   uv run python src/init_db.py
   ```

3. Run the server:
   ```bash
   uv run uvicorn src.main:app --reload
   ```
