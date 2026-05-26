### class DragEvent

```cangjie
public class DragEvent {
    public let useCustomDropAnimation: Bool
    public let dragBehavior: DragBehavior
}
```

**功能：** 拖拽事件类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let dragBehavior

```cangjie
public let dragBehavior: DragBehavior
```

**功能：** 切换复制和剪贴模式的角标显示状态。

**类型：** [DragBehavior](#enum-dragbehavior)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let useCustomDropAnimation

```cangjie
public let useCustomDropAnimation: Bool
```

**功能：** 当拖拽结束时，是否使能并使用系统默认落位动效。<br/>应用可将该值设定为true来禁用系统默认落位动效，并实现自己的自定义落位动效。<br/>当不配置或设置为false时，系统默认落位动效生效，当松手位置的控件可接收拖拽的数据时，落位为缩小消失动效，若不可接收数据，则为放大消失动效。<br/>当未禁用系统默认落位动效情况下，应用不应再实现自定义动效，以避免动效上的冲突。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### func getDisplayX()

```cangjie
public func getDisplayX(): Float64
```

**功能：** 当前拖拽点相对于屏幕左上角的x轴坐标，单位为vp。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Float64|x轴坐标值。|

#### func getDisplayY()

```cangjie
public func getDisplayY(): Float64
```

**功能：** 当前拖拽点相对于屏幕左上角的y轴坐标，单位为vp。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Float64|y轴坐标值。|

#### func getModifierKeyState(Array\<String>)

```cangjie
public func getModifierKeyState(keys: Array<String>): Bool
```

**功能：** 获取功能键按压状态。报错信息请参考以下错误码。支持功能键 "Ctrl"|"Alt"|"Shift"|"Fn"，设备外接带Fn键的键盘不支持Fn键查询。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|keys|Array\<String>|是|-|功能键字符串数组。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|按压状态。|

#### func getPreviewRect()

```cangjie
public func getPreviewRect(): Rectangle
```

**功能：** 获取拖拽跟手图相对于当前窗口的位置，以及跟手图尺寸信息，单位VP，其中x和y代表跟手图左上角的窗口坐标，width和height代表跟手图的尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[Rectangle](./cj-common-types.md#class-rectangle)|拖拽跟手图位置信息。|

#### func getResult()

```cangjie
public func getResult(): DragResult
```

**功能：** 从DragEvent中获取拖拽结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[DragResult](#enum-dragresult)|拖拽结果。|

#### func getVelocity()

```cangjie
public func getVelocity(): Float64
```

**功能：** 获取当前拖拽的主方向拖动速度。为xy轴方向速度的平方和的算术平方根。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Float64|主方向拖动速度。|

#### func getVelocityX()

```cangjie
public func getVelocityX(): Float64
```

**功能：** 获取当前拖拽的x轴方向拖动速度。坐标轴原点为屏幕左上角，单位为vp，分正负方向速度，从左往右为正，反之为负。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Float64|x轴方向拖动速度。|