#!/usr/bin/env python3
"""news-23 b218 heroes-scene: THE WORLD TODAY, Monday 23 November 2026.
31 stories: 3 hero scenes + 10 cards + 18 ALSO. Draws entry.png 1024x1024."""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (18, 18, 18)
RED = (178, 34, 34)
DARKRED = (139, 0, 0)
BLUE = (23, 58, 120)
TEAL = (14, 90, 90)
GREY = (90, 90, 90)
LIGHT = (232, 226, 210)
MAPLAND = (214, 205, 178)
MAPSEA = (222, 232, 238)

FDIR = "/usr/share/fonts/truetype/dejavu"
def font(name, size):
    return ImageFont.truetype(os.path.join(FDIR, name), size)

F_MAST = font("DejaVuSerif-Bold.ttf", 62)
F_MAST_SM = font("DejaVuSerif.ttf", 15)
F_KICK = font("DejaVuSans-Bold.ttf", 15)
F_NUM = font("DejaVuSans-Bold.ttf", 30)
F_NUML = font("DejaVuSans.ttf", 10)
F_REG = font("DejaVuSans-Bold.ttf", 11)
F_HERO_H = font("DejaVuSans-Bold.ttf", 21)
F_HERO_B = font("DejaVuSans.ttf", 12)
F_HERO_N = font("DejaVuSans-Bold.ttf", 26)
F_CARD_H = font("DejaVuSans-Bold.ttf", 12)
F_CARD_B = font("DejaVuSans.ttf", 10)
F_CHIP = font("DejaVuSans-Bold.ttf", 8)
F_MAP_L = font("DejaVuSans.ttf", 10)
F_ALSO_H = font("DejaVuSans-Bold.ttf", 11)
F_ALSO = font("DejaVuSans.ttf", 10)
F_DC_H = font("DejaVuSans-Bold.ttf", 13)
F_DC = font("DejaVuSans.ttf", 11)
F_NUML9 = font("DejaVuSans.ttf", 9)
F_HERO_N20 = font("DejaVuSans-Bold.ttf", 20)
F_HERO_B13 = font("DejaVuSans-Bold.ttf", 13)
F_FOOT = font("DejaVuSans.ttf", 10)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def tw(text, f):
    return d.textlength(text, font=f)

def wrap(text, f, maxw):
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if tw(t, f) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines

def box(x0, y0, x1, y1, fill=None, outline=None, width=1):
    d.rectangle([x0, y0, x1, y1], fill=fill, outline=outline, width=width)

# ---------------- masthead ----------------
d.rectangle([0, 0, W, 6], fill=INK)
title = "THE WORLD TODAY"
d.text(((W - tw(title, F_MAST)) / 2, 12), title, font=F_MAST, fill=INK)
d.line([24, 82, W - 24, 82], fill=INK, width=2)
sub = "MONDAY 23 NOVEMBER 2026  •  31 STORIES FROM SIX REGIONS  •  PRICE $2.50"
d.text(((W - tw(sub, F_MAST_SM)) / 2, 88), sub, font=F_MAST_SM, fill=INK)
d.line([24, 108, W - 24, 108], fill=INK, width=1)

# ---------------- kicker ----------------
kick = "AI ROUT SENDS KOSPI TO ITS WORST DAY — GUTERRES: REGULATE AI — US LEAD OVER CHINA AT RECORD LOW"
d.text(((W - tw(kick, F_KICK)) / 2, 114), kick, font=F_KICK, fill=DARKRED)

# ---------------- numbers strip 5x2 ----------------
strip = [
    ("186", "DRONES AT UKRAINE"),
    ("161", "SHOT DOWN"),
    ("720", "KM OF FRONT LINE"),
    ("9", "DAYS OF TALKS"),
    ("98.79%", "YES VOTE"),
    ("$120bn", "AI INVESTMENT"),
    ("35%", "TARIFF ON IMPORTS"),
    ("44h", "RESCUE OPERATION"),
    ("50", "DELEGATIONS"),
    ("24", "SUMMIT NATIONS"),
]
sy, sh, sw = 136, 46, 196
for i, (num, lab) in enumerate(strip):
    r, c = divmod(i, 5)
    x0 = 16 + c * 200
    y0 = sy + r * sh
    box(x0, y0, x0 + sw, y0 + sh - 4, fill=(255, 255, 255), outline=(180, 175, 160))
    d.text((x0 + 8, y0 + 2), num, font=F_NUM, fill=INK)
    lx = x0 + 8 + tw(num, F_NUM) + 8
    if lx + tw(lab, F_NUML) > x0 + sw - 4:
        d.text((x0 + 8, y0 + 28), lab, font=F_NUML9, fill=GREY)
    else:
        d.text((lx, y0 + 12), lab, font=F_NUML, fill=GREY)

