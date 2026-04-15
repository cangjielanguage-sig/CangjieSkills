## class HorizontalAlignParam

```cangjie
public class HorizontalAlignParam {
    public var anchor: ?String
    public var align: ?HorizontalAlign
    public init(anchor: ?String, align: ?HorizontalAlign)
}
```

**功能：** 水平对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var anchor

```cangjie
public var anchor: ?String
```

**功能：** 设置组件水平对齐的锚点。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var align

```cangjie
public var align: ?HorizontalAlign
```

**功能：** 设置组件水平方向对齐方式。

**类型：** ?[HorizontalAlign](#enum-horizontalalign)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?String, ?HorizontalAlign)

```cangjie
public init(anchor: ?String, align: ?HorizontalAlign)
```

**功能：** 构造一个HorizontalAlignment对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|anchor|?String|是|-|设置组件水平对齐的锚点。|
|align|?[HorizontalAlign](#enum-horizontalalign)|是|-|设置组件水平方向对齐方式。|

## class VerticalAlignParam

```cangjie
public class VerticalAlignParam {
    public var anchor: ?String
    public var align: ?VerticalAlign
    public init(anchor: ?String, align: ?VerticalAlign)
}
```

**功能：** 垂直对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var anchor

```cangjie
public var anchor: ?String
```

**功能：** 设置组件垂直对齐的锚点。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var align

```cangjie
public var align: ?VerticalAlign
```

**功能：** 设置组件垂直方向对齐方式。

**类型：** ?[VerticalAlign](#enum-verticalalign)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?String, ?VerticalAlign)

```cangjie
public init(anchor: ?String, align: ?VerticalAlign)
```

**功能：** 构造一个VerticalAlignment对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|anchor|?String|是|-|设置组件垂直对齐的锚点。|
|align|?[VerticalAlign](#enum-verticalalign)|是|-|设置组件垂直方向对齐方式。|

## class Bias

```cangjie
public class Bias {
    public var horizontal: ?Float32
    public var vertical: ?Float32
    public init(horizontal!: ?Float32 = None, vertical!: ?Float32 = None)
}
```

**功能：** 设置组件对齐的偏移量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var horizontal

```cangjie
public var horizontal: ?Float32
```

**功能：** 设置组件水平方向的偏移量。

**类型：** ?Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var vertical

```cangjie
public var vertical: ?Float32
```

**功能：** 设置组件垂直方向的偏移量。

**类型：** ?Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?Float32, ?Float32)

```cangjie
public init(horizontal!: ?Float32 = None, vertical!: ?Float32 = None)
```

**功能：** 构造一个Bias对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|horizontal|?Float32|否|None|**命名参数。** 设置组件水平方向的偏移量。初始值为0.5。|
|vertical|?Float32|否|None|**命名参数。** 设置组件垂直方向的偏移量。初始值为0.5。|