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

## Troubleshooting

### Other repository / addon errors (not from VibeStream)

- **"Repository Twilight0 uses old schema"**  
  This refers to a different addon (Twilight0), not VibeStream. The VibeStream repo already uses the modern `<dir>` schema. To fix Twilight0: remove the old repository, then install the latest version from the author’s source if they provide an updated repo.

- **"Universal Scrapers does not have matching 21.0.0"**  
  This is another addon (Universal Scrapers). Kodi 21.x is Nexus; the addon may not support it yet. Options: update Universal Scrapers from its repo if a Kodi 21–compatible version exists, or disable/remove it until it’s updated. This does not affect VibeStream.

- **"Control 55 in window 10025 has been asked to focus"**  
  Window 10025 is often Kodi’s Videos window (or another core/skin window). The message usually means something tried to focus a control that doesn’t exist or can’t receive focus. It can come from another addon or the skin. Try: enable **Debug** in Kodi (Settings → System → Logging), reproduce the issue, then check the log to see which addon/skin triggers it; temporarily disable other video addons or switch skins to see if the error goes away.

---
*VibeStream is built for speed and stability. Enjoy the ultimate streaming experience.*
