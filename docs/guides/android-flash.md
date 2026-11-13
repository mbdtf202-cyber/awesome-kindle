# Android on Kindle (overview)

> Last reviewed: 2026-11-13

Some older Kindles can be reflashed to **Android**, letting you run Android apps (e.g. the
e-ink **WeRead / 微信读书** app). This is the **highest-risk** path — it repartitions storage
and can brick the device. Read the whole official guide before touching anything.

## Prerequisites
- A **supported model** + a **jailbreak** first (see the jailbreak guides).
- KUAL + MRPI installed.
- A full backup and a recovery plan; charged battery; reliable USB cable.

## High-level path
1. Jailbreak → install **KUAL + MRPI**.
2. Install the **uboot** / bootloader package for your exact model.
3. Flash the **Android image** for your model (follow the community guide precisely).
4. Boot Android, install the **WeRead e-ink** APK (or other apps).
5. Keep the original firmware image so you can restore.

## Reality check
- Wrong model/image = **brick**. There is no universal guide.
- Android on e-ink is slow; battery life drops.
- If you only want to read local books, **jailbreak + KOReader** is far safer.

## Official / community
- Start from the [KindleModding wiki](https://kindlemodding.org/) and model-specific threads.
- Example community guide (verify for your model): https://github.com/Ooonana/Guide-to-installing-android-on-kindle

---

## 中文速览
- 部分老机型可刷 **Android**，装微信读书墨水屏版；这是**最高风险**路线，会重新分区、可能变砖。
- 前置：先越狱 → KUAL+MRPI → 按机型装 uboot → 刷对应 Android 镜像 → 装微信读书 → 保留原固件以便恢复。
- 只想读本地书：**越狱 + KOReader** 安全得多。务必按机型找专门教程、先备份。
