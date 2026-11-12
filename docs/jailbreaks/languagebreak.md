# LanguageBreak

> **Status:** 🗄️ Archived  ·  **Firmware:** ≤ 5.16.2.1.1  ·  **Models:** Older mainstream models

Archived legacy method for very old firmware (≤ 5.16.2.1.1).

## Compatibility

| Item | Value |
| --- | --- |
| Firmware | ≤ 5.16.2.1.1 |
| Models | Older mainstream models |
| Amazon account | No |
| Ads / Special Offers | No |
| Status | 🗄️ Archived |

## Before you start
1. **Identify your exact device + firmware** — Settings → Device Options → Device Info. Note the full version (e.g. `5.16.2.1.1`) and the model code.
2. **Back up and block OTA** — fill the storage or follow “Prevent Automatic Updates”, so a background update can't kill the process mid-way.
3. **Charge fully and use a reliable USB cable** — never lose power during the process.
4. **Read the official page for this method first** — steps change over time; the official wiki always wins.

## Steps
1. On the Kindle, open the browser and go to the official page for this method (link below).
2. Download the jailbreak package for your exact model / firmware.
3. Run it exactly as the official page says (tap the link / run the script / trigger the exploit).
4. Wait patiently — do **not** unplug or power off while it runs.
5. When it finishes the device usually reboots; confirm if prompted.
6. Verify success with the method's own check (e.g. the jailbreak marker or the provided test).

## After jailbreak — do this immediately
1. Install **Hotfix** — blocks OTA from wiping the jailbreak and prevents bricks.
2. Install **KPM** (Kindle Package Manager) and **Jobman** — your app store and manager.
3. Delete any leftover `.bin` update files from the USB root.
4. Reboot once and confirm the jailbreak survives.

## Rollback & troubleshooting
- Jailbreaking does not flash firmware; a factory reset typically returns to a clean state.
- **Without a jailbreak you cannot downgrade** — never flash a mismatched firmware.
- If the device won't boot, follow the official recovery / serial-flash guide for your model.
- If a step fails, stop, re-check model + firmware, and re-read the official page.

## Official links
- [Wiki](https://kindlemodding.org/jailbreaking/Legacy/LanguageBreak.html)
- [Repo](https://github.com/KindleModding/LanguageBreak)

---

## 中文速览

已归档的旧方案，仅用于极老固件（≤ 5.16.2.1.1）。

- **适用固件：** ≤ 5.16.2.1.1
- **适用机型：** Older mainstream models
- **需要 Amazon 账号：** No　**仅限广告版：** No
- **步骤：** 识别机型固件 → 备份并阻断 OTA → 下载并执行（全程勿断电）→ 成功后**先装 Hotfix** → 再装 KPM / Jobman → 删除根目录 `.bin` → 重启验证。
- **风险：** 没有越狱不能降级，乱刷会变砖；**一切以官方 Wiki 为准**。
