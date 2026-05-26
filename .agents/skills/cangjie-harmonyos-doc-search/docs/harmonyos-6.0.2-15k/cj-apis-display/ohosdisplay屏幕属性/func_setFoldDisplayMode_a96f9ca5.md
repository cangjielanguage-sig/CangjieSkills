## func setFoldDisplayMode(FoldDisplayMode)

```cangjie
public func setFoldDisplayMode(mode: FoldDisplayMode): Unit
```

**功能：** 设置可折叠设备的显示模式。

**系统接口：** 此接口为系统接口。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[FoldDisplayMode](#enum-folddisplaymode)|是|-|可折叠设备的显示模式。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[屏幕错误码](../errorcodes/cj-errorcode-display.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1400003|This display manager service works abnormally.|

**示例:**

```cangjie
import ohos.display.*

func setFoldDisplayModeExample() {
    try {
        let mode = FoldDisplayMode.FOLD_DISPLAY_MODE_FULL
        setFoldDisplayMode(mode)
    } catch (exception: Exception) {
        AppLog.error(exception.toString())
    }
}
```