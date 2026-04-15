## class ComponentInfo

```cangjie
public class ComponentInfo {
    public var size: Size
    public var localOffset: Offset
    public var windowOffset: Offset
    public var screenOffset: Offset
    public var translate: TranslateResult
    public var scale: ScaleResult
    public var rotate: RotateResult
    public var transform: Matrix4Result
    public init(size: Size, localOffset: Offset, windowOffset: Offset, screenOffset: Offset, translate: TranslateResult,
    scale: ScaleResult, rotate: RotateResult, transform: Matrix4Result)
}
```

**功能：** 组件实例对象的坐标位置和大小等信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var localOffset

```cangjie
public var localOffset: Offset
```

**功能：** 设置组件相对于父组件信息。

**类型：** [Offset](#class-offset)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var rotate

```cangjie
public var rotate: RotateResult
```

**功能：** 设置组件旋转信息。

**类型：** [RotateResult](#class-rotateresult)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var scale

```cangjie
public var scale: ScaleResult
```

**功能：** 设置组件缩放信息。

**类型：** [ScaleResult](#class-scaleresult)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var screenOffset

```cangjie
public var screenOffset: Offset
```

**功能：** 设置组件相对于屏幕信息。

**类型：** [Offset](#class-offset)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var size

```cangjie
public var size: Size
```

**功能：** 设置组件大小信息。

**类型：** [Size](#class-size)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var transform

```cangjie
public var transform: Matrix4Result
```

**功能：** 设置组件变换矩阵信息。

**类型：** [Matrix4Result](#type-matrix4result)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var translate

```cangjie
public var translate: TranslateResult
```

**功能：** 设置组件平移信息。

**类型：** [TranslateResult](#class-translateresult)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var windowOffset

```cangjie
public var windowOffset: Offset
```

**功能：** 设置组件相对于窗口信息。

**类型：** [Offset](#class-offset)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(Size, Offset, Offset, Offset, TranslateResult, ScaleResult, RotateResult, Matrix4Result)

```cangjie
public init(size: Size, localOffset: Offset, windowOffset: Offset, screenOffset: Offset, translate: TranslateResult,
    scale: ScaleResult, rotate: RotateResult, transform: Matrix4Result)
```

**功能：** 构建一个ComponentInfo类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Size](#class-size)|是|-|组件大小信息。|
|localOffset|[Offset](#class-offset)|是|-|组件相对于父组件信息。|
|windowOffset|[Offset](#class-offset)|是|-|组件相对于窗口信息。|
|screenOffset|[Offset](#class-offset)|是|-|组件相对于屏幕信息。|
|translate|[TranslateResult](#class-translateresult)|是|-|组件平移信息。|
|scale|[ScaleResult](#class-scaleresult)|是|-|组件缩放信息。|
|rotate|[RotateResult](#class-rotateresult)|是|-|组件旋转信息。|
|transform|[Matrix4Result](#type-matrix4result)|是|-|组件变换矩阵信息。|