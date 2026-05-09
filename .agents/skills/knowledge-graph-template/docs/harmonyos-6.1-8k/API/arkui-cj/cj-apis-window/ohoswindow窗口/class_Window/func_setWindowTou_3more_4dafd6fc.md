### func setWindowTouchable(Bool)

```cangjie
public func setWindowTouchable(isTouchable: Bool): Unit
```

**功能：** 设置是否可触摸。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isTouchable|Bool|是|-|如果为true则可触摸，如果为false则不可触摸。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1300002|This window state is abnormal.|

### func showWindow()

```cangjie
public func showWindow(): Unit
```

**功能：** 显示此窗口。此API仅对系统窗口或应用程序子窗口生效。对于应用程序的主窗口，当主窗口已显示时，此API会将其移到顶部。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1300002|This window state is abnormal.|

### func snapshot()

```cangjie
public func snapshot(): PixelMap
```

**功能：** 获取窗口快照。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|返回不带值的Promise。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1300002|This window state is abnormal.|