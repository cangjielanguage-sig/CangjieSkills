### func indicator(?ResourceStr, ?Length)

```cangjie
public func indicator(icon!: ?ResourceStr = None, space!: ?Length = None): This
```

**功能：** 设置指针样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None| **命名参数。** 初始值: "SystemStyle"。 指针样式："SystemStyle"为三角箭头，"null"为无指针。|
|space|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 初始值: 8.0.vp。 指针距离圆环外边的间距(不支持百分比)。<br>单位：vp。|

### func startAngle(?Float32)

```cangjie
public func startAngle(angle: ?Float32): This
```

**功能：** 设置量规图起始角度位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|angle|?Float32|是|-|起始角度位置，时钟0点为0度，顺时针方向为正角度。初始值: 0.0。|

### func strokeWidth(?Length)

```cangjie
public func strokeWidth(length: ?Length): This
```

**功能：** 设置环形量规图的环形厚度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|length|?[Length](./cj-common-types.md#interface-length)|是|-|环形量规图的环形厚度。<br>初始值: 4.0.vp。<br>单位：vp。<br>**说明：**<br>设置小于0的值时，按默认值显示。<br>环形厚度的最大值为圆环的半径，超过最大值按最大值处理。<br>不支持百分比。|

### func trackShadow(?Float32, ?Float32, ?Float32)

```cangjie
public func trackShadow(radius!: ?Float32 = None, offsetX!: ?Float32 = None, offsetY!: ?Float32 = None): This
```

**功能：** 设置阴影样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|radius|?Float32|否|None| **命名参数。** 初始值: 20.0 投影模糊半径。<br>单位：vp。|
|offsetX|?Float32|否|None| **命名参数。** 初始值: 5.0 X轴的偏移量。|
|offsetY|?Float32|否|None| **命名参数。** 初始值: 5.0 Y轴的偏移量 。|

### func value(?Float32)

```cangjie
public func value(value: ?Float32): This
```

**功能：** 设置量规图的数据值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Float32|是|-|量规图的数据值，可用于动态修改量规图的数据值。<br>初始值: 0.0。|