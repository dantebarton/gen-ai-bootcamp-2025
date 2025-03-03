#!/usr/bin/env python

from app import app

if __name__ == "__main__":
    print("Initializing database...")
    app.db.init(app)
    print("Database initialization complete. All tables have been created.")

