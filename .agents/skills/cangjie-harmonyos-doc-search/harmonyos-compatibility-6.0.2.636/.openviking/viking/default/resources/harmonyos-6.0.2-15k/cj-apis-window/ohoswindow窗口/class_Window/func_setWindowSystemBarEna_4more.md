### func setWindowSystemBarEnable(Array\<String>)

```cangjie
public func setWindowSystemBarEnable(names: Array<String>): Unit
```

**功能：** 设置主窗口三键导航栏、状态栏、底部导航条的可见模式。状态栏与底部导航条通过status控制、三键导航栏通过navigation控制。

> **说明：**
>
> - 该接口在2in1设备上调用不生效，其他设备在分屏模式（即窗口模式为[WindowStatusType.SPLIT_SCREEN](#enum-windowstatustype)）、自由悬浮窗口模式（即窗口模式为[WindowStatusType.FLOATING](#enum-windowstatustype)）、自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下调用不会立刻生效，只有进入全屏主窗口才会生效。
>
> - 调用生效后返回并不表示三键导航栏、状态栏和底部导航条的显示或隐藏已完成。子窗口调用后不生效。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|names|Array\<String>|是|-|设置窗口全屏模式时状态栏、三键导航栏和底部导航条是否显示。例如，需全部显示，该参数设置为['status', 'navigation']；不设置，则默认不显示。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] setWindowSystemBarEnable: This window state is abnormal.|

### func setWindowSystemBarProperties(SystemBarProperties)

```cangjie
public func setWindowSystemBarProperties(systemBarProperties: SystemBarProperties): Unit
```

**功能：** 设置主窗口三键导航栏、状态栏的属性。

> **说明：**
>
> - 该接口在2in1设备上调用不生效。其他设备在分屏模式（即窗口模式为[WindowStatusType.SPLIT_SCREEN](#enum-windowstatustype)）、自由悬浮窗口模式（即窗口模式为[WindowStatusType.FLOATING](#enum-windowstatustype)）、自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下调用不会立刻生效，只有进入全屏主窗口才会生效。
>
> - 子窗口调用后不生效。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|systemBarProperties|[SystemBarProperties](#class-systembarproperties)|是|-|三键导航栏、状态栏的属性。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] setWindowSystemBarProperties: This window state is abnormal.|

### func setWindowTouchable(Bool)

```cangjie
public func setWindowTouchable(isTouchable: Bool): Unit
```

**功能：** 设置窗口是否为可触状态。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isTouchable|Bool|是|-|窗口是否为可触状态。true表示可触；false表示不可触。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] setWindowTouchable: This window state is abnormal.|

### func showWindow()

```cangjie
public func showWindow(): Unit
```

**功能：** 显示当前窗口。

> **说明：**
>
> 仅支持系统窗口及应用子窗口，或将已显示的应用主窗口的层级提升至顶部。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|This window state is abnormal.|