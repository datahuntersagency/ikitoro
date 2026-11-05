"""Render the Drink Menu and Spirits List PDFs in the Iki Toro main-menu style:
the same page size, background art (header mark, cherry blossom, koi), Noto Serif
type, plum headings, two-column layout with right-aligned prices."""
import io
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit, ImageReader
from pypdf import PdfReader, PdfWriter
from menu_data import *

W, H = 701.008, 1169.01
pdfmetrics.registerFont(TTFont("NS", "fonts/NotoSerifRegular.ttf"))
pdfmetrics.registerFont(TTFont("NSI", "fonts/NotoSerifItalic.ttf"))
PLUM = (71/255, 4/255, 43/255)
INK = (0.08, 0.07, 0.07)
L0, L1 = 38, 327          # left column, as on the food menu
R0, R1 = 374, 654         # right column
PCOL = 56                 # spacing between price columns
SUNTORY = "src/suntory.png"

def fmt(p):
    if p is None: return ""
    if isinstance(p, str): return p
    return f"{p:,}"

class Page:
    def __init__(self, c): self.c = c
    def y(self, top): return H - top    # top-based coordinates

    def heading(self, text, x0, x1, top, size=17):
        c = self.c
        c.saveState()
        c.setFillColorRGB(*PLUM); c.setStrokeColorRGB(*PLUM)
        c.setLineWidth(size * 0.032); c._code.append("2 Tr")  # fill+stroke = semibold look
        c.setFont("NS", size)
        c.drawCentredString((x0 + x1) / 2, self.y(top), text)
        c._code.append("0 Tr")
        c.restoreState()

    def italic_center(self, text, x0, x1, top, size=8.2, color=INK, lead=11.6):
        c = self.c; c.setFillColorRGB(*color); c.setFont("NSI", size)
        lines = simpleSplit(text, "NSI", size, x1 - x0)
        for i, ln in enumerate(lines):
            c.drawCentredString((x0 + x1) / 2, self.y(top + i * lead), ln)
        return top + len(lines) * lead

    def group_label(self, text, x0, x1, top):
        self.heading(text, x0, x1, top, size=12.5)
        return top + 20

    def price_labels(self, labels, x1, top):
        c = self.c; c.setFont("NS", 9.2); c.setFillColorRGB(*INK)
        for i, lab in enumerate(reversed(labels)):
            c.drawRightString(x1 - i * PCOL, self.y(top), lab)
        return top + 16

    def item(self, it, x0, x1, top, ncols):
        name, suffix, desc, prices = it
        c = self.c
        pw = PCOL * ncols
        c.setFillColorRGB(*INK)
        c.setFont("NS", 11)
        nmax = x1 - x0 - pw - 6
        c.drawString(x0, self.y(top), name)
        nw = pdfmetrics.stringWidth(name, "NS", 11)
        if suffix:
            sx = x0 + nw + 4
            if sx + pdfmetrics.stringWidth(suffix, "NSI", 9.4) <= x0 + nmax:
                c.setFont("NSI", 9.4); c.drawString(sx, self.y(top), suffix)
            else:  # no room beside the name: lead the description line with it
                desc = suffix + (" — " + desc if desc else "")
        c.setFont("NS", 11)
        for i, p in enumerate(reversed(prices)):
            c.drawRightString(x1 - i * PCOL, self.y(top), fmt(p))
        top += 11.5
        if desc:
            c.setFont("NSI", 7.3)
            for ln in simpleSplit(desc, "NSI", 7.3, x1 - x0 - pw + PCOL * 0.4 - 4):
                c.drawString(x0, self.y(top), ln); top += 9.2
        return top + (11 if desc else 6.5)

    def items(self, items, x0, x1, top, ncols=1):
        for it in items:
            top = self.item(it, x0, x1, top, ncols)
        return top

    def section(self, title, sub, items, x0, x1, top, labels=None, groups=None):
        self.heading(title, x0, x1, top)
        top += 16
        if sub: top = self.italic_center(sub, x0, x1, top) + 4
        else: top += 6
        ncols = len(labels) if labels else 1
        if labels: top = self.price_labels(labels, x1, top + 4)
        else: top += 8
        if groups:
            for gname, gitems in groups:
                top = self.group_label(gname, x0, x1, top + 4)
                top = self.items(gitems, x0, x1, top, ncols)
        else:
            top = self.items(items, x0, x1, top, ncols)
        return top

    def split_section(self, title, sub, items, top, labels=None, image=None):
        """Full-width heading, items flowing into the two columns."""
        self.heading(title, L0, R1, top, size=19)
        top += 18
        if sub: top = self.italic_center(sub, L0 + 60, R1 - 60, top, size=9) + 2
        if image:
            img = ImageReader(image); iw, ih = img.getSize()
            w = 300; h = w * ih / iw
            self.c.drawImage(img, (W - w) / 2, self.y(top + h - 6), w, h, mask="auto")
            top += h - 2
        ncols = len(labels) if labels else 1
        if labels:
            self.price_labels(labels, L1, top + 8); top = self.price_labels(labels, R1, top + 8)
        else: top += 14
        half = (len(items) + 1) // 2
        a = self.items(items[:half], L0, L1, top, ncols)
        b = self.items(items[half:], R0, R1, top, ncols)
        return max(a, b)

    def footer(self, text):
        c = self.c
        c.setStrokeColorRGB(0, 0, 0); c.setLineWidth(0.6)
        c.line(36, self.y(1117), 654, self.y(1117))
        c.setFillColorRGB(*INK); c.setFont("NSI", 8.6)
        c.drawCentredString(W / 2, self.y(1134), text)


