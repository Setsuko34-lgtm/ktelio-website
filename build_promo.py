"""
Ktelio promo/advert image (v3) — back to the simple first-concept layout,
but with a proper laptop (keyboard deck + trackpad, not a tablet), and the
laptop screen redrawn to faithfully match the REAL hero section content
pulled straight from ktelio-landing.html (nav, badge, real H1, real buttons,
real stats, all 4 real "Popular right now" entries).

No headless browser is available in this sandbox (npm/pip/apt all blocked,
no chromium binary) so a literal screenshot of the live page isn't possible —
this hand-recreates the real copy/layout pixel-by-pixel instead.
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 1160

NAVY, NAVY_DARK = (13, 40, 71), (8, 26, 46)
BLUE, SKY = (28, 95, 168), (234, 242, 251)
GOLD, GOLD_DARK, GOLD_LIGHT = (216, 161, 58), (185, 133, 42), (232, 195, 128)
INK, MUTED, WHITE, LINE = (28, 37, 48), (92, 107, 122), (255, 255, 255), (226, 232, 239)
LIVE_GREEN = (63, 191, 111)

F_SERIF_B  = "/usr/share/fonts/truetype/liberation2/LiberationSerif-Bold.ttf"
F_SERIF_BI = "/usr/share/fonts/truetype/liberation2/LiberationSerif-BoldItalic.ttf"
F_SANS_B   = "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf"
F_SANS_R   = "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def text_w(d, text, fnt):
    b = d.textbbox((0, 0), text, font=fnt)
    return b[2] - b[0]

def center_text(d, cy, text, fnt, fill, cx=W // 2):
    b = d.textbbox((0, 0), text, font=fnt)
    tw, th = b[2] - b[0], b[3] - b[1]
    d.text((cx - tw / 2 - b[0], cy - th / 2 - b[1]), text, font=fnt, fill=fill)
    return tw

def rounded_shadow(size, radius, blur, alpha=110):
    w, h = size
    pad = blur * 3
    layer = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    ld.rounded_rectangle([pad, pad, pad + w, pad + h], radius=radius, fill=(0, 0, 0, alpha))
    return layer.filter(ImageFilter.GaussianBlur(blur)), pad

# ---------- background ----------
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
t = np.clip((xx / W) * 0.35 + (yy / H) * 0.65, 0, 1)
bg = np.empty((H, W, 3), dtype=np.float32)
for c in range(3):
    bg[:, :, c] = NAVY[c] * (1 - t) + NAVY_DARK[c] * t
gx, gy = W * 0.18, H * 0.08
dist = np.sqrt((xx - gx) ** 2 + ((yy - gy) * 1.15) ** 2)
glow = np.clip(1 - dist / (W * 0.55), 0, 1) ** 2 * 0.35
for c in range(3):
    bg[:, :, c] = bg[:, :, c] * (1 - glow) + GOLD[c] * glow
canvas = Image.fromarray(np.clip(bg, 0, 255).astype(np.uint8), "RGB").convert("RGBA")

dots = Image.new("RGBA", (W, H), (0, 0, 0, 0))
dd = ImageDraw.Draw(dots)
for gyp in range(0, H, 26):
    for gxp in range(0, W, 26):
        dd.ellipse([gxp, gyp, gxp + 1, gyp + 1], fill=(255, 255, 255, 22))
canvas = Image.alpha_composite(canvas, dots)
draw = ImageDraw.Draw(canvas)

# ---------- top text (unchanged from the first concept) ----------
center_text(draw, 78, "K T E L I O", font(F_SERIF_B, 38), GOLD)
center_text(draw, 158, "Greece's regional buses.", font(F_SERIF_B, 54), WHITE)
center_text(draw, 222, "Finally in one place.", font(F_SERIF_BI, 54), GOLD)
center_text(draw, 276, "20 real routes  ·  book free yourself, or let us handle it for €5",
            font(F_SANS_R, 21), (199, 212, 229))

# =====================================================================
# BROWSER WINDOW MOCKUP — flat, no fake hardware: a simple window frame
# (title bar + traffic-light dots + address pill) holding the real page.
# =====================================================================
LW, TB_H, CH = 760, 34, 480
WH = TB_H + CH

win = Image.new("RGBA", (LW, WH), (255, 255, 255, 255))
wd = ImageDraw.Draw(win)
wd.rectangle([0, 0, LW, TB_H], fill=(237, 239, 243, 255))
wd.line([0, TB_H, LW, TB_H], fill=(210, 214, 220, 255), width=1)
for cxo, dotc in zip([20, 40, 60], [(255, 95, 87), (255, 189, 46), (40, 200, 64)]):
    wd.ellipse([cxo - 6, TB_H/2 - 6, cxo + 6, TB_H/2 + 6], fill=dotc)
addr_fnt = font(F_SANS_R, 13)
addr = "ktelio.gr"
aw = text_w(wd, addr, addr_fnt)
apw = aw + 40
ax0 = LW/2 - apw/2
wd.rounded_rectangle([ax0, TB_H/2 - 11, ax0 + apw, TB_H/2 + 11], radius=11,
                      fill=(255, 255, 255, 255), outline=(210, 214, 220, 255), width=1)
wd.text((LW/2, TB_H/2), addr, font=addr_fnt, fill=(90, 100, 115), anchor="mm")

# ---- faithful mini recreation of the REAL hero section (fills the content
# area edge-to-edge, same as a real browser viewport) ----
sw, sh = LW, CH
myy, mxx = np.mgrid[0:sh, 0:sw].astype(np.float32)
mt = np.clip((mxx / sw) * 0.3 + (myy / sh) * 0.7, 0, 1)
mbg = np.empty((sh, sw, 3), dtype=np.float32)
for c in range(3):
    mbg[:, :, c] = NAVY[c] * (1 - mt) + NAVY_DARK[c] * mt
scr = Image.fromarray(mbg.astype(np.uint8), "RGB").convert("RGBA")
sd = ImageDraw.Draw(scr)

pad = 28
# --- mini nav bar (real nav items) ---
sd.text((pad, 14), "Ktelio", font=font(F_SERIF_B, 17), fill=GOLD)
sd.text((pad + 78, 18), "How it works    Routes    Why trust us    FAQ",
        font=font(F_SANS_R, 11), fill=(160, 176, 197))
nav_btn = "Get your ticket"
nb_w = text_w(sd, nav_btn, font(F_SANS_B, 10)) + 22
sd.rounded_rectangle([sw - pad - nb_w, 12, sw - pad, 12 + 22], radius=11, outline=GOLD, width=1)
sd.text((sw - pad - nb_w + 11, 15), nav_btn, font=font(F_SANS_B, 10), fill=GOLD)
sd.line([0, 46, sw, 46], fill=(255, 255, 255, 18), width=1)

# --- real badge pill ---
badge_txt = "Now booking · Greece, one route at a time"
by = 66
sd.ellipse([pad, by + 5, pad + 7, by + 12], fill=LIVE_GREEN)
sd.text((pad + 15, by), badge_txt, font=font(F_SANS_B, 11), fill=(216, 222, 231))

# --- real headline ---
sd.text((pad, 92), "Greece's intercity buses,", font=font(F_SERIF_B, 33), fill=WHITE)
sd.text((pad, 130), "finally easy to book.", font=font(F_SERIF_BI, 33), fill=GOLD)

# --- real lead line (condensed to fit) ---
sd.text((pad, 178), "Greece's fragmented bus network, finally in one place —",
        font=font(F_SANS_R, 13.5), fill=(191, 205, 222))
sd.text((pad, 197), "reach ", font=font(F_SANS_R, 13.5), fill=(191, 205, 222))
w1 = text_w(sd, "reach ", font(F_SANS_R, 13.5))
sd.text((pad + w1, 195), "Delphi", font=font(F_SERIF_BI, 15), fill=GOLD)
w2 = text_w(sd, "Delphi", font(F_SERIF_BI, 15))
sd.text((pad + w1 + w2, 197), " without hunting for the right site.", font=font(F_SANS_R, 13.5), fill=(191, 205, 222))

# --- real button pair ---
by2 = 226
btn1 = "Find my route"
b1w = text_w(sd, btn1, font(F_SANS_B, 15)) + 44
sd.rounded_rectangle([pad, by2, pad + b1w, by2 + 40], radius=20, fill=GOLD)
sd.text((pad + b1w/2, by2 + 20), btn1, font=font(F_SANS_B, 15), fill=NAVY_DARK, anchor="mm")
btn2 = "How it works"
b2x = pad + b1w + 12
b2w = text_w(sd, btn2, font(F_SANS_B, 15)) + 44
sd.rounded_rectangle([b2x, by2, b2x + b2w, by2 + 40], radius=20, outline=(255, 255, 255, 200), width=1)
sd.text((b2x + b2w/2, by2 + 20), btn2, font=font(F_SANS_B, 15), fill=WHITE, anchor="mm")

# --- real stats row (condensed inline) ---
sy_stats = 298
stats = [("20", "routes covered"), ("€5*", "concierge fee"), ("100%", "free option, always")]
sxp = pad
for num, label in stats:
    sd.text((sxp, sy_stats), num, font=font(F_SERIF_B, 22), fill=GOLD)
    nw = text_w(sd, num, font(F_SERIF_B, 22))
    sd.text((sxp, sy_stats + 28), label, font=font(F_SANS_R, 10.5), fill=(160, 176, 197))
    sxp += max(nw, text_w(sd, label, font(F_SANS_R, 10.5))) + 26

# --- real "Popular right now" hero-card (all 4 real entries) ---
card_w, card_h = 232, 358
cx0, cy0 = sw - card_w - 26, (sh - card_h) // 2 + 6
sd.rounded_rectangle([cx0, cy0, cx0 + card_w, cy0 + card_h], radius=16, fill=WHITE)
sd.text((cx0 + 20, cy0 + 18), "POPULAR RIGHT NOW", font=font(F_SANS_B, 11), fill=MUTED)
ry = cy0 + 54
for name, price in [("Delphi", "€15"), ("Meteora", "€29"), ("Nafplio", "€13"), ("Thessaloniki", "€40")]:
    sd.text((cx0 + 20, ry), name, font=font(F_SERIF_B, 16.5), fill=INK)
    pb = sd.textbbox((0, 0), price, font=font(F_SANS_B, 13))
    pw_ = pb[2] - pb[0]
    sd.rounded_rectangle([cx0 + card_w - 20 - pw_ - 16, ry + 1, cx0 + card_w - 20, ry + 23], radius=11, fill=SKY)
    sd.text((cx0 + card_w - 20 - pw_ - 8, ry + 4), price, font=font(F_SANS_B, 13), fill=BLUE)
    ry += 44
    if name != "Thessaloniki":
        sd.line([cx0 + 20, ry - 8, cx0 + card_w - 20, ry - 8], fill=LINE, width=1)

win.paste(scr, (0, TB_H), scr)

# clip the whole assembled window to rounded corners (title bar + content
# together), so the flat panel reads as one clean rounded card
mask = Image.new("L", (LW, WH), 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, LW, WH], radius=14, fill=255)
win.putalpha(mask)

shadow, spad = rounded_shadow((LW, WH), 14, 22, alpha=120)
WIN_X, WIN_Y = 55, 360
canvas.paste(shadow, (WIN_X - spad + 6, WIN_Y - spad + 14), shadow)
canvas.paste(win, (WIN_X, WIN_Y), win)

# =====================================================================
# PHONE MOCKUP (unchanged from the first concept)
# =====================================================================
PW, PH = 300, 610
phone = Image.new("RGBA", (PW, PH), (0, 0, 0, 0))
pd = ImageDraw.Draw(phone)
pd.rounded_rectangle([0, 0, PW, PH], radius=46, fill=(23, 27, 33, 255))
pinset = 12
psx0, psy0, psx1, psy1 = pinset, pinset, PW - pinset, PH - pinset
pd.rounded_rectangle([psx0, psy0, psx1, psy1], radius=36, fill=NAVY)
notch_w = 110
pd.rounded_rectangle([PW/2 - notch_w/2, psy0, PW/2 + notch_w/2, psy0 + 22], radius=11, fill=(23, 27, 33, 255))

psw, psh = psx1 - psx0, psy1 - psy0
pyy, pxx = np.mgrid[0:psh, 0:psw].astype(np.float32)
pt = np.clip(pyy / psh, 0, 1)
pmbg = np.empty((psh, psw, 3), dtype=np.float32)
for c in range(3):
    pmbg[:, :, c] = NAVY[c] * (1 - pt) + NAVY_DARK[c] * pt
pscr = Image.fromarray(pmbg.astype(np.uint8), "RGB").convert("RGBA")
psd = ImageDraw.Draw(pscr)

ppad = 24
psd.text((ppad, 46), "Ktelio", font=font(F_SERIF_B, 20), fill=GOLD)
psd.text((ppad, 86), "Greece's buses,", font=font(F_SERIF_B, 25), fill=WHITE)
psd.text((ppad, 116), "finally easy.", font=font(F_SERIF_BI, 25), fill=GOLD)
btn_w2, btn_h2 = 150, 38
psd.rounded_rectangle([ppad, 168, ppad + btn_w2, 168 + btn_h2], radius=btn_h2 // 2, fill=GOLD)
bd2 = psd.textbbox((0, 0), "Browse routes", font=font(F_SANS_B, 14))
psd.text((ppad + btn_w2/2 - (bd2[2]-bd2[0])/2, 168 + btn_h2/2 - (bd2[3]-bd2[1])/2 - bd2[1]), "Browse routes", font=font(F_SANS_B, 14), fill=NAVY_DARK)

pcard_w, pcard_h = psw - ppad * 2, 190
pcx0, pcy0 = ppad, 234
psd.rounded_rectangle([pcx0, pcy0, pcx0 + pcard_w, pcy0 + pcard_h], radius=14, fill=WHITE)
psd.text((pcx0 + 18, pcy0 + 16), "POPULAR NOW", font=font(F_SANS_B, 11), fill=MUTED)
pry = pcy0 + 48
for name, price in [("Delphi", "€15"), ("Meteora", "€29")]:
    psd.text((pcx0 + 18, pry), name, font=font(F_SERIF_B, 17), fill=INK)
    ppb = psd.textbbox((0, 0), price, font=font(F_SANS_B, 13))
    psd.rounded_rectangle([pcx0 + pcard_w - 18 - (ppb[2]-ppb[0]) - 16, pry + 1, pcx0 + pcard_w - 18, pry + 23], radius=11, fill=SKY)
    psd.text((pcx0 + pcard_w - 18 - (ppb[2]-ppb[0]) - 8, pry + 4), price, font=font(F_SANS_B, 13), fill=BLUE)
    pry += 62
    psd.line([pcx0 + 18, pry - 24, pcx0 + pcard_w - 18, pry - 24], fill=LINE, width=1)

phone.paste(pscr, (psx0, psy0), pscr)
pshadow, pspad = rounded_shadow((PW, PH), 46, 22, alpha=140)
phone_rot = phone.rotate(5, expand=True, resample=Image.BICUBIC)
pshadow_rot = pshadow.rotate(5, expand=True, resample=Image.BICUBIC)
PHONE_X, PHONE_Y = 800, 440
canvas.paste(pshadow_rot, (PHONE_X - pspad + 12, PHONE_Y - pspad + 28), pshadow_rot)
canvas.paste(phone_rot, (PHONE_X, PHONE_Y), phone_rot)

draw = ImageDraw.Draw(canvas)

# ---------- bottom line (unchanged from the first concept) ----------
center_text(draw, 1100, "Delphi · Meteora · Nafplio · Olympia · Monemvasia + 15 more routes",
            font(F_SANS_R, 18), (150, 168, 190))

canvas.convert("RGB").save("ktelio-promo.png", quality=95)
print("saved", canvas.size)
