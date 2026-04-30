## func shiftAppWindowFocus(Int32, Int32)

```cangjie
public func shiftAppWindowFocus(sourceWindowId: Int32, targetWindowId: Int32): Unit
```

**功能：** 在同应用内将窗口焦点从源窗口转移到目标窗口。

> **说明：**
>
> 仅支持应用主窗和子窗的焦点转移。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sourceWindowId|Int32|是|-|源窗口id，必须是获焦状态。|
|targetWindowId|Int32|是|-|目标窗口id。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|[Window] showWindow: This window state is abnormal.|
  |801|[Window] showWindow: This window state is abnormal.|
  |1300002|[Window] showWindow: This window state is abnormal.|
  |1300003|[Window] showWindow: This window state is abnormal.|
  |1300004|[Window] showWindow: This window state is abnormal.|