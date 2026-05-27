### 9568359 安装设置selinux失败

**错误信息：**

error: installd set selinux label failed.

**错误描述：**

安装设置selinux失败。

**可能原因：**

签名配置文件中APL字段错误。APL有“normal”、“system_basic”和“system_core”三种等级。

**处理步骤：**

1. 确认签名文件p7b中apl字段是否有误。

    ![示例图](./figures/zh-cn_image_9568359.png)

2. 若apl字段有误，修改UnsgnedReleasedProfileTemplate.json文件中apl字段，并重新签名。

    ![示例图](./figures/zh-cn_image_9568359_2.png)

### 9568403 安装加密校验失败

**错误信息：**

error: check encryption failed.

**错误描述：**

安装加密校验失败。

**可能原因：**

可能是镜像版本较老；或者HAP包lib目录内非so文件导致。

**处理步骤：**

1. 安装新版本镜像。
2. 删除HAP工程中lib目录内非so文件，重新签名打包。

### 9568413 应用设备类型不支持当前设备

**错误信息：**

error: check syscap filed and device type is not supported.

**错误描述：**

应用配置的设备类型不支持安装。

**可能原因：**

应用配置的设备类型和安装设备不一致。

**处理步骤：**

调整正确的设备类型。

### 9568417 签名校验失败

**错误信息：**

error: bundle cannot be installed because the appId is not same with preinstalled bundle.

**错误描述：**

签名校验失败。

**可能原因：**

安装的应用与已经预置的同包名应用签名不一致。

**处理步骤：**

如果安装的应用是预置应用，需要保证安装应用的签名与预置应用的一致。

### 9568278 安装包的版本号不一致

**错误信息：**

error: install version code not same.

**可能原因：**

1. 设备上安装的应用和安装报错的应用包版本号（versionCode）不一致。
2. 安装多个包中存在版本号（versionCode）不一致。

**处理步骤：**

1. 调整安装包的版本和设备中已存在的应用包的版本号（versionCode）一致，或者卸载设备中的应用，再去安装新的应用包。
2. 调整安装的多个包的版本号（versionCode），所有的包都需要保持版本号（versionCode）一致。

### 9568380 卸载系统应用失败

**错误信息：**

error: uninstall system app error.

**错误描述：**

卸载系统应用失败。

**可能原因：**

部分系统应用设置为不可卸载，不支持卸载此类应用。

**处理步骤：**

不能卸载不可卸载的应用。

### 9568387 卸载未安装的模块，导致卸载失败

**错误信息：**

error: uninstall missing installed module.

**错误描述：**

卸载未安装的模块。

**可能原因：**

卸载未安装的模块。

**处理步骤：**

使用[bm dump -n](#查询应用信息命令dump)命令查看应用配置，确认要卸载的模块已经安装。

### 9568333 模块名称为空

**错误信息：**

error: Install failed due to hap moduleName is empty.

**错误描述：**

模块名称为空，导致安装失败。

**可能原因：**

模块名称为空。

**处理步骤：**

检查[module.json5](../cj-start/basic-knowledge/module-configuration-file.md)的name字段是否为空。

### 9568331 签名信息不一致

**错误信息：**

error: Install incompatible signature info.

**错误描述：**

签名信息不一致，导致安装失败。

**可能原因：**

安装多HAP包的应用时，HAP包的签名信息不一致。

**处理步骤：**

重新签名，使多个HAP包签名信息一致。参考[应用/服务签名](../../Cangjie_Deveco_Studio/source_zh_cn/cj-ide-signing.md)。

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

[module.json、pack.info](../cj-start/basic-knowledge/application-package-structure-stage.md)等配置文件缺失。

**处理步骤：**

使用DevEco Studio重新构建、打包、安装。