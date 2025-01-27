import re


def create_drug_info_card():
    info_card = f"""<a href="{{search_url}}"><b>{{drug_name}}</b></a>

🔭 <b>Class</b>
- ✴️ <b>Chemical:</b> ➡️ {{chemical_class}}
- ✴️ <b>Psychoactive:</b> ➡️ {{psychoactive_class}}

⚖️ <b>Dosages</b>
{{dosage_info}}

⏱️ <b>Duration</b>
{{duration_info}}

⚠️ <b>Addiction Potential</b> ⚠️
{{addiction_potential}}

🚫 <b>Interactions</b> 🚫
{{interactions_info}}

<b>Notes</b>
{{notes}}

🧠 <b>Subjective Effects</b>
{{subjective_effects}}

📈 <b>Tolerance</b>
{{tolerance_info}}

🕒 <b>Half-life</b>
{{half_life_info}}
"""
    return info_card


def format_message(input_string):
    formatted_string = input_string.replace("```html", "").replace("```", "")

    return formatted_string


def escape_markdown_v2(text):
    escape_chars = r"_*[]()~`>#\+=-|{}.!"
    return "".join("\\" + char if char in escape_chars else char for char in text)


def sanitize_html(html):
    allowed_tags = ["a", "b", "i", "code", "pre"]
    sanitized_html = re.sub(
        r"<(?!/?({})\b)[^>]*>".format("|".join(allowed_tags)), "", html
    )
    return sanitized_html


def convert_to_telegram_html(text):
    text = re.sub(r"## (.*)", r"<b>\1</b>", text)
    text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"__(.*?)__", r"<u>\1</u>", text)
    text = re.sub(r"\*(.*?)\*", r"<i>\1</i>", text)
    text = re.sub(r"_(.*?)_", r"<i>\1</i>", text)
    text = re.sub(r"\+\+(.*?)\+\+", r"<u>\1</u>", text)
    text = re.sub(r"~~(.*?)~~", r"<s>\1</s>", text)
    text = re.sub(r"\|\|(.*?)\|\|", r'<span class="tg-spoiler">\1</span>', text)
    text = re.sub(r"\[(.*?)\]\((http[s]?:\/\/.*?)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(
        r"\[(.*?)\]\(tg:\/\/user\?id=(\d+)\)", r'<a href="tg://user?id=\2">\1</a>', text
    )
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"```([^`]*)```", r"<pre>\1</pre>", text, flags=re.DOTALL)
    text = re.sub(r"^> (.*)", r"<blockquote>\1</blockquote>", text, flags=re.MULTILINE)

    return text
