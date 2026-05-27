### class LocalizedHorizontalAlignParam

```cangjie
public class LocalizedHorizontalAlignParam {
    public LocalizedHorizontalAlignParam (
        public var anchor!: String,
        public var align!: HorizontalAlign
    )
}
```

**功能：** 设置横向对齐方式的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var align

```cangjie
public var align: HorizontalAlign
```

**功能：** 设置相对于锚点组件的横向对齐方式。

**类型：** [HorizontalAlign](./cj-common-types.md#enum-horizontalalign)

**读写能力：** 可读写

**起始版本：** 19

#### var anchor

```cangjie
public var anchor: String
```

**功能：** 设置作为锚点的组件的id值。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### class LocalizedVerticalAlignParam

```cangjie
public class LocalizedVerticalAlignParam {
    public LocalizedVerticalAlignParam (
        public var anchor!: String,
        public var align!: VerticalAlign
    )
}
```

**功能：** 设置纵向对齐方式的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var align

```cangjie
public var align: VerticalAlign
```

**功能：** 设置相对于锚点组件的纵向对齐方式。

**类型：** [VerticalAlign](./cj-common-types.md#enum-verticalalign)

**读写能力：** 可读写

**起始版本：** 19

#### var anchor

```cangjie
public var anchor: String
```

**功能：** 设置作为锚点的组件的id值。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

#### LocalizedVerticalAlignParam(String, VerticalAlign)

```cangjie
public LocalizedVerticalAlignParam (
    public var anchor!: String,
    public var align!: VerticalAlign
)
```

**功能：** 创建LocalizedVerticalAlignParam类型的对象。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|anchor|String|是|-| **命名参数。** 作为锚点的组件的id值。|
|align|[VerticalAlign](./cj-common-types.md#enum-verticalalign)|是|-| **命名参数。** 相对于锚点组件的纵向对齐方式。|

### class VerticalAnchor

```cangjie
public class VerticalAnchor {
    public VerticalAnchor (
        public var anchor: String,
        public var align: VerticalAlign
    )
}
```

**功能：** 设置垂直对齐参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var align

```cangjie
public var align: VerticalAlign
```

**功能：** 设置相对于锚点组件的对齐方式。

**类型：** [VerticalAlign](./cj-common-types.md#enum-verticalalign)

**读写能力：** 可读写

**起始版本：** 12

#### var anchor

```cangjie
public var anchor: String
```

**功能：** 设置作为锚点的组件的id值。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

#### VerticalAnchor(String, VerticalAlign)

```cangjie
public VerticalAnchor (
    public var anchor: String,
    public var align: VerticalAlign
)
```

**功能：** 创建一个 VerticalAnchor 类型的对象。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|anchor|String|是|-|作为锚点的组件的id值。|
|align|[VerticalAlign](./cj-common-types.md#enum-verticalalign)|是|-|相对于锚点组件的对齐方式。|

### enum ChainStyle

```cangjie
public enum ChainStyle {
    | SPREAD
    | SPREAD_INSIDE
    | PACKED
}
```

**功能：** 定义链的风格。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### PACKED

```cangjie
PACKED
```

**功能：** 链内子组件无间隙。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### SPREAD

```cangjie
SPREAD
```

**功能：** 组件在约束锚点间均匀分布。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### SPREAD_INSIDE

```cangjie
SPREAD_INSIDE
```

**功能：** 除首尾2个子组件的其他组件在约束锚点间均匀分布。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19