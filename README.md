# VibeStream

VibeStream is a high-performance, modular Kodi addon for streaming from Debrid services and Easynews. It is a modernized and refined version of the classic Fen Light, rebuilt with a focus on reliability, visual excellence, and personalized discovery.

## ✨ Key Features

- **🛡️ Auto-Fallback Playback**: Intelligent watchdog that detects buffer issues or resolve failures and automatically steps down to the next best source.
- **📈 Hoster Health Scoring**: Performance-based provider ranking that deprioritizes unreliable hosters based on success rates and latency.
- **🎯 Smart Recommendations**: A "New For You" discovery engine that analyzes your watch history and suggests personalized content based on your favorite genres.
- **⚡ Adaptive Quality Presets**: Quickly toggle between 4K, Balanced, and Efficient streaming modes to match your bandwidth.
- **🧹 Auto-Hygiene**: Automated database and cache cleanup to maintain peak performance without manual intervention.
- **🎨 Visual Rebrand**: Completely updated visual identity with premium assets and a streamlined "Simple" mode for the Extras page.

## 🚀 Installation

### 🕯️ Step 1: Install the VibeStream Repository
1. In Kodi, go to **Settings** -> **File Manager** -> **Add Source**.
2. Enter the URL: `https://mritsurgeon.github.io/vibestream`
3. Name it **VibeStream Repo Source**.
4. Go back to **Settings** -> **Add-ons** -> **Install from zip file**.
5. Select **VibeStream Repo Source** and install `packages/repository.vibestream/repository.vibestream-1.0.0.zip`.

### 🎬 Step 2: Install VibeStream Addon
1. Once the repository is installed, go to **Settings** -> **Add-ons** -> **Install from repository**.
2. Select **VibeStream Repository**.
3. Go to **Video add-ons** -> **VibeStream** -> **Install**.

> [!IMPORTANT]
> **Dependency Note**: VibeStream requires **CocoScrapers**. If the installation fails, please ensure you have the **CocoScrapers Repository** installed first. You can find it at: `https://cocoscrapers.github.io/`

## Repository structure (Kodi add-on development)

