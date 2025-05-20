# This script is used to set up a poetry.
pip install poetry
poetry init
poetry install

# Generate mock data using the schema ✅
poetry run ghost-you-be generate --schema schema.yml --count 10

# save data to local db SQLite
poetry run ghost-you-be generate --schema schema.yml --count 10 --db-url sqlite:///data.db --table users

# save data to db type SQL
poetry run ghost-you-be generate --schema schema.yml --count 10 --db-url mysql://user:password@localhost:3306/dbname --table users

# save data to db type NoSQL
poetry run ghost-you-be generate --schema schema.yml --count 10 --db-url mongodb://localhost:27017/dbname --table users

# create schema from api
poetry run ghost-you-be generate-schema --api-url https://api.example.com/users --output schema.yml

# run mock api
poetry run ghost-you-be mock-api --schema schema.yml --port 8000