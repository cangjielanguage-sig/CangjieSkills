## class SystemBarProperties

```cangjie
public class SystemBarProperties {
    public var statusBarColor: String = "#66000000"
    public var isStatusBarLightIcon: Bool = false
    public var statusBarContentColor: String = "#E5FFFFFF"
    public var navigationBarColor: String = "#66000000"
    public var isNavigationBarLightIcon: Bool = false
    public var navigationBarContentColor: String = "#E5FFFFFF"
    public var enableStatusBarAnimation: Bool = false
    public var enableNavigationBarAnimation: Bool = false
    public init(
        statusBarColor!: String = "#66000000",
        isStatusBarLightIcon!: Bool = false,
        statusBarContentColor!: String = "#E5FFFFFF",
        navigationBarColor!: String = "#66000000",
        isNavigationBarLightIcon!: Bool = false,
        navigationBarContentColor!: String = "#E5FFFFFF",
        enableStatusBarAnimation!: Bool = false,
        enableNavigationBarAnimation!: Bool = false
    )
}
```

**功能：** 状态栏和导航栏的属性，不会自动更新。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### var enableNavigationBarAnimation

```cangjie
public var enableNavigationBarAnimation: Bool = false
```

**功能：** 启用导航栏动画。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### var enableStatusBarAnimation

```cangjie
public var enableStatusBarAnimation: Bool = false
```

**功能：** 启用状态栏动画。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### var isNavigationBarLightIcon

```cangjie
public var isNavigationBarLightIcon: Bool = false
```

**功能：** 导航栏浅色图标。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### var isStatusBarLightIcon

```cangjie
public var isStatusBarLightIcon: Bool = false
```

**功能：** 状态栏浅色图标。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### var navigationBarColor

```cangjie
public var navigationBarColor: String = "#66000000"
```

**功能：** 导航栏颜色。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### var navigationBarContentColor

```cangjie
public var navigationBarContentColor: String = "#E5FFFFFF"
```

**功能：** 导航栏内容颜色。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### var statusBarColor

```cangjie
public var statusBarColor: String = "#66000000"
```

**功能：** 状态栏颜色。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### var statusBarContentColor

```cangjie
public var statusBarContentColor: String = "#E5FFFFFF"
```

**功能：** 状态栏内容颜色。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22