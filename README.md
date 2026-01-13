
# Configuration Management for GCP Cloud Functions

This project demonstrates **configuration management patterns** for GCP Cloud Functions using:

- Environment variables (12-factor style config)
- A parameter manager abstraction (see `app/services/parameter_manager.py`)
- A secret manager abstraction (see `app/services/secret_manager.py`)

The function entrypoint is implemented using the Python Functions Framework with a CloudEvent trigger.

## Local setup

1) Create a `.env` file (do not commit it):

```bash
APP_DEBUG=true
SECRET_KEY=local-dev-secret
DATABASE_URL=postgres://user:pass@localhost:5432/db
```

2) Install deps:

```bash
python -m pip install -r requirements.txt
```

3) Run the Functions Framework locally:

```bash
functions-framework --target main --signature-type cloudevent --port 8080
```

If your shell can’t find `functions-framework`, run it via Python instead:

```bash
python -m functions_framework --target main --signature-type cloudevent --port 8080
```

Notes on the command:

- `--target` must be the Python function name (here: `main`), not the filename.
- Don’t include a trailing `--` at the end of the command.

4) Send a sample CloudEvent:

```bash
curl -X POST http://localhost:8080 \
	-H 'Content-Type: application/cloudevents+json' \
	-d '{
		"specversion": "1.0",
		"type": "com.example.test",
		"source": "local",
		"id": "1",
		"time": "2026-01-13T00:00:00Z",
		"data": {"hello": "world"}
	}'
```

## Notes

- `.env` is loaded for local development via `python-dotenv`.
- The current handler prints `SECRET_KEY` to logs (fine for demos, unsafe for real apps).
