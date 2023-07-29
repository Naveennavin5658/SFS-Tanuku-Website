from flask import Flask

app = Flask(__name__)

# Load the configuration based on the environment
app.config.from_object('config.development')  # Change to 'config.production' for production

# Initialize extensions (if any) here

from app import routes
