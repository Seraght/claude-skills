# Excel (.xlsx)

## Rules

None yet. A file is finished on its rendered check alone.

**Tested, and needing nothing:** a cell from openpyxl's default package, wrap text on, TH Sarabun New 16 pt, broke Thai between words in Excel with no added markup (2026-10-18, Microsoft 365 on Windows 11). Word's line-breaking rule does not carry over — this is recorded so that it is not copied here by analogy.

## Rendering

```powershell
$x = New-Object -ComObject Excel.Application; $x.Visible = $false; $x.DisplayAlerts = $false
try { $b = $x.Workbooks.Open($xlsx, 0, $true); $b.ExportAsFixedFormat(0, $pdf); $b.Close($false) }
finally { $x.Quit() }
```

The workbook opens read-only; `0` is PDF.

## Untested

- Thai problems have been met in Office files other than Word before, with no record of which format or what they were. The first one seen again goes here, with the file it was seen in.
- Row heights that auto-fit too short, clipping the marks above and below a Thai line.
- Wrapping in merged cells.
