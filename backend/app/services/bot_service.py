import sqlite3

DB_PATH = "bots.db"

def create_bot(bot_id, name, system_prompt, website_url):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bots (
            bot_id TEXT PRIMARY KEY,
            name TEXT,
            system_prompt TEXT,
            website_url TEXT
        )
    """)

    cursor.execute(
        "INSERT OR REPLACE INTO bots VALUES (?, ?, ?, ?)",
        (bot_id, name, system_prompt, website_url)
    )

    conn.commit()
    conn.close()

    print("BOT SAVED:", bot_id)


# ✅ THIS FUNCTION MUST EXIST
def get_bot(bot_id: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT bot_id, name, system_prompt, website_url FROM bots WHERE bot_id = ?",
        (bot_id,)
    )

    row = cursor.fetchone()
    conn.close()

    if not row:
        return None

    return {
        "bot_id": row[0],
        "name": row[1],
        "system_prompt": row[2],
        "website_url": row[3],
    }
