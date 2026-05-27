### func minResponsiveDistance(Int64)

```cangjie
public func minResponsiveDistance(value: Int64): This
```

**功能：** 设置滑动响应的最小距离。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int64|是|-|设置滑动响应的最小距离，滑动超过此距离后才响应使滑块滑动。<br/>**说明**：<br/>单位与参数min和max一致。<br/>当value小于0、大于MAX-MIN或非法值时，取初始值。<br/>初始值：0。|

### func selectedBorderRadius(Length)

```cangjie
public func selectedBorderRadius(value: Length): This
```

**功能：** 设置已滑动部分（高亮）圆角半径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|已选择部分圆角半径。<br/>初始值：style值为SliderStyle.InSet或SliderStyle.OutSet时，跟随底板圆角；style值为SliderStyle.NONE时，为0。不支持百分比设置，设定值小于0时取初始值。|

### func selectedColor(ResourceColor)

```cangjie
public func selectedColor(value: ResourceColor): This
```

**功能：** 根据指定的Color设置滑轨已滑动部分的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|滑轨已滑动部分的颜色。<br/>初始值：@r(sys.color.ohos_id_color_emphasize)。|

### func showSteps(Bool)

```cangjie
public func showSteps(value: Bool): This
```

**功能：** 设置当前是否显示步长刻度值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|当前是否显示步长刻度值。<br/>初始值：false。|

### func showTips(Bool, ?String)

```cangjie
public func showTips(value: Bool, content!: ?String = None): This
```

**功能：** 设置滑动时是否显示气泡提示。

当direction的值为Axis.Horizontal时，tip显示在滑块上方，如果上方空间不够，则在下方显示。值为Axis.Vertical时，tip显示在滑块左边，如果左边空间不够，则在右边显示。不设置周边边距或者周边边距比较小时，tip会被截断。

tip的绘制区域为Slider自身节点的overlay。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|滑动时是否显示气泡提示。<br/>初始值：false。|
|content|?String|否|None| **命名参数。** 气泡提示的文本内容，默认显示当前百分比。|

### func slideRange(?Float32, ?Float32)

```cangjie
public func slideRange( from!: ?Float32 = None, to!: ?Float32 = None): This
```

**功能：** 设置有效滑动区间。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|from|?Float32|否|None| **命名参数。** 设置有效滑动区间的开始。|
|to|?Float32|否|None| **命名参数。** 设置有效滑动区间的结束。|

### func slideRange(?Int64, ?Int64)

```cangjie
public func slideRange(from!: ?Int64 = None, to!: ?Int64 = None): This
```

**功能：** 设置有效滑动区间。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|from|?Int64|否|None| **命名参数。** 设置有效滑动区间的开始。|
|to|?Int64|否|None| **命名参数。** 设置有效滑动区间的结束。|