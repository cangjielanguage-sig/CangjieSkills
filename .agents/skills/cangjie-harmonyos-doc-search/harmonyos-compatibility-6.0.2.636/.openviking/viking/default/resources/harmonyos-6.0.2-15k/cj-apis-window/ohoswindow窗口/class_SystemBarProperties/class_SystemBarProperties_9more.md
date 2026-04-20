## class SystemBarProperties

```cangjie
public class SystemBarProperties {
    public SystemBarProperties(
        public var statusBarColor!: String = "#66000000",
        public var isStatusBarLightIcon!: Bool = false,
        public var statusBarContentColor!: String = "#E5FFFFFF",
        public var navigationBarColor!: String = "#66000000",
        public var isNavigationBarLightIcon!: Bool = false,
        public var navigationBarContentColor!: String = "#E5FFFFFF",
        public var enableStatusBarAnimation!: Bool = false,
        public var enableNavigationBarAnimation!: Bool = false
    )
}
```

**功能：** 状态栏、导航栏的属性。在设置窗口级状态栏、导航栏属性时使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### var statusBarColor

```cangjie
public var statusBarColor: String = "#66000000"
```

**功能：** 设置状态栏背景颜色，为十六进制RGB或ARGB颜色。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var isStatusBarLightIcon

```cangjie
public var isStatusBarLightIcon: Bool = false
```

**功能：** 设置状态栏图标是否为高亮状态。true表示高亮；false表示不高亮。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var statusBarContentColor

```cangjie
public var statusBarContentColor: String = "#E5FFFFFF"
```

**功能：** 设置状态栏文字颜色。当设置此属性后， [isStatusBarLightIcon](#var-isstatusbarlighticon)属性设置无效。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var navigationBarColor

```cangjie
public var navigationBarColor: String = "#66000000"
```

**功能：** 设置导航栏背景颜色，为十六进制RGB或ARGB颜色，不区分大小写。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var isNavigationBarLightIcon

```cangjie
public var isNavigationBarLightIcon: Bool = false
```

**功能：** 设置导航栏图标是否为高亮状态。true表示高亮；false表示不高亮。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var navigationBarContentColor

```cangjie
public var navigationBarContentColor: String = "#E5FFFFFF"
```

**功能：** 设置导航栏文字颜色。当设置此属性后， [isNavigationBarLightIcon](#var-isnavigationbarlighticon)属性设置无效。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var enableStatusBarAnimation

```cangjie
public var enableStatusBarAnimation: Bool = false
```

**功能：** 设置是否使能状态栏属性变化时动画效果。true表示变化时使能动画效果；false表示没有使能动画效果。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var enableNavigationBarAnimation

```cangjie
public var enableNavigationBarAnimation: Bool = false
```

**功能：** 设置是否使能导航栏属性变化时动画效果。true表示变化时使能动画效果；false表示没有使能动画效果。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19