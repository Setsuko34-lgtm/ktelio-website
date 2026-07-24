PATH = "ktelio-landing.html"

with open(PATH, encoding="utf-8") as f:
    content = f.read()

COPY_A = "Rather do a guided day trip than the bus?"
COPY_B_TEMPLATE = "{} See guided tour options"

# route_id -> (question text, url)
entries = [
    ("route-meteora-thess", COPY_A, "https://www.getyourguide.com/thessaloniki-l115/meteora-day-trip-t481628/"),
    ("route-nafplio", COPY_A, "https://www.getyourguide.com/nafplio-l7909/"),
    ("route-olympia", COPY_A, "https://www.getyourguide.com/athens-l91/one-day-tour-to-ancient-olympia-t454472/"),
    ("route-ioannina-zagori", "Exploring Zagorochoria once you're there?", "https://www.getyourguide.com/zagori-l146630/"),
    ("route-ouranoupoli", "Want to see Mount Athos from the water?", "https://www.getyourguide.com/ouranoupoli-l112587/cruises-boat-tours-tc48/"),
    ("route-galaxidi-itea", COPY_A, "https://www.getyourguide.com/galaxidi-l228789/"),
    ("route-patras-olympia", "Stopping in Patras for a while?", "https://www.getyourguide.com/patras-l122165/"),
    ("route-volos", "Exploring Pelion once you're in Volos?", "https://www.getyourguide.com/volos-l2545/"),
    ("route-ioannina", "Exploring Zagorochoria once you're there?", "https://www.getyourguide.com/zagori-l146630/"),
    ("route-kalamata", "Exploring the Mani once you're there?", "https://www.getyourguide.com/kalamata-l42432/"),
    ("route-thess-kavala", COPY_A, "https://www.getyourguide.com/thessaloniki-l115/day-trips-tc360/kavala-tl89351/"),
    ("route-corinth", COPY_A, "https://www.getyourguide.com/corinth-l118/"),
]

needle = '<div class="link-caption">'

count = 0
for route_id, question, url in entries:
    anchor = f'id="{route_id}">'
    pos = content.index(anchor)
    cap_start = content.index(needle, pos)
    # find end of this link-caption div (its own closing </div>)
    cap_end = content.index('</div>', cap_start) + len('</div>')
    tag_html = f'\n        <div class="route-alt">{question} <a href="{url}" target="_blank" rel="sponsored noopener">See tour options</a></div>'
    if question == COPY_A:
        tag_html = f'\n        <div class="route-alt">Rather do a guided day trip than the bus? <a href="{url}" target="_blank" rel="sponsored noopener">See tour options</a></div>'
    content = content[:cap_end] + tag_html + content[cap_end:]
    count += 1

with open(PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Inserted", count, "new tour links.")
print("Total route-alt divs now:", content.count('class="route-alt"'))
