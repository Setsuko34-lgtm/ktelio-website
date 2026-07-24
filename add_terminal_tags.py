PATH = "ktelio-landing.html"

with open(PATH, encoding="utf-8") as f:
    content = f.read()

# route id -> terminal class + label
mapping = [
    ("route-delphi", "liosion", "Liosion terminal"),
    ("route-meteora", "liosion", "Liosion terminal"),
    ("route-nafplio", "kifissos", "Kifissos terminal"),
    ("route-olympia", "kifissos", "Kifissos terminal"),
    ("route-monemvasia", "kifissos", "Kifissos terminal"),
    ("route-ioannina-zagori", "liosion", "Liosion terminal (1st leg)"),
    ("route-galaxidi-itea", "liosion", "Liosion terminal"),
    ("route-thessaloniki", "kifissos", "Kifissos terminal"),
    ("route-patras", "kifissos", "Kifissos terminal"),
    ("route-larissa", "liosion", "Liosion terminal"),
    ("route-volos", "liosion", "Liosion terminal"),
    ("route-ioannina", "kifissos", "Kifissos terminal"),
    ("route-kalamata", "kifissos", "Kifissos terminal"),
    ("route-corinth", "kifissos", "Kifissos terminal"),
    ("route-tripoli", "kifissos", "Kifissos terminal"),
]

needle = '</span></div><span class="route-price">'

for route_id, cls, label in mapping:
    anchor = f'id="{route_id}">'
    pos = content.index(anchor)
    insert_at = content.index(needle, pos)
    tag_html = f'<span class="terminal-tag {cls}">{label}</span>'
    # insert tag_html right after the duration span's closing </span>, before the wrapper </div>
    split_point = insert_at + len('</span>')
    content = content[:split_point] + tag_html + content[split_point:]

with open(PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Inserted", len(mapping), "terminal tags.")
print("liosion count:", content.count('terminal-tag liosion'))
print("kifissos count:", content.count('terminal-tag kifissos'))
