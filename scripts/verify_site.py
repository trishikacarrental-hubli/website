# Verify site-optimized: parse HTML, check internal links/assets resolve to files
import os, re
from html.parser import HTMLParser

SO = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'site-optimized')
pages = []
for dp, _, fns in os.walk(SO):
    for fn in fns:
        if fn.endswith('.html'):
            pages.append(os.path.join(dp, fn))

class Check(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.stack = []; self.errors = []
        self.voids = {'img','br','meta','link','input','source','hr','area','base','col','embed','track','wbr'}
    def handle_starttag(self, tag, attrs):
        if tag not in self.voids: self.stack.append(tag)
        d = dict(attrs)
        for k in ('href', 'src', 'poster'):
            if k in d and d[k]: self.links.append(d[k])
    def handle_endtag(self, tag):
        if tag in self.voids: return
        if self.stack and self.stack[-1] == tag: self.stack.pop()
        elif tag in self.stack:
            self.errors.append(f'mismatched </{tag}> (open: {self.stack[-3:]})')
            while self.stack and self.stack[-1] != tag: self.stack.pop()
            if self.stack: self.stack.pop()

problems = 0
for p in sorted(pages):
    rel = os.path.relpath(p, SO)
    c = Check(); c.feed(open(p, encoding='utf-8').read())
    if c.stack: print(f'{rel}: UNCLOSED tags: {c.stack}'); problems += 1
    for e in c.errors: print(f'{rel}: {e}'); problems += 1
    for l in c.links:
        if l.startswith(('http', 'tel:', 'mailto:', 'data:', '//')): continue
        path = l.split('#')[0].split('?')[0]
        if not path: continue
        if path.startswith('/'):
            fs = os.path.join(SO, path.lstrip('/').replace('/', os.sep))
        else:
            fs = os.path.join(os.path.dirname(p), path.replace('/', os.sep))
        fs_ix = os.path.join(fs, 'index.html')
        if not (os.path.exists(fs) or os.path.exists(fs_ix)):
            print(f'{rel}: BROKEN ref -> {l}'); problems += 1
print(f'\n{len(pages)} pages checked, {problems} problems')
