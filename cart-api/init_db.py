from apps.models import Cart

from apps import create_app
from apps.db import db

app = create_app()
app.app_context().push()

db.create_all()