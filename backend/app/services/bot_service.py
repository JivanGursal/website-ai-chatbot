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
