### 查看帮助命令

```shell
hilog -h
```

**使用样例：**

```shell
   $ hilog -h
   Usage:
   -h --help
   Show all help information.
   Show single help information with option:
   query/clear/buffer/stats/persist/private/kmsg/flowcontrol/baselevel/domain/combo
   Querying logs options:
   No option performs a blocking read and keeps printing.
   -x --exit
      Performs a non-blocking read and exits when all logs in buffer are printed.
   -a <n>, --head=<n>
      Show n lines logs on head of buffer.
   -z <n>, --tail=<n>
      Show n lines logs on tail of buffer.
```

### 非阻塞读日志

```shell
hilog -x
```

**使用样例：**

```shell
$ hilog -x
11-15 15:51:02.087  2823  2823 I A01B05/com.ohos.sceneboard/AOD: AodClockFullScreen --> timeTextLineHeight:313.3333333333333 clockMarginTop:99
11-15 15:51:02.087  2823  2823 I A01B05/com.ohos.sceneboard/AOD: AodClockFullScreen --> timeFontSize:114.48717948717947
11-15 15:51:02.090  2823  2823 I A01B05/com.ohos.sceneboard/AOD: AodClockFullScreen --> timeTextWidth:202,timeTextHeight:292
11-15 15:51:02.100  2823  2823 I A01B05/com.ohos.sceneboard/AOD: ComponentUtil --> Component(ComponentId-AodClockNumber) draw complete.
11-15 15:51:02.110  1197  1197 E C01406/render_service/OHOS::RS: [LoadImgsbyResolution] Can't find resolution (1084 x 2412) in config file
11-15 15:51:02.127  1197  1197 E C01406/render_service/OHOS::RS: [LoadImgsbyResolution] Can't find resolution (1084 x 2412) in config file
```

### 查看日志缓冲区大小

```shell
hilog -g
```

**使用样例：**

```shell
$ hilog -g
Log type app buffer size is 16.0M
Log type init buffer size is 16.0M
Log type core buffer size is 16.0M
Log type only_prerelease buffer size is 16.0M
```

### 修改日志缓冲区大小

```shell
hilog -G size
```

**使用样例：**

```shell
$ hilog -G 16M
Set log type app buffer size to 16.0M successfully
Set log type init buffer size to 16.0M successfully
Set log type core buffer size to 16.0M successfully
Set log type only_prerelease buffer size to 16.0M successfully
```

### 清除缓冲区日志

```shell
hilog -r
```

**使用样例：**

```shell
$ hilog -r
Log type core,app,only_prerelease buffer clear successfully
```

### 内核日志读取开关控制

```shell
hilog -k on/off
```

**使用样例：**

```shell
$ hilog -k on
Set hilogd storing kmsg log on successfully
$
$ hilog -k off
Set hilogd storing kmsg log off successfully
```

### 查询统计信息

```shell
hilog -s
```

**使用样例：**

```shell
$ param set persist.sys.hilog.stats true
Set parameter persist.sys.hilog.stats true success
$ reboot
$ hilog -s
Log statistic report (Duration: 0h0m32s.564, From: 11-15 16:04:08.628):
Total lines: 137517, length: 8.0M
DEBUG lines: 0(0%), length: 0.0B(0%)
INFO lines: 101795(74%), length: 6.1M(76%)
WARN lines: 10268(7.5%), length: 719.9K(8.8%)
ERROR lines: 25452(19%), length: 1.2M(15%)
FATAL lines: 2(0.0015%), length: 259.0B(0.0031%)
------------------------------------------------------------
Domain Table:
LOGTYPE- DOMAIN---- TAG----------------------------- MAX_FREQ-- TIME---------------- MAX_TP---- TIME---------------- LINES----- LENGTH---- DROPPED---
app----- 0xf00----- -------------------------------- 924.00---- 11-15 16:04:25.594-- 111975.00- 11-15 16:04:25.594-- 3386------ 371.5K---- 0---------
app----- 0x0------- -------------------------------- 285.00---- 11-15 16:04:34.877-- 44242.00-- 11-15 16:04:34.877-- 990------- 129.2K---- 0---------
```

**统计信息说明：**

```shell
MAX_FREQ：日志打印频率最高的每秒行数
TIME：    对应发生时间
MAX_TP：  日志打印频率最高的每秒字节数
LINES：   统计周期内的总行数
LENGTH：  统计周期内的总字节数
DROPPED： 统计周期内丢失的行数
```

### 清除统计信息

```shell
hilog -S
```

**使用样例：**

```shell
$ hilog -S
Statistic info clear successfully
```