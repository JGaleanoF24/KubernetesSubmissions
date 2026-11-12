# Log output

Generates a random string (UUID) on startup, keeps it in memory, and prints it with a UTC timestamp every 5 seconds.

```
2026-11-12T14:05:01.123Z: 8523ecb1-c716-4cb6-a044-b9e83bb98e43
2026-11-12T14:05:06.128Z: 8523ecb1-c716-4cb6-a044-b9e83bb98e43
```

## Run locally

```sh
python3 app.py
```

## Run with Docker

```sh
docker build -t log-output .
docker run --rm log-output
```
