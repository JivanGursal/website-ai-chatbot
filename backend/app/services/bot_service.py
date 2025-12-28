def create_bot(bot_id, name, system_prompt, website_url):
    print("BOT CREATE:", bot_id)

    website_content = crawl_website(website_url)

    final_prompt = f"""
{system_prompt}

Use ONLY the information below to answer user questions.
If the answer is not found, politely ask the user to leave contact details.

WEBSITE CONTENT:
{website_content}
"""

    cursor.execute(
        "INSERT OR REPLACE INTO bots VALUES (?, ?, ?, ?)",
        (bot_id, name, final_prompt, website_url)
    )
    conn.commit()

    print("BOT SAVED SUCCESSFULLY")

def get_bot(bot_id: str):
    cursor.execute(
        "SELECT bot_id, name, system_prompt, website_url FROM bots WHERE bot_id = ?",
        (bot_id,)
    )
    row = cursor.fetchone()

    if not row:
        return None

    return {
        "bot_id": row[0],
        "name": row[1],
        "system_prompt": row[2],
        "website_url": row[3]
    }
