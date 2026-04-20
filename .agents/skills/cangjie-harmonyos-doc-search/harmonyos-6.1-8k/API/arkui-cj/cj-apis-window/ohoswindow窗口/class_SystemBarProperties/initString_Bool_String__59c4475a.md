### init(String, Bool, String, String, Bool, String, Bool, Bool)

```cangjie
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
```

**功能：** SystemBarProperties构造函数。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|statusBarColor|String|否|"#66000000"| **命名参数。** 状态栏颜色。|
|isStatusBarLightIcon|Bool|否|false| **命名参数。** 状态栏浅色图标。|
|statusBarContentColor|String|否|"#E5FFFFFF"| **命名参数。** 状态栏内容颜色。|
|navigationBarColor|String|否|"#66000000"| **命名参数。** 导航栏颜色。|
|isNavigationBarLightIcon|Bool|否|false| **命名参数。** 导航栏浅色图标。|
|navigationBarContentColor|String|否|"#E5FFFFFF"| **命名参数。** 导航栏内容颜色。|
|enableStatusBarAnimation|Bool|否|false| **命名参数。** 启用状态栏动画。|
|enableNavigationBarAnimation|Bool|否|false| **命名参数。** 启用导航栏动画。|