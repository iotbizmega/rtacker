# معماری پیشنهادی سامانهٔ واقعی

> **این‌ها پیشنهادند، نه تصمیم نهایی.** پیش از شروع، تیم باید مدل دستگاه‌ها/پروتکل ارتباطی، تعداد خودرو، محل استقرار (ابری/داخلی)، و الزامات امنیتی/قانونی را تأیید کند. پروتکل‌های نام‌برده فرضیه‌اند.

## نمای کلی
```
دستگاه‌ها (GPS/DVR/ADAS/DSM) ──TCP/UDP/MQTT──► Ingestion Gateway ──► Queue (Kafka/Redis Streams/NATS)
                                                         │                       │
                              Media Server ◄─ ویدئو ─────┘                       ├─► Telemetry Worker → TimescaleDB/PostGIS
                              (WebRTC/HLS)                                        ├─► Rules/Alert Engine → Alerts + Notifications
                                   │                                              └─► WebSocket Hub ─► مرورگر (نقشهٔ زنده)
مرورگر (SPA فارسی RTL) ──REST/OpenAPI──► API (احراز هویت، RBAC، CRUD، گزارش) ──► PostgreSQL
                                                                               └► Object Storage (کلیپ/فایل صوتی/گزارش)
```

## مؤلفه‌ها و گزینه‌های پیشنهادی
- **فرانت‌اند:** مهاجرت دمو به SPA ماژولار (TypeScript + React یا Vue + Vite)، RTL، i18n، تقویم شمسی؛ نقشه Leaflet یا MapLibre. هر صفحهٔ فعلی (`docs/PAGES.md`) یک ماژول.
- **API:** سرویس REST با قرارداد OpenAPI (Node/NestJS، Python/FastAPI، یا Go؛ هر کدام تیم بلد است). احراز هویت JWT/OIDC + RBAC بر پایهٔ جدول «نقش»؛ محدودسازی دسترسی بر اساس ناوگان.
- **دیتابیس:** PostgreSQL + PostGIS؛ سری‌زمانی با TimescaleDB یا پارتیشن زمانی. Redis برای کش و presence.
- **ورود داده:** Gateway جدا برای پروتکل دستگاه‌ها (مثلاً JT/T 808 برای موقعیت، JT/T 1078 برای ویدئو، یا MQTT/HTTP سازنده — **باید با مستند دستگاه تأیید شود**).
- **موتور هشدار:** سرویس جدا که صفحات «قوانین آنالوگ/جریان ویدئو/هشدار مجازی/محدوده جغرافیایی» را اجرا می‌کند و Alert می‌سازد.
- **ویدئو:** سرور رسانه (MediaMTX/SRS/ZLMediaKit یا معادل) برای تبدیل به WebRTC/HLS؛ مجوز کوتاه‌عمر برای هر استریم؛ ذخیره‌سازی کلیپ در S3/MinIO.
- **زمان‌واقعی به مرورگر:** WebSocket (یا SSE) با کانال‌های `vehicle:{id}`, `fleet:{id}`, `alerts`.
- **استقرار:** Docker Compose برای توسعه، Kubernetes/VM برای تولید؛ CI در GitHub Actions؛ مانیتورینگ (Prometheus/Grafana)، لاگ ساخت‌یافته.
- **امنیت:** TLS، هش رمز (argon2/bcrypt)، rate-limit، لاگ ممیزی، حداقل دسترسی، پشتیبان‌گیری، رعایت حریم خصوصی تصاویر رانندگان.

## مرزبندی ماژول‌ها (پیشنهاد مخزن)
```
apps/web        فرانت‌اند (جایگزین تدریجی src/)
apps/api        سرویس REST
services/ingest دروازهٔ دستگاه‌ها
services/rules  موتور هشدار
services/media  پیکربندی سرور رسانه
packages/shared تایپ‌ها/قرارداد OpenAPI
legacy-demo/    همین دموی فعلی (src/, assets/, build.py) تا پایان مهاجرت
```
