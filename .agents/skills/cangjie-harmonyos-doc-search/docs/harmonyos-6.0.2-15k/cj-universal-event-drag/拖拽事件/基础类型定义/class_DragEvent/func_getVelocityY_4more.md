#### func getVelocityY()

```cangjie
public func getVelocityY(): Float64
```

**功能：** 获取当前拖拽的y轴方向拖动速度。坐标轴原点为屏幕左上角，单位为vp，分正负方向速度，从上往下为正，反之为负。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Float64|y轴方向拖动速度。|

#### func getWindowX()

```cangjie
public func getWindowX(): Float64
```

**功能：** 当前拖拽点相对于窗口左上角的x轴坐标，单位为vp。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Float64|x轴坐标值。|

#### func getWindowY()

```cangjie
public func getWindowY(): Float64
```

**功能：** 当前拖拽点相对于窗口左上角的y轴坐标，单位为vp。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Float64|y轴坐标值。|

#### func setResult(DragResult)

```cangjie
public func setResult(dragRect: DragResult): Unit
```

**功能：** 向DragEvent中设置拖拽结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dragRect|[DragResult](#enum-dragresult)|是|-|拖拽结果。|