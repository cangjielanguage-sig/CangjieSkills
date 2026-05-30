### func updateCursor(CursorInfo)

```cangjie
public func updateCursor(cursorInfo: CursorInfo): Unit
```

**功能：** 当编辑框内的光标信息发生变化时，调用该接口使输入法感知到光标变化。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cursorInfo|[CursorInfo](#class-cursorinfo)|是|-|光标信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.|
  |12800003|input method client error.|
  |12800008|input method manager service error.|
  |12800009|input method client is detached.|

- IllegalStateException：

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |unknown code|未知的错误码。|联系仓颉团队处理。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IMEKit.*

let controller = getController()
let cursorInfo = CursorInfo(0.0, 0.0, 600.0, 800.0)
controller.updateCursor(cursorInfo)
```