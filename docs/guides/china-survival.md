# Kindle 退出中国后的生存指南

> Last reviewed: 2026-11-13

> Amazon 已于 2023 年停止 Kindle 中国电子书店运营、2024 年停止相关服务。很多用户反馈
> **联网后本地中文书会被清理**，账号/手机号也可能失效。下面是不踩坑的几条路。

## 先做：防删书（最重要）
1. 开 **飞行模式**，别让设备联网；需要传书时用 **USB**。
2. 把 `documents/` 整目录**备份到电脑**；删除前先导出。
3. 关闭自动更新 / 装 Hotfix 阻断 OTA（见越狱指南）。
4. 用 **Calibre** 管理并在本地转 EPUB/AZW3 再侧载，不依赖云端。

## 路线 A：越狱 + 本地阅读（推荐，风险低）
- 越狱后装 **KOReader**，直接读本地 EPUB/PDF/CBZ；配 **Calibre-Web** 可自建书库、浏览器推送。
- 不需要账号、不联网也能用；笔记用 KOReader 导出（见《KOReader 笔记导出》）。

## 路线 B：微信读书
- **网页版**体验一般（每章联网加载），但零风险：用内置浏览器开 `weread.qq.com`。
- **进阶**：越狱 → 装 KUAL/MRPI → 刷 **Android** → 安装**微信读书墨水屏版**。
  这是社区最常见做法，但**刷 Android 风险高**，务必先看官方/社区教程并备份。
  - 参考路径：越狱 → MRPI + KUAL → uboot → 刷 Android → 装微信读书墨水屏版。

## 路线 C：换区账号
- 把账号切到美亚/其他区可继续用商店（需对应支付/地址），但中文书资源有限。

## 风险与提醒
- 刷 Android / 改分区可能**变砖**；没有把握就先用路线 A（越狱+KOReader）。
- 任何固件/分区操作前，确认机型与固件、备份、留回滚方案。
- 一切以官方 Wiki 与成熟社区教程为准。

---

## English summary
After Kindle exited China (store closed 2023, services 2024), many users report **sideloaded
Chinese books being deleted when the device goes online**. Safest path: **airplane mode + USB
sideload + Calibre**, back up `documents/`, and jailbreak + **KOReader** for local reading.
For **WeRead**, either use the web version (low risk) or the advanced route: jailbreak →
KUAL/MRPI → flash **Android** → install the e-ink WeRead app (high risk — back up first).
Switching to a US/other-region account is another option but has limited Chinese catalog.
