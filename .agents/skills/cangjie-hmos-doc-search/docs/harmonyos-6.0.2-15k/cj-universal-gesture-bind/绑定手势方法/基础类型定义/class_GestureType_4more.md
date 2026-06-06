### class GestureType

```cangjie
public open class GestureType {}
```

**功能：** 所有手势类型的基础类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### func tag(String)

```cangjie
public func tag(tag: String): This
```

**功能：** 设置手势标志，用于自定义手势判定时区分绑定的手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|tag|String|是|-|设置手势标志，用于自定义手势判定时区分绑定的手势。|

### class EventTarget

```cangjie
public class EventTarget {
    public EventTarget(
        public var area: Area
    )
}
```

**功能：** 触发手势事件的元素对象显示区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var area

```cangjie
public var area: Area
```

**功能：** 目标元素的区域信息。

**类型：** [Area](cj-common-types.md#class-area)

**读写能力：** 可读写

**起始版本：** 19

#### EventTarget(Area)

```cangjie
public EventTarget(
    public var area: Area
)
```

**功能：** 构造触发手势事件的元素对象显示区域类型的对象。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|area|Area|是|-|目标元素的区域信息。|

### class FingerInfo

```cangjie
public class FingerInfo {
    public let id: Int32
    public let globalX: Float64
    public let globalY: Float64
    public let localX: Float64
    public let localY: Float64
}
```

**功能：** 手指信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### let id

```cangjie
public let id: Int32
```

**功能：** 手指的索引编号。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

#### let globalX

```cangjie
public let globalX: Float64
```

**功能：** 相对于应用窗口左上角的x轴坐标，单位为vp。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

#### let globalY

```cangjie
public let globalY: Float64
```

**功能：** 相对于应用窗口左上角的y轴坐标，单位为vp。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

#### let localX

```cangjie
public let localX: Float64
```

**功能：** 相对于当前组件元素原始区域左上角的x轴坐标，单位为vp。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

#### let localY

```cangjie
public let localY: Float64
```

**功能：** 相对于当前组件元素原始区域左上角的y轴坐标，单位为vp。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

### enum GestureMask

```cangjie
public enum GestureMask {
    | Normal
    | IgnoreInternal
}
```

**功能：** 事件响应设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Normal

```cangjie
Normal
```

**功能：** 不屏蔽子组件的手势，按照默认手势识别顺序进行识别。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### IgnoreInternal

```cangjie
IgnoreInternal
```

**功能：** 屏蔽子组件的手势，包括子组件上系统内置的手势，如子组件为List组件时，内置的滑动手势同样会被屏蔽。 若父子组件区域存在部分重叠，则只会屏蔽父子组件重叠的部分。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19