import urllib.request, ssl
ctx = ssl.create_default_context()
urls = [
    'http://trishikacarrentalhubli.in/',
    'http://www.trishikacarrentalhubli.in/',
    'https://trishikacarrentalhubli.in/',
    'https://www.trishikacarrentalhubli.in/',
    'https://trishikacarrentalhubli.in/index.html',
    'https://trishikacarrentalhubli.in/nonexistent-page-xyz',
    'https://trishikacarrentalhubli.in/contact/',
    'https://trishikacarrentalhubli.in/wp-admin/',
    'https://trishikacarrentalhubli.in/style.css',
    'https://trishikacarrentalhubli.in/script.js',
    'https://trishikacarrentalhubli.in/images/hero-bg.png',
]
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k): return None
op = urllib.request.build_opener(NoRedirect, urllib.request.HTTPSHandler(context=ctx))
for u in urls:
    req = urllib.request.Request(u, headers={'User-Agent':'Mozilla/5.0 audit','Accept-Encoding':'gzip, br'})
    try:
        r = op.open(req, timeout=20)
        code, h = r.status, r.headers
    except urllib.error.HTTPError as e:
        code, h = e.code, e.headers
    except Exception as e:
        print(f'{u}\n  -> ERROR {e}'); continue
    loc = h.get('Location',''); enc = h.get('Content-Encoding','none')
    cl = h.get('Content-Length','?'); cache = h.get('Cache-Control','-'); ct = h.get('Content-Type','')
    server = h.get('Server',''); xcto = h.get('X-Content-Type-Options','-')
    print(f'{u}\n  -> {code} {("-> "+loc) if loc else ""} enc:{enc} len:{cl} cache:{cache} ct:{ct} server:{server} xcto:{xcto}')
