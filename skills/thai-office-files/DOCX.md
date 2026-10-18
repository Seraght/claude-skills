# Word (.docx)

## Rules

### Word breaks Thai into words only when two conditions both hold

1. **The text carries the complex-script flag `<w:cs/>`.** Set it once in the document defaults — `<w:docDefaults><w:rPrDefault><w:rPr>` in `styles.xml` — or in the `Normal` style, and every run inherits it; setting it on each run works the same.
2. **`settings.xml` carries a `<w:compat>` element** holding a compatibility mode of 14 or 15, or `<w:applyBreakingRules/>`. As Word writes it:

   ```xml
   <w:compat><w:compatSetting w:name="compatibilityMode" w:uri="http://schemas.microsoft.com/office/word" w:val="15"/></w:compat>
   ```

   A package with no `settings.xml`, or with no `<w:compat>` in it, opens in compatibility mode 12.

With either missing, Word reads a stretch of Thai with no spaces as one long word. It ends the line at the last space it found — leaving that line short — and then breaks the long "word" wherever the right margin falls, inside a word: `สื่|อสาร`, `การวั|ด`. The forced lines reach the margin like well-broken ones, so line length cannot tell them apart; the line ends can. Under Thai distributed alignment the short line is then stretched to the margin, which is the symptom people see first.

**What the usual tools give by default:**

| Built with | `<w:cs/>` | `<w:compat>` | Thai breaks |
|---|---|---|---|
| Word itself | written on each run | mode 15 | between words |
| python-docx | absent | mode 14 | inside words — add `<w:cs/>` to the document defaults |
| Hand-written OOXML | whatever was written | whatever was written | between words only with both |

**Evidence** (2026-10-18; Microsoft 365 Word on Windows 11; TH Sarabun New 16 pt; one long paragraph; breaks read from the exported PDF):

- Twelve packages without `settings.xml` — runs bare, with fonts, or with `<w:cs/>`; language set East-Asian or bidi; left or Thai distributed — all broke inside words. Word reported them, and one with only `<w:applyBreakingRules/>`, as compatibility mode 12 (`Document.CompatibilityMode`).
- `<w:cs/>` alone, and `<w:compat>` alone (mode 15, `applyBreakingRules`, or both), broke inside words; both together broke between words in all six combinations tried.
- From a document Word made itself, each of its 14 `settings.xml` elements was removed in turn: only removing `<w:compat>` broke inside words. Keeping one child of `<w:compat>` at a time: `compatibilityMode` alone and `applyBreakingRules` alone each sufficed; none of the other five did.
- `<w:cs/>` in `docDefaults`, or in the `Normal` style, with bare runs, broke between words like `<w:cs/>` on each run.
- python-docx's default package (mode 14): inside words without `<w:cs/>`, between words with it.

Why this is checked on the page rather than in the markup: [ADR 0021](../../docs/adr/0021-a-thai-file-is-checked-on-the-page.md).

## Rendering

```powershell
$w = New-Object -ComObject Word.Application; $w.Visible = $false; $w.DisplayAlerts = 0
try { $d = $w.Documents.Open($docx, $false, $true); $d.ExportAsFixedFormat($pdf, 17); $d.Close($false) }
finally { $w.Quit() }
```

`17` is PDF. The document opens read-only, so the export never alters the file being checked.

## Untested

- The Thai font has to sit in the complex-script slot, `<w:rFonts w:cs="…"/>` — python-docx's `font.name` sets only `ascii` and `hAnsi`.
- Bold and size need their complex-script twins, `<w:bCs/>` and `<w:szCs/>`, to reach Thai text.
- Exact line spacing clips the marks above and below a Thai line.
- What docx-js — the library Anthropic's docx skill builds with — writes by default.
- Word for Mac, and Word versions other than the one above.
