## class ComponentInfo

```cangjie
public class ComponentInfo {
    public ComponentInfo(
        public let size: Size,
        public let localOffset: Offset,
        public let windowOffset: Offset,
        public let screenOffset: Offset,
        public let translate: TranslateResult,
        public let scale: ScaleResult,
        public let rotate: RotateResult,
        public let transform: Array<Float32>
    )
}
```

**功能：** 组件实例对象的坐标位置和大小等信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let localOffset

```cangjie
public let localOffset: Offset
```

**功能：** 设置组件相对于父组件信息。

**类型：** [Offset](#class-offset)

**读写能力：** 只读

**起始版本：** 19

### let rotate

```cangjie
public let rotate: RotateResult
```

**功能：** 设置组件旋转信息。

**类型：** [RotateResult](#class-rotateresult)

**读写能力：** 只读

**起始版本：** 19

### let scale

```cangjie
public let scale: ScaleResult
```

**功能：** 设置组件缩放信息。

**类型：** [ScaleResult](#class-scaleresult)

**读写能力：** 只读

**起始版本：** 19

### let screenOffset

```cangjie
public let screenOffset: Offset
```

**功能：** 设置组件相对于屏幕信息。

**类型：** [Offset](#class-offset)

**读写能力：** 只读

**起始版本：** 19

### let size

```cangjie
public let size: Size
```

**功能：** 设置组件大小。

**类型：** [Size](./cj-apis-measure.md#struct-size)

**读写能力：** 只读

**起始版本：** 19

### let translate

```cangjie
public let translate: TranslateResult
```

**功能：** 设置组件平移信息。

**类型：** [TranslateResult](#class-translateresult)

**读写能力：** 只读

**起始版本：** 19

### let transform

```cangjie
public let transform: Array<Float32>
```

**功能：** 设置仿射矩阵信息，根据入参创建的四阶矩阵对象。

**类型：** Array\<Float32>

**读写能力：** 只读

**起始版本：** 19

### let windowOffset

```cangjie
public let windowOffset: Offset
```

**功能：** 设置组件相对于窗口信息。

**类型：** [Offset](#class-offset)

**读写能力：** 只读

**起始版本：** 19

### ComponentInfo(Size, Offset, Offset, Offset, TranslateResult, ScaleResult, RotateResult, Array\<Float32>)

```cangjie
public ComponentInfo(
    public let size: Size,
    public let localOffset: Offset,
    public let windowOffset: Offset,
    public let screenOffset: Offset,
    public let translate: TranslateResult,
    public let scale: ScaleResult,
    public let rotate: RotateResult,
    public let transform: Array<Float32>
)
```

**功能：** 构建一个ComponentInfo类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Size](./cj-apis-measure.md#struct-size)|是|-|组件大小。|
|localOffset|[Offset](#class-offset)|是|-|组件相对于父组件信息。|
|windowOffset|[Offset](#class-offset)|是|-|组件相对于窗口信息。|
|screenOffset|[Offset](#class-offset)|是|-|组件相对于屏幕信息。|
|translate|[TranslateResult](#class-translateresult)|是|-|组件平移信息。|
|scale|[ScaleResult](#class-scaleresult)|是|-|组件缩放信息。|
|rotate|[RotateResult](#class-rotateresult)|是|-|组件旋转信息。|
|transform|Array\<Float32>|是|-|仿射矩阵信息，根据入参创建的四阶矩阵对象。|