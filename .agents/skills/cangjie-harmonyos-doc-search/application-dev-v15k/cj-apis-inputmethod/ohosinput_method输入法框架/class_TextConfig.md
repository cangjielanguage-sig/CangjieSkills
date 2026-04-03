## class TextConfig

```cangjie
public class TextConfig {
    public TextConfig(
        public var inputAttribute!: InputAttribute,
        public var cursorInfo!: CursorInfo = CursorInfo(-1.0, -1.0, -1.0,-1.0),
        public var selection!: Range = Range(-1, -1),
        public var windowId!: UInt32 = 0xFFFF_FFFF
    )
}
```

**功能：** 编辑框配置信息类型。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### var cursorInfo

```cangjie
public var cursorInfo: CursorInfo = CursorInfo(-1.0, -1.0, -1.0, -1.0)
```

**功能：** 光标信息。

**类型：** [CursorInfo](#class-cursorinfo)

**读写能力：** 可读写

**起始版本：** 19

### var inputAttribute

```cangjie
public var inputAttribute: InputAttribute
```

**功能：** 编辑框属性。

**类型：** [InputAttribute](#class-inputattribute)

**读写能力：** 可读写

**起始版本：** 19

### var selection

```cangjie
public var selection: Range = Range(-1, -1)
```

**功能：** 文本选中的范围。

**类型：** [Range](#class-range)

**读写能力：** 可读写

**起始版本：** 19

### var windowId

```cangjie
public var windowId: UInt32 = 0xFFFF_FFFF
```

**功能：** 编辑框所在的窗口Id。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### TextConfig(InputAttribute, CursorInfo, Range, UInt32)

```cangjie
public TextConfig(
    public var inputAttribute!: InputAttribute,
    public var cursorInfo!: CursorInfo = CursorInfo(-1.0, -1.0, -1.0,-1.0),
    public var selection!: Range = Range(-1, -1),
    public var windowId!: UInt32 = 0xFFFF_FFFF
)
```

**功能：** 构建编辑框配置信息类型的对象。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|inputAttribute|[InputAttribute](#class-inputattribute)|是|-| **命名参数。** 编辑框属性。|
|cursorInfo|[CursorInfo](#class-cursorinfo)|否|CursorInfo(- 1.0, - 1.0, - 1.0, - 1.0)| **命名参数。** 光标信息。|
|selection|[Range](#class-range)|否|Range(- 1, - 1)| **命名参数。** 文本选中的范围。|
|windowId|UInt32|否|0xFFFF_FFFF| **命名参数。** 编辑框所在的窗口Id。|