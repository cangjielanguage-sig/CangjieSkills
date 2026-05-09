### class ColorStop

```cangjie
public class ColorStop {
    public var color: ResourceColor
    public var offset: Length
    public init(color: ResourceColor, offset: Length)
}
```

**功能：** 颜色断点类型，用于描述渐进色颜色断点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var color

```cangjie
public var color: ResourceColor
```

**功能：** 颜色值。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var offset

```cangjie
public var offset: Length
```

**功能：** 渐变色断点（0~1之间的比例值，若数据值小于0则置为0，若数据值大于1则置为1）。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(ResourceColor, Length)

```cangjie
public init(color: ResourceColor, offset: Length)
```

**功能：** 创建ColorStop对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|颜色值。|
|offset|[Length](./cj-common-types.md#interface-length)|是|-|渐变色断点（0~1之间的比例值，若数据值小于0则置为0，若数据值大于1则置为1）。|