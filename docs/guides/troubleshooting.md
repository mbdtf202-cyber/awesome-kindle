# Troubleshooting & brick rescue

> Always cross-check with the official wiki: https://kindlemodding.org/

## Common issues
| Symptom / error | Likely cause | Fix |
| --- | --- | --- |
| Jailbreak "not supported" | Firmware/model mismatch | Re-check exact version; use the matching method |
| Update wipes jailbreak | OTA installed | Install **Hotfix**; delete `.bin`; block updates |
| `UPDATE ERROR 2` | Wrong model/firmware update file | Download the exact `.bin` for your device |
| `UPDATE ERROR 4` | Corrupted download | Re-download, verify size, retry |
| Stuck on "Updating" | Interrupted / bad file | Wait, then force-restart; re-flash correct file |
| KUAL won't open | Missing Hotfix / wrong install | Reinstall Hotfix + KUAL per wiki |
| No Wi-Fi after tweak | Network service broken | Revert the tweak; reboot; factory reset last resort |

## Brick rescue decision tree
1. **Does it boot to the UI?** → Yes: reinstall Hotfix, delete `.bin`, reboot.
2. **Boot loop / stuck logo?** → Try a **forced restart** (hold power ~20s). Then a **factory reset** from recovery.
3. **Still dead?** → **Serial/Downgrade recovery** per your model (see wiki). Without a jailbreak you cannot simply downgrade.
4. **Hardware-level** → last resort: serial flash / recovery image per the official guide.

## Golden rules
- Model + firmware must match **exactly**.
- Never flash a mismatched `.bin`.
- Keep **Hotfix** installed and OTA blocked.
- When unsure, stop and read the official page.

---

## 中文速览

- 任何操作先对照官方 Wiki。
- 常见：`UPDATE ERROR 2` = 机型/固件包不匹配；`ERROR 4` = 文件损坏；越狱被 OTA 覆盖 = 没装 Hotfix。
- 救砖顺序：能进系统→重装 Hotfix/删 `.bin`；卡 logo→强制重启/恢复出厂；仍不行→按机型串口/降级恢复；最后才是硬件级。
- 铁律：机型固件必须完全匹配，绝不乱刷 `.bin`，始终装 Hotfix + 阻断 OTA。
