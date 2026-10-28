# NekoNexa — Portal Anime

NekoNexa is a mobile-first web portal for iPhone. It offers a shortcut to the Kawaii Animes website, a web search helper, and a link to SpawnDroid for running compatible Android builds in a cloud-hosted Android session.

## What it does

- Responsive dark/pink interface for iPhone and desktop.
- Kawaii Animes website and official Android download-page shortcuts.
- Search helper that opens a web search in a new tab.
- Add-to-Home-Screen guidance and a web app manifest/icon.
- A pre-deployment sanity check for required files, local links, manifest and core UI.

## What it does not do

- It is **not** a native iOS app or an Android emulator.
- iOS cannot install or run APK files directly.
- NekoNexa does not embed Kawaii Animes, its catalogue, video streams, accounts, or private APIs.
- The SpawnDroid link is an external service, not an automatic integration: users sign in there and upload an APK/AAB they have permission to run. SpawnDroid is in early access; service limits and availability can change.

## Deploy with GitHub Pages

The workflow at `.github/workflows/pages.yml` runs `scripts/check_site.py` before deploying the static site. On GitHub, open **Settings → Pages** and select **GitHub Actions** as the build/deployment source if Pages is not already configured. Then open the Actions tab and confirm the latest workflow run succeeds.

Published URL (once deployment is successful): https://pachecostiven47-sudo.github.io/Apk/

## Add to iPhone

Open the published HTTPS URL in Safari, tap **Share**, choose **Add to Home Screen**, and confirm. This creates a shortcut/web app experience; it does not install an Android APK.

## External links

- Kawaii Animes: https://www.kawaiianimes.app/
- Official Android download page: https://www.kawaiianimes.app/descargas/android/
- SpawnDroid console: https://app.spawndroid.io
- SpawnDroid first-APK guide: https://spawndroid.io/help/upload-your-first-apk/

External sites, services, applications and content remain the responsibility of their respective owners.
