# PowerPoint (.pptx)

## Rules

None yet. A file is finished on its rendered check alone.

**Tested, and needing nothing:** a text box from python-pptx's default package, word wrap on, TH Sarabun New 28 pt, broke Thai between words in PowerPoint with no added markup (2026-10-18, Microsoft 365 on Windows 11). Word's line-breaking rule does not carry over — this is recorded so that it is not copied here by analogy.

## Rendering

```powershell
$p = New-Object -ComObject PowerPoint.Application
try { $x = $p.Presentations.Open($pptx, $true, $false, $false); $x.SaveAs($pdf, 32); $x.Close() }
finally { $p.Quit() }
```

The arguments open it read-only, untitled, and without a window; `32` is PDF.

## Untested

- Thai problems have been met in Office files other than Word before, with no record of which format or what they were. The first one seen again goes here, with the file it was seen in.
- Text that overflows a fixed box, or is shrunk by autofit, given the extra height Thai's stacked marks take.
- A Thai font missing on the machine that presents the file, and what replaces it.
