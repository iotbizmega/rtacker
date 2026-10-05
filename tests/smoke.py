"""Smoke tests for the demo build. Run: python build.py && python tests/smoke.py
Needs: pip install -r requirements-dev.txt && python -m playwright install chromium
Checks: every page renders (desktop+mobile, no horizontal scroll, no JS errors),
realistic vehicle motion (km/tick close to speed), toast cap, license-alert count."""
import sys, pathlib
from playwright.sync_api import sync_playwright
URL = (pathlib.Path(__file__).resolve().parent.parent / 'dist' / 'VSS-Fleet-Platform.html').as_uri()
fails = []
def check(ok, msg):
    print(('OK   ' if ok else 'FAIL ') + msg)
    if not ok: fails.append(msg)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1366, 'height': 800}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(URL); pg.wait_for_timeout(500); pg.evaluate('enter()')
    pages = pg.evaluate('NAV.flatMap(n=>n[1].map(s=>[n[0],s]))'); bad = []
    for w in (1366, 390):
        pg.set_viewport_size({'width': w, 'height': 800})
        for g, s in pages:
            pg.evaluate('([g,s])=>go(g,s)', [g, s]); pg.wait_for_timeout(50)
            n, hs = pg.evaluate("[document.querySelector('#mn').innerText.trim().length,document.documentElement.scrollWidth>innerWidth]")
            if n < 5 or hs: bad.append((w, s))
    check(not bad, f'{len(pages)} pages render at 1366px and 390px, no horizontal scroll {bad}')
    r = pg.evaluate("""()=>{PAU=1;SPD=1;let mx=0,jumps=0,prev={};ID.forEach(i=>prev[i]=LS[i].pos.slice());
      for(let t=0;t<300;t++){step();ID.forEach(i=>{const s=LS[i],d=km(prev[i],s.pos),e=s.spd/3600*12;if(d>e*2.5+0.3)jumps++;mx=Math.max(mx,d);prev[i]=s.pos.slice()})}return{mx,jumps}}""")
    check(r['jumps'] == 0 and r['mx'] < 0.6, f"vehicle motion consistent with speed (max {r['mx']:.2f} km/tick, jumps {r['jumps']})")
    pg.evaluate('for(let i=0;i<60;i++)step()'); pg.wait_for_timeout(200)
    check(pg.locator('#toasts .to').count() <= 3, 'at most 3 toasts at once')
    check(pg.evaluate("ALR.filter(a=>a.ty.includes('گواهینامه')).length") <= 6, 'license alerts are not flooding')
    check(not errs, f'no JS errors {errs[:2]}')
    b.close()
sys.exit(1 if fails else 0)