# ---------------- region bar ----------------
regions = [("ASIA", 7, (200, 60, 60)), ("EUROPE", 8, (23, 58, 120)),
           ("MIDEAST", 6, (14, 90, 90)), ("AMERICAS", 5, (120, 80, 160)),
           ("AFRICA", 3, (180, 120, 20)), ("OCEANIA", 2, (40, 120, 60))]
ry = 230
x = 16
d.text((16, ry), "REGIONS:", font=F_REG, fill=INK)
x = 16 + tw("REGIONS: ", F_REG) + 6
bx = x
total_w = W - 32 - (bx - 16)
for name, n, col in regions:
    seg = int(total_w * n / 31)
    d.rectangle([bx, ry + 2, bx + seg - 2, ry + 14], fill=col)
    bx += seg
lx = 16
d.text((16, ry + 18), "ASIA 7  •  EUROPE 8  •  MIDEAST 6  •  AMERICAS 5  •  AFRICA 3  •  OCEANIA 2  =  31 STORIES",
       font=F_NUML, fill=GREY)

# ---------------- heroes ----------------
hy = 262
# hero 1: KOSPI (left)
hx0, hw = 16, 492
box(hx0, hy, hx0 + hw, hy + 152, fill=(16, 22, 38))
d.text((hx0 + 12, hy + 8), "AI ROUT HITS SEOUL", font=F_HERO_H, fill=(255, 255, 255))
d.text((hx0 + 12, hy + 36), "KOSPI -3.3% — WORST DAY SINCE THE PANIC · -5.8% INTRADAY", font=F_HERO_B, fill=(200, 205, 220))
# buildings with lit windows (left half)
for bx0, bw_, bh_ in [(28, 60, 62), (96, 44, 78), (146, 52, 56), (206, 40, 70)]:
    d.rectangle([hx0 + bx0, hy + 152 - bh_, hx0 + bx0 + bw_, hy + 152], fill=(38, 48, 74))
    for wy in range(hy + 152 - bh_ + 6, hy + 148, 12):
        for wx in range(hx0 + bx0 + 6, hx0 + bx0 + bw_ - 4, 12):
            if (wx + wy) % 3:
                d.rectangle([wx, wy, wx + 5, wy + 6], fill=(255, 214, 90))
# falling chart line (right half)
pts = [(hx0 + 300, hy + 58), (hx0 + 335, hy + 70), (hx0 + 365, hy + 64),
       (hx0 + 395, hy + 86), (hx0 + 430, hy + 80), (hx0 + 465, hy + 100), (hx0 + 488, hy + 104)]
d.line(pts, fill=(255, 70, 60), width=4)
d.text((hx0 + 300, hy + 108), "-3.3%", font=F_HERO_N, fill=(255, 120, 100))
d.text((hx0 + 300, hy + 138), "KOSPI 4,708.54", font=F_HERO_B, fill=(255, 255, 255))

# hero 2: Guterres (right)
hx1 = 516
box(hx1, hy, hx1 + 492, hy + 152, fill=(255, 255, 255), outline=(180, 175, 160))
d.text((hx1 + 12, hy + 8), "GUTERRES: REGULATE AI", font=F_HERO_H, fill=INK)
d.text((hx1 + 12, hy + 36), "UN CHIEF CALLS FOR GLOBAL RULES", font=F_HERO_B, fill=GREY)
# globe
cx, cy, cr = hx1 + 62, hy + 100, 34
d.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=(70, 130, 200), outline=BLUE, width=2)
d.ellipse([cx - 14, cy - cr, cx + 14, cy + cr], outline=(255, 255, 255), width=1)
d.line([cx - cr, cy, cx + cr, cy], fill=(255, 255, 255), width=1)
d.arc([cx - cr, cy - 16, cx + cr, cy + 16], 0, 360, fill=(255, 255, 255), width=1)
# 4 flags
flagcols = [(200, 60, 60), (23, 58, 120), (14, 90, 90), (180, 120, 20)]
for i, col in enumerate(flagcols):
    fx = hx1 + 115 + i * 48
    d.line([fx + 4, hy + 66, fx + 4, hy + 108], fill=INK, width=2)
    d.rectangle([fx + 4, hy + 66, fx + 42, hy + 88], fill=col, outline=INK)
    d.rectangle([fx + 4, hy + 77, fx + 42, hy + 88], fill=(255, 255, 255), outline=INK)
d.text((hx1 + 120, hy + 116), "150 DELEGATES — BRIDGETOWN · BARBADOS", font=F_HERO_B13, fill=INK)
d.text((hx1 + 120, hy + 136), "UN chief urges binding rules on frontier AI.", font=F_HERO_B, fill=INK)

