# Add track-conversions.js to /site-optimized/ and reference it on every HTML page.
# Idempotent: skips pages that already load it.
import os, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SO = os.path.join(ROOT, 'site-optimized')

# 1. copy the snippet into the site root
src = os.path.join(ROOT, 'ads', 'import', 'track-conversions.js')
dst = os.path.join(SO, 'track-conversions.js')
shutil.copyfile(src, dst)
print('copied track-conversions.js ->', os.path.relpath(dst, SO))

TAG = '  <script src="/track-conversions.js" defer></script>\n'
n_added = n_skip = 0
for dp, _, fns in os.walk(SO):
    for fn in fns:
        if not fn.endswith('.html'):
            continue
        p = os.path.join(dp, fn)
        html = open(p, encoding='utf-8').read()
        if 'track-conversions.js' in html:
            n_skip += 1
            continue
        # insert right before the closing </body>
        if '</body>' in html:
            html = html.replace('</body>', TAG + '</body>', 1)
            open(p, 'w', encoding='utf-8').write(html)
            n_added += 1
        else:
            print('  WARN no </body>:', os.path.relpath(p, SO))
print(f'added to {n_added} pages, skipped {n_skip} already-present')
