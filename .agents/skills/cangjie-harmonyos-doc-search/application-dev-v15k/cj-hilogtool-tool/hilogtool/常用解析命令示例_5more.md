## 常用解析命令示例

### 解析当前目录下所有的hilog文件（推荐）

在当前日志所在目录，通过cmd进入shell窗口，在shell窗口直接执行hilogtool parse，即可进行解析操作，如下图：

![hilogtool4.png](./figures/hilogtool4.png)

### 解析指定目录下的hilog文件

```bash
hilogtool parse -i D:\09-temp\dict-test -d D:\09-temp\dict-test
```

![hilogtool5.png](./figures/hilogtool5.png)

### 解析单个hilog文件

```bash
hilogtool parse -i D:\09-temp\dict-test\hilog.025.20231020-154659.gz -d D:\09-temp\dict-test
```

![hilogtool6.png](./figures/hilogtool6.png)

## 自动化脚本

自动化调试脚本，将脚本与hilogtool工具放在同一目录下，执行get_hilog.bat，脚本会导出设备中的data/log/hilog日志，并且自动解析生成明文日志。

### windows平台脚本

windows平台 get_hilog.bat 脚本内容参考:

```bash
@set Ymd=%date:~0,4%_%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%%time:~6,2%
@set Ymd=%Ymd: =0%
@set Dir=LOG_%YMD%
md %Dir%
hdc file recv /data/log/hilog/ .\%Dir%\
hilogtool parse -i .\%Dir% -d .\%Dir%
pause
```

脚本运行结果：

![hilogtool7.png](./figures/hilogtool7.png)

### mac平台脚本

mac平台脚本内容参考：

```bash
Ymd=$(date "+%Y_%m%d_%H%M%S")
Dir=LOG_$Ymd
mkdir $Dir
hdc file recv /data/log/hilog/ ./$Dir/
./hilogtool parse -i ./$Dir -d ./$Dir
```

## 可能有影响的场景

### 自动化分析日志

部分领域涉及到自动化分析/data/log/hilog目录下的明文日志文件，目前hilog轻量化后，日志以二进制保存，需要适配一下自动化反编译二进制日志动作。

### 日志转发他人

直接从手机/data/log/hilog目录下recv出来的日志文件为二进制日志文件，直接发送给他人，无法正常查看，建议解析后再发送，或者将二进制日志文件与数据字典一同转发。

## 错误码

|错误码|含义|处理方法|
|200|解码成功|不涉及|
|300|解码失败，存在部分领域的日志和字典不匹配|1、只有部分日志解析失败，一般不影响开发自调试，可不用关注<br>2、若影响自调试，可参考下方常见问题，增量生成数据字典|
|500|解析工具版本不匹配|更新hilogtool解析工具版本|
|999|日志是明文落盘的，不需要解析|不涉及|

## 常见问题

工具解析时，显示 there is no hilog dict zip in xxx, use -d to specify ，或者 open dict xxx fail, errno is: No such file or directory

解析完的日志中，显示 OpenUuidFile fail, unknown log, uuid is: xxxxxx

原因：

解析日志时，未找到对应的数据字典导致的，可能有三个原因。

1. 解析命令使用错误，具体参考[常用解析命令示例](#常用解析命令示例)。
2. 开发本地替换bin/so调试的场景，需要触发生成新的数据字典，才能解析，以下触发命令三选一即可。

    （1）使用增量生成数据字典命令：

    ```bash
    hilog -d xxx
    ```

    例如推送hilog相关测试程序bin文件hilogTest到 /system/bin/下面，想查看hilogTest打印的日志，需要执行以下命令，增量生成hilogTest的数据字典：

    ```bash
    hdc shell hilog -d /system/bin/hilogTest
    ```

    数据字典生成成功后hilogTest则可以正常打印日志。

    （2）重启hilogd：

    ```bash
    service_control stop hilogd && service_control start hilogd
    ```

    （3）重启设备；

3. 数据字典被删掉了，检查导出的日志中是否存在hilog_dict.2024xxxx-xxxxxx.zip格式的数据字典文件

若不存在，则大概率是被 rm -rf data/log/hilog/* 命令删除掉了，需要重启设备生成新的数据字典，然后解析。