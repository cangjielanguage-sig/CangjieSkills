## 17700034 指定的module是overlay特征的module

**错误信息**

The specified module is an overlay module.

**错误描述**

查询指定的目标module所关联的overlayModuleInfo时, 指定的module是overlay特征module。

**可能原因**

指定的module是overlay特征的module。

**处理步骤**

检查指定的module是否为overlay特征的module。

## 17700035 指定的应用只包含overlay特征的module

**错误信息**

The specified bundle is an overlay bundle.

**错误描述**

查询指定应用的目标module所关联的overlayModuleInfo时, 指定的应用只包含overlay特征的module。

**可能原因**

指定的应用只包含overlay特征的module。

**处理步骤**

检查指定的应用是否只包含overlay特征的module。

## 17700036 共享库缺少AllowAppShareLibrary特权导致安装失败

**错误信息**

Failed to install the HSP because lacks appropriate permissions.

**错误描述**

共享库未申请配置AllowAppShareLibrary特权，可能存在安全隐私风险，不允许安装。

**可能原因**

发布共享库前，未申请配置AllowAppShareLibrary特权。

**处理步骤**

为共享库申请配置AllowAppShareLibrary特权，重新签名并发布。

## 17700037 被卸载的shared library版本被其他应用依赖

**错误信息**

The version of shared bundle is dependent on other applications.

**错误描述**

当卸载shared library某一版本时，指定的shared library的版本被其他应用依赖，卸载失败。

**可能原因**

1. 当前卸载的版本是shared library的最高版本，且该shared library被其他应用依赖。
2. 当前卸载时未指定shared library的版本，会卸载shared library的所有版本，该shared library被其他应用依赖。

**处理步骤**

1. 检查被卸载的shared library是否被其他应用依赖。
2. 检查被卸载的版本是否为shared library的最高版本。

## 17700038 被卸载的shared library不存在

**错误信息**

The specified shared bundle does not exist.

**错误描述**

当卸载shared library时，卸载的shared library不存在。

**可能原因**

1. 当前指定卸载的版本不存在与被卸载的shared library中。
2. 当前指定卸载的shared library不存在与设备中。

**处理步骤**

1. 检查被卸载的shared library是否存在于当前设备中。
2. 检查被卸载的版本是否存在于被卸载的shared library中。

## 17700039 不允许安装应用间共享库

**错误信息**

Failed to install because disallow install a shared bundle by hapFilePaths.

**错误描述**

安装应用时，传入的安装包为应用间共享库类型。

**可能原因**

1. 通过bm工具安装应用时，-p参数传入了应用间共享库的安装包路径。
2. 通过install接口安装应用时，hapFilePaths参数传入了应用间共享库的安装包路径。

**处理步骤**

1. 通过-s参数指定应用间共享库的安装包路径。
2. 通过installParam参数的sharedBundleDirPaths字段指定应用间共享库的安装包路径。

## 17700040 不允许卸载应用间共享库

**错误信息**

The specified bundle is a shared bundle which cannot be uninstalled.

**错误描述**

卸载应用时，传入的是应用间共享库的包名。

**可能原因**

1. 通过bm工具卸载应用时，-n参数传入了应用间共享库的包名。
2. 通过uninstall接口卸载应用时，bundleName传入的是应用间共享库的包名。

**处理步骤**

1. 通过-s参数指定卸载的应用为共享库应用。
2. 通过UninstallParam参数的bundleName及versionCode指定卸载的共享库的包名及版本。

## 17700041 企业设备管理不允许安装该应用

**错误信息**

Failed to install because enterprise device management disallow install.

**错误描述**

安装应用时，企业设备管理不允许安装。

**可能原因**

企业设备管理不允许安装该应用。

**处理步骤**

请在设备中检查应用是否被企业设备管理禁止安装。