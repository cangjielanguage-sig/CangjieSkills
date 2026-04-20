### class ShadowOptionsResult

```cangjie
public class ShadowOptionsResult {
    ShadowOptionsResult(
        public let radius: Float64,
        public let color: String,
        public let offsetX: Float64,
        public let offsetY: Float64
    )
}
```

**功能：** 文字阴影效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### let color

```cangjie
public let color: String
```

**功能：** 表示阴影的颜色。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

#### let offsetX

```cangjie
public let offsetX: Float64
```

**功能：** 表示阴影的X轴偏移量。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

#### let offsetY

```cangjie
public let offsetY: Float64
```

**功能：** 表示阴影的Y轴偏移量。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

#### let radius

```cangjie
public let radius: Float64
```

**功能：** 表示阴影模糊半径。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

#### ShadowOptionsResult()

```cangjie
ShadowOptionsResult(
        public let radius: Float64,
        public let color: String,
        public let offsetX: Float64,
        public let offsetY: Float64
    )
```

**功能：** 创建ShadowOptionsResult类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|radius|Float64|是|-|阴影模糊半径。|
|color|String|是|-|阴影的颜色。|
|offsetX|Float64|是|-|阴影的X轴偏移量。|
|offsetY|Float64|是|-|阴影的Y轴偏移量。|

### class TextDecorationResult

```cangjie
public class TextDecorationResult {
    public TextDecorationResult(
        public var `type`: TextDecorationType,
        public var color: String
    )
}
```

**功能：** 后端返回的文本装饰信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var \`type\`

```cangjie
public var `type`: TextDecorationType
```

**功能：** 表示装饰线类型。

**类型：** [TextDecorationType](./cj-common-types.md#enum-TextDecorationType)

**读写能力：** 可读写

**起始版本：** 12

#### var color

```cangjie
public var color: String
```

**功能：** 表示装饰颜色。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

#### TextDecorationResult(TextDecorationType, String)

```cangjie
public TextDecorationResult(
    public var `type`: TextDecorationType,
    public var color: String
)
```

**功能：** 创建TextDecorationResult类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[TextDecorationType](./cj-common-types.md#enum-TextDecorationType)|是|-|装饰线类型。|
|color|String|是|-|装饰颜色。|

### class TextRange

```cangjie
public class TextRange {
    public TextRange(
        public var start: Int32,
        public var end: Int32
    )
}
```

**功能：** 文本范围。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var start

```cangjie
public var start: Int32
```

**功能：** 表示起始索引。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

#### var end

```cangjie
public var end: Int32
```

**功能：** 表示结束索引。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

#### TextRange(Int32, Int32)

```cangjie
public TextRange(
    public var start: Int32,
    public var end: Int32
)
```

**功能：** 创建TextRange类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|Int32|是|-|起始索引。|
|end|Int32|是|-|结束索引。|