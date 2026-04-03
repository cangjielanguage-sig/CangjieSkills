### func blockBorderColor(ResourceColor)

```cangjie
public func blockBorderColor(value: ResourceColor): This
```

**功能：** 设置滑块描边颜色。

当滑块形状设置为SliderBlockType.DEFAULT时，blockBorderColor可设置默认圆形滑块描边颜色。

当滑块形状设置为SliderBlockType.IMAGE时，滑块无描边，设置blockBorderColor不生效。

当滑块形状设置为SliderBlockType.SHAPE时，blockBorderColor可设置自定义形状中线的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|滑块描边颜色。<br/>初始值：0x00000000。|

### func blockBorderWidth(Length)

```cangjie
public func blockBorderWidth(value: Length): This
```

**功能：** 设置滑块描边粗细。

当滑块形状设置为SliderBlockType.DEFAULT时，blockBorderWidth可设置默认圆形滑块描边粗细。

当滑块形状设置为SliderBlockType.IMAGE时，滑块无描边，设置blockBorderWidth不生效。

当滑块形状设置为SliderBlockType.SHAPE时，blockBorderWidth可设置自定义形状中线的粗细。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#enum-lengthtype)|是|-|滑块描边粗细。不支持百分比设置。|

### func blockColor(ResourceColor)

```cangjie
public func blockColor(value: ResourceColor): This
```

**功能：** 设置滑块的颜色。

当滑块形状设置为SliderBlockType.DEFAULT时，blockColor可设置默认圆形滑块颜色。

当滑块形状设置为SliderBlockType.IMAGE时，滑块无填充，设置blockColor不生效。

当滑块形状设置为SliderBlockType.SHAPE时，blockColor可设置自定义形状的填充颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|滑块的颜色。<br/>初始值：@r(sys.color.ohos_id_color_foreground_contrary)。|

### func blockSize(Length, Length)

```cangjie
public func blockSize(width!: Length = 0.vp, height!: Length = 0.vp): This
```

**功能：** 设置滑块大小。

当滑块形状设置为SliderBlockType.DEFAULT时，取宽高的最小值作为圆形半径。

当滑块形状设置为SliderBlockType.IMAGE时，用于设置图片的尺寸大小，图片采用ObjectFit.Cover策略进行缩放。

当滑块形状设置为SliderBlockType.SHAPE时，用于设置自定义形状的大小，自定义形状也会采用ObjectFit.Cover策略进行缩放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 滑块宽度。|
|height|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 滑块高度。|

> **说明：**
>
> 当参数style的值设置为SliderStyle.OutSet时初始值为{width: 16, height: 16}。
> 当参数style的值设置为SliderStyle.InSet时初始值为{width: 12, height: 12}。
> 当参数style的值设置为SliderStyle.NONE时为，此字段不生效。
> 当设置的blockSize的宽高值不相等时，取较小值的尺寸。
> 当设置的宽高值中有一个或两个都小于等于0的时候，取初始值。