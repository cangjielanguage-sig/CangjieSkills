## class ShadowOptions

```cangjie
public class ShadowOptions {
    public var radius: ?Float64
    public var shadowType: ?ShadowType
    public var color: ?ResourceColor
    public var offsetX: ?Float64
    public var offsetY: ?Float64
    public var fill: ?Bool
    public init(radius!: ?Float64, shadowType!: ?ShadowType = None, color!: ?ResourceColor = None, offsetX!: ?Float64 = None, offsetY!: ?Float64 = None, fill!: ?Bool = None)
}
```

**功能：** 阴影选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var radius

```cangjie
public var radius: ?Float64
```

**功能：** 设置阴影的模糊半径。

**类型：** ?Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var shadowType

```cangjie
public var shadowType: ?ShadowType
```

**功能：** 设置阴影类型。

**类型：** ?[ShadowType](#enum-shadowtype)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var color

```cangjie
public var color: ?ResourceColor
```

**功能：** 设置阴影颜色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var offsetX

```cangjie
public var offsetX: ?Float64
```

**功能：** 设置阴影的水平偏移量。

**类型：** ?Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var offsetY

```cangjie
public var offsetY: ?Float64
```

**功能：** 设置阴影的垂直偏移量。

**类型：** ?Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var fill

```cangjie
public var fill: ?Bool
```

**功能：** 是否填充。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?Float64, ?ShadowType, ?ResourceColor, ?Float64, ?Float64, ?Bool)

```cangjie
public init(radius!: ?Float64, shadowType!: ?ShadowType = None, color!: ?ResourceColor = None, offsetX!: ?Float64 = None, offsetY!: ?Float64 = None, fill!: ?Bool = None)
```

**功能：** 构造一个ShadowOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|radius|?Float64|是|-|**命名参数。** 设置阴影的模糊半径。|
|shadowType|?[ShadowType](./cj-common-types.md#enum-shadowtype)|否|None|**命名参数。** 设置阴影类型。初始值为ShadowType.Color。|
|color|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None|**命名参数。** 设置阴影颜色。初始值为Color.Black。|
|offsetX|?Float64|否|None|**命名参数。** 设置阴影的水平偏移量。初始值为0.0。|
|offsetY|?Float64|否|None|**命名参数。** 设置阴影的垂直偏移量。初始值为0.0。|
|fill|?Bool|否|None|**命名参数。** 设置阴影是否填充。初始值为false。|