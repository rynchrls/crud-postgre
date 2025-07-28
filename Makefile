run:
	uvicorn app.main:app --host localhost --port 5000 --reload

# start-prod:
# 	uvicorn app.main:app --host=0.0.0.0 --port=8000

# test:
# 	pytest -v --cov=app

# lint:
# 	ruff app

# format:
# 	black app

# migrate:
# 	alembic upgrade head

# makemigration:
# 	alembic revision --autogenerate -m "new migration"

# worker:
# 	celery -A app.workers.tasks worker --loglevel=info
