### prop shadowBlur

```cangjie
public mut prop shadowBlur: Option<Float64>
```

**功能：** 阴影模糊半径。值不能为负数。

**类型：** Option\<Float64>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop shadowColor

```cangjie
public mut prop shadowColor: Option<ResourceColor>
```

**功能：** 阴影颜色。

**类型：** Option\<[ResourceColor](./cj-common-types.md#interface-resourcecolor)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop shadowOffsetX

```cangjie
public mut prop shadowOffsetX: Option<Float64>
```

**功能：** 阴影的水平偏移距离。

**类型：** Option\<Float64>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop shadowOffsetY

```cangjie
public mut prop shadowOffsetY: Option<Float64>
```

**功能：** 阴影的垂直偏移距离。

**类型：** Option\<Float64>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop imageSmoothingEnabled

```cangjie
public mut prop imageSmoothingEnabled: Option<Bool>
```

**功能：** 用于设置绘制图片时是否进行图像平滑度调整。true为启用，false为不启用。

**类型：** Option\<Bool>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop imageSmoothingQuality

```cangjie
public mut prop imageSmoothingQuality: Option<String>
```

**功能：** 用于设置图像平滑度。

**类型：** Option\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop direction

```cangjie
public mut prop direction: Option<String>
```

**功能：** 文本绘制方向。

**类型：** Option\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop filter

```cangjie
public mut prop filter: Option<String>
```

**功能：** 提供模糊、灰度等滤镜效果。

**类型：** Option\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop height

```cangjie
public prop height: Float64
```

**功能：** 默认值为0，绑定指定画布的高度。该值为只读。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop width

```cangjie
public prop width: Float64
```

**功能：** 默认值为0，绑定指定画布的宽度。该值为只读。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func setLineDash(?Array\<Float64>)

```cangjie
public func setLineDash(segments: ?Array<Float64>): Unit
```

**功能：** 为线条设置虚线模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|segments|?Array\<Float64>|是|-|描述线段如何交替和线段间距长度的数组。<br>默认单位：vp|

### func fillRect(Float64, Float64, Float64, Float64)

```cangjie
public func fillRect(x: Float64, y: Float64, w: Float64, h: Float64): Unit
```

**功能：** 填充指定的矩形区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|指定矩形左上角点的x坐标。<br>默认单位：vp。|
|y|Float64|是|-|指定矩形左上角点的y坐标。<br>默认单位：vp。|
|w|Float64|是|-|指定矩形的宽度。<br>默认单位：vp。|
|h|Float64|是|-|指定矩形的高度。<br>默认单位：vp。|