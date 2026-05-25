### func colors(?Array\<(ResourceColor, Int32)>)

```cangjie
public func colors(value: ?Array<(ResourceColor, Int32)>): This
```

**功能：** 设置量规图的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Array\<([ResourceColor](./cj-common-types.md#interface-resourcecolor), Int32)>|是|-|量规图的颜色，支持分段颜色设置。|

### func colors(?Array\<(LinearGradient, Int32)>)

```cangjie
public func colors(value: ?Array<(LinearGradient, Int32)>): This
```

**功能：** 设置量规图的分段渐变颜色组。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Array\<([LinearGradient](cj-information-display-datapanel.md#class-lineargradient), Int32)>|是|-|量规图的渐变色，支持分段颜色设置，最多9组。LinearGradient类型见datapanel组件，Int32为该段颜色的宽度范围。|

### func colors(?LinearGradient)

```cangjie
public func colors(value: ?LinearGradient): This
```

**功能：** 设置量规图的分段渐变颜色组。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[LinearGradient](./cj-information-display-datapanel.md#class-lineargradient)|是|-|量规图的渐变色，支持分段颜色设置，最多9组。|

### func colors(?ResourceColor)

```cangjie
public func colors(value: ?ResourceColor): This
```

**功能：** 设置量规图的颜色。

参数类型为ResourceColor，则圆环类型为单色环。

参数类型为LinearGradient，则圆环类型为渐变环。

参数类型为数组，则圆环类型为分段渐变环，第一个参数为颜色值，若设置为非颜色类型，则置为"0xFFE84026"。第二个参数为颜色所占比重，若设置为负数或是非数值类型，则将比重置为0。

分段渐变环最大显示段数为9段，若多于9段，则多于部分不显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|量规图的颜色，支持分段颜色设置。|

### func description(?CustomBuilder)

```cangjie
public func description(builder: ?CustomBuilder): This
```

**功能：** 设置量规图的说明内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|?[CustomBuilder](./cj-common-types.md#type-custombuilder)|是|-|说明内容，@Builder中的内容由开发者自定义，建议使用文本。<br>初始值：{ => }。|

### func endAngle(?Float32)

```cangjie
public func endAngle(angle: ?Float32): This
```

**功能：** 设置终止角度位置。

> **说明：**
>
> 当起始角度位置和终止角度位置差过小时，会绘制出异常图像，请选取合理的起始角度位置和终止角度位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|angle|?Float32|是|-|终止角度位置，时钟0点为0度，顺时针方向为正角度。<br>初始值: 360.0。|