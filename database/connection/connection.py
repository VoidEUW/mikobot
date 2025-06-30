def connect_database():
    """Connect to the SQLite database."""
    import sqlite3
    from config import PATH_DATABASE

    db = sqlite3.connect(PATH_DATABASE)
    db.row_factory = sqlite3.Row
    return db
