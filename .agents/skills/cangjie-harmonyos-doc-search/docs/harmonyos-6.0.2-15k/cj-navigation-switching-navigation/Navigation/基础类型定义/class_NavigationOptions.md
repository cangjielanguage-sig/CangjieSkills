### class NavigationOptions

```cangjie
public class NavigationOptions {
    public var launchMode: LaunchMode = LaunchMode.Standard
    public var animated: Bool = true
    public init(launchMode!: LaunchMode = LaunchMode.Standard, animated!: Bool = true)
}
```

**功能：** 表示Navigation启动选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### var animated

```cangjie
public var animated: Bool = true
```

**功能：** 设置是否支持转场动画。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 20

#### var launchMode

```cangjie
public var launchMode: LaunchMode = LaunchMode.Standard
```

**功能：** 设置页面栈的操作模式。初始值：LaunchMode.Standard

**类型：** [LaunchMode](#enum-launchmode)

**读写能力：** 只读

**起始版本：** 20

#### init(LaunchMode, Bool)

```cangjie
public init(launchMode!: LaunchMode = LaunchMode.Standard, animated!: Bool = true)
```

**功能：** 创建NavigationOptions。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|launchMode|[LaunchMode](#enum-launchmode)|否|LaunchMode.Standard|页面栈的操作模式。|
|animated|Bool|否|true|是否支持转场动画。|