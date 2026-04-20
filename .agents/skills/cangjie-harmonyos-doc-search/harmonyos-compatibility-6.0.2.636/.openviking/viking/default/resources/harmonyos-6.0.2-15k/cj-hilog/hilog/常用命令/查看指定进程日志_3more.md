### 查看指定进程日志

```shell
hilog -P pid
```

**使用样例：**

```shell
$ hilog -P 618
08-28 10:19:16.872   618 17729 I C02D15/hiview/XPower: [task_52]#current system load is: 0.028767
08-28 10:19:23.997   618 17580 I C02D10/hiview/CpuCollector: CalculateProcessCpuStatInfos: startTime=1724811553746, endTime=1724811563996, startBootTime=47001084, endBootTime=47011335, period=10251
08-28 10:19:23.999   618 17580 I C02D10/hiview/CpuCollector: CollectProcessCpuStatInfos: collect process cpu statistics information size=234, isNeedUpdate=1
08-28 10:19:24.002   618 17580 W C01650/hiview/Rdb:  DB :
08-28 10:19:24.002   618 17580 W C01650/hiview/Rdb:  device: 12583051 inode: 40230 mode: 432 size: 569344 natime: Wed Aug 28 00:00:06 2024
08-28 10:19:24.002   618 17580 W C01650/hiview/Rdb:  smtime: Wed Aug 28 00:34:30 2024
08-28 10:19:24.002   618 17580 W C01650/hiview/Rdb:  sctime: Wed Aug 28 00:34:30 2024
```

### 查看符合正则匹配关键字的日志

```shell
hilog -e start
```

**使用样例：**

```shell
$ hilog -e start
11-15 16:17:17.578   547  4504 I C01800/samgr/SAMGR: AddProc start proc:media_analysis_service spend 223ms
11-15 16:17:17.578   547  4504 I C01800/samgr/SAMGR: Scheduler proc:media_analysis_service handle started event
11-15 16:17:17.578   547  4504 I C01800/samgr/SAMGR: Scheduler proc:media_analysis_service started
11-15 16:17:17.580  8877  8877 I C01810/media_analysis_service/SAFWK: start tasks proc:media_analysis_service end,spend 1ms
11-15 16:17:17.582  8877  8877 I C01651/media_analysis_service/DataShare: [operator()()-data_share_manager_impl.cpp:134]: RecoverObs start
11-15 16:17:17.589  8877  8893 I C01651/media_analysis_service/DataShare: [Connect()-ams_mgr_proxy.cpp:67]: connect start, uri = ******/media
11-15 16:17:18.225  1155  1633 I C02943/power_host/ThermalHdi: CreateLogFile start
11-15 16:17:18.264  1155  1633 I C02943/power_host/ThermalHdi: CompressFile start
```

### 查看和设置落盘任务

```shell
hilog -w control
```

> **说明：**
>
> 查询当前任务： hilog -w query
>
> 开启hilog落盘任务，并且设置落盘文件数量为1000个： hilog -w start -n 1000
>
> 开启kmsglog落盘任务，并且设置落盘文件数量为100个： hilog -w start -n 100 -t kmsg
>
> 停止当前落盘任务： hilog -w stop
>
> 开启kmsglog落盘任务，并且设置落盘规则，其中压缩方式可以为zlib，zstd，none。以设置规则为例：文件名为kmsglog，大小为2M，数量为100个, 其压缩方式为zlib压缩，命令行为： hilog -w start -t kmsg -f kmsglog -l 2M -n 100 -m zlib

**使用样例：**

```shell
$ hilog -w query
Persist task query failed
No running persistent task [CODE: -63]
$
$ hilog -w start -n 1000
Persist task [jobid:1][fileNum:1000][fileSize:4194304] start successfully
$
$ hilog -w start -n 100 -t kmsg
Persist task [jobid:2][fileNum:100][fileSize:4194304] start successfully
$
$ hilog -w stop
Persist task [jobid:1] stop successfully
Persist task [jobid:2] stop successfully
$
$ hilog -w start -t kmsg -f kmsglog -l 2M -n 100 -m zlib
Persist task [jobid:2][fileNum:100][fileSize:2097152] start successfully
```