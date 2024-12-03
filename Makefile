# Define the default target
.DEFAULT_GOAL := help

# Display help information
help:
	@echo "Available make targets:"
	@echo "  db-start         - Start the database container"
	@echo "  db-migrate       - Run database migrations"
	@echo "  build-api        - Build the Flask API Docker image"
	@echo "  start-api        - Start the Flask API container"
	@echo "  clean            - Stop and clean up all containers"

# Target to start the database container
db-start:
	@echo "Starting the database container..."
	@docker-compose up -d db

# Target to run database migrations
db-migrate:
	@echo "Applying database migrations..."
	# Ensure API container is running
	@docker-compose up -d api
	# Initialize migrations folder if not already created
	@docker-compose exec api flask db init || echo "Migrations folder already exists, skipping init."
	# Generate migration scripts if changes are detected
	@docker-compose exec api flask db migrate -m "DB Migration via Makefile" || echo "No changes detected, skipping migrate."
	# Apply migrations to the database
	@docker-compose exec api flask db upgrade

# Target to build the Flask API Docker image
build-api:
	@echo "Building the Flask API Docker image..."
	@docker-compose build api

# Target to start the API container (ensures DB is up and migrations are applied)
start-api:
	@echo "Starting the API container..."
	# Start DB container if not running
	$(MAKE) db-start
	# Run DB migrations
	$(MAKE) db-migrate
	# Start API container
	@docker-compose up -d api

# Clean up all running containers
clean:
	@echo "Stopping and removing all containers..."
	@docker-compose down

# Ensure prerequisites are installed (optional, add as needed)
prerequisites:
	@echo "Checking prerequisites..."
	@command -v docker >/dev/null 2>&1 || { echo >&2 "Docker is not installed. Please install Docker."; exit 1; }
	@command -v docker-compose >/dev/null 2>&1 || { echo >&2 "Docker Compose is not installed. Please install Docker Compose."; exit 1; }
	@command -v make >/dev/null 2>&1 || { echo >&2 "Make is not installed. Please install Make."; exit 1; }
