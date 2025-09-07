from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

# Paths
assets = os.path.join("docs","_assets")
os.makedirs(assets, exist_ok=True)

# Brand colors
BG = (13, 20, 26)          # #0d141a
CYAN = (24, 212, 224)      # #18d4e0
PURPLE = (178, 108, 255)   # #b26cff

def load_font(size):
    # Try a couple of Windows fonts, else default
    for p in (r"C:\Windows\Fonts\segoeui.ttf",
              r"C:\Windows\Fonts\arial.ttf"):
        try:
            return ImageFont.truetype(p, size=size)
        except Exception:
            pass
    return ImageFont.load_default()

def neon_text(img, text, center, font, fill, glow, glow2=None):
    xdraw = ImageDraw.Draw(img)
    bbox = xdraw.textbbox((0,0), text, font=font)
    w, h = bbox[2]-bbox[0], bbox[3]-bbox[1]
    x = center[0] - w//2
    y = center[1] - h//2

    # purple outer glow
    if glow2:
        g2 = Image.new("RGBA", img.size, (0,0,0,0))
        ImageDraw.Draw(g2).text((x,y), text, font=font, fill=(*glow2,255))
        g2 = g2.filter(ImageFilter.GaussianBlur(24))
        img.alpha_composite(g2)

    # inner glow
    g = Image.new("RGBA", img.size, (0,0,0,0))
    ImageDraw.Draw(g).text((x,y), text, font=font, fill=(*glow,255))
    g = g.filter(ImageFilter.GaussianBlur(12))
    img.alpha_composite(g)

    # main text
    ImageDraw.Draw(img).text((x,y), text, font=font, fill=(*fill,255))

def make_logo(path, size=512):
    img = Image.new("RGBA", (size,size), (*BG,255))
    font = load_font(int(size*0.22))
    neon_text(img, "Aldin AI", (size//2, size//2), font, CYAN, PURPLE, glow2=(120,80,200))
    img.save(path, optimize=True)

def make_favicon(path, size=128):
    img = Image.new("RGBA", (size,size), (*BG,255))
    font = load_font(int(size*0.36))
    neon_text(img, "AI", (size//2, size//2), font, CYAN, PURPLE)
    img.save(path, optimize=True)

make_logo(os.path.join(assets,"aldin-logo.png"), 512)
make_favicon(os.path.join(assets,"aldin-favicon.png"), 128)
print("Wrote:", os.path.join(assets,"aldin-logo.png"), os.path.join(assets,"aldin-favicon.png"))
