import sqlite3
from dataclasses import dataclass


@dataclass
class TodoItem:
    id: int
    title: str
    description: str
    completed: bool


def get_connection(db_path: str = "todo.db") -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(conn: sqlite3.Connection) -> None:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS todo_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0
        )
    """)
    conn.commit()


def create_todo(conn: sqlite3.Connection, title: str, description: str) -> TodoItem:
    cur = conn.execute(
        "INSERT INTO todo_items(title, description, completed) VALUES (?, ?, 0)",
        (title, description),
    )
    conn.commit()
    return TodoItem(
        id=cur.lastrowid, title=title, description=description, completed=False
    )


def get_all_todos(conn: sqlite3.Connection) -> list[TodoItem]:
    rows = conn.execute(
        "SELECT id, title, description, completed FROM todo_items"
    ).fetchall()
    return [
        TodoItem(int(r["id"]), r["title"], r["description"], bool(r["completed"]))
        for r in rows
    ]


def mark_completed(conn: sqlite3.Connection, todo_id: int) -> None:
    conn.execute("UPDATE todo_items SET completed = 1 WHERE id = ?", (todo_id,))
    conn.commit()


def delete_todo(conn: sqlite3.Connection, todo_id: int) -> None:
    conn.execute("DELETE FROM todo_items WHERE id = ?", (todo_id,))
    conn.commit()
