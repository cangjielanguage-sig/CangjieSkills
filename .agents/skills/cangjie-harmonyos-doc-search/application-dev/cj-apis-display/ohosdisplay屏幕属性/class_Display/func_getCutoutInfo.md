### func getCutoutInfo()

```cangjie
public func getCutoutInfo(): CutoutInfo
```

**功能：** 获取显示屏的刘海信息。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[CutoutInfo](#class-cutoutinfo)|返回显示屏的刘海信息。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1400001|Invalid display or screen.|
  |1400003|This display manager service works abnormally.|

**示例：**

<!-- code_check_manual -->

```cangjie
import ohos.display.*

func getCutoutInfoExample() {
    try {
        let displayClass = getDefaultDisplaySync()
        let cutout = displayClass.getCutoutInfo()
        println(cutout.boundingRects.size)
    } catch (exception: Exception) {
        AppLog.error(exception.toString())
    }
}
```