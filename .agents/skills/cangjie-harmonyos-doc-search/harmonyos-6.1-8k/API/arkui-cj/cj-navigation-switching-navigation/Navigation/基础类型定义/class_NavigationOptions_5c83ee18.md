### class NavigationOptions

```cangjie
public class NavigationOptions {
    public var launchMode: ?LaunchMode
    public var animated: ?Bool
    public init(launchMode!: ?LaunchMode = None, animated!: ?Bool = None)
}
```

**功能：** 表示栈操作的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var animated

```cangjie
public var animated: ?Bool
```

**功能：** 是否支持过渡动画。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var launchMode

```cangjie
public var launchMode: ?LaunchMode
```

**功能：** 导航栈操作模式。

**类型：** ?[LaunchMode](#enum-launchmode)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?LaunchMode, ?Bool)

```cangjie
public init(launchMode!: ?LaunchMode = None, animated!: ?Bool = None)
```

**功能：** NavigationOptions的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|launchMode|?[LaunchMode](#enum-launchmode)|否|None|导航栈操作模式。初始值：LaunchMode.Standard。|
|animated|?Bool|否|None|是否支持过渡动画。初始值：true。|