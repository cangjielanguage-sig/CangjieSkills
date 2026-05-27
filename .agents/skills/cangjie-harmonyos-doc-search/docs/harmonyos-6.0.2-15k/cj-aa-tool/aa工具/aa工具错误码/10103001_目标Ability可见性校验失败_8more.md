### 10103001 目标Ability可见性校验失败

**错误信息**

Failed to verify the visibility of the target ability.

**错误描述**

目标Ability可见性校验失败时，aa工具将返回该错误码。

**可能原因**

当目标应用在module.json5配置文件中的[abilities标签](../cj-start/basic-knowledge/module-configuration-file.md#abilities标签)/[extensionAbilities标签](../cj-start/basic-knowledge/module-configuration-file.md#extensionabilities标签)中的exported字段配置为false时，表示对应UIAbility组件/ExtensionAbility组件不可以被其他应用调用，也无法被aa工具命令拉起。

**处理步骤**

需要检查目标应用module.json5中对应Ability字段的exported配置是否为true，如果不为true，改为true重试即可。

### 10104001 指定的Ability不存在

**错误信息**

The specified ability does not exist.

**错误描述**

当指定的Ability名称不存在时，aa工具将返回该错误码。

**可能原因**

指定的Ability未安装。

**处理步骤**

1. 检查aa命令的-a的参数abilityName和-b的参数bundleName是否正确。
2. 检查指定的bundleName对应的应用是否安装。可使用如下命令查询已安装的应用列表，若该bundleName不在查询结果中，说明应用未安装成功。

    ```bash
    hdc shell bm dump -a
    ```

3. 多HAP应用需确认Ability所属的HAP是否已被安装。可使用如下命令查询应用的包信息，若安装的应用中没有对应的HAP和Ability，说明Ability所属的HAP未被安装。

    ```bash
    hdc shell bm dump -n 包名
    ```

### 10105001 Ability服务连接失败

**错误信息**

Failed to connect to the ability service.

**错误描述**

连接Ability服务失败。

**可能原因**

调用接口时Ability服务断开。

**处理步骤**

尝试重启设备重新执行。

### 10105002 获取Ability信息失败

**错误信息**

Failed to obtain ability information.

**错误描述**

获取Ability信息失败。

**可能原因**

生成Ability请求时通过BMS获取AbilityInfo为空。

**处理步骤**

检查指定的bundleName对应的应用是否安装。可使用如下命令查询已安装的应用列表，若该bundleName不在查询结果中，说明应用未安装成功。

```bash
hdc shell bm dump -a
```

### 10105003 App服务连接失败

**错误信息**

Failed to connect to the app service.

**错误描述**

App服务连接失败。

**可能原因**

调用接口时App服务断开。

**处理步骤**

尝试重启设备。

### 10106001 当前设备不是开发者模式

**错误信息**

The current device is not in developer mode.

**错误描述**

当前设备不是开发者模式。

**可能原因**

当前设备不是开发者模式。

**处理步骤**

在设置中打开开发者模式。

### 10106002 目标应用不支持Debug模式

**错误信息**

The target application does not support debug mode.

**错误描述**

目标应用不支持Debug模式。

**可能原因**

目标应用当前使用签名工具中“type”参数不为“debug”。

**处理步骤**

使用Debug签名证书重新签名，安装新签名出的HAP后，再尝试执行该该命令。

### 10100101 获取应用信息失败

**错误信息**

Failed to obtain application information.

**错误描述**

从BMS查询到的App信息异常。

**可能原因**

从BMS查询到的App信息中应用名或包名异常。

**处理步骤**

1. 检查aa命令的-a的参数abilityName和-b的参数bundleName是否正确。
2. 检查指定的bundleName对应的应用是否安装。可使用如下命令查询已安装的应用列表，若该bundleName不在查询结果中，说明应用未安装成功。

    ```bash
    hdc shell bm dump -a
    ```

3. 多HAP应用需确认Ability所属的HAP是否已被安装。可使用如下命令查询应用的包信息，若安装的应用中没有对应的HAP和Ability，说明Ability所属的HAP未被安装。

    ```bash
    hdc shell bm dump -n 包名
    ```