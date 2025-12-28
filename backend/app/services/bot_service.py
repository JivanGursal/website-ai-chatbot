from app.db.database import cursor, conn
from app.services.crawler_service import crawl_website

# 🔹 BOT CREATE + AUTO TRAIN
def create_bot(bot_id: str, name: str, system_prompt: str, website_url: str):
    website_content = crawl_website(website_url)

    final_prompt = f"""
{system_prompt}

Use ONLY the information below to answer user questions.
If the answer is not found, politely ask the user to leave contact details.

WEBSITE CONTENT:
{website_content}
"""

    cursor.execute(
        """
        INSERT INTO bots (id, name, system_prompt, website_url)
        VALUES (?, ?, ?, ?)
        """,
        (bot_id, name, final_prompt, website_url)
    )
    conn.commit()


# 🔹 BOT FETCH (THIS WAS MISSING ❗)
def get_bot(bot_id: str):
    cursor.execute(
        "SELECT system_prompt FROM bots WHERE id = ?",
        (bot_id,)
    )
    row = cursor.fetchone()
    return row[0] if row else None
