def get_tone_prompt(tone, email_text):
    return f"""
You are an expert in rewriting professional emails.

Here is the draft email:
{email_text}

Rewrite this email in a {tone.lower()} tone. Keep it professional and polite. The message should be clear and the tone should reflect the chosen style.

Output only the rewritten email.
"""