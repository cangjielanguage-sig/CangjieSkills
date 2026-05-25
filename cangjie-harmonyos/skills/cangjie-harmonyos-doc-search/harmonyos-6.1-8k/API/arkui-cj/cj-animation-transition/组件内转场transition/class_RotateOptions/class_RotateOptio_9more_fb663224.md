## class RotateOptions

```cangjie
public class RotateOptions {
    public var x: ?Float32
    public var y: ?Float32
    public var z: ?Float32
    public var centerX: ?Length
    public var centerY: ?Length
    public var centerZ: ?Length
    public var perspective: ?Float32
    public var angle: ?Float32
    public init(angle: ?Float32, x!: ?Float32 = None, y!: ?Float32 = None, z!: ?Float32 = None, centerX!: ?Length = None,
        centerY!: ?Length = None, centerZ!: ?Length = None, perspective!: ?Float32 = None)
}
```

**功能：** 旋转参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var angle

```cangjie
public var angle: ?Float32
```

**功能：** 旋转角度。取值为正时相对于旋转轴方向顺时针转动，取值为负时相对于旋转轴方向逆时针转动。

**类型：** ?Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var x

```cangjie
public var x: ?Float32
```

**功能：** 旋转轴向量的X坐标。

**类型：** ?Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var y

```cangjie
public var y: ?Float32
```

**功能：** 旋转轴向量的Y坐标。

**类型：** ?Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var z

```cangjie
public var z: ?Float32
```

**功能：** 旋转轴向量的Z坐标。

**类型：** ?Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var centerX

```cangjie
public var centerX: ?Length
```

**功能：** 变换中心点x轴坐标。表示组件变换中心点（即锚点）的x方向坐标。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var centerY

```cangjie
public var centerY: ?Length
```

**功能：** 变换中心点y轴坐标。表示组件变换中心点（即锚点）的y方向坐标。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var centerZ

```cangjie
public var centerZ: ?Length
```

**功能：** Z轴锚点，即3D旋转中心点的z分量。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var perspective

```cangjie
public var perspective: ?Float32
```

**功能：** 相机放置的z轴坐标。数值大小表示视距，即相机到z=0平面的距离。取值的正负决定了相机观察的方向。当perspective=0，系统会自动计算适合的相机z轴位置，取值为负数。旋转轴和旋转中心点都基于坐标系设定，组件发生位移时，坐标系不会随之移动。

**类型：** ?Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22