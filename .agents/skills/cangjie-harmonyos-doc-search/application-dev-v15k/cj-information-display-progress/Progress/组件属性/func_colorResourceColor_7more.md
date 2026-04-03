### func color(ResourceColor)

```cangjie
public func color(baseColor: ResourceColor): This
```

**功能：** 设置进度条前景色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|baseColor|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|进度条前景色。<br/>初始值：<br/>- Capsule：'0x33007dff'<br/>- Ring：起始端：'0xff86c1ff'，结束端：'0xff254ff7'<br/>- 其他样式：'0xff007dff'|

### func color(Array\<ColorStop>)

```cangjie
public func color(value: Array<ColorStop>): This
```

**功能：** 设置进度条前景色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Array\<[ColorStop](./cj-information-display-datapanel.md#class-colorstop)>|是|-|进度条前景色。<br/>初始值：<br/>- Capsule：'0x33007dff'<br/>- Ring：起始端：'0xff86c1ff'，结束端：'0xff254ff7'<br/>- 其他样式：'0xff007dff'|

### func style(Length, Int32, Length)

```cangjie
public func style(strokeWidth!: Length = 10.vp, scaleCount!: Int32 = 120, scaleWidth!: Length = 2.vp): This
```

**功能：** 设置进度条的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|strokeWidth|[Length](./cj-common-types.md#interface-length)|否|10.vp| **命名参数。** 设置进度条宽度（不支持百分比设置）。|
|scaleCount|Int32|否|120| **命名参数。** 设置环形进度条总刻度数。|
|scaleWidth|[Length](./cj-common-types.md#interface-length)|否|2.vp| **命名参数。** 设置环形进度条刻度粗细（不支持百分比设置），刻度粗细大于进度条宽度时，为系统默认粗细。|

### func style(RingStyleOptions)

```cangjie
public func style(ringStyle: RingStyleOptions): This
```

**功能：** 设置进度条Ring的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|ringStyle|[RingStyleOptions](#class-ringstyleoptions)|是|-|设置Ring的样式。|

### func style(EclipseStyleOptions)

```cangjie
public func style(eclipseStyle: EclipseStyleOptions): This
```

**功能：** 设置进度条Eclipse的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eclipseStyle|[EclipseStyleOptions](#class-eclipsestyleoptions)|是|-|设置Eclipse的样式。|

### func style(ScaleRingStyleOptions)

```cangjie
public func style(scaleRingStyle: ScaleRingStyleOptions): This
```

**功能：** 设置进度条ScaleRing的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scaleRingStyle|[ScaleRingStyleOptions](#class-scaleringstyleoptions)|是|-|设置ScaleRing的样式。|

### func style(ProgressStyleOptions)

```cangjie
public func style(progressStyle: ProgressStyleOptions): This
```

**功能：** 设置进度条的基础样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|progressStyle|[ProgressStyleOptions](#class-progressstyleoptions)|是|-|仅可设置各类型进度条的基本样式。|