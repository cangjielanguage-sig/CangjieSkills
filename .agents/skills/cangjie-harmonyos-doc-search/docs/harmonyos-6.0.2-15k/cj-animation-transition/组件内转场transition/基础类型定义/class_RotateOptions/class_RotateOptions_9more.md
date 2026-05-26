### class RotateOptions

```cangjie
public class RotateOptions {
    public var angle: Float32
    public var x: Float32
    public var y: Float32
    public var z: Float32
    public var centerX: Length
    public var centerY: Length
    public var centerZ: Length
    public var perspective: Float32
    public init(
        angle: Float32,
        x!: Float32 = 0.0,
        y!: Float32 = 0.0,
        z!: Float32 = 0.0,
        centerX!: Length = 50.percent,
        centerY!: Length = 50.percent,
        centerZ!: Length = 0,
        perspective!: Float32 = 0.0
    )
}
```

**功能：** 设置旋转参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var angle

```cangjie
public var angle: Float32
```

**功能：** 表示旋转角度。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var x

```cangjie
public var x: Float32
```

**功能：** 表示旋转轴向量x坐标。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var y

```cangjie
public var y: Float32
```

**功能：** 表示旋转轴向量y坐标。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var z

```cangjie
public var z: Float32
```

**功能：** 表示旋转轴向量z坐标。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var centerX

```cangjie
public var centerX: Length
```

**功能：** 表示组件变换中心点（即锚点）的x方向坐标。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var centerY

```cangjie
public var centerY: Length
```

**功能：** 表示组件变换中心点（即锚点）的y方向坐标。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var centerZ

```cangjie
public var centerZ: Length
```

**功能：** 表示z轴锚点，即3D旋转中心点的z轴分量。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var perspective

```cangjie
public var perspective: Float32
```

**功能：** 表示视距，即视点到z=0平面的距离。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12