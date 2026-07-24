PATH = "ktelio-landing.html"

with open(PATH, encoding="utf-8") as f:
    content = f.read()

# route_id -> (old_google_href, new_real_href, old_caption_html, new_caption_html)
entries = [
    (
        "route-olympia",
        "https://www.google.com/search?q=Athens%20%E2%86%92%20Olympia%20KTEL%20bus%20tickets%20book%20online",
        "https://online.ktelileias.gr/gr/",
        '<span class="cap-muted">Opens a search — not mapped yet</span>',
        '<span class="cap-good">Official site</span>',
    ),
    (
        "route-monemvasia",
        "https://www.google.com/search?q=Athens%20%E2%86%92%20Monemvasia%20KTEL%20bus%20tickets%20book%20online",
        "https://ktelbus.gr/lak/ticketweb/",
        '<span class="cap-muted">Opens a search — not mapped yet</span>',
        '<span class="cap-good">Official site</span>',
    ),
    (
        "route-ioannina-zagori",
        "https://www.google.com/search?q=Athens%20%E2%86%92%20Kalambaka%20%E2%86%92%20Ioannina%20KTEL%20bus%20tickets",
        "https://eticket.ktelioannina.gr/#!/dashboard/overview/search",
        '<span class="cap-muted">Two tickets — or we can route you direct instead</span>',
        '<span class="cap-good">Official site (2nd leg)</span>',
    ),
    (
        "route-larissa",
        "https://www.google.com/search?q=Athens%20%E2%86%92%20Larissa%20KTEL%20bus%20tickets%20book%20online",
        "https://ktellarisas.e-ticketing.gr/Pages/Destinations.aspx",
        '<span class="cap-muted">Opens a search — not mapped yet</span>',
        '<span class="cap-good">Official site</span>',
    ),
    (
        "route-volos",
        "https://www.google.com/search?q=Athens%20%E2%86%92%20Volos%20KTEL%20bus%20tickets%20book%20online",
        "https://ktelvolou.e-ticketing.gr/Pages/Destinations.aspx",
        '<span class="cap-muted">Opens a search — not mapped yet</span>',
        '<span class="cap-good">Official site</span>',
    ),
    (
        "route-kalamata",
        "https://www.google.com/search?q=Athens%20%E2%86%92%20Kalamata%20KTEL%20bus%20tickets%20book%20online",
        "https://ktelbus.gr/mes/ticketweb/",
        '<span class="cap-muted">Opens a search — not mapped yet</span>',
        '<span class="cap-good">Official site</span>',
    ),
    (
        "route-thess-larissa",
        "https://www.google.com/search?q=Thessaloniki%20%E2%86%92%20Larissa%20KTEL%20bus%20tickets%20book%20online",
        "https://ktellarisas.e-ticketing.gr/Pages/Destinations.aspx",
        '<span class="cap-muted">Opens a search — not mapped yet</span>',
        '<span class="cap-good">Official site</span>',
    ),
    (
        "route-thess-kavala",
        "https://www.google.com/search?q=Thessaloniki%20%E2%86%92%20Kavala%20KTEL%20bus%20tickets%20book%20online",
        "https://ktelbus.gr/kav/ticketweb/",
        '<span class="cap-muted">Opens a search — not mapped yet</span>',
        '<span class="cap-good">Official site</span>',
    ),
    (
        "route-corinth",
        "https://www.google.com/search?q=Athens%20%E2%86%92%20Corinth%20KTEL%20bus%20tickets%20book%20online",
        "https://ktelbus.gr/kor/ticketweb/",
        '<span class="cap-muted">Opens a search — not mapped yet</span>',
        '<span class="cap-good">Official site</span>',
    ),
    (
        "route-tripoli",
        "https://www.google.com/search?q=Athens%20%E2%86%92%20Tripoli%20KTEL%20bus%20tickets%20book%20online",
        "https://ktelbus.gr/ark/ticketweb/",
        '<span class="cap-muted">Opens a search — not mapped yet</span>',
        '<span class="cap-good">Official site</span>',
    ),
]

count = 0
for route_id, old_href, new_href, old_caption, new_caption in entries:
    anchor = f'id="{route_id}">'
    pos = content.index(anchor)
    end = content.index('</div>\n      </div>', pos)  # end of this card, loose upper bound
    card_slice = content[pos:end]

    # 1. swap href
    assert old_href in card_slice, f"href not found for {route_id}"
    new_card = card_slice.replace(old_href, new_href, 1)
    # 2. swap button label
    assert "Search official tickets" in new_card, f"label not found for {route_id}"
    new_card = new_card.replace("Search official tickets", "Book it yourself", 1)
    # 3. swap caption
    assert old_caption in new_card, f"caption not found for {route_id}"
    new_card = new_card.replace(old_caption, new_caption, 1)

    content = content[:pos] + new_card + content[end:]
    count += 1

with open(PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated", count, "routes.")
print('Remaining "Search official tickets":', content.count("Search official tickets"))
print('Remaining google.com search hrefs:', content.count("google.com/search"))