def render(pages, title, out):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(W, H))
    c.setTitle(title); c.setAuthor("Iki Toro"); c.setSubject("Iki Toro Japanese Restaurant, Glendale")
    for fn in pages:
        p = Page(c); fn(p); c.showPage()
    c.save()
    tpl = PdfReader("template.pdf").pages[0]
    over = PdfReader(io.BytesIO(buf.getvalue()))
    w = PdfWriter()
    for pg in over.pages:
        base = w.add_blank_page(W, H)
        base.merge_page(tpl); base.merge_page(pg)
    w.add_metadata({"/Title": title, "/Author": "Iki Toro"})
    with open(out, "wb") as f: w.write(f)
    print("wrote", out)

# ---------------- DRINK MENU ----------------
def drinks_p1(p):
    t = p.split_section("Specialty Cocktails", "Featuring", COCKTAILS, 197, image=SUNTORY)
    t += 18
    a = p.section("Mocktails", "Zero-proof, made to order", MOCKTAILS, L0, L1, t)
    b = p.section("Sake by the Glass", "", SAKE_GLASS, R0, R1, t)
    t = max(a, b) + 18
    p.split_section("Japanese Sake", "By the bottle, from junmai to ten-year aged yamahai", SAKE_BOTTLES, t,
                    labels=["300 ml", "720 ml"])
    p.footer("Please enjoy responsibly. Ask your server about pairing sake with your meal.")

def drinks_p2(p):
    p.heading("Wine", L0, R1, 197, size=19)
    t = p.italic_center("Champagne and sparkling, white, red and Japanese fruit wine", L0 + 60, R1 - 60, 215, size=9) + 6
    # left: sparkling + white ; right: red + fruit
    def col(x0, x1, groups, top):
        top = p.price_labels(["Glass", "Bottle"], x1, top + 6)
        for gname, items in groups:
            top = p.group_label(gname, x0, x1, top + 6)
            top = p.items(items, x0, x1, top, 2)
        return top
    a = col(L0, L1, [("Champagne & Sparkling", WINE_SPARKLING), ("White", WINE_WHITE)], t)
    b = col(R0, R1, [("Red", WINE_RED), ("Fruit Wine", WINE_FRUIT)], t)
    t = max(a, b) + 20
    a = p.section("Beer", "", [], L0, L1, t, groups=[("12 oz", BEER_12), ("22 oz", BEER_22)])
    b = p.section("Tea", "Japanese teas and matcha", TEA, R0, R1, t)
    t = max(a, b) + 20
    p.split_section("Soft Drinks", "Sodas, lemonades and Japanese Calpico", SOFT, t)
    p.footer("Please enjoy responsibly. Must be 21 or older to be served alcohol.")

# ---------------- SPIRITS LIST ----------------
def spirits_p1(p):
    p.split_section("Japanese Whisky", "Served as a 50 ml pour: neat, on a large cube, or as a highball", WHISKY, 197)
    p.footer("Our cellar changes with availability. Ask your server about rare and limited pours.")

def spirits_p2(p):
    a = p.section("Tequila & Mezcal", "Agave, from blanco to extra añejo", TEQUILA, L0, L1, 197)
    b = p.section("Cognac & Brandy", "Fine French cognac and our house blend", COGNAC, R0, R1, 197)
    t = max(a, b) + 22
    p.split_section("Vodka, Gin, Rum & Spirits", "Including Japanese vodka and gin from the House of Suntory and Nikka", WHITE_SPIRITS, t)
    p.footer("Please enjoy responsibly. Must be 21 or older to be served alcohol.")

if __name__ == "__main__":
    render([drinks_p1, drinks_p2], "Iki Toro Drink Menu", "../../menus/iki-toro-drink-menu.pdf")
    render([spirits_p1, spirits_p2], "Iki Toro Spirits List", "../../menus/iki-toro-spirits-list.pdf")
