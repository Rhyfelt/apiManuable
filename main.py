from server import app, start_server
from routes import shipments

app.include_router(shipments.router)

start_server()