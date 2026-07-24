import re

PATH = "ktelio-landing.html"

with open(PATH, encoding="utf-8") as f:
    content = f.read()

start_marker = '<section id="routes">'
start = content.index(start_marker)
end_marker = "\n</section>\n"
end = content.index(end_marker, start) + len(end_marker)
old_block = content[start:end]

new_block = '''<section id="routes">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">20 routes and counting</span>
      <h2>Explore the routes</h2>
      <p>Ten scenic trips to Greece's top destinations, and ten high-volume domestic connections. Prices shown are estimates — the exact fare is confirmed when you book.</p>
    </div>
    <div class="tabs" role="tablist" aria-label="Route categories">
      <button class="tab-btn active" data-tab="tourist" role="tab" aria-selected="true" aria-controls="tourist" id="tab-tourist">Tourist destinations</button>
      <button class="tab-btn" data-tab="intercity" role="tab" aria-selected="false" aria-controls="intercity" id="tab-intercity">Major intercity</button>
    </div>

    <div class="route-panel active" id="tourist" role="tabpanel" aria-labelledby="tab-tourist">
      <div class="route-card reveal" id="route-delphi">
        <div class="route-top"><div><h4>Athens → Delphi</h4><span>~3h · Sacred oracle site</span></div><span class="route-price">from €15</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://www.ktel-fokidas.gr/en/delphi" target="_blank" rel="noopener">Book it yourself</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-good">Official site</span><span class="cap-good">We book it for you</span></div>
      </div>
      <div class="route-card reveal" id="route-meteora">
        <div class="route-top"><div><h4>Athens → Meteora (Kalambaka)</h4><span>~5h · Via Trikala, cliff-top monasteries</span></div><span class="route-price">from €29</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://ktel-trikala.gr/en/direct-itinerary-from-athens-to-kalambaka-meteora/" target="_blank" rel="noopener">Book it yourself</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-good">Official site</span><span class="cap-good">We book it for you</span></div>
      </div>
      <div class="route-card reveal" id="route-meteora-thess">
        <div class="route-top"><div><h4>Thessaloniki → Meteora (Kalambaka)</h4><span>~3h · Closer than from Athens</span></div><span class="route-price">from €21</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://ktel-trikala.gr/en/bus-to-meteora/" target="_blank" rel="noopener">Book it yourself</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-good">Official site</span><span class="cap-good">We book it for you</span></div>
      </div>
      <div class="route-card reveal" id="route-nafplio">
        <div class="route-top"><div><h4>Athens → Nafplio</h4><span>~2h15m · Greece's first capital</span></div><span class="route-price">from €13</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://www.ktelargolida.gr/en/athina-isthmos-fichti-mikines-argos-nafplio/" target="_blank" rel="noopener">Book it yourself</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-good">Official site</span><span class="cap-good">We book it for you</span></div>
      </div>
      <div class="route-card reveal" id="route-olympia">
        <div class="route-top"><div><h4>Athens → Olympia</h4><span>~5h · Via Pyrgos, birthplace of the Olympics</span></div><span class="route-price">from €30</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://www.google.com/search?q=Athens%20%E2%86%92%20Olympia%20KTEL%20bus%20tickets%20book%20online" target="_blank" rel="noopener">Search official tickets</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-muted">Opens a search — not mapped yet</span><span class="cap-good">We book it for you</span></div>
      </div>
      <div class="route-card reveal" id="route-monemvasia">
        <div class="route-top"><div><h4>Athens → Monemvasia</h4><span>~5h45m · Medieval castle town, via Sparti</span></div><span class="route-price">from €30</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://www.google.com/search?q=Athens%20%E2%86%92%20Monemvasia%20KTEL%20bus%20tickets%20book%20online" target="_blank" rel="noopener">Search official tickets</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-muted">Opens a search — not mapped yet</span><span class="cap-good">We book it for you</span></div>
      </div>
      <div class="route-card reveal" id="route-ioannina-zagori">
        <div class="route-top"><div><h4>Athens → Ioannina</h4><span>Via Kalambaka · Gateway to Zagorochoria</span></div><span class="route-price">2-leg trip</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://www.google.com/search?q=Athens%20%E2%86%92%20Kalambaka%20%E2%86%92%20Ioannina%20KTEL%20bus%20tickets" target="_blank" rel="noopener">Search official tickets</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-muted">Two tickets — or we can route you direct instead</span><span class="cap-good">We book it for you</span></div>
      </div>
      <div class="route-card reveal" id="route-ouranoupoli">
        <div class="route-top"><div><h4>Thessaloniki → Ouranoupoli</h4><span>~2h15m · Halkidiki &amp; Mount Athos gateway</span></div><span class="route-price">from €12</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://ktel-chalkidikis.gr/en/" target="_blank" rel="noopener">Book it yourself</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-good">Official site</span><span class="cap-good">We book it for you</span></div>
      </div>
      <div class="route-card reveal" id="route-galaxidi-itea">
        <div class="route-top"><div><h4>Athens → Galaxidi / Itea</h4><span>~2.5–3.5h · Seaside towns near Delphi</span></div><span class="route-price">from €17</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://www.ktel-fokidas.gr/en/itea" target="_blank" rel="noopener">Book it yourself</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-good">Official site</span><span class="cap-good">We book it for you</span></div>
      </div>
      <div class="route-card reveal" id="route-patras-olympia">
        <div class="route-top"><div><h4>Patras → Olympia</h4><span>~3h · Via Pyrgos, for ferry arrivals from Italy</span></div><span class="route-price">from €10</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://www.ktelachaias.gr/en/δρομολόγια-2/patra-pyrgos-patra/" target="_blank" rel="noopener">Book it yourself</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-good">Official site</span><span class="cap-good">We book it for you</span></div>
      </div>
    </div>

    <div class="route-panel" id="intercity" role="tabpanel" aria-labelledby="tab-intercity">
      <div class="route-card reveal" id="route-thessaloniki">
        <div class="route-top"><div><h4>Athens → Thessaloniki</h4><span>~5.5h · Direct intercity</span></div><span class="route-price">from €40</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://ktelthes.gr/en/routes-athens-pireaus-thessaloniki/" target="_blank" rel="noopener">Book it yourself</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-good">Official site</span><span class="cap-good">We book it for you</span></div>
      </div>
      <div class="route-card reveal" id="route-patras">
        <div class="route-top"><div><h4>Athens → Patras</h4><span>~3h · Ferry connections</span></div><span class="route-price">from €22</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://www.ktelachaias.gr/en/" target="_blank" rel="noopener">Book it yourself</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-good">Official site</span><span class="cap-good">We book it for you</span></div>
      </div>
      <div class="route-card reveal" id="route-larissa">
        <div class="route-top"><div><h4>Athens → Larissa</h4><span>~4h · Central Greece hub</span></div><span class="route-price">from €30</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://www.google.com/search?q=Athens%20%E2%86%92%20Larissa%20KTEL%20bus%20tickets%20book%20online" target="_blank" rel="noopener">Search official tickets</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-muted">Opens a search — not mapped yet</span><span class="cap-good">We book it for you</span></div>
      </div>
      <div class="route-card reveal" id="route-volos">
        <div class="route-top"><div><h4>Athens → Volos</h4><span>~4h · Gateway to Pelion</span></div><span class="route-price">from €26</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://www.google.com/search?q=Athens%20%E2%86%92%20Volos%20KTEL%20bus%20tickets%20book%20online" target="_blank" rel="noopener">Search official tickets</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-muted">Opens a search — not mapped yet</span><span class="cap-good">We book it for you</span></div>
      </div>
      <div class="route-card reveal" id="route-ioannina">
        <div class="route-top"><div><h4>Athens → Ioannina</h4><span>~5.5h · Direct intercity</span></div><span class="route-price">from €35</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://ktelioannina.gr/en/" target="_blank" rel="noopener">Book it yourself</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-good">Official site</span><span class="cap-good">We book it for you</span></div>
      </div>
      <div class="route-card reveal" id="route-kalamata">
        <div class="route-top"><div><h4>Athens → Kalamata</h4><span>~3h15m · Southern Peloponnese</span></div><span class="route-price">from €20</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://www.google.com/search?q=Athens%20%E2%86%92%20Kalamata%20KTEL%20bus%20tickets%20book%20online" target="_blank" rel="noopener">Search official tickets</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-muted">Opens a search — not mapped yet</span><span class="cap-good">We book it for you</span></div>
      </div>
      <div class="route-card reveal" id="route-thess-larissa">
        <div class="route-top"><div><h4>Thessaloniki → Larissa</h4><span>~2.5h · Central Greece connector</span></div><span class="route-price">from €11</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://www.google.com/search?q=Thessaloniki%20%E2%86%92%20Larissa%20KTEL%20bus%20tickets%20book%20online" target="_blank" rel="noopener">Search official tickets</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-muted">Opens a search — not mapped yet</span><span class="cap-good">We book it for you</span></div>
      </div>
      <div class="route-card reveal" id="route-thess-kavala">
        <div class="route-top"><div><h4>Thessaloniki → Kavala</h4><span>~2h20m · Northern coast</span></div><span class="route-price">from €16</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://www.google.com/search?q=Thessaloniki%20%E2%86%92%20Kavala%20KTEL%20bus%20tickets%20book%20online" target="_blank" rel="noopener">Search official tickets</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-muted">Opens a search — not mapped yet</span><span class="cap-good">We book it for you</span></div>
      </div>
      <div class="route-card reveal" id="route-corinth">
        <div class="route-top"><div><h4>Athens → Corinth</h4><span>~1h · Canal &amp; ancient site</span></div><span class="route-price">from €9</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://www.google.com/search?q=Athens%20%E2%86%92%20Corinth%20KTEL%20bus%20tickets%20book%20online" target="_blank" rel="noopener">Search official tickets</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-muted">Opens a search — not mapped yet</span><span class="cap-good">We book it for you</span></div>
      </div>
      <div class="route-card reveal" id="route-tripoli">
        <div class="route-top"><div><h4>Athens → Tripoli</h4><span>~3h15m · Gateway to Arcadia</span></div><span class="route-price">from €16</span></div>
        <div class="route-actions"><a class="btn-sm free-link" href="https://www.google.com/search?q=Athens%20%E2%86%92%20Tripoli%20KTEL%20bus%20tickets%20book%20online" target="_blank" rel="noopener">Search official tickets</a><a class="btn-sm paid-link open-request" href="#request">Let us handle it — €5</a></div>
        <div class="link-caption"><span class="cap-muted">Opens a search — not mapped yet</span><span class="cap-good">We book it for you</span></div>
      </div>
    </div>

    <div class="route-callout reveal">
      <p>Don't see your destination? <a href="#request" id="routeNotListed">Tell us where you're going</a> — we're adding routes based on real requests, not guesses.</p>
    </div>
  </div>
</section>
'''

assert old_block.count('route-card reveal') == 23, f"expected 23 old cards, found {old_block.count('route-card reveal')}"
assert new_block.count('route-card reveal') == 20, f"expected 20 new cards, found {new_block.count('route-card reveal')}"

content = content[:start] + new_block + content[end:]

with open(PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Routes section replaced successfully.")
print("New card count:", new_block.count('route-card reveal'))
