# This script is used to set up a poetry.
pip install poetry
poetry init
poetry install

# Generate mock data using the schema ✅
poetry run ghost-your-be generate --schema schema.yml --count 10

# save data to local db SQLite
poetry run ghost-your-be generate --schema schema.yml --count 10 --db-url sqlite:///data.db --table users

# save data to db type SQL ✅
poetry run ghost-your-be generate --schema schema.yml --count 10 --db-url mysql://user:password@localhost:3306/dbname --table users

# save data to db type NoSQL
poetry run ghost-your-be generate --schema schema.yml --count 10 --db-url mongodb://localhost:27017/dbname --table users

# create schema from api
poetry run ghost-your-be generate-schema --api-url https://api.example.com/users --output schema.yml

# run mock api ✅
poetry run ghost-your-be mock-api --schema schema.yml --port 8000

# compare api
poetry run ghost-your-be compare --mock http://localhost:8000/mock/users --real https://api.example.com/users

# pro activate
poetry run ghost-your-be activate --key VALID_KEY_123

# packaging 
# python setup.py sdist bdist_wheel
# twine upload dist/*