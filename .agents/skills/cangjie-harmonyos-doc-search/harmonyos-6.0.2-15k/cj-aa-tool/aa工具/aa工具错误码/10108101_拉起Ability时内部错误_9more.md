### 10108101 拉起Ability时内部错误

**错误信息**

An internal error occurs while attempting to launch the ability.

**错误描述**

当内存申请、多线程处理异常等内部处理错误时，方法将返回该错误码。

**可能原因**

内存申请、多线程处理等内核通用错误。具体原因可能包括：内部对象为空、处理超时、包管理获取应用信息失败、系统服务获取失败、启动的Ability实例已达到上限等原因。

**处理步骤**

内部错误是系统运行过程中出现的内部错误，开发者无法处理。

### 10103201 目标Ability不是ServiceAbility类型

**错误信息**

The target ability is not of the ServiceAbility type.

**错误描述**

操作的目标Ability不是ServiceAbility类型。

**可能原因**

aa stop命令停止ServiceAbility时，-a的参数abilityName对应的Ability不是Service类型。

**处理步骤**

检查aa -a的参数abilityName对应的Abiility是否为ServiceAbility类型。

### 10104002 获取指定包信息失败

**错误信息**

Failed to retrieve specified package information.

**错误描述**

获取指定包信息失败。

**可能原因**

指定的包名对应的应用没有安装。

**处理步骤**

1. 检查指定的包名是否正确。
2. 检查指定的bundleName对应的应用是否安装。可使用如下命令查询已安装的应用列表，若该bundleName不在查询结果中，说明应用未安装成功。

    ```bash
    hdc shell bm dump -a
    ```

### 10106401 杀死进程失败

**错误信息**

Failed to terminate the process.

**错误描述**

杀死进程失败。

**可能原因**

1. aa force-stop命令指定的应用不存在。
2. 未成功连接到AppManagerService。

**处理步骤**

1. 检查指定的bundleName对应的应用是否安装。可使用如下命令查询已安装的应用列表，若该bundleName不在查询结果中，说明应用未安装成功。

    ```bash
    hdc shell bm dump -a
    ```

2. 尝试重启设备。

### 10106402 常驻进程无法被杀死

**错误信息**

Persistent processes cannot be terminated.

**错误描述**

常驻进程无法被杀死。

**可能原因**

aa force-stop命令指定的bundleName是常驻进程。

**处理步骤**

检查目标应用是否为常驻进程，常驻进程无法通过命令杀死。

### 10108501 aa test命令内部错误

**错误信息**

An internal error occurs during the execution of the aa test command.

**错误描述**

当内存申请、多线程处理异常等内部处理错误时，方法将返回该错误码。

**可能原因**

内存申请、多线程处理等内核通用错误。具体原因可能包括：内部对象为空、处理超时、系统服务获取失败等原因。

**处理步骤**

内部错误是系统运行过程中出现的内部错误，开发者无法处理。

### 10108601 进入/退出调试模式时内部错误

**错误信息**

An internal error occurs while attempting to enter/exit debug mode.

**错误描述**

当内存申请、多线程处理异常等内部处理错误时，方法将返回该错误码。

**可能原因**

内存申请、多线程处理等内核通用错误。具体原因可能包括：内部对象为空、处理超时、系统服务获取失败等原因。

**处理步骤**

内部错误是系统运行过程中出现的内部错误，开发者无法处理。

### 10103601 指定的包名不存在

**错误信息**

The specified bundleName does not exist.

**错误描述**

用户指定的包名未找到时返回该错误码。

**可能原因**

aa attach/detach命令指定的包名不存在。

**处理步骤**

检查指定的bundleName对应的应用是否安装。可使用如下命令查询已安装的应用列表，若该bundleName不在查询结果中，说明应用未安装成功。

```bash
hdc shell bm dump -a
```

### 10106701 目标应用不是Debug应用

**错误信息**

The target application is not a debug application.

**错误描述**

目标应用不是Debug应用。

**可能原因**

当前使用签名工具中“type”参数不为“debug”。

**处理步骤**

使用Debug签名证书重新签名，安装新签名出的HAP后，再尝试执行该该命令。
签名工具及签名证书的生成方式可以参考：[签名工具指导](../../Cangjie_Deveco_Studio/source_zh_cn/cj-ide-signing.md)。