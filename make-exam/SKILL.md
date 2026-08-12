---
name: make-exam
description: ออกข้อสอบสำหรับวิชาในคลัง second-brain — สร้าง blueprint ผูก CLO/Bloom, item bank, เฉลย, rubric ตามลำดับที่กำหนด. Use when user says /make-exam, ออกข้อสอบ, or asks to write midterm/final/practical/quiz items for a course.
---

# make-exam — ออกข้อสอบ

กติกาต้นทางฉบับเต็ม: [`.Subject/CLAUDE.md`](../../../.Subject/CLAUDE.md) §3.3 — skill นี้เป็น checklist เรียงลำดับ ห้ามข้ามขั้น
หลักการอ้างอิงหลัก: [`_shared/assessment/`](../../../.Subject/_shared/assessment/)
(blooms-taxonomy, test-blueprint, item-writing, rubric-design, practical-exam, item-analysis)

## ขั้นตอน

1. **ระบุชุดข้อสอบ** — สร้าง/เปิด `assessment/<ปีการศึกษา พ.ศ.>/<midterm|final|practical|quiz-XX>/`
2. **อ่าน syllabus** — `digest/00-course-syllabus.md` ของวิชานั้น ดึง CLO, สัดส่วนคะแนน, จำนวนชั่วโมงสอนแต่ละบท
3. **ค้นคว้าเฉพาะชุดนี้ถ้าจำเป็น** → เขียนลง `00-research.md` (ห้ามค้นซ้ำของที่มีอยู่แล้วใน `_shared/assessment/` — กฎ 1)
4. **เขียน `01-blueprint.md`** จาก [`_templates/blueprint.md`](../../../.Subject/_templates/blueprint.md) —
   ทุกข้อต้อง map กับ **CLO** และให้น้ำหนักข้อสอบ**สอดคล้องจำนวนชั่วโมงสอน**ของแต่ละบทตาม syllabus จริง (ห้ามเดา)
5. **เขียน `02-items.md`** จาก [`_templates/item-bank.md`](../../../.Subject/_templates/item-bank.md) —
   **ทุกข้อต้องระบุ CLO + ระดับ Bloom กำกับ** อ้าง [`blooms-taxonomy.md`](../../../.Subject/_shared/assessment/blooms-taxonomy.md)
   และ [`item-writing.md`](../../../.Subject/_shared/assessment/item-writing.md)
6. **เขียน `04-answer-key.md`** — เฉลยทุกข้อ พร้อมเหตุผลของตัวลวง (distractor) ถ้าเป็นข้อสอบปรนัย
7. **เขียน `05-rubric.md`** จาก [`_templates/rubric.md`](../../../.Subject/_templates/rubric.md) เฉพาะข้อที่เป็นอัตนัย/ปฏิบัติ
   อ้าง [`rubric-design.md`](../../../.Subject/_shared/assessment/rubric-design.md) — ถ้าเป็นสอบปฏิบัติให้อ้าง
   [`practical-exam.md`](../../../.Subject/_shared/assessment/practical-exam.md) เพิ่ม
8. **ถ้าแยกเล่มข้อสอบจาก item bank** → เขียน `03-paper.md` เพิ่ม
9. **ตรวจก่อนจบ** — รวมน้ำหนักคะแนนใน blueprint ต้องตรงกับสัดส่วนใน syllabus แล้วรัน
   `powershell -ExecutionPolicy Bypass -File _scripts\check-links.ps1`
