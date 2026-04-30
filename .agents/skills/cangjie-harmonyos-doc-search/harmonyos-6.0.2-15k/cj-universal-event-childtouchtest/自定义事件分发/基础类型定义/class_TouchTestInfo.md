### class TouchTestInfo

```cangjie
public class TouchTestInfo {
    public let windowX: Float32
    public let windowY: Float32
    public let parentX: Float32
    public let parentY: Float32
    public let x: Float32
    public let y: Float32
    public let rect: RectResult
    public let id: String
    public init(windowX: Float32, windowY: Float32, parentX: Float32, parentY: Float32, x: Float32, y: Float32, rect: RectResult, id: String)
}
```

**功能：** 表示当前按压点所在组件的坐标系、id和尺寸相关信息的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let id

```cangjie
public let id: String
```

**功能：** 存放当前按压点所在组件的id。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let parentX

```cangjie
public let parentX: Float32
```

**功能：** 存放按压点相对于父组件左上角的横向坐标。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let parentY

```cangjie
public let parentY: Float32
```

**功能：** 存放按压点相对于父组件左上角的纵向坐标。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let rect

```cangjie
public let rect: RectResult
```

**功能：** 存放子组件的大小信息。

**类型：** [RectResult](./cj-common-types.md#class-rectresult)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let windowX

```cangjie
public let windowX: Float32
```

**功能：** 存放按压点相对于窗口左上角的横向坐标。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let windowY

```cangjie
public let windowY: Float32
```

**功能：** 存放按压点相对于窗口左上角的纵向坐标。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let x

```cangjie
public let x: Float32
```

**功能：** 存放按压点相对于子组件的左上角的横向坐标。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let y

```cangjie
public let y: Float32
```

**功能：** 存放按压点相对于子组件的左上角的纵向坐标。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Float32, Float32, Float32, Float32, Float32, Float32, RectResult, String)

```cangjie
public init(windowX: Float32, windowY: Float32, parentX: Float32, parentY: Float32, x: Float32, y: Float32, rect: RectResult, id: String)
```

**功能：** 构建一个TouchTestInfo类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|windowX|Float32|是|-|按压点相对于窗口左上角的x轴坐标。|
|windowY|Float32|是|-|按压点相对于窗口左上角的y轴坐标。|
|parentX|Float32|是|-|按压点相对于父组件左上角的x轴坐标。|
|parentY|Float32|是|-|按压点相对于父组件左上角的y轴坐标。|
|x|Float32|是|-|按压点相对于子组件左上角的x轴坐标。|
|y|Float32|是|-|按压点相对于子组件左上角的y轴坐标。|
|rect|[RectResult](./cj-common-types.md#class-rectresult)|是|-|子组件的大小。|
|id|String|是|-|通过id属性设置的组件id。|