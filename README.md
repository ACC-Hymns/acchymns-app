# acchymns-app

A repository which contains the cordova related code for the ACC Hymns app for the app store and play store.

## Build Prep

Install [node](https://nodejs.org/en/download/current/).

Install cordova globally: 
```bash
npm install -g cordova
```

Initialize submodule
```bash
git submodule update --init
```

Symlink the submodule with the www/ directory
### Mac/Linux
```bash
ln -s acchymns-web www
```

### Windows
```bash
mklink /D www acchymns-web
```

## Build for Android

```
cordova platform add android
cordova build android
cordova emulate android
```

## Build for IOS

```
cordova platform add ios
cordova build ios
cordova emulate ios
```
