### func blockBorderColor(?ResourceColor)

```cangjie
public func blockBorderColor(value: ?ResourceColor): This
```

**功能：** 设置滑块描边颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|滑块描边颜色。<br>初始值：0x00000000。|

### func blockColor(?ResourceColor)

```cangjie
public func blockColor(value: ?ResourceColor): This
```

**功能：** 设置滑块的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|滑块的颜色。|

### func selectedColor(?ResourceColor)

```cangjie
public func selectedColor(value: ?ResourceColor): This
```

**功能：** 根据指定的Color设置滑轨已滑动部分的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|滑轨已滑动部分的颜色。|

### func showSteps(?Bool)

```cangjie
public func showSteps(value: ?Bool): This
```

**功能：** 设置当前是否显示步长刻度值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|当前是否显示步长刻度值。<br>初始值：false。|

### func showTips(?Bool, ?ResourceStr)

```cangjie
public func showTips(value: ?Bool, content!: ?ResourceStr = None): This
```

**功能：** 设置滑动时是否显示气泡提示。

当direction的值为Axis.Horizontal时，tip显示在滑块上方，如果上方空间不够，则在下方显示。值为Axis.Vertical时，tip显示在滑块左边，如果左边空间不够，则在右边显示。不设置周边边距或者周边边距比较小时，tip会被截断。

tip的绘制区域为Slider自身节点的overlay。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|滑动时是否显示气泡提示。<br>初始值：false。|
|content|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None| **命名参数。** 气泡提示的文本内容，默认显示当前百分比。|

### func trackColor(?ResourceColor)

```cangjie
public func trackColor(value: ?ResourceColor): This
```

**功能：** 根据指定的Color设置滑轨的背景颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|滑轨的背景颜色。<br>**说明**：<br>设置渐变色时，若颜色断点颜色值为非法值或者渐变色断点为空时，渐变色不起效果。|