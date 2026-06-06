## class StartOptions

```cangjie
public open class StartOptions {
    public var windowMode: WindowMode = WINDOW_MODE_UNDEFINED
    public var displayId: Int32 = 0
    public var withAnimation: Bool = true
    public var windowLeft: Int32 = 0
    public var windowTop: Int32 = 0
    public var windowWidth: Int32 = 0
    public var windowHeight: Int32 = 0
    public var processMode: ?ProcessMode = None
    public var startupVisibility: ?StartupVisibility = None

    public init(
        windowMode!: WindowMode = WINDOW_MODE_UNDEFINED,
        displayId!: Int32 = 0
    )
}
```

**功能：** 用于指定目标Ability的窗口模式。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### var windowMode

```cangjie
public var windowMode: WindowMode = WINDOW_MODE_UNDEFINED
```

**功能：** 启动Ability时的窗口模式，详见[WindowMode](#enum-windowmode)。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [WindowMode](#enum-windowmode)

**读写能力：** 可读写

**起始版本：** 12

### var displayId

```cangjie
public var displayId: Int32 = 0
```

**功能：** 屏幕ID模式。默认是0，表示当前屏幕。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

### var processMode

```cangjie
public var processMode: ?ProcessMode = None
```

**功能：** 进程模式。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ?[ProcessMode](#enum-processmode)

**读写能力：** 可读写

**起始版本：** 19

### var startupVisibility

```cangjie
public var startupVisibility: ?StartupVisibility = None
```

**功能：** Ability启动后的可见性。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ?[StartupVisibility](#enum-startupvisibility)

**读写能力：** 可读写

**起始版本：** 19

### var windowHeight

```cangjie
public var windowHeight: Int32 = 0
```

**功能：** 窗口的高度。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var windowLeft

```cangjie
public var windowLeft: Int32 = 0
```

**功能：** 窗口左边的位置。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var windowTop

```cangjie
public var windowTop: Int32 = 0
```

**功能：** 窗口顶部的位置。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var windowWidth

```cangjie
public var windowWidth: Int32 = 0
```

**功能：** 窗口的宽度。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### let withAnimation

```cangjie
public let withAnimation: Bool = true
```

**功能：** Ability是否具有动画效果。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19