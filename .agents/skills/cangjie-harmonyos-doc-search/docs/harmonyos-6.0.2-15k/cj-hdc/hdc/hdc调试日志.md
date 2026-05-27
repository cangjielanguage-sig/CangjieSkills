## hdc调试日志

### server端日志

#### 指定运行时日志等级

hdc运行时日志等级，默认为LOG_INFO，命令格式如下：

```shell
hdc -l [level] [command]
```

**参数：**

| 参数 | 说明 |
| -------- | -------- |
| [level] | 指定运行时日志等级<br/>0：LOG_OFF<br/>1：LOG_FATAL<br/>2：LOG_WARN<br/>3：LOG_INFO<br/>4：LOG_DEBUG<br/>5：LOG_ALL <br/>6：LOG_LIBUSB。 |
| command | hdc支持的命令。 |

> **说明：**
>
> 当配置运行时日志级别为6（LOG_LIBUSB）时，将激活libusb相关的增量日志输出，增量日志级别的详细程度高、数据量大，有助于精确诊断服务进程中与USB相关的异常情况。USB相关操作主要由服务进程执行，因此，只有服务进程具备打印增量日志的功能。相应地，客户端侧的日志几乎不包含增量日志信息。
> 指定运行时日志等级仅适用于当前进程（包括客户端与服务进程），无法更改已存在的进程日志等级。

**返回值：**

| 返回值 | 说明 |
| -------- | -------- |
| 命令执行返回内容 | 请参见对应命令的返回值。 |
| 日志信息 | 对应指定的运行时等级日志打印。 |

**使用方法：**

客户端打印LOG_DEBUG级别日志，以执行shell ls为例，命令示例如下:

```shell
hdc -l 5 shell ls
```

服务进程前台模式启动指定LOG_LIBUSB级别日志，命令示例如下:

```shell
hdc kill && hdc -l 6 -m
```

> **说明：**
> `-m`参数指定以前台模式启动服务进程，可以直接观察前台日志输出，按下Ctrl+C退出进程。

服务进程后台启动模式指定LOG_LIBUSB级别日志，命令示例如下:

```shell
hdc kill && hdc -l 6 start
```

> **说明：**
> 以后台模式启动，可以在hdc.log中观察日志输出，日志路径可以查看**日志获取**章节的描述。

#### 日志获取

执行以下命令开启日志获取：

```shell
hdc kill
hdc -l5 start
```

收集到的完整日志存放路径：

| 平台 | 路径 | 备注 |
| -------- | -------- | -------- |
| Windows | %temp%\hdc.log | 实际路径参考，实际使用请替换用户名变量<br/>C:\Users\用户名\AppData\Local\Temp\hdc.log。 |
| Linux | /tmp/hdc.log | - |
| macOS | $TMPDIR/hdc.log | - |

日志相关环境变量：

| 环境变量名称  | 默认值 | 说明   |
|-------|-----|--------|
| OHOS_HDC_LOG_LEVEL | 5   | 用于配置服务进程日志记录级别，日志级别详情参见<br>[server端日志](#server端日志)指定运行时日志等级章节。  |

环境变量配置方法：

以下通过配置OHOS_HDC_LOG_LEVEL环境变量为例，配置环境变量值为：5，介绍环境变量配置方法。

| 操作系统 | 配置方法 |
|---|---|
| Windows  | 在**此电脑 &gt; 属性 &gt; 高级系统设置 &gt; 高级 &gt; 环境变量**中，添加环境变量名称为OHOS_HDC_LOG_LEVEL，变量值为5。配置完毕后点击确认。环境变量配置完成后，关闭并重启命令行或其他使用到HarmonyOS SDK的软件，以生效新配置的环境变量。  |
| Linux  | 在~/.bash_profile文件末尾追加内容export OHOS_HDC_LOG_LEVEL=5并保存后，执行`source ~/.bash_profile`生效当前环境变量。 |
| macOS  | 在~/.zshrc文件末尾追加内容export OHOS_HDC_LOG_LEVEL=5并保存后，执行`source ~/.zshrc`生效当前环境变量。环境变量配置完成后，关闭并重启命令行或其他使用到HarmonyOS SDK的软件，以生效新配置的环境变量。 |

### 设备端日志

开启hilog日志工具，获取对应日志，命令如下：

```shell
hdc shell hilog -w start      # 开启hilog日志落盘
hdc shell ls /data/log/hilog  # 查看已落盘hilog日志
hdc file recv /data/log/hilog # 获取hilog已落盘日志（包含内核日志）
```