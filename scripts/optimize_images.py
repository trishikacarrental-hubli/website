# Phase 3 — image pipeline for /site-optimized/
# PNG/JPEG -> WebP at render-appropriate sizes; clean gallery filenames; og-image recompress.
import os, shutil
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SO = os.path.join(ROOT, 'site-optimized')
IMG = os.path.join(SO, 'images')
GAL = os.path.join(IMG, 'Fleet Gallery')
NEWGAL = os.path.join(IMG, 'gallery')
os.makedirs(NEWGAL, exist_ok=True)

def to_webp(src, dst, max_w, q=78):
    im = Image.open(src)
    if im.mode in ('P',): im = im.convert('RGBA')
    if im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    im.save(dst, 'WEBP', quality=q, method=6)
    print(f'{os.path.relpath(dst, SO):50s} {os.path.getsize(src)//1024:>6} KB -> {os.path.getsize(dst)//1024:>4} KB')

# 1. hero background (desktop LCP)
to_webp(os.path.join(IMG, 'hero-bg.png'), os.path.join(IMG, 'hero-bg.webp'), 1920, 75)

# 2. fleet card renders
for n in ['sedan', 'ertiga', 'innova', 'tempo', 'minibus']:
    to_webp(os.path.join(IMG, f'{n}.png'), os.path.join(IMG, f'{n}.webp'), 640, 82)

# 3. gallery -> clean names (mapping preserved for HTML update)
GALLERY_MAP = [
    ('WhatsApp Image 2026-03-01 at 20.34.50.jpeg', 'fleet-01.webp'),
    ('WhatsApp Image 2026-03-01 at 20.34.55.jpeg', 'fleet-02.webp'),
    ('WhatsApp Image 2026-03-01 at 20.34.58.jpeg', 'fleet-03.webp'),
    ('WhatsApp Image 2026-03-01 at 20.35.05.jpeg', 'fleet-04.webp'),
    ('WhatsApp Image 2026-03-01 at 20.35.07.jpeg', 'fleet-05.webp'),
    ('WhatsApp Image 2026-03-01 at 20.35.09.jpeg', 'fleet-06.webp'),
    ('WhatsApp Image 2026-03-01 at 20.35.11.jpeg', 'fleet-07.webp'),
    ('WhatsApp Image 2026-03-01 at 20.35.14.jpeg', 'fleet-08.webp'),
    ('WhatsApp Image 2026-03-01 at 20.35.18.jpeg', 'fleet-09.webp'),
    ('WhatsApp Image 2026-03-01 at 20.35.22.jpeg', 'fleet-10.webp'),
    ('hero_bg.jpeg', 'fleet-11.webp'),
    ('tempo.jpeg', 'fleet-12.webp'),
]
for old, new in GALLERY_MAP:
    to_webp(os.path.join(GAL, old), os.path.join(NEWGAL, new), 640, 75)

# 4. og-image: keep JPEG (social-crawler compatibility), resize to 1200w
im = Image.open(os.path.join(SO, 'assets', 'og-image.jpg')).convert('RGB')
if im.width > 1200: im = im.resize((1200, round(im.height * 1200 / im.width)), Image.LANCZOS)
im.save(os.path.join(SO, 'assets', 'og-image.jpg'), 'JPEG', quality=80, optimize=True, progressive=True)
print('og-image.jpg ->', os.path.getsize(os.path.join(SO, 'assets', 'og-image.jpg'))//1024, 'KB')

# 5. remove dead/replaced originals from the deploy copy
for p in ['hero_bg.png', 'hero-bg.png', 'sedan.png', 'ertiga.png', 'innova.png', 'tempo.png', 'minibus.png']:
    os.remove(os.path.join(IMG, p))
shutil.rmtree(GAL)   # replaced by /images/gallery/*.webp (incl. unused mobile_hero.jpeg)
print('cleaned originals; site-optimized/images now:')
total = 0
for dp, _, fns in os.walk(IMG):
    for fn in fns:
        total += os.path.getsize(os.path.join(dp, fn))
print('total images dir:', total // 1024, 'KB')
