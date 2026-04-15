# ohos.window（窗口）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

提供窗口相关功能。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## func findWindow(String)

```cangjie
public func findWindow(name: String): Window
```

**功能：** 根据名称查找窗口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|窗口名称，即Configuration中的name值。|

**返回值：**

|类型|说明|
|:----|:----|
|[Window](#class-window)|返回找到的窗口。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1300002|This window state is abnormal.|

## func createWindow(Configuration)

```cangjie
public func createWindow(config: Configuration): Window
```

**功能：** 使用特定配置创建窗口。当config.windowType == TypeFloat时，需要"ohos.permission.SYSTEM_FLOAT_WINDOW"权限。

**需要权限：** ohos.permission.SYSTEM_FLOAT_WINDOW

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|config|[Configuration](#class-configuration)|是|-|窗口创建参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[Window](#class-window)|返回创建的窗口。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |201|Permission verification failed. The application does not have the permission required to call the API.|
  |401|Parameter error. Possible cause: 1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types.|
  |1300003|This window manager service works abnormally.|
  |1300006|This window context is abnormal.|

## func shiftAppWindowFocus(Int32, Int32)

```cangjie
public func shiftAppWindowFocus(sourceWindowId: Int32, targetWindowId: Int32): Unit
```

**功能：** 在同应用内将窗口焦点从源窗口转移到目标窗口，仅支持应用主窗、子窗范围内的焦点转移。

目标窗口需确保具有获得焦点的能力（可通过[setWindowFocusable()](#func-setwindowfocusablebool)设置），并确保调用[showWindow()](#func-showwindow)成功且执行完毕。

> **说明：**
>
> 在调用shiftAppWindowFocus()前，建议确保目标窗口已调用[loadContent()](#func-loadcontentstring)并生效，否则可能会导致不可见窗口获取焦点，造成功能异常或影响用户体验。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sourceWindowId|Int32|是|-|焦点转移的源窗口ID。|
|targetWindowId|Int32|是|-|焦点转移的目标窗口ID。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |401|Parameter error. Possible cause: 1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types.|
  |801|Capability not supported. Failed to call the API due to limited device capabilities.|
  |1300002|This window state is abnormal.|
  |1300003|This window manager service works abnormally.|
  |1300004|Unauthorized operation.|