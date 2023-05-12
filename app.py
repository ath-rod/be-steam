from flask import Flask
from flask_cors import CORS

# locals
from config import env

# Initialize database connection
import database.connection

# Resources
from resources.users import resourse as users_api

# Initialize application
app = Flask(__name__)
app.secret_key = env.SESSION_SECRET

# Uncomment below statement to
# bypass browser CORS errors.
# CORS(app)

# Enable APIs
app.register_blueprint(users_api, url_prefix="/users")

if __name__ == "__main__":
    app.run(host=env.HOST, port=env.PORT, debug=True)
