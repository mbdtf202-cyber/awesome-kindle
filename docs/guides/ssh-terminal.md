# SSH & terminal on Kindle

With a jailbreak you can get a shell — locally with **kterm**, remotely over **SSH**.

## Local terminal
1. Install **kterm** via KPM (or manually).
2. Launch it from KUAL/Jobman — you get a shell on the device.

## Enable SSH (USBNetLite)
1. Install **USBNetLite** → https://github.com/notmarek/kindle-usbnetlite
2. Choose USB or Wi-Fi mode; note the device IP.
3. Set a root password (per its README) before exposing it on Wi-Fi.

## Connect from your computer
```bash
ssh root@<kindle-ip>
# or over USB (usbnet): ssh root@192.168.15.244
```
- Copy files: `scp book.epub root@<kindle-ip>:/mnt/us/documents/`
- Be careful: you can break the system as root. Keep a backup and Hotfix installed.

---

## 中文速览

- **本地终端**：KPM 装 **kterm**，从 KUAL/Jobman 启动即得 shell。
- **开 SSH**：装 **USBNetLite**，选 USB/Wi-Fi 模式，记下 IP，先设 root 密码再对外。
- **连接**：`ssh root@<ip>`；传文件 `scp book.epub root@<ip>:/mnt/us/documents/`。
- **注意**：root 能把系统搞坏；务必装 Hotfix 并备份。
