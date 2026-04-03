## class Window

```cangjie
public class Window {}
```

**功能：** 当前窗口实例，窗口管理器管理的基本单元。

> **说明：**
>
> 下列API示例中都需先使用[getLastWindow()](#func-getlastwindowstagecontext)、[createWindow()](#func-createwindowconfiguration)、[findWindow()](#func-findwindowstring)中的任一方法获取到[Window](#class-window)实例，再通过此实例调用对应方法。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### func createSubWindowWithOptions(String, SubWindowOptions)

```cangjie
public func createSubWindowWithOptions(name: String, option: SubWindowOptions): Window
```

**功能：** 创建主窗口、子窗口或悬浮窗下的子窗口。

> **说明：**
>
> 该接口仅在2in1设备上调用生效。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|子窗口的名字。|
|option|[SubWindowOptions](#class-subwindowoptions)|是|-|子窗口参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[Window](#class-window)|返回当前Window下创建的子窗口对象|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[WindowStage] get subWindow: This window state is abnormal.|

### func destroyWindow()

```cangjie
public func destroyWindow(): Unit
```

**功能：** 销毁当前窗口。

> **说明：**
>
> 仅支持系统窗口及应用子窗口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] destroyWindow: This window state is abnormal.|

### func disableLandscapeMultiWindow()

```cangjie
public func disableLandscapeMultiWindow(): Unit
```

**功能：** 应用部分界面支持横向布局时，在退出该界面时去使能，去使能后不支持进入横向多窗。不建议竖向布局界面使用。

> **说明：**
>
> 此接口只对应用主窗口生效，且需要在 `module.json5` 配置文件中 `abilities` 标签中配置 `preferMultiWindowOrientation` 属性为 `"landscape_auto"`。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] disableLandscapeMultiWindow: This window state is abnormal.|

### func enableLandscapeMultiWindow()

```cangjie
public func enableLandscapeMultiWindow(): Unit
```

**功能：** 应用部分界面支持横向布局时，在进入该界面时使能，使能后可支持进入横向多窗。不建议竖向布局界面使用。

> **说明：**
>
> 此接口只对应用主窗口生效，且需要在 `module.json5` 配置文件中 `abilities标签` 中配置 `preferMultiWindowOrientation` 属性为 `"landscape_auto"`。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] enableLandscapeMultiWindow: This window state is abnormal.|