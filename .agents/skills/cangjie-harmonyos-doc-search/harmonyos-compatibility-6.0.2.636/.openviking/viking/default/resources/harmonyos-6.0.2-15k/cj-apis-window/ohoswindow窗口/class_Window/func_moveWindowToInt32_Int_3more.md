### func moveWindowTo(Int32, Int32)

```cangjie
public func moveWindowTo(x: Int32, y: Int32): Unit
```

**功能：** 移动窗口位置。

> **说明：**
>
> - 在2in1设备上所有窗口模式都能生效，其他设备仅在除智慧多窗外的自由悬浮窗口模式（即窗口模式为WindowStatusType.FLOATING）下生效。
>
> - 在2in1设备上窗口相对于屏幕移动，其他设备上窗口相对于父窗口移动。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int32|是|-|窗口在x轴方向移动到的坐标位置，单位为px，值为正表示位置在x轴右侧；值为负表示位置在x轴左侧；值为0表示位置在x轴坐标原点。|
|y|Int32|是|-|窗口在y轴方向移动到的坐标位置，单位为px，值为正表示位置在y轴下侧；值为负表示位置在y轴上侧；值为0表示位置在y轴坐标原点。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] moveWindowTo: This window state is abnormal.|

### func off("String")

```cangjie
public func off(callbackType: String): Unit
```

**功能：** 关闭固定态输入法窗口软键盘高度变化的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callbackType|String|是|-|监听事件，固定为'keyboardHeightChange'，即键盘高度变化事件。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|"[Window] Unregister callbackType failed: This window state is abnormal.|

### func off(WindowCallbackType, Callback1Argument\<Size>)

```cangjie
public func off(callbackType: WindowCallbackType, callback: Callback1Argument<Size>): Unit
```

**功能：** 关闭窗口尺寸变化的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callbackType|[WindowCallbackType](#enum-windowcallbacktype)|是|-|监听事件类型，WindowCallbackType.WindowSizeChange为窗口尺寸变化事件。|
|callback|[Callback1Argument](../apis/BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[Size](cj-apis-measure.md#struct-size)>|是|-|回调函数实例对象。返回当前的窗口尺寸。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible cause: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types.|