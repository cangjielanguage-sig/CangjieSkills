### class RichEditorBaseController

```cangjie
public open class RichEditorBaseController {
    protected init(id: Int64)
}
```

**功能：** 提供RichEditor的基础控制器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(Int64)

```cangjie
protected init(id: Int64)
```

**功能：** 创建实例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|Int64|是|-|标识号|

#### func getCaretOffset()

```cangjie
public func getCaretOffset(): Int32
```

**功能：** 从控制器获取光标偏移量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:---|:---|
|Int32|光标偏移量。|

#### func setCaretOffset(?Int32)

```cangjie
public func setCaretOffset(offset: ?Int32): Bool
```

**功能：** 设置光标偏移量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|?Int32|是|-|光标偏移量。初始值：-1。|

**返回值：**

|类型|说明|
|:---|:---|
|Bool|设置结果。|