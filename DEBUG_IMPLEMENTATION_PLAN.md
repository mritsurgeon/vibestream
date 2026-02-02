# VibeStream Debug Implementation Plan

Based on codebase review, Kodi forum research, and web search for:
- **NoneType / object not subscriptable** errors
- **Control 55 in window 10025** focus errors
- **sqlite3 is not defined** (or "name sqlite3 is not defined")

---

## 1. Root cause summary

| Issue | Cause | Fix |
|-------|--------|-----|
| **sqlite3 is not defined** | `cache_manager.py` imports `sqlite3 as database` but uses `sqlite3.OperationalError` in except block. The name in scope is `database`, not `sqlite3`. | Use `database.OperationalError` (or keep `import sqlite3 as database` and reference `database` only). |
| **NoneType / object not subscriptable** | Code uses `x[0]`, `fetchone()[0]`, or `new_value[1]` without checking that the value is non-None or that the sequence has enough elements. | Add null/empty checks before subscript; use safe get pattern (e.g. `(row[0] if row else None)`). |
| **Control 55 / window 10025** | Kodi skin/core tries to focus control ID 55 in the Videos window (10025 = MyVideoNav). Often a list view. Occurs when the addon leaves the list in an inconsistent state (e.g. no items, wrong content) or when the skin expects a control that isn’t present. | Ensure addon always calls `end_directory()` and passes valid list/content; document as known skin/Kodi behavior; avoid triggering navigation with empty or invalid lists. |

---

## 2. Fixes implemented

### 2.1 sqlite3 not defined
- **File:** `plugin.video.fenlight/resources/lib/modules/cache_manager.py`
- **Change:** In the `except` block use `database.OperationalError` instead of `sqlite3.OperationalError` (module is imported as `import sqlite3 as database`).

### 2.2 NoneType / subscript safety
- **settings_cache.py `set_from_list`:** Guard `new_value[1]`: only use subscript if `new_value` is a list/tuple with at least 2 elements; otherwise skip or use a safe default.
- **menu_editor.py:** `match = [i for i in x[1] if ...][0]` — already in try/except; ensure `x[1]` exists (e.g. `if not x or len(x) < 2: continue`).
- **extras.py:** `self.mode_config.get(self.mode, self.mode_config[0])` — use `self.mode_config.get(self.mode, self.mode_config.get(0, ()))` so we never assume key `0` exists.
- **BaseCache.get (base_cache.py):** When using `cache_data` from `fetchone()`, guard `cache_data[1]` before `json.loads` (e.g. only parse if `cache_data` and `len(cache_data) > 1` and `cache_data[1]` is not None).
- **trakt_cache / other caches:** Any `fetchone()` result used as `row[0]` or `row[1]`: check `row is not None` and `len(row)` as needed before subscripting.
- **kodi_utils / base_cache clear_icons:** `icon` and `fanart` from `fetchone()` — already checked `if icon is not None` / `if fanart is not None` before `icon[0]`; keep pattern consistent elsewhere.

### 2.3 Control 55 / window 10025
- **Documentation:** Add a short note in README (or this doc): “Control 55 in window 10025” is a known Kodi/skin message; enable Debug Log and check for addon errors; ensure addon always ends directory and doesn’t open empty lists.
- **Code:** Already ensured `Navigator.main()` always calls `end_directory()` (with try/except and fallback). No further code change for Control 55 beyond keeping directory/list handling robust.

---

## 3. Files modified (checklist)

1. **cache_manager.py** — use `database.OperationalError` instead of `sqlite3.OperationalError`. ✓
2. **settings_cache.py** — guard `set_from_list`: validate `new_value` is tuple/list with ≥2 elements before `new_value[1]`. ✓
3. **menu_editor.py** — in `_remove_active_shortcut_folder`, check `x` and `x[1]` exist and use non-empty `matches` before `[0]`; catch `IndexError, TypeError, KeyError`. ✓
4. **extras.py** — use `self.mode_config.get(0, ())` and `.get(self.mode, default_tasks)` so no bare `[0]` on dict; build `task_names` safely. ✓
5. **base_cache.py** — in `BaseCache.get`, only use `cache_data` when not None and `len(cache_data) >= 2`; guard `json.loads` when `cache_data[1]` is not None. ✓
6. **trakt_cache.py** — in `get()` and `reset_activity()`, guard `fetchone()` result: check not None, len ≥ 1, and `data[0]` not None before `json.loads`. ✓
7. **meta_cache.py** — guard all `fetchone()` uses: check not None, len ≥ 2 (or ≥ 3 for get_function), and relevant index not None before eval/use. ✓
8. **navigator_cache.py** — guard `row` from fetchone/fetchall: check not None, len, and row[0]/row[1] not None before eval. ✓
9. **README** — added “Control 55 / window 10025” and “NoneType / sqlite3” troubleshooting notes. ✓

---

## 4. References

- Kodi forum: Control 55 / window focus — https://forum.kodi.tv/showthread.php?tid=345281  
- Window 10025 = Videos (MyVideoNav); control 55 often list view; enable Debug Log for real cause.
- NoneType subscript: add null checks and safe get patterns before `[]`.
- sqlite3 in Kodi: use the same name as in the import (e.g. `database` when `import sqlite3 as database`).
