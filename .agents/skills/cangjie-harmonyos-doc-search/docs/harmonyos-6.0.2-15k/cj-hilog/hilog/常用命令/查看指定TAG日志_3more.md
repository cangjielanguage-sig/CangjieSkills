### 查看指定TAG日志

```shell
hilog -T tag
```

**使用样例：**

```shell
$ hilog -T SAMGR
08-28 09:27:59.581   610 11504 I C01800/samgr/SAMGR: CommonEventCollect save extraData 1661
08-28 09:27:59.581   610 11504 I C01800/samgr/SAMGR: OnReceiveEvent get action: usual.event.BATTERY_CHANGED code: 0, extraDataId 1661
08-28 09:27:59.582   610 11504 I C01800/samgr/SAMGR: DoEvent:4 name:usual.event.BATTERY_CHANGED value:0
08-28 09:27:59.582   610 11504 W C01800/samgr/SAMGR: LoadSa SA:10120 AddDeath fail,cnt:1,callpid:610
08-28 09:27:59.583   610 11504 I C01800/samgr/SAMGR: LoadSa SA:10120 size:1,count:1
08-28 09:27:59.601   610 11504 I C01800/samgr/SAMGR: Scheduler SA:10120 loading
08-28 09:27:59.965 11518 11518 I C01800/media_analysis_service/SAMGR: SA:10120 OpenSo spend 315ms
08-28 09:27:59.965   610  4064 I C01800/samgr/SAMGR: AddProc:media_analysis_service. size:75
```

### 查看缓冲区前n行日志

```shell
hilog -a 8
```

**使用样例：**

```shell
$ hilog -a 8
11-15 16:04:08.628     0     0 I I00000/HiLog: ========Zeroth log of type: init
11-15 16:04:08.603   506   506 I I02C01/cust_carrier_mount/CustCarrierMount: MountCarrierToShared start
11-15 16:04:08.604   506   506 I I02C01/cust_carrier_mount/CustCarrierMount: success to mount carrier to shared
11-15 16:04:15.394   972   972 I I02C01/cust_carrier_mount/CustCarrierMount: UpdateCotaOpkeyLink start
11-15 16:04:15.396   972   972 W I02C01/cust_carrier_mount/CustCarrierMount: not exsit CUST_GLOBAL_CARRIER_DIR or COTA_PARAM_CARRIER_DIR
11-15 16:04:15.887   972   972 I I02C01/cust_carrier_mount/CustCarrierMount: success to update cota carrier
11-15 16:04:48.749  5777  5901 I A00001/com.hiai.core/HiAI_Metadata: metadata is null
11-15 16:04:48.749  5777  5901 I A00001/com.hiai.core/HiAI_PluginAbilityInfo: abilityInfo is null
```

### 查看缓冲区后n行日志

```shell
hilog -z 8
```

**使用样例：**

```shell
$ hilog -z 8
11-15 16:12:19.015  1899  7867 W C01719/wifi_manager_service/ffrt: 423:FFRTQosApplyForOther:244 tid 7867, Operation not permitted, ret:-1, eno:1
11-15 16:12:19.125  1043  1072 I C01C42/time_service/TimeService: uid: 1010 id:428551571 name:wifi_manager_service wk:0
11-15 16:12:19.125  1043  1072 I C01C42/time_service/TimeService: bat: -1 id:428551571 we:505225000000 mwe:512725000000
11-15 16:12:19.125  1043  1072 I C01C42/time_service/TimeService: typ:3 trig: 505 225000000, bt: 495230369193
11-15 16:12:19.125  1043  1072 I C01C42/time_service/TimeService: cb: 428551571 ret: 0
11-15 16:12:19.435  3086  7813 I C01719/com.ohos.contactsdataability/ffrt: 45:~WorkerThread:72 to exit, qos[3]
11-15 16:12:19.691   800  1404 I C01713/resource_schedule_service/SUSPEND_MANAGER: [(HasSpecialStateFromBgtask):759] 20020107_com.ohos.medialibrary.medialibrarydata
11-15 16:12:19.691   800  1404 I C01713/resource_schedule_service/SUSPEND_MANAGER: [(DozeFreezeUnit):890] Doze has special:ERR_HAS_PID_EFFICIENCY_RESOURCE
```