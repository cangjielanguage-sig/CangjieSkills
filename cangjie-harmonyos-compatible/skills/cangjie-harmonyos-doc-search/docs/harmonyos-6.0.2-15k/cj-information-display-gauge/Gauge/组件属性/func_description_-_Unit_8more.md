### func description(() -> Unit)

```cangjie
public func description(builder: () -> Unit): This
```

**功能：** 设置量规图的说明内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|()->Unit|是|-|说明内容，@Builder中的内容由开发者自定义，建议使用文本。|

### func endAngle(Float64)

```cangjie
public func endAngle(value: Float64): This
```

**功能：** 设置终止角度位置。

> **说明：**
>
> 当起始角度位置和终止角度位置差过小时，会绘制出异常图像，请取合理的起始角度位置和终止角度位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|终止角度位置，时钟0点为0度，顺时针方向为正角度。<br>初始值：360.0。|

### func endAngle(Int64)

```cangjie
public func endAngle(value: Int64): This
```

**功能：** 设置终止角度位置。

> **说明：**
>
> 当起始角度位置和终止角度位置差过小时，会绘制出异常图像，请取合理的起始角度位置和终止角度位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int64|是|-|终止角度位置，时钟0点为0度，顺时针方向为正角度。<br>初始值：360.0。|

### func indicator(String, Float64)

```cangjie
public func indicator(icon!: String = "default", space!: Float64 = 8.0): This
```

**功能：** 设置指针样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|String|否|"default"| **命名参数。** 指针样式："default"为三角箭头，"null"为无指针。|
|space|Float64|否|8.0| **命名参数。** 指针距离圆环外边的间距(不支持百分比)。<br>单位：vp。|

### func indicator(String, UInt64)

```cangjie
public func indicator(icon!: String = "default", space!: UInt64): This
```

**功能：** 设置指针样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|String|否|"default"| **命名参数。** 指针样式："default"为三角箭头，"null"为无指针。|
|space|UInt64|是|-| **命名参数。** 指针距离圆环外边的间距(不支持百分比)。<br>单位：vp。|

### func privacySensitive(Option\<Bool>)

```cangjie
public func privacySensitive(isPrivacySensitiveMode: Option<Bool>): This
```

**功能：** 设置隐私敏感。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isPrivacySensitiveMode|Option\<Bool>|是|-|设置隐私敏感，隐私模式下Gauge指针指向0位置，最大值最小值文本将被遮罩，量程显示灰色或者底色。<br>**说明：**<br>设置成None则不敏感。|

### func startAngle(Float64)

```cangjie
public func startAngle(value: Float64): This
```

**功能：** 设置量规图起始角度位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|起始角度位置，时钟0点为0度，顺时针方向为正角度。<br>初始值：0.0。|

### func startAngle(Int64)

```cangjie
public func startAngle(value: Int64): This
```

**功能：** 设置量规图起始角度位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int64|是|-|起始角度位置，时钟0点为0度，顺时针方向为正角度。<br>初始值：0.0。|