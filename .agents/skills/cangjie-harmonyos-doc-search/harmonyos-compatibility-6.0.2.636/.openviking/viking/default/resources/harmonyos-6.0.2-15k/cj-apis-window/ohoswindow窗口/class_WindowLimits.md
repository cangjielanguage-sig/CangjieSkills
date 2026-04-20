## class WindowLimits

```cangjie
public class WindowLimits {
    public WindowLimits(
        public var maxWidth!: UInt32 = UInt32.Max,
        public var maxHeight!: UInt32 = UInt32.Max,
        public var minWidth!: UInt32= 1,
        public var minHeight!: UInt32 = 1
    )
}
```

**功能：** 窗口尺寸限制参数。可以通过[setWindowLimits](#func-setwindowlimitswindowlimits)设置窗口尺寸限制，并且可以通过[getWindowLimits](#func-getwindowlimits)获得当前的窗口尺寸限制。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### var maxWidth

```cangjie
public var maxWidth: UInt32 = UInt32.Max
```

**功能：** 设置窗口的最大宽度。单位为px。值默认为UInt32.Max，表示系统限定的最大宽度。下限值为0，上限值为系统限定的最大宽度。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### var maxHeight

```cangjie
public var maxHeight: UInt32 = UInt32.Max
```

**功能：** 设置窗口的最大高度。单位为px。值默认为UInt32.Max，表示系统限定的最大宽度。下限值为0，上限值为系统限定的最大高度。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### var minWidth

```cangjie
public var minWidth: UInt32 = 1
```

**功能：** 设置设置窗口的最小宽度。单位为px。值默认为1。下限值为0，上限值为系统限定的最小宽度。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### var minHeight

```cangjie
public var minHeight: UInt32 = 1
```

**功能：** 设置窗口的最小高度。单位为px。值默认为1。下限值为0，上限值为系统限定的最小高度。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### WindowLimits(UInt32, UInt32, UInt32, UInt32)

```cangjie
public WindowLimits(
    public var maxWidth!: UInt32 = UInt32.Max,
    public var maxHeight!: UInt32 = UInt32.Max,
    public var minWidth!: UInt32= 1,
    public var minHeight!: UInt32 = 1
)
```

**功能：** 构建一个WindowLimits的类型的对象。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|maxWidth|UInt32|否|UInt32.Max| **命名参数。** 窗口的最大宽度。单位为px。下限值为0，上限值为系统限定的最大宽度。|
|maxHeight|UInt32|否|UInt32.Max| **命名参数。** 窗口的最大高度。单位为px。下限值为0，上限值为系统限定的最大高度。|
|minWidth|UInt32|否|1| **命名参数。** 窗口的最小宽度。单位为px。下限值为0，上限值为系统限定的最小宽度。|
|minHeight|UInt32|否|1| **命名参数。** 窗口的最小高度。单位为px。下限值为0，上限值为系统限定的最小高度。|