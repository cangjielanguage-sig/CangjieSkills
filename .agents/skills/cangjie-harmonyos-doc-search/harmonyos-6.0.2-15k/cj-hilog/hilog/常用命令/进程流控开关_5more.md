### 进程流控开关

```shell
hilog -Q pidon/pidoff
```

**使用样例：**

```shell
$ hilog -Q pidon
Set flow control by process to enabled successfully
$
$ hilog -Q pidoff
Set flow control by process to disabled successfully
```

### domain流控开关

```shell
hilog -Q domainon/domainoff
```

**使用样例：**

```shell
$ hilog -Q domainon
Set flow control by domain to enabled successfully
$
$ hilog -Q domainoff
Set flow control by domain to disabled successfully
```

### 查看指定级别日志

```shell
hilog -L D/I/W/E/F
```

**使用样例：**

```shell
$ hilog -L E
08-28 09:01:25.730  2678  2678 E A00F00/com.aidataservice/AiDataService_5.10.7.320: DataChangeNotifyManager: notifyDataChange CommonEntity no valid entity to notify
08-28 09:01:56.058  8560  8560 E A00500/com.ohos.settingsdata/SettingsData: DB not ready request = datashare:///com.ohos.settingsdata/entry/settingsdata/SETTINGSDATA?Proxy=true&key=analysis_service_switch_on , retry after DB startup
08-28 09:01:56.082  8560  8560 E A00500/com.ohos.settingsdata/SettingsData: decoder failure: /data/migrate/settings_global.xml , error code:-1
08-28 09:01:56.082  8560  8560 E A00500/com.ohos.settingsdata/SettingsData: clearXml failed:No such file or directory, error code:13900002
08-28 09:01:56.083  8560  8560 E A00500/com.ohos.settingsdata/SettingsData: readText failed:No such file or directory, error code:13900002
08-28 09:01:56.371  8586  8586 E A00500/com.ohos.settingsdata/SettingsData: DB not ready request =    datashare:///com.ohos.settingsdata/entry/settingsdata/SETTINGSDATA?Proxy=true&key=photo_network_connection_status , retry after DB startup
08-28 09:01:56.408  8586  8586 E A00500/com.ohos.settingsdata/SettingsData: decoder failure: /data/migrate/settings_global.xml , error code:-1
```

### 查看指定类型日志

```shell
hilog -t app
```

**使用样例：**

```shell
$ hilog -t app
11-15 16:04:45.903  5630  5630 I A0A5A5/os.hiviewcare:staticSubscriber/Diagnosis: [DetectionFilter]820001084: switch off
11-15 16:04:45.905  5630  5630 I A0A5A5/os.hiviewcare:staticSubscriber/Diagnosis: [DetectionFilter]847005050: frequency limit
11-15 16:04:45.905  5630  5630 I A0A5A5/os.hiviewcare:staticSubscriber/Diagnosis: [SmartNotifyHandler]detections after filter: []
11-15 16:04:45.905  5630  5630 I A0A5A5/os.hiviewcare:staticSubscriber/Diagnosis: [SmartNotifyHandler]no detections to detect
11-15 16:04:45.924  5687  5687 I A01B06/common/KG: MetaBalls-SystemTopPanelController --> init charging status = 3
```

### 查看指定domain日志

```shell
hilog -D 01B06
```

**使用样例：**

```shell
$ hilog -D 01B06
11-15 16:04:54.981  5687  5687 I A01B06/common/KG: MetaBalls-MetaBallRenderer --> pressTime = 0 appearTime = 1731657885972
11-15 16:04:54.981  5687  5687 I A01B06/common/KG: MetaBalls-MetaBallRenderer --> backAnimator on finish
11-15 16:04:54.982  5687  5687 I A01B06/common/KG: MetaBalls-MetaBallRenderer --> setTimeout over 9s and begin animate on finish
11-15 16:04:55.297  5687  5687 I A01B06/common/KG: MetaBalls-MetaBallRenderer --> chargingTextExitAnimation onFinish
11-15 16:04:55.494  5687  5687 I A01B06/common/KG: MetaBalls-MetaBallRenderer --> uiExtension session send data success,type: exitAnimationFinish
```