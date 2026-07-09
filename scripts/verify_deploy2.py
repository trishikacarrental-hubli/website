import urllib.request, ssl
ctx = ssl.create_default_context()
def body(u):
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache', 'Pragma': 'no-cache'})
    return urllib.request.urlopen(req, timeout=20, context=ctx).read().decode('utf-8', 'ignore')
h = body('https://trishikacarrentalhubli.in/?v=2')
print('video tag on homepage:', '<video' in h)
print('fonts async (media="print"):', 'media="print"' in h)
print('poster preload link:', 'rel="preload" as="image" href="images/hero-poster.webp"' in h)
c = body('https://trishikacarrentalhubli.in/style.css?v=2')
print('css mobile poster bg:', "url('images/hero-poster.webp')" in c)
print('css video display none:', 'display: none;' in c.split('.hero-mobile-video')[-1][:120])
