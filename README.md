# STIV3N APK

A lightweight, mobile-first web companion with a black-and-red interface.

## Important platform limitation

An iPhone cannot natively install or run Android `.apk` packages. This project does **not** emulate Android, convert APK binaries to iOS apps, or install APK files. The file picker only displays the selected filename locally; it does not upload or execute the file.

To adapt a specific Android app for iPhone, we need one of:
- the app's existing web version;
- the app's source code and permission to adapt it;
- an official iOS version or a supported alternative.

## Run locally

Open `index.html` in a modern browser. For PWA/service-worker behavior, serve the folder over HTTPS or localhost.

## Publish with GitHub Pages

1. Open repository Settings → Pages.
2. Under Build and deployment, choose **Deploy from a branch**.
3. Choose branch `main` and folder `/ (root)`, then Save.
4. Wait for the Pages deployment to finish and open the published URL.

The workflow in `.github/workflows/pages.yml` can also deploy the site automatically on pushes to `main`.

## Install on iPhone

Open the published HTTPS URL in Safari → Share → Add to Home Screen. This installs a web shortcut/PWA, not an Android runtime.

## Privacy

The APK file picker does not read the contents of the chosen file or send it to a server.