The repo follows [Kodi add-on repository](https://kodi.wiki/view/Add-on_repositories) and [add-on development](https://johanzietsman.com/kodi-add-on-development/) practices:

- **Root**: `addons.xml` (index of add-ons and versions), `addons.xml.md5` (checksum for update checks).
- **Repository add-on**: Installed from zip; its `addon.xml` points `<info>` / `<checksum>` / `<datadir>` at the hosted URLs (e.g. GitHub Pages).
- **Plugin zips**: Under `packages/plugin.video.fenlight/` as `plugin.video.fenlight-${version}.zip`; Kodi downloads these when installing or updating.
- **Caching**: Kodi caches downloaded packages; clearing the `addons/packages/` folder (see Troubleshooting) forces it to re-download the latest version.

See also: [Kodi Add-on development](https://kodi.wiki/view/Add-on_development), [rigacci.org Kodi addon notes](https://www.rigacci.org/wiki/doku.php/doc/appunti/software/kodi_addon).

## Testing & development

Ways to test and develop the addon without affecting your main Kodi install, based on the [Kodi forum: Best way to develop kodi addons](https://forum.kodi.tv/showthread.php?tid=350884):

### Run automated tests (no Kodi required)

The addon includes unit tests that mock Kodi APIs so you can run them on your machine:

```bash
cd plugin.video.fenlight/resources/lib
python3 -m unittest discover -s tests -v
```

Or run a single test file: `python3 -m unittest tests.test_base_cache -v`.  
As [Roman_V_M notes](https://forum.kodi.tv/showthread.php?tid=350884), automated tests are best used as sanity checks (typos, logic) and for code that doesn’t depend on Kodi; full UI flows still need to be tested inside Kodi.

### Dev environment options (from the forum)

1. **Portable Kodi** ([black_eagle](https://forum.kodi.tv/showthread.php?tid=350884))  
   Install Kodi to a separate folder and run with the **`-p`** (portable) switch so it uses its own profile and doesn’t touch your main install. See [Kodi wiki: Portable mode](https://kodi.wiki/view/HOW-TO:Install_Kodi_for_Windows#Portable_Mode).

2. **Edit code without repacking** ([Roman_V_M](https://forum.kodi.tv/showthread.php?tid=350884))  
   Install the addon from the repo zip once (dependencies install automatically), then **symlink** the addon directory from your project into Kodi’s `addons` folder. Edits in your IDE are used by Kodi on next run without repacking.

3. **IDE support**  
   Use **kodistubs** (e.g. `pip install kodistubs`) so your editor/IDE can resolve Kodi modules. For VS Code, set `PYTHONPATH` in a `.env` file using the paths Kodi prints in the debug log when the addon runs.

4. **Debugging inside Kodi**  
   [kodi.web-pdb](https://github.com/romanvm/kodi.web-pdb) lets you use a web-based debugger while the addon runs in Kodi. Alternatively use log-based debugging or an exception logger.

## Troubleshooting

### Not seeing the latest update (e.g. 1.0.102) in Kodi

The repository uses **GitHub Pages** to serve `addons.xml`. If Kodi still shows an older version:

1. **Enable GitHub Pages** (one-time, on the repo):
   - Open **https://github.com/mritsurgeon/vibestream**
   - Go to **Settings** → **Pages**
   - Under **Build and deployment**, set **Source** to **Deploy from a branch**
   - Choose branch **main** and folder **/ (root)**, then **Save**
   - Wait 1–2 minutes; the site will be at `https://mritsurgeon.github.io/vibestream`

2. **In Kodi**, force a refresh:
   - **Settings** → **Add-ons** → **Check for updates** (or open **VibeStream Repository** and it will re-fetch)
   - Or: **Settings** → **Add-ons** → **My add-ons** → **Video add-ons** → **VibeStream** → **Update** (if available)

3. **Clear Kodi’s addon package cache** (so Kodi re-downloads the latest zip instead of using a cached old one):
   - As per [Kodi add-on development](https://johanzietsman.com/kodi-add-on-development/): *“Kodi caches the packages locally after the first download. Simply uninstalling an add-on does not remove the cached package.”*
   - Delete cached zips so the next update fetches 1.0.102:
     - **Windows**: `%APPDATA%\Kodi\addons\packages\` — delete any `plugin.video.fenlight*.zip` (or the whole `packages` folder).
     - **Linux**: `~/.kodi/addons/packages/` (or `/var/lib/kodi/.kodi/addons/packages/` for system-wide).
     - **macOS**: `~/Library/Application Support/Kodi/addons/packages/`
   - Restart Kodi, then **Check for updates** or open **VibeStream Repository** again.

4. If it still doesn’t update, remove the **VibeStream Repository** addon, reinstall it from the zip (Step 1 above), then install/update VibeStream from the repo again.

### Other repository / addon errors (not from VibeStream)

- **"Repository Twilight0 uses old schema"**  
  This refers to a different addon (Twilight0), not VibeStream. The VibeStream repo already uses the modern `<dir>` schema. To fix Twilight0: remove the old repository, then install the latest version from the author’s source if they provide an updated repo.

- **"Universal Scrapers does not have matching 21.0.0"**  
  This is another addon (Universal Scrapers). Kodi 21.x is Nexus; the addon may not support it yet. Options: update Universal Scrapers from its repo if a Kodi 21–compatible version exists, or disable/remove it until it’s updated. This does not affect VibeStream.

- **"Control 55 in window 10025 has been asked to focus"**  
  Window 10025 is Kodi’s Videos window (MyVideoNav); control 55 is often a list view. The message means something tried to focus a control that doesn’t exist or can’t receive focus. It can be triggered by the skin or by an addon leaving the list in an inconsistent state. VibeStream has been updated to always call `end_directory()` so the list is properly closed. If you still see it: enable **Debug** in Kodi (Settings → System → Logging), reproduce, then check the log for the line before the Control 55 message to see which addon/skin triggered it; try another skin or temporarily disable other video addons. See also [Kodi forum: Control 55](https://forum.kodi.tv/showthread.php?tid=345281).

- **"NoneType object is not subscriptable" or "name 'sqlite3' is not defined"**  
  These are addon bugs that have been fixed in recent versions: (1) All subscript access on possibly-None values (e.g. `fetchone()` results, dialog returns) is now guarded. (2) The sqlite3 reference in cache maintenance now uses the correct import name (`database.OperationalError` where the module is imported as `database`). If you still see them, ensure you’re on the latest VibeStream version and that Kodi’s Python has the `sqlite3` module (on some systems, e.g. FreeBSD, you may need a package like `py3*-sqlite3`). See `DEBUG_IMPLEMENTATION_PLAN.md` in the repo for technical details.

---
*VibeStream is built for speed and stability. Enjoy the ultimate streaming experience.*
