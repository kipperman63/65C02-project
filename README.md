# 65C02 + VS Code + ca65 starter (macOS-friendly)

**What you get**
- VS Code tasks for `ca65` and `ld65`
- 32 KiB ROM at **$8000..$FFFF** (`cfg/rom_32k_at_8000.cfg`)
- Symbols/map/listing: `build/labels.lbl`, `build/rom.map`, `build/main.lst`

## Prereqs (macOS)
```bash
brew install cc65
```
(Optionally, `brew install acme` if you also want ACME.)

## Build
Open this folder in VS Code, then press **⌘⇧B** to run the **build** task.
Outputs land in `build/`:
- `rom.bin` (32768 bytes)
- `main.lst` (assembler listing)
- `rom.map` (linker map)
- `labels.lbl` (label export)
- `rom.dbg` (debug symbols file)

## Files
- `src/main.s` — minimal 65C02 program with reset & vectors
- `cfg/rom_32k_at_8000.cfg` — linker script
- `.vscode/tasks.json` — build tasks
- `.vscode/settings.json` — file associations & editor prefs

## Notes
- Vectors are assembled into the `VECTORS` segment which the linker places at `$FFFA..$FFFF`.
- If your code grows near `$FFFA`, the linker will error before overlapping the vectors.
- Change ROM base/size by editing `cfg/rom_32k_at_8000.cfg`.

Happy hacking!
