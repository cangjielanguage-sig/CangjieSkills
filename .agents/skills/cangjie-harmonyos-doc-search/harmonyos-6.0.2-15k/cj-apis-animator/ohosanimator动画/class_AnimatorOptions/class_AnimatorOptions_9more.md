## class AnimatorOptions

```cangjie
public class AnimatorOptions {
    public AnimatorOptions(
        public let duration!: Int32 = 0,
        public let easing!: String = "ease",
        public let delay!: Int32 = 0,
        public let fill!: AnimatorFill = None,
        public let direction!: AnimatorDirection = Normal,
        public let iterations!: Int32 = 0,
        public let begin!: Float64 = 0.0,
        public let end!: Float64 = 1.0
    )
}
```

**功能：** 动画选项类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let begin

```cangjie
public let begin: Float64
```

**功能：** 设置动画插值起点。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

### let delay

```cangjie
public let delay: Int32
```

**功能：** 设置动画延时播放时长。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let direction

```cangjie
public let direction: AnimatorDirection
```

**功能：** 设置动画播放模式。

**类型：** [AnimatorDirection](#enum-animatordirection)

**读写能力：** 只读

**起始版本：** 12

### let duration

```cangjie
public let duration: Int32
```

**功能：** 设置动画播放的时长。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let easing

```cangjie
public let easing: String
```

**功能：** 设置动画插值曲线。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let end

```cangjie
public let end: Float64
```

**功能：** 设置动画插值终点。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

### let fill

```cangjie
public let fill: AnimatorFill
```

**功能：** 设置动画执行后是否恢复到初始状态。

**类型：** [AnimatorFill](#enum-animatorfill)

**读写能力：** 只读

**起始版本：** 12

### let iterations

```cangjie
public let iterations: Int32
```

**功能：** 设置动画播放次数。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12