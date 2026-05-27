## class DividerStyleOptions

```cangjie
public class DividerStyleOptions {
    public let strokeWidth: Length
    public let color: ResourceColor
    public let startMargin: Length
    public let endMargin: Length
    public init(strokeWidth: Length,color: ResourceColor,startMargin: Length,endMargin: Length)
}
```

**功能：** 分割线样式属性集合，用于描述分割线相关信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let color

```cangjie
public let color: ResourceColor
```

**功能：** 分割线的颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let endMargin

```cangjie
public let endMargin: Length
```

**功能：** 分割线与菜单侧边结束端的距离。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let startMargin

```cangjie
public let startMargin: Length
```

**功能：** 分割线与菜单侧边起始端的距离。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let strokeWidth

```cangjie
public let strokeWidth: Length
```

**功能：** 分割线的线宽。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### init(Length, ResourceColor, Length, Length)

```cangjie
public init(strokeWidth: Length,color: ResourceColor,startMargin: Length,endMargin: Length
)
```

**功能：** 初始化一个DividerStyleOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|strokeWidth|[Length](./cj-common-types.md#interface-length)|是|-|分割线的线宽。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|分割线的颜色。|
|startMargin|[Length](./cj-common-types.md#interface-length)|是|-|分割线与菜单侧边起始端的距离。|
|endMargin|[Length](./cj-common-types.md#interface-length)|是|-|分割线与菜单侧边结束端的距离。|