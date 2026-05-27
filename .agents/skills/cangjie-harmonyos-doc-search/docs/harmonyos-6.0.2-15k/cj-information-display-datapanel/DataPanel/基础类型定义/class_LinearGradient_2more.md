### class LinearGradient

```cangjie
public class LinearGradient {
    public var colorStops: Array<ColorStop>
    public init(colorStops: Array<ColorStop>)
    public init(color: ResourceColor)
}
```

**功能：** 线性渐变颜色描述。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var colorStops

```cangjie
public var colorStops: Array<ColorStop>
```

**功能：** 存储渐变颜色和渐变点。

**类型：** Array\<[ColorStop](#class-colorstop)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(Array\<ColorStop>)

```cangjie
public init(colorStops: Array<ColorStop>)
```

**功能：** 渐变颜色描述。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|colorStops|Array\<[ColorStop](#class-colorstop)>|是|-|存储渐变颜色和渐变点。|

#### init(ResourceColor)

```cangjie
public init(color: ResourceColor)
```

**功能：** 渐变颜色描述。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|单一渐变颜色。|

### class ColorStop

```cangjie
public class ColorStop {
    public var color: UInt32
    public var offset: Length
    public init(color: ResourceColor, offset: Length)
}
```

**功能：** 颜色断点类型，用于描述渐进色颜色断点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var color

```cangjie
public var color: UInt32
```

**功能：** 颜色值。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var offset

```cangjie
public var offset: Length
```

**功能：** 渐变色断点（0~1之间的比例值，若数据值小于0则置为0，若数据值大于1则置为1）。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(ResourceColor, Length)

```cangjie
public init(color: ResourceColor, offset: Length)
```

**功能：** 渐进色颜色断点描述。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|颜色值。|
|offset|[Length](./cj-common-types.md#interface-length)|是|-|渐变色断点（0~1之间的比例值，若数据值小于0则置为0，若数据值大于1则置为1）。|