### 9568282 targetAPIVersion不一致，导致安装失败

**错误信息：**

error: install releaseType target not same.

**错误描述：**

targetAPIVersion字段不一致，导致安装失败。

**可能原因：**

待安装的路径下的多个安装包的targetAPIVersion不一致。

**处理步骤：**

检查待安装路径下的安装包，确保所有安装包的app.json5配置文件中targetAPIVersion一致。

### 9568314 安装应用间共享库失败

**错误信息：**

error: Failed to install the HSP because installing a shared bundle specified by hapFilePaths is not allowed.

**错误描述：**

安装应用间共享库失败。

**可能原因：**

安装应用间共享HSP时使用“hdc app install ***”指令。

**处理步骤：**

安装应用间HSP时使用`hdc install -s ***`指令。

### 9568349 操作文件时传入参数异常

**错误信息：**

error: installd param error.

**错误描述：**

操作文件时传入参数异常，导致安装失败。

**可能原因：**

安装过程中，传入参数无效或者传入目录路径为空。

**处理步骤：**

1. 重启手机后再次尝试安装应用。
2. 重复上述步骤3到5次后依旧安装失败，请导出日志文件提[在线工单](https://developer.huawei.com/consumer/cn/support/feedback/#/)获取帮助。

```bash
# 导出日志文件
hdc file recv /data/log/hilog/
```

### 9568351 创建文件目录异常导致安装失败

**错误信息：**

error: installd create dir failed.

**错误描述：**

创建文件目录异常，导致安装失败。

**可能原因：**

创建文件目录时没有写权限。

**处理步骤：**

1. 重启手机后再次尝试安装应用。
2. 重复上述步骤3到5次后依旧安装失败，请导出日志文件提[在线工单](https://developer.huawei.com/consumer/cn/support/feedback/#/)获取帮助。

```bash
# 导出日志文件
hdc file recv /data/log/hilog/
```

### 9568354 删除文件目录异常导致安装失败

**错误信息：**

error: installd remove dir failed.

**错误描述：**

删除文件目录失败，导致安装失败。

**可能原因：**

删除文件目录不存在，或者当前目录没有可写权限。

**处理步骤：**

1. 重启手机后再次尝试安装应用。
2. 重复上述步骤3到5次后依旧安装失败，请导出日志文件提[在线工单](https://developer.huawei.com/consumer/cn/support/feedback/#/)获取帮助。

```bash
# 导出日志文件
hdc file recv /data/log/hilog/
```

### 9568355 安装包中提取文件失败

**错误信息：**

error: installd extract files failed.

**错误描述：**

安装包中提取文件失败，导致安装失败。

**可能原因：**

安装过程中，解压so的目录创建失败，导致HAP包中提取so失败。

**处理步骤：**

1. 重启手机后再次尝试安装应用。
2. 重复上述步骤3到5次后依旧安装失败，请导出日志文件提[在线工单](https://developer.huawei.com/consumer/cn/support/feedback/#/)获取帮助。

```bash
# 导出日志文件
hdc file recv /data/log/hilog/
```

### 9568356 安装过程中重命名目录名失败

**错误信息：**

error: installd rename dir failed.

**错误描述：**

重命名目录名失败，导致安装失败。

**可能原因：**

安装过程中，重命名目录，目录名称超出260字符，或者当前目录没有可写权限。

**处理步骤：**

1. 重启手机后再次尝试安装应用。
2. 重复上述步骤3到5次后依旧安装失败，请导出日志文件提[在线工单](https://developer.huawei.com/consumer/cn/support/feedback/#/)获取帮助。

```bash
# 导出日志文件
hdc file recv /data/log/hilog/
```

### 9568357 清理文件失败

**错误信息：**

error: installd clean dir failed.

**错误描述：**

清理文件失败，导致安装失败。

**可能原因：**

安装过程中，待清理的文件无可写权限导致清理文件失败。

**处理步骤：**

1. 重启手机后再次尝试安装应用。
2. 重复上述步骤3到5次后依旧安装失败，请导出日志文件提[在线工单](https://developer.huawei.com/consumer/cn/support/feedback/#/)获取帮助。

```bash
# 导出日志文件
hdc file recv /data/log/hilog/
```