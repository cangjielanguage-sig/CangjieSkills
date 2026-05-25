### func lineTo(Int64, Int64)

```cangjie
public func lineTo(x: Int64, y: Int64): Unit
```

**功能：** 从当前点绘制一条直线到目标点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int64|是|-|目标点X轴坐标。<br>默认单位：vp。|
|y|Int64|是|-|目标点Y轴坐标。<br>默认单位：vp。|

### func moveTo(Float64, Float64)

```cangjie
public func moveTo(x: Float64, y: Float64): Unit
```

**功能：** 将路径的当前坐标点移动到目标点，移动过程中不绘制线条。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|目标点X轴坐标。<br>默认单位：vp。|
|y|Float64|是|-|目标点Y轴坐标。<br>默认单位：vp。|

### func moveTo(Int64, Int64)

```cangjie
public func moveTo(x: Int64, y: Int64): Unit
```

**功能：** 将路径的当前坐标点移动到目标点，移动过程中不绘制线条。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int64|是|-|目标点X轴坐标。<br>默认单位：vp。|
|y|Int64|是|-|目标点Y轴坐标。<br>默认单位：vp。|

### func quadraticCurveTo(Float64, Float64, Float64, Float64)

```cangjie
public func quadraticCurveTo(
    cpx: Float64,
    cpy: Float64,
    x: Float64,
    y: Float64
): Unit
```

**功能：** 创建二次贝赛尔曲线的路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cpx|Float64|是|-|贝塞尔参数的x坐标值。<br>默认单位：vp。|
|cpy|Float64|是|-|贝塞尔参数的y坐标值。<br>默认单位：vp。|
|x|Float64|是|-|路径结束时的x坐标值。<br>默认单位：vp。|
|y|Float64|是|-|路径结束时的y坐标值。<br>默认单位：vp。|

### func quadraticCurveTo(Int64, Int64, Int64, Int64)

```cangjie
public func quadraticCurveTo(
    cpx: Int64,
    cpy: Int64,
    x: Int64,
    y: Int64
): Unit
```

**功能：** 创建二次贝赛尔曲线的路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cpx|Int64|是|-|贝塞尔参数的x坐标值。<br>默认单位：vp。|
|cpy|Int64|是|-|贝塞尔参数的y坐标值。<br>默认单位：vp。|
|x|Int64|是|-|路径结束时的x坐标值。<br>默认单位：vp。|
|y|Int64|是|-|路径结束时的y坐标值。<br>默认单位：vp。|

### func rect(Float64, Float64, Float64, Float64)

```cangjie
public func rect(x: Float64, y: Float64, width: Float64, height: Float64): Unit
```

**功能：** 创建矩形路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|指定矩形的左上角x坐标值。<br>默认单位：vp。|
|y|Float64|是|-|指定矩形的左上角y坐标值。<br>默认单位：vp。|
|width|Float64|是|-|指定矩形的宽度。<br>默认单位：vp。|
|height|Float64|是|-|指定矩形的高度。<br>默认单位：vp。|

### func rect(Int64, Int64, Int64, Int64)

```cangjie
public func rect(x: Int64, y: Int64, width: Int64, height: Int64): Unit
```

**功能：** 创建矩形路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int64|是|-|指定矩形的左上角x坐标值。<br>默认单位：vp。|
|y|Int64|是|-|指定矩形的左上角y坐标值。<br>默认单位：vp。|
|width|Int64|是|-|指定矩形的宽度。<br>默认单位：vp。|
|height|Int64|是|-|指定矩形的高度。<br>默认单位：vp。|