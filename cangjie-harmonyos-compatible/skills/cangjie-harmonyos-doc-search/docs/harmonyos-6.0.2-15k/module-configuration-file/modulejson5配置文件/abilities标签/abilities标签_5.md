abilities示例：

<!--RP3-->

```json
{
  "abilities": [{
    "name": "EntryAbility",
    "srcEntry": "ohos_app_cangjie_entry.MainAbility",
    "launchType":"singleton",
    "description": "$string:description_main_ability",
    "icon": "$media:layered_image",
    "label": "Login",
    "permissions": [],
    "metadata": [],
    "exported": true,
    "continuable": true,
    "skills": [{
      "actions": ["ohos.want.action.home"],
      "entities": ["entity.system.home"],
      "uris": []
    }],
    "backgroundModes": [
      "dataTransfer",
      "audioPlayback",
      "audioRecording",
      "location",
      "bluetoothInteraction",
      "multiDeviceConnection",
      "wifiInteraction",
      "voip",
      "taskKeeping"
    ],
    "startWindow": "$profile:start_window",
    "startWindowIcon": "$media:icon",
    "startWindowBackground": "$color:red",
    "removeMissionAfterTerminate": true,
    "orientation": "$string:orientation",
    "supportWindowMode": ["fullscreen", "split", "floating"],
    "maxWindowRatio": 3.5,
    "minWindowRatio": 0.5,
    "maxWindowWidth": 2560,
    "minWindowWidth": 1400,
    "maxWindowHeight": 300,
    "minWindowHeight": 200,
    "excludeFromMissions": false,
    "unclearableMission": false,
    "excludeFromDock": false,
    "preferMultiWindowOrientation": "default",
    "isolationProcess": false,
    "continueType": [
      "continueType1",
      "continueType2"
    ],
    "continueBundleName": [
      "com.example.myapplication1",
      "com.example.myapplication2"
    ],
    "process": ":processTag"
  }]
}
```

<!--RP3End-->