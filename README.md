# Modular API

### Description

// Put some content here

### Scaffolding

**API specific**:

- `/dao`, which refers to _Database Access Object_ contains the low-level logic of the
  backend application handling the database queries accordingly.
- `/services`, are modules meant to be implemented accros the application and handles
  the business logic of the applciations sometimes consuming the _database access object_.
- `/resources`, modules that handle the incoming data from HTTP Requests. These modules
  implement the necessary logic to guarantee that incoming data is healthy and delegates
  data handling to services.
- `/utils`, app logic-independent modules that may be consumed by services, resources or
  database access objects.
- `/tests`, contains the testing suite of the backend and its utilities.

### Set up and deployment

- Dockerized PostgreSQL database

      sudo apt update && sudo apt upgrade -y && \
      sudo apt install docker-ce docker-compose && \
      cd database && docker-compose up

- Virtual environment and dependencies

      python -m pip install virtualenv && \
      python -m virtualenv .env && \
      . .env/bin/activate && \
      python -m pip install -r requirements.txt

- Initialize server _(development)_

  Notice that this script will create the database,
  execute the migrations and initializes the Flask backend.

      ./build_dev.sh

- Initialize server _(production)_

      gunicorn app:app --bind 127.0.0.1:5000

- Running tests

  Similar the the command from above, is creates a test database,
  executes the necessary migrations and runs the testing suite.

      ./run_tests.sh

### Deploy API Reference

The deployment of the API Reference requires [Yarn](https://classic.yarnpkg.com/en/), which you can
install following [this documentation](https://classic.yarnpkg.com/lang/en/docs/install/#debian-stable).

```
./api_reference.sh

# or

cd docs && \
yarn install && \
npx @redocly/cli preview-docs api-reference.yaml && \
```

---

### Troubleshooting

- In case you run with issues while setting up `psycopg2`,
  run this command to make your machine compatible with
  the driver.

        sudo apt install postgresql libpq-dev

- In case any Frontend application fails to consume the API due to CORS errors,
  **uncomment the line 19** from `app.py`, i.e., enable the `CORS` module:

      ...

      # Initialize application
      app = Flask(__name__)
      app.secret_key = env.SESSION_SECRET

      # Uncomment below statement to
      # bypass browser CORS errors.
      CORS(app)
      ...
