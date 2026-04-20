### class LinearGradient

```cangjie
public class LinearGradient {
    public init(colorStops: Array<ColorStop>)
    public init(color: ResourceColor)
}
```

**功能：** 线性渐变颜色描述。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(Array\<ColorStop>)

```cangjie
public init(colorStops: Array<ColorStop>)
```

**功能：** 渐变颜色描述。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|colorStops|Array\<[ColorStop](#class-colorstop)>|是|-| 存储渐变颜色和渐变点。|

#### init(ResourceColor)

```cangjie
public init(color: ResourceColor)
```

**功能：** 渐变颜色描述。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|单一渐变颜色。|