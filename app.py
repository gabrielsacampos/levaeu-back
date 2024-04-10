from src.server.server import app
from src.models.database.settings.connection import connection_handler

if __name__ == '__main__':
    app.run(debug=True)