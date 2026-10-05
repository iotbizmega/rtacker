## Single-file HTML + template/build split
- Chose: یک فایل HTML مستقل؛ تصاویر base64 با build.py
- Because: کاربر فایل قابل‌دانلودی می‌خواهد که روی هر مرورگری باز شود
- Rejected: چندفایلی/فریم‌ورک

## Persian RTL labels, Latin identifiers
- Chose: متن فارسی؛ شناسهٔ خودرو/کانال لاتین (102 [جلو])
- Because: وفاداری به UI اصلی

## Menu order locked
- Chose: پیشگیری، پایش لحظه‌ای، مستندات / شواهد، عملیات، نگهداری، گزارش‌ها، داشبورد
- Because: ترتیب تأییدشده از اسکرین‌شات‌ها

## Map: OSM → CARTO → Esri chain
- Chose: Leaflet + Esri street default, fallback OSM-France / OpenTopoMap, layer switcher, SVG fallback
- Because: OSM tiles blocked from file://; CARTO now needs API key
- Rejected: OSM direct, CARTO

## Camera images from user's screenshots
- Chose: crop 6 tiles from the video-wall screenshot (assets/crops)
- Because: user asked to use their images; lightbox enlarges them

## Sub-pages are plausible sample templates
- Chose: generic table spec `S` + custom `CU` pages with fake Persian data
- Because: user wanted every submenu to look professional; real content unknown (not in screenshots)

## Responsive
- Chose: breakpoints 900/480, hamburger menu, stacked columns, horizontally-scrolling tables
- Because: user reported not responsive on mobile/tablet; verified by Playwright at 390 and 820 px

## Live engine as separate src/live.js
- Chose: ماژول جدا که build.py در template تزریق می‌کند؛ توابع go/stc/stab با wrapper بازنویسی شدند
- Because: template را کوچک نگه می‌دارد و تغییرات زنده یک‌جا هستند
- Rejected: بازنویسی کامل template

## 5-minute cycle with time-lapse odometer
- Chose: چرخهٔ ۳۰۰ ثانیه‌ای تکرارشونده؛ کیلومترشمار ×۱۲ فشرده؛ آستانه‌محور + سناریو برای هشدارها
- Because: کاربر می‌خواست در پرزنت ۵ دقیقه‌ای ارقام واقعاً تغییر کنند
- Rejected: داده تصادفی بی‌منطق

## Phase 2 plan stored in NEXT_PHASE.md
- Chose: همهٔ درخواست‌های کاربر (نقشهٔ متحرک، ناوگان ×۵، موتور هشدار، ویدئوی واقعی دوربین‌ها، فهرست ارتقاء حرفه‌ای) در یک فایل دستورالعمل داخل زیپ؛ اجرا با جملهٔ «شروع کن»
- Because: کاربر می‌خواهد زیپ را در چت جدید آپلود کند و Claude بدون توضیح مجدد اجرا کند
- Note: دانلود ویدئو ممکن است به‌خاطر محدودیت شبکهٔ sandbox شدنی نباشد؛ جایگزین = دادن عبارت جستجو به کاربر

## Live map motion patch
- Chose: ردمسیر + رنگ وضعیت + transition CSS + flyTo در msync
- Because: در زوم ۸ حرکت ۳px/s دیده نمی‌شد؛ ردمسیر و رنگ حرکت را قابل‌مشاهده می‌کند
- Note: علت واقعی با Playwright تأیید نشد

## Generated fleet via vGP profiles
- Chose: تولید ۲۷ خودرو با seed ثابت (sin-hash) و پروفایل حرکت/پارک/آفلاین؛ نام‌های جدید با پیشوند v (تداخل FM با فرم تنظیمات)
- Because: داده تکرارپذیر و بدون تصادف؛ تداخل نام کل اسکریپت را از کار انداخته بود

## Tree/table override pattern
- Chose: بازتعریف `tree` و `stc` در انتهای live.js (با `let tree`)؛ جستجو فقط `#tl` را بازرسم می‌کند
- Because: فوکوس input حفظ شود و template کوچک بماند

## CRUD seeded from live data
- Chose: S['خودرو'/'ناوگان'/'راننده'].r در زمان بارگذاری از V/LS/DRV ساخته می‌شود
- Because: یک منبع حقیقت؛ ۳۰ ردیف همیشه با درخت و جدول وضعیت یکسان است

## Rules drive alerts via A() wrapper
- Chose: بازنویسی A() و hook بعد از step؛ قانون = منبع حقیقت (آستانه/شدت/فعال/اقدام) و هشدارهای سخت‌کد داخلی مسدود
- Because: تغییر در جدول تنظیمات باید فوراً روی هشدارها اثر کند
- Note: پیامک/ایمیل فقط ثبت لاگ شبیه‌سازی‌شده است، ارسال واقعی نیست

## Escalation/notification state in NS
- Chose: تنظیمات اعلان در آبجکت NS (حافظهٔ صفحه)، ارتقاء با شمارش ثانیه‌های شبیه‌سازی (SPD)
- Because: ساده و قابل‌مشاهده در دمو؛ با ×۱۰ سرعت هم متناسب است

## Video: optional embed, JPG fallback
- Chose: build.py ویدئوهای موجود در assets/videos را embed می‌کند؛ نبودن فایل = JPG
- Because: دانلود در sandbox ممکن نبود؛ کاربر خودش ویدئو می‌دهد

## Dashboard: exceptions first
- Chose: ۴ KPI اصلی + فهرست «نیازمند توجه»؛ هشدارهای «عادی» (ورود/خروج محدوده) در شمارندهٔ «هشدار باز» نمی‌آیند
- Because: ۳۶۰+ هشدار عادی KPI را بی‌معنا می‌کرد

## Historical video = sample poster unless videos exist
- Chose: پخش‌کنندهٔ تاریخی با ساعت شبیه‌سازی‌شده؛ بدون ویدئو فقط تصویر نمونه و یادداشت صریح
- Because: ادعای «ویدئوی واقعی» نادرست است

## Sort mutates DB in place
- Chose: مرتب‌سازی جدول CRUD ترتیب ردیف‌های DB را عوض می‌کند (نه نمای جدا)
- Because: ساده؛ اندیس‌های ویرایش/حذف با نمایش هم‌خوان می‌مانند

## Header responsive trade-off
- Chose: کنترل‌های اضافه (نقش/نمایش/Ctrl+K) در ≤۱۲۶۰px پنهان می‌شوند
- Because: هدر تک‌ردیفی با nowrap سرریز می‌کرد؛ جایگزین (wrap/منوی ⋯) پیچیده‌تر بود

## No On-time widget
- Chose: ویجت On-time ساخته نشد
- Because: داده‌ای برای محاسبهٔ صادقانه ندارد؛ چیزی ساختگی «واقعی» نشان داده نشود

## Column hiding via CSS, selection checkbox inside first cell
- Chose: پنهان‌کردن ستون با nth-child و قراردادن چک‌باکس داخل اولین سلول
- Because: هندلر مرتب‌سازی به اندیس th وابسته است؛ افزودن/حذف ستون واقعی آن را می‌شکست
