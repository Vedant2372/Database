# models.py

import sqlite3

DB_PATH = "document_metadata.db"

def init_db():
    """
    Initialize the SQLite FTS5 database with 'documents' table.
    Fields:
        - filename: name of the file
        - path: full path to the file
        - extension: file extension
        - size: file size in bytes
        - indexed_on: timestamp when it was indexed
    """
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS documents USING fts5(
                filename,
                path,
                extension,
                size,
                indexed_on UNINDEXED
            );
        """)
        conn.commit()
