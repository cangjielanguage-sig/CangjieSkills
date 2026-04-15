### class TextRange

```cangjie
public class TextRange {
    public var start: ?Int32
    public var end: ?Int32
    public init(start: ?Int32, end: ?Int32)
}
```

**功能：** 定义文本类型组件的范围。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var start

```cangjie
public var start: ?Int32
```

**功能：** 起始偏移量。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var end

```cangjie
public var end: ?Int32
```

**功能：** 结束偏移量。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Int32, ?Int32)

```cangjie
public init(start: ?Int32, end: ?Int32)
```

**功能：** TextRange构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|?Int32|是|-|起始偏移量。初始值：-1。|
|end|?Int32|是|-|结束偏移量。初始值：-1。|

### class PasteEvent

```cangjie
public class PasteEvent {}
```

**功能：** 定义粘贴事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### func preventDefault()

```cangjie
public func preventDefault(): Unit
```

**功能：** 覆盖系统粘贴事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### class RichEditorInsertValue

```cangjie
public class RichEditorInsertValue {
    public var insertOffset: Int32
    public var insertValue: String
    public init(
        insertOffset: ?Int32,
        insertValue: ?String
    )
}
```

**功能：** 定义RichEditor插入值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var insertOffset

```cangjie
public var insertOffset: Int32
```

**功能：** 插入偏移量。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var insertValue

```cangjie
public var insertValue: String
```

**功能：** 插入值。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Int32, ?String)

```cangjie
public init(
    insertOffset: ?Int32,
    insertValue: ?String
)
```

**功能：** RichEditorInsertValue构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|insertOffset|?Int32|是|-|插入偏移量。初始值：0。|
|insertValue|?String|是|-|插入值。初始值：""。|