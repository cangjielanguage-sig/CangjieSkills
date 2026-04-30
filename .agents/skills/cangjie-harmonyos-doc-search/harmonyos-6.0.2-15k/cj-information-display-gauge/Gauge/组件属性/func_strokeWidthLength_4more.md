### func strokeWidth(Length)

```cangjie
public func strokeWidth(value: Length): This
```

**功能：** 设置环形量规图的环形厚度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|环形量规图的环形厚度。<br>初始值：4.vp。<br>单位：vp。<br>**说明：**<br>设置小于0的值时，按默认值显示。<br>环形厚度的最大值为圆环的半径，超过最大值按最大值处理。<br>不支持百分比。|

### func trackShadow(Float64, Float64, Float64)

```cangjie
public func trackShadow(radius!: Float64 = 20.0, offsetX!: Float64 = 5.0, offsetY!: Float64 = 5.0): This
```

**功能：** 设置阴影样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|radius|Float64|否|20.0| **命名参数。** 投影模糊半径。<br>单位：vp。|
|offsetX|Float64|否|5.0| **命名参数。** X轴的偏移量。|
|offsetY|Float64|否|5.0| **命名参数。** Y轴的偏移量 。|

### func value(Float64)

```cangjie
public func value(gaugeValue: Float64): This
```

**功能：** 设置量规图的数据值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|gaugeValue|Float64|是|-|量规图的数据值，可用于动态修改量规图的数据值。<br>初始值：0.0。|

### func value(Int64)

```cangjie
public func value(gaugeValue: Int64): This
```

**功能：** 设置量规图的数据值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|gaugeValue|Int64|是|-|量规图的数据值，可用于动态修改量规图的数据值。<br>初始值：0.0。|