---
name: update-portfolio
description: อัปเดต PORTFOLIO.md (แผนผลงานขอ ผศ.) โดยนับผลงานสอนจาก .Subject/ และงานอำนวยการจาก .Admin/ ให้ครบ — ต้องสั่งจาก root ของคลัง. Use when user says /update-portfolio, อัปเดตพอร์ตโฟลิโอ, or asks to review/sync progress toward ผศ. across trees.
---

# update-portfolio — อัปเดตแผนผลงานขอ ผศ.

กติกาต้นทางฉบับเต็ม: root [`CLAUDE.md`](../../../CLAUDE.md) §1, §3 — skill นี้คร่อม 3 tree
**ต้องรันจาก root ของคลัง (`second-brain/`) ไม่ใช่จากใน `.Research/`** เพราะต้องอ่านทั้ง `.Subject/INDEX.md`
และ `.Admin/` ไปพร้อมกัน เปิด session จาก tree เดียวจะไม่เห็นกติกาของอีกสองฝั่ง

## ขั้นตอน

1. **อ่านสถานะปัจจุบัน** — [`.Research/PORTFOLIO.md`](../../../.Research/PORTFOLIO.md) ทั้งไฟล์
   (ไฟล์นี้เป็นเอกสารยุทธศาสตร์ระดับบน ไม่อยู่ใน MAP.md — อ่านทั้งฉบับเสมอ ไม่ใช้ offset/limit)
2. **เช็คฝั่งงานสอน** — เปิด [`.Subject/INDEX.md`](../../../.Subject/INDEX.md) คอลัมน์ "นับเป็นผลงาน (ผศ.)"
   เทียบกับ §4 ของ PORTFOLIO.md ว่าตรงกันไหม
3. **เช็คฝั่งงานอำนวยการ** — เปิด [`.Admin/_shared/sop/README.md`](../../../.Admin/_shared/sop/README.md)
   ดูสถานะ 🔴/🟡/🟢 ของ SOP/คู่มือ เทียบกับตาราง §5 ทาง ก. ของ PORTFOLIO.md และเช็คว่ามีโครงการ IT ไหน
   บันทึก "โจทย์วิจัยที่งอกได้" ใหม่หรือยัง (ทาง ข. — [`.Admin/CLAUDE.md`](../../../.Admin/CLAUDE.md) กฎ 7)
4. **เช็คฝั่งงานวิจัย** — สถานะโครงการช่องที่ 1/2 ใน §2 ยังตรงกับ `PROJECT.md`/`DECISIONS.md`
   ของแต่ละโครงการที่ผูกอยู่หรือไม่
5. **ถ้ามีอะไรเปลี่ยน** — แก้ตาราง/checklist ที่เกี่ยวข้อง แล้วเพิ่ม 1 แถวใหม่ใน §3
   "ประวัติการตัดสินใจที่คร่อมโครงการ" ระบุวันที่ + สิ่งที่เปลี่ยน + ผล (ห้ามลบแถวเก่า — เป็นบันทึกประวัติ)
6. **อัปเดต frontmatter** — `verified:` และ `updated:` เป็นวันที่วันนี้
7. **ตรวจก่อนจบ** — `powershell -ExecutionPolicy Bypass -File _scripts\check-links.ps1`
   (ไฟล์นี้ลิงก์ข้าม 3 tree เสี่ยงลิงก์เสียมากกว่าไฟล์อื่นในคลัง)
