### 9568433 应用缺少ohos.permission.SUPPORT_PLUGIN权限

**错误信息**

error: Failed to install the plugin because host application check permission failed.

**错误描述**

应用安装插件时，应用的权限校验失败。

**可能原因**

应用缺少ohos.permission.SUPPORT_PLUGIN权限。

**处理步骤**

1. 参考[权限申请指导](../security/AccessToken/cj-declare-permissions.md)申请[ohos.permission.kernel.SUPPORT_PLUGIN权限](../security/AccessToken/cj-restricted-permissions.md#ohospermissionkernelsupport_plugin)。<!--Del-->
2. 该权限等级为system_basic，若[应用APL等级](../security/AccessToken/cj-app-permission-mgmt-overview.md#权限机制中的基本概念)低于system_basic，请[申请受限权限](../security/AccessToken/cj-declare-permissions-in-acl.md)。

<!--DelEnd-->

### 9568333 模块名称为空

**错误信息：**

error: Install failed due to hap moduleName is empty.

**错误描述：**

模块名称为空，导致安装失败。

**可能原因：**

模块名称为空。

**处理步骤：**

检查[module.json5](../cj-start/basic-knowledge/cj-module-configuration-file.md)的name字段是否为空。

### 9568331 签名信息不一致

**错误信息：**

error: Install incompatible signature info.

**错误描述：**

签名信息不一致，导致安装失败。

**可能原因：**

安装多HAP包的应用时，HAP包的签名信息不一致。

**处理步骤：**

重新[签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing)，使多个HAP包签名信息一致。

### 9568334 模块名称重复

**错误信息：**

error: Install failed due to hap moduleName duplicate.

**错误描述：**

模块名称重复，导致安装失败。

**可能原因：**

一个应用同时安装多个模块时，模块名称存在重复。

**处理步骤：**

同一个应用多个模块的名称要保证唯一性。

### 9568340 配置文件缺失

**错误信息：**

error: Install parse no profile.

**错误描述：**

HAP包没有配置文件，导致安装失败。

**可能原因：**

[module.json、pack.info](../cj-start/basic-knowledge/cj-application-package-structure-stage.md)等配置文件缺失。

**处理步骤：**

使用DevEco Studio重新构建、打包、安装。

### 9568341 安装时解析配置文件失败

**错误信息：**

error: Install parse bad profile.

**错误描述：**

安装时解析配置文件失败。

**可能原因：**

[module.json、pack.info](../cj-start/basic-knowledge/cj-application-package-structure-stage.md)等配置文件格式异常。

**处理步骤：**

使用DevEco Studio重新构建、打包、安装。

### 9568342 配置文件数据类型错误

**错误信息：**

error: Install parse profile prop type error.

**错误描述：**

安装解析配置文件时，数据类型错误，导致安装失败。

**可能原因：**

[module.json、pack.info](../cj-start/basic-knowledge/cj-application-package-structure-stage.md)等配置文件存在数据类型错误的字段。

**处理步骤：**

使用DevEco Studio重新构建、打包、安装。

### 9568345 配置文件中的字符串长度或者数组大小过大

**错误信息：**

error: Too large size of string or array type element in the profile.

**错误描述：**

安装解析配置文件时，字符串长度或者数组大小过大，导致安装失败。

**可能原因：**

[module.json、pack.info](../cj-start/basic-knowledge/cj-application-package-structure-stage.md)等配置文件存在字符串长度或者数组大小过大的字段。

**处理步骤：**

使用DevEco Studio重新构建、打包、安装。