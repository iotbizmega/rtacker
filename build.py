# Build: python3 build.py  ->  dist/VSS-Fleet-Platform.html
# Also inlines src/live.js (live engine + new pages) at /*__LIVE__*/.
# Embeds the 6 camera crops (assets/crops) into src/template.html as base64 (placeholder __IMS__).
import json,base64,os
D=os.path.dirname(os.path.abspath(__file__))
N=['102-front','102-back','106-ch1','106-ch2','108-front','108-back']  # order = IM[0..5] in the template
L=['data:image/jpeg;base64,'+base64.b64encode(open(f'{D}/assets/crops/{n}.jpg','rb').read()).decode() for n in N]
# optional real camera videos: assets/videos/<name>.mp4|webm (same names as crops) -> base64 into live.js (/*__VIDS__*/)
VD=[]
for n in N:
    for e,m in (('mp4','video/mp4'),('webm','video/webm')):
        f=f'{D}/assets/videos/{n}.{e}'
        if os.path.exists(f): VD.append('data:%s;base64,'%m+base64.b64encode(open(f,'rb').read()).decode()); break
    else: VD.append(None)
print('videos embedded:',sum(1 for x in VD if x),'of',len(N),'(%d KB)'%(sum(len(x) for x in VD if x)//1024))
CV=('data:video/webm;base64,'+base64.b64encode(open(f'{D}/assets/videos/clip-fatigue.webm','rb').read()).decode()) if os.path.exists(f'{D}/assets/videos/clip-fatigue.webm') else None  # __CLIPV__
FN='data:font/woff2;base64,'+base64.b64encode(open(f'{D}/assets/fonts/Vazirmatn.woff2','rb').read()).decode()
LV=open(f'{D}/src/live.js',encoding='utf-8').read().replace('/*__VIDS__*/[]',json.dumps(VD)).replace('/*__FONT__*/""',json.dumps(FN)).replace('/*__CLIPV__*/""',json.dumps(CV))
LG=lambda n:'data:image/png;base64,'+base64.b64encode(open(f'{D}/assets/brand/{n}.png','rb').read()).decode()
t=open(f'{D}/src/template.html',encoding='utf-8').read().replace('__LOGO96__',LG('logo96')).replace('__LOGO256__',LG('logo256')).replace('__IMS__',json.dumps(L)).replace('/*__LIVE__*/',LV)
os.makedirs(f'{D}/dist',exist_ok=True)
open(f'{D}/dist/VSS-Fleet-Platform.html','w',encoding='utf-8').write(t)
print('built',len(t)//1024,'KB')