# hero 3: Power Index (full width)
hy3 = 420
box(16, hy3, W - 16, hy3 + 92, fill=(255, 255, 255), outline=(180, 175, 160))
d.text((28, hy3 + 8), "US LEAD OVER CHINA AT RECORD LOW", font=F_HERO_H, fill=INK)
d.text((28, hy3 + 36), "POWER INDEX 2026", font=F_HERO_B, fill=GREY)
bars = [("US", 78.9, (23, 58, 120)), ("CHINA", 73.6, (200, 60, 60)), ("INDIA", 40.5, (180, 120, 20))]
by = hy3 + 56
for i, (nm, val, col) in enumerate(bars):
    bx0 = 28 + i * 330
    d.text((bx0, by), nm, font=F_HERO_B, fill=INK)
    d.rectangle([bx0 + 62, by + 2, bx0 + 62 + int(val * 2.2), by + 14], fill=col)
    d.text((bx0 + 62 + int(val * 2.2) + 6, by), f"{val}", font=F_HERO_B, fill=INK)
d.text((700, hy3 + 8), "GAP 5.3 — NARROWEST SINCE 2018", font=F_HERO_B, fill=DARKRED)

# ---------------- 10 cards 5x2 ----------------
cards = [
    ("COP31 NO DEAL", "Antalya talks end without a deal as the final text slips to Tuesday.", "REPORTED"),
    ("186 DRONES", "Overnight barrage at Ukraine; 161 shot down, air defences stretched thin.", "REPORTED"),
    ("PATRIOT RADARS", "Two radars claimed struck in Bahrain; US says damage assessed.", "CLAIM"),
    ("ANTHROPIC IPO", "Shares priced at $83/share in one of the year's biggest listings.", "REPORTED"),
    ("HORMUZ TRAFFIC", "Tanker flows hold as insurers watch the strait.", "REPORTED"),
    ("CHIP STOCKS", "AI rout spreads to chipmakers; suppliers fall across Asia.", "REPORTED"),
    ("EU LEADERS", "Energy and defence top the agenda in Brussels.", "REPORTED"),
    ("GAZA AID", "Crossings reopen as aid trucks roll in under escort.", "REPORTED"),
    ("SUDAN TALKS", "Ceasefire talks resume after a week of deadlock.", "REPORTED"),
    ("BENGHAZI BLAST", "Explosion under investigation; officials urge calm.", "CLAIM"),
]
cy0 = 520
for i, (h_, b_, chip) in enumerate(cards):
    r, c = divmod(i, 5)
    x0 = 16 + c * 200
    y0 = cy0 + r * 76
    box(x0, y0, x0 + 196, y0 + 70, fill=(255, 255, 255), outline=(180, 175, 160))
    col = RED if chip == "CLAIM" else TEAL
    cw = tw(chip, F_CHIP) + 10
    d.rectangle([x0 + 196 - cw - 6, y0 + 5, x0 + 190, y0 + 17], fill=col)
    d.text((x0 + 196 - cw - 1, y0 + 6), chip, font=F_CHIP, fill=(255, 255, 255))
    maxw = 196 - cw - 16
    hh = h_
    while tw(hh, F_CARD_H) > maxw and len(hh) > 4:
        hh = hh[:-1]
    if hh != h_:
        hh = hh[:-1] + "…"
    d.text((x0 + 8, y0 + 5), hh, font=F_CARD_H, fill=INK)
    lines = wrap(b_, F_CARD_B, 180)
    for j, ln in enumerate(lines[:3]):
        d.text((x0 + 8, y0 + 24 + j * 13), ln, font=F_CARD_B, fill=(40, 40, 40))

# ---------------- map + ALSO ----------------
my0 = 676
box(16, my0, 640, my0 + 184, fill=MAPSEA, outline=(180, 175, 160))
d.text((28, my0 + 6), "THE WORLD IN ONE LOOK", font=F_ALSO_H, fill=INK)
# continents (rough blobs)
NA = [(60, 700), (280, 690), (300, 720), (270, 780), (200, 800), (120, 790), (60, 740)]
SA = [(230, 800), (300, 800), (290, 850), (240, 850)]
EU = [(320, 688), (460, 688), (460, 740), (380, 748), (320, 725)]
AF = [(330, 750), (480, 750), (470, 845), (360, 845), (330, 790)]
AS = [(460, 682), (628, 682), (628, 780), (540, 800), (470, 750)]
AU = [(540, 820), (600, 820), (600, 850), (540, 850)]
for poly in (NA, SA, EU, AF, AS, AU):
    d.polygon(poly, fill=MAPLAND, outline=(150, 140, 115))

