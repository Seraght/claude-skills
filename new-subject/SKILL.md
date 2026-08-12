---
name: new-subject
description: เปิดวิชาใหม่ในคลัง second-brain — สร้าง skeleton โฟลเดอร์, ย่อยตารางสอน/มคอ.3 เป็น digest, สร้าง SUBJECT.md, ลงทะเบียนใน INDEX.md. Use when user says /new-subject, เปิดวิชาใหม่, or provides ตารางสอน/มคอ.3 for a course not yet in .Subject/INDEX.md.
---

# new-subject — เปิดวิชาใหม่

กติกาต้นทางฉบับเต็ม: [`.Subject/CLAUDE.md`](../../../.Subject/CLAUDE.md) §3.1 — skill นี้เป็น checklist เรียงลำดับ ห้ามข้ามขั้น

## ขั้นตอน

1. **ตรวจว่ามีอยู่แล้วหรือยัง** — เช็ค [`.Subject/INDEX.md`](../../../.Subject/INDEX.md) ก่อนสร้างซ้ำ
2. **สร้าง skeleton** — โฟลเดอร์ `<รหัสวิชา>-<slug-อังกฤษ>/` (ห้ามเว้นวรรค) พร้อม 5 โฟลเดอร์ย่อย: `source/ digest/ research/ design/ assessment/`
3. **วางต้นฉบับ** — ตารางสอน/มคอ.3 ลง `source/` (ห้ามแก้ไฟล์นี้ทีหลัง)
4. **ย่อยเป็น digest** จาก [`_templates/digest.md`](../../../.Subject/_templates/digest.md) → เขียนเป็น `digest/00-course-syllabus.md`
   ต้องดึงให้ครบ 8 อย่าง: รหัส/ชื่อวิชา · หน่วยกิต · หลักสูตร+ชั้นปี+จำนวนนักศึกษา · ภาค/ปีการศึกษา ·
   CLO และการ map กับ PLO · ตารางรายสัปดาห์ 15 ครั้ง · สัดส่วนคะแนน+สัปดาห์สอบ · ทีมผู้สอน
5. **สร้าง `SUBJECT.md`** จาก [`_templates/SUBJECT.md`](../../../.Subject/_templates/SUBJECT.md)
6. **เพิ่ม 1 แถวใน `INDEX.md`**
7. **เช็คหลักสูตร** — ถ้าหลักสูตรนี้ยังไม่มีใน `_programs/` ให้สร้างโฟลเดอร์ `_programs/<program-slug>/`
   พร้อมบันทึก PLO ไว้ที่นั่น (ไม่ใช่ในวิชา — ดูกฎ 4 เรื่องหลักสูตรเดียวกันอาจมีหลาย มคอ.2 ฉบับ)
8. **ตรวจก่อนจบ** — `powershell -ExecutionPolicy Bypass -File _scripts\check-status.ps1`
   และ `powershell -ExecutionPolicy Bypass -File _scripts\check-links.ps1`
