### SystemBarProperties(String, Bool, String, String, Bool, String, Bool, Bool)

```cangjie
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
```

**功能：** 构建一个SystemBarProperties类型的对象。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|statusBarColor|String|否|"#66000000"| **命名参数。** 状态栏背景颜色，为十六进制RGB或ARGB颜色，不区分大小写。|
|isStatusBarLightIcon|Bool|否|false| **命名参数。** 状态栏图标是否为高亮状态。true表示高亮；false表示不高亮。|
|statusBarContentColor|String|否|"#E5FFFFFF"| **命名参数。** 状态栏文字颜色。当设置此属性后， isStatusBarLightIcon属性设置无效。|
|navigationBarColor|String|否|"#66000000"| **命名参数。** 导航栏背景颜色，为十六进制RGB或ARGB颜色，不区分大小写。|
|isNavigationBarLightIcon|Bool|否|false| **命名参数。** 导航栏图标是否为高亮状态。true表示高亮；false表示不高亮。|
|navigationBarContentColor|String|否|"#E5FFFFFF"| **命名参数。** 导航栏文字颜色。当设置此属性后， isNavigationBarLightIcon属性设置无效。|
|enableStatusBarAnimation|Bool|否|false| **命名参数。** 是否使能状态栏属性变化时动画效果。true表示变化时使能动画效果；false表示没有使能动画效果。<br>**系统能力：** SystemCapability.Window.SessionManager|
|enableNavigationBarAnimation|Bool|否|false| **命名参数。** 是否使能导航栏属性变化时动画效果。true表示变化时使能动画效果；false表示没有使能动画效果。<br>**系统能力：** SystemCapability.Window.SessionManager|