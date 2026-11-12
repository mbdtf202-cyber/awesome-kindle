# Troubleshooting & brick rescue

> Always cross-check with the official wiki: https://kindlemodding.org/
> Rule #1: **model + firmware must match exactly**; never flash a mismatched `.bin`.

## By symptom (quick table)
| Symptom / error | Likely cause | Fix |
| --- | --- | --- |
| Jailbreak "not supported" | Firmware/model mismatch | Re-check exact version; use the matching method |
| Update wipes jailbreak | OTA installed | Reinstall **Hotfix**, delete `.bin`, block updates |
| `UPDATE ERROR 2` | Wrong model/firmware update file | Download the exact `.bin` for your device |
| `UPDATE ERROR 4` | Corrupted download | Re-download, verify size, retry |
| Error `007` on Hotfix | Hotfix package/model mismatch or partial download | Re-download the Universal Hotfix; try re-running it |
| Hotfix runs then **crash dump**, `;log` stops | Known on PW3 / 5.16.2.1.1 with some Hotfix builds | Reboot fully; retry Hotfix; if still failing, a full reboot usually restores `;log` |
| KUAL opens then returns to home | Hotfix/MRPI not installed in order | Install Hotfix → MRPI → KUAL; full reboot |
| `;log mrpi` does nothing | `mrpackages/` missing or MRPI not installed | Put the `.bin` in `mrpackages/`, install MRPI first |
| KUAL & Hotfix vanish after reset | Factory reset wiped booklets | Reinstall Hotfix, then MRPI, then KUAL |
| Can't write/delete over USB | Filesystem quirk after JB | Reboot; use a file manager app or `scp`; re-mount |

## By device
- **PW3 / 5.16.2.1.1** — many Hotfix 2.x crash reports. Try a full reboot after the booklet; `DISABLE_CORE_DUMP` empty file reduces crash dumps. WB2 recent builds may not need the Hotfix at all — check the method page.
- **K4 / DX / DXG** — modern Hotfix does **not** support these. Use NiLuJe's legacy K5 jailbreak + hotfix from MobileRead.
- **PW1 / old PW5 & HTTPS fails** — the built-in browser often can't load HTTPS. Host the jailbreak page locally over **http** (`node ./api/index.js` → `http://<your-ip>:3000`) or use an http mirror.
- **Colorsoft** — jailbreak works, but the "stay-jailbroken after reboot / Hotfix" step was unreliable; read the current method page.
- **MTP Kindles** — the disk-filler script may not work; fill storage manually with junk files (and remove `.partial.tmp.bin`).

## KPM not installing / add-repo fails
- The `;` search-bar commands are whitelisted by Amazon's `scriptExecutor` — arguments with `:` or `.` (e.g. a repo URL) are **silently dropped**.
- Workaround: install via **KPM scriptlet** or run `kpm install file:///...` from **kterm**; or use the repo's install scriptlet instead of a raw URL.

## Brick rescue decision tree
1. **Boots to UI?** → reinstall Hotfix, delete `.bin`, reboot.
2. **Boot loop / stuck logo?** → forced restart (hold power ~20s); then recovery factory reset.
3. **Still dead?** → serial / downgrade recovery per your model — **downgrade requires an existing jailbreak**.
4. **Hardware-level** → last resort: serial flash / recovery image.

---

## 中文速览

- 铁律：机型+固件必须完全匹配，绝不乱刷 `.bin`；始终装 Hotfix + 阻断 OTA。
- 错误码：`UPDATE ERROR 2`=包不匹配；`UPDATE ERROR 4`=文件损坏；`007`=Hotfix 包不匹配/没下全。
- PW3/5.16.2.1.1 Hotfix 崩溃：整机重启后再试；`DISABLE_CORE_DUMP` 可减少崩溃转储。
- K4/DX/DXG 新版 Hotfix 不支持，用 NiLuJe 旧版 K5 越狱。
- PW1/老 PW5 打不开 HTTPS：本地用 http 托管（`node ./api/index.js`）。
- KPM add-repo 带 URL 会被 `;` 命令白名单吞掉：改用 KPM scriptlet 或 `kterm` 里 `kpm install file://...`。
- 救砖顺序：进系统→重装 Hotfix/删 bin；卡 logo→强制重启/恢复出厂；仍不行→按机型串口/降级（需已越狱）；最后硬件级。
