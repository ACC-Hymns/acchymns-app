# acchymns-app

A repository which contains the cordova related code for the ACC Hymns app for the app store and play store.

## Build Prep

Install [node](https://nodejs.org/en/download/current/) & [python](https://www.python.org/downloads/).

Install cordova & uglifyjs globally: 
```bash
npm install -g cordova uglify-js
```

Initialize submodule
```bash
git submodule update --init
```

Copy selectively using python script
```bash
python copy.py
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