PINS = {
    "Washington": (150, 720), "Bridgetown": (210, 790), "Manchester": (330, 700),
    "Paris": (345, 718), "Warsaw": (395, 700), "Kyiv": (415, 712),
    "Antalya": (420, 735), "Beirut": (445, 738), "Gaza": (462, 758),
    "Benghazi": (400, 760), "Khartoum": (450, 800), "Kinshasa": (380, 815),
    "Seoul": (560, 715),
}
LAND = NA + SA + EU + AF + AS + AU
def point_in_poly(x, y, poly):
    inside = False
    n = len(poly)
    j = n - 1
    for i in range(n):
        xi, yi = poly[i]; xj, yj = poly[j]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            inside = not inside
        j = i
    return inside

for name, (px, py) in PINS.items():
    assert any(point_in_poly(px, py, p) for p in (NA, SA, EU, AF, AS, AU)), f"pin {name} outside land"
names = list(PINS)
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        x1, y1 = PINS[names[i]]; x2, y2 = PINS[names[j]]
        dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        assert dist >= 19, f"pins {names[i]}/{names[j]} only {dist:.1f}px apart"
for name, (px, py) in PINS.items():
    d.ellipse([px - 4, py - 4, px + 4, py + 4], fill=RED, outline=(255, 255, 255), width=1)
LABELS = {
    "Washington": (118, 706), "Bridgetown": (150, 796), "Manchester": (296, 686),
    "Paris": (300, 722), "Warsaw": (372, 686), "Kyiv": (424, 700),
    "Antalya": (428, 742), "Beirut": (452, 726), "Gaza": (470, 750),
    "Benghazi": (352, 766), "Khartoum": (458, 806), "Kinshasa": (330, 822),
    "Seoul": (540, 700),
}
for name, (lx, ly) in LABELS.items():
    d.text((lx, ly), name, font=F_MAP_L, fill=INK)
d.text((28, my0 + 168), "● 13 CITIES IN THE NEWS", font=F_NUML, fill=GREY)

# ALSO 18 (right column, 2 columns x 9)
ax0 = 652
d.text((ax0, my0 + 6), "ALSO IN THE NEWS", font=F_ALSO_H, fill=INK)
d.line([ax0, my0 + 24, W - 16, my0 + 24], fill=INK, width=1)
also = [
    "COP31 host confirms text delay",
    "Seoul readies 10T-won fund",
    "Manchester police clear cordon",
    "Paris AI safety summit Tue",
    "Kyiv power grid stabilised",
    "Warsaw hosts EU ministers",
    "Beirut port repairs resume",
    "Kinshasa flood relief arrives",
    "Khartoum aid corridor opens",
    "Bridgetown climate fund pledge",
    "Washington Fed minutes Wed",
    "Beijing chip curbs eased",
    "New Delhi air quality alert",
    "London markets steady",
    "Tokyo Nikkei follows KOSPI",
    "Sydney bushfire crews sent",
    "Cairo Gaza talks continue",
    "Riyadh oil output steady",
]
F_ALSO9 = font("DejaVuSans.ttf", 9)
for i, item in enumerate(also):
    cc, rr = divmod(i, 9)
    xx = ax0 + cc * 180
    yy = my0 + 32 + rr * 15
    d.text((xx, yy), "• " + item, font=F_ALSO9, fill=(40, 40, 40))

# ---------------- DATE CHECK red box ----------------
dy0 = 872
box(16, dy0, W - 16, dy0 + 118, fill=(255, 240, 240), outline=RED, width=2)
d.text((28, dy0 + 6), "DATE CHECK — WHAT DID NOT MAKE 23 NOVEMBER", font=F_DC_H, fill=DARKRED)
d.line([28, dy0 + 26, W - 28, dy0 + 26], fill=RED, width=1)
d.text((28, dy0 + 32), "LEFT OUT — NOT 23 NOV STORIES:", font=F_DC, fill=DARKRED)
leftout = ["Dems 258", "Sparta II fire", "El Chapo", "EU–Indonesia pact", "Nigeria boat", "ICJ Myanmar ruling"]
for i, item in enumerate(leftout):
    r, c = divmod(i, 3)
    d.text((28 + c * 220, dy0 + 50 + r * 16), "✕ " + item, font=F_DC, fill=INK)
d.text((700, dy0 + 32), "NOT YET — STILL TO COME:", font=F_DC, fill=DARKRED)
notyet = ["COP31 final text (Tue)", "Fed decision (Wed)", "Anthropic IPO pricing (Thu)", "Ukraine talks round 2 (Fri)"]
for i, item in enumerate(notyet):
    d.text((700, dy0 + 50 + i * 16), "○ " + item, font=F_DC, fill=INK)

# ---------------- footer ----------------
d.line([24, 998, W - 24, 998], fill=INK, width=1)
foot = "Sources: wires, exchanges, UN briefings • KOSPI 4,708.54 • All figures checked at press time • THE WORLD TODAY"
d.text(((W - tw(foot, F_FOOT)) / 2, 1004), foot, font=F_FOOT, fill=GREY)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out)
print("saved", out, os.path.getsize(out), "bytes")
