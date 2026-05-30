### func keepKeyboardOnFocus(Bool)

```cangjie
public func keepKeyboardOnFocus(keepKeyboardFlag: Bool): Unit
```

**功能：** 窗口获焦时保留由其他窗口创建的软键盘，仅支持系统窗口与应用子窗口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|keepKeyboardFlag|Bool|是|-|是否保留其他窗口创建的软键盘。true表示保留；false表示不保留。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] keepKeyboardOnFocus: This window state is abnormal.|
  |1300004|[Window] keepKeyboardOnFocus: Unauthorized operation.|

### func maximize(MaximizePresentation)

```cangjie
public func maximize(presentation!: MaximizePresentation = MaximizePresentation.ENTER_IMMERSIVE): Unit
```

**功能：** 主窗口调用，实现最大化功能。

> **说明：**
>
> 仅2in1设备可用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|presentation|[MaximizePresentation](#enum-maximizepresentation)|否|MaximizePresentation.ENTER_IMMERSIVE| **命名参数。** 主窗口最大化时候的布局枚举。<br>初始值：<br>MaximizePresentation.ENTER_IMMERSIVE<br>即默认最大化时进入沉浸式布局。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|[Window] maximize: Parameter error.|
  |1300002|[Window] maximize: This window state is abnormal.|

### func minimize()

```cangjie
public func minimize(): Unit
```

**功能：** 最小化或隐藏窗口，根据调用对象不同，实现不同的功能。

> **说明：**
>
> 此接口根据调用对象不同，实现不同的功能：
>
> - 当调用对象为主窗口时，实现最小化功能，可在Dock栏中还原。
>
> - 当调用对象为子窗口时，实现隐藏功能，不可在Dock栏中还原，可以使用[showWindow()](#func-showwindow)进行还原。
>
> - 悬浮窗类型的窗口对象，调用此接口会报1300002错误码。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|[Window] minimize: Capability not supported.|
  |1300002|[Window] minimize: This window state is abnormal.|