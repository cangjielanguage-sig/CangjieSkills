# ohos.window（窗口）

ohos.window提供管理窗口的一些基础能力，包括对当前窗口的创建、销毁、各属性设置，以及对各窗口间的管理调度。

该模块提供以下窗口相关的常用功能：

- [Window](#class-window)：当前窗口实例，窗口管理器管理的基本单元。

- [WindowStage](#class-windowstage)：窗口管理器。管理各个基本窗口单元。

> **说明：**
>
> ohos.window仅支持纯仓颉场景，不支持用于ArkTS与仓颉混合开发场景。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## func createWindow(Configuration)

```cangjie
public func createWindow(config: Configuration): Window
```

**功能：** 创建子窗口或者系统窗口。

**需要权限：** ohos.permission.SYSTEM_FLOAT_WINDOW（仅当创建窗口类型为WindowType.TYPE_FLOAT时需要申请）

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|config|[Configuration](#class-configuration)|是|-|创建窗口时的参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[Window](#class-window)|返回当前创建的窗口对象|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|[Window] createWindow: Permission verification failed, usually the result returned by VerifyAccessToken.|
  |401|[Window] createWindow: Parameter error.|
  |1300003|[Window] createWindow: This window manager service works abnormally.|
  |1300006|[Window] createWindow: This window context is abnormal.|

## func findWindow(String)

```cangjie
public func findWindow(name: String): Window
```

**功能：** 查找name所对应的窗口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|窗口名字，即[Configuration](#class-configuration)中的name。|

**返回值：**

|类型|说明|
|:----|:----|
|[Window](#class-window)|当前查找的窗口对象|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible cause: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types.|
  |1300002|This window state is abnormal.|

## func getLastWindow(StageContext)

```cangjie
public func getLastWindow(ctx: StageContext): Window
```

**功能：** 获取当前应用内最上层的子窗口，若无应用子窗口，则返回应用主窗口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|ctx|[StageContext](../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext)|是|-|当前应用上下文信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[Window](#class-window)|返回当前应用内最后显示的窗口对象|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] getLastWindow: This window state is abnormal|