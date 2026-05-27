### func getWindowStatus()

```cangjie
public func getWindowStatus(): WindowStatusType
```

**功能：** 获取当前应用窗口的模式。

> **说明：**
>
> 在2in1设备上调用本接口时，在窗口最大化状态时返回值对应为WindowStatusType.FULL_SCREEN。<br>若想在2in1设备上区分当前窗口状态为最大化还是全屏，可在窗口状态为WindowStatusType.FULL_SCREEN的情况下，再调用[getImmersiveModeEnabledState()](#func-getimmersivemodeenabledstate) 接口进行进一步判断，到底是最大化状态还是全屏状态。若接口返回true则表示当前窗口为全屏状态，若接口返回false则表示当前窗口为最大化状态。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[WindowStatusType](#enum-windowstatustype)|当前窗口模式。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|[Window] getWindowStatus: Capability not supported.|
  |1300002|[Window] getWindowStatus: This window state is abnormal.|

### func getWindowSystemBarProperties()

```cangjie
public func getWindowSystemBarProperties(): SystemBarProperties
```

**功能：** 主窗口获取三键导航栏、状态栏的属性。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[SystemBarProperties](#class-systembarproperties)|当前三键导航栏、状态栏属性。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] getWindowSystemBarProperties: This window state is abnormal.|

### func isFocused()

```cangjie
public func isFocused(): Bool
```

**功能：** 判断当前窗口是否已获焦。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|当前窗口是否已获焦。<br>true表示当前窗口已获焦，false则表示当前窗口未获焦。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] IsFocused: This window state is abnormal.|

### func isWindowShowing()

```cangjie
public func isWindowShowing(): Bool
```

**功能：** 判断当前窗口是否已显示。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|当前窗口是否已显示。true表示当前窗口已显示，false则表示当前窗口未显示。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] isWindowShowing: This window state is abnormal.|

### func isWindowSupportWideGamut()

```cangjie
public func isWindowSupportWideGamut(): Bool
```

**功能：** 判断当前窗口是否支持广色域模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示当前窗口支持广色域模式，返回false表示当前窗口不支持广色域模式。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] isWindowSupportWideGamut: This window state is abnormal.|