import urllib.request, ssl
ctx = ssl.create_default_context()
def get(u):
    req = urllib.request.Request(u, headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache','Pragma':'no-cache'})
    r = urllib.request.urlopen(req, timeout=20, context=ctx)
    return r.status, r.read().decode('utf-8','ignore')
# the snippet file itself
s, body = get('https://trishikacarrentalhubli.in/track-conversions.js?v=4')
print('track-conversions.js:', s, '| has whatsapp_click:', 'whatsapp_click' in body, '| has call_click:', 'call_click' in body)
# referenced on pages
for u in ['https://trishikacarrentalhubli.in/?v=4',
          'https://trishikacarrentalhubli.in/services/airport-taxi-hubli/?v=4',
          'https://trishikacarrentalhubli.in/routes/hubli-to-goa-taxi/?v=4']:
    st, b = get(u)
    print(st, u.split('?')[0], '| loads snippet:', 'track-conversions.js' in b)
