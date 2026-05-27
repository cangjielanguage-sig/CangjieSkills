### func setDialogBackGestureEnabled(Bool)

```cangjie
public func setDialogBackGestureEnabled(enabled: Bool): Unit
```

**功能：** 设置模态窗口是否响应手势返回事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enabled|Bool|是|-|是否响应手势返回事件。true表示响应手势返回事件，触发onBackPress回调；false表示不响应手势返回事件，不触发onBackPress回调。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|[Window] setDialogBackGestureEnabled: Capability not supported.|
  |1300002|[Window] setDialogBackGestureEnabled: This window state is abnormal.|

### func setImmersiveModeEnabledState(Bool)

```cangjie
public func setImmersiveModeEnabledState(enabled: Bool): Unit
```

**功能：** 设置当前窗口是否开启沉浸式布局，该调用不会改变窗口模式和窗口大小。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enabled|Bool|是|-|是否开启沉浸式布局。true表示开启，false表示关闭。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] setImmersiveModeEnabledState: This window state is abnormal.|

### func setPreferredOrientation(Orientation)

```cangjie
public func setPreferredOrientation(orientation: Orientation): Unit
```

**功能：** 设置主窗口的显示方向属性。

> **说明：**
>
> 仅在支持跟随sensor旋转的设备上生效，子窗口调用后不生效。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|orientation|[Orientation](#enum-orientation)|是|-|窗口显示方向的属性。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible cause: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed.|
  |1300002|This window state is abnormal.|