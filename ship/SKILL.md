---
name: ship
description: ปิดงานคลัง second-brain — จัดกลุ่ม commit ตามหัวเรื่อง, เขียนข้อความ commit ภาษาไทยผ่านไฟล์ (-F), regen MAP.md เมื่อจำเป็น, ตรวจสถานะ README. Use when user says /ship, ปิดงาน, commit งานค้าง, or asks to commit/save work in this repo.
---

# ship — ปิดงานเป็น commit ที่สะอาด

## ขั้นตอน

1. **สำรวจงานค้าง** — `git status --short` แล้วจัดกลุ่มไฟล์ตามหัวเรื่อง (วิชา/โครงการ/กติกา)
   หนึ่ง commit = หนึ่งเรื่อง อย่ารวม `feat` เนื้อหากับ `docs` กติกาในก้อนเดียว
2. **ไฟล์แปลกปลอม** — เจอไฟล์ที่ไม่รู้ที่มา (สำเนา conflict ของ Drive เช่น `ชื่อ (1).md`) ให้ถามผู้ใช้ ห้ามเงียบ ๆ add
3. **แตะ `_shared/` หรือ `_domains/`?** → รัน `powershell -ExecutionPolicy Bypass -File _scripts\check-status.ps1`
   สถานะ 🔴/🟡/🟢 ใน README ต้องตรงไฟล์จริงก่อน commit
   **แตะ `.Admin/`?** → ตรวจ diff ด้วยตาอีกรอบว่าไม่มีชื่อ/อีเมล/รหัสของนักศึกษาหรือบุคลากรรายบุคคล
   หลุดเข้ามา ([`.Admin/CLAUDE.md`](../../../.Admin/CLAUDE.md) §6) — commit แล้ว post-commit hook
   เขียน bundle ทันที **ลบย้อนหลังไม่ได้จริง**
4. **ไฟล์ใหญ่เปลี่ยน?** (สร้าง/ขยายไฟล์จน >30 KB) → regen สารบัญ:
   `powershell -ExecutionPolicy Bypass -File _scripts\generate-map.ps1` แล้วรวม `MAP.md` เข้า commit ก้อนสุดท้าย
5. **ข้อความ commit ภาษาไทย: เขียนลงไฟล์ใน scratchpad แล้ว `git commit -F <ไฟล์>`**
   ห้ามใช้ `-m` กับ here-string (PowerShell 5.1 ตัด argument ผิดเมื่อมี `"`) — ดู root [`CLAUDE.md`](../../../CLAUDE.md) §4
   รูปแบบ: บรรทัดแรก `feat:`/`fix:`/`docs:` + สรุปไทย · ตามด้วย bullet รายละเอียด
6. **hooks จัดการที่เหลือเอง** — pre-commit ตรวจลิงก์ (เสีย = commit ไม่ผ่าน → แก้ลิงก์หรือขึ้นบัญชี
   `_scripts/check-links-planned.txt`) · post-commit สำรอง bundle เบื้องหลังอัตโนมัติ
7. **ตรวจจบ** — `git status` ต้องสะอาด ถ้ามีไฟล์ค้างสถานะ M ทั้งที่ไม่ได้แก้ (อาการ Drive stat หลอก
   หลัง checkout ใหญ่) ให้ตรวจ `git hash-object` เทียบ HEAD แล้ว `git add -u` ล้าง — ดู root CLAUDE.md §4
