### class ButtonStyle

```cangjie
public class ButtonStyle {
    public var left: ?Float64
    public var top: ?Float64
    public var width: ?Float64
    public var height: ?Float64
    public var icons: ?ButtonIconOptions
    public init(
        left!: ?Float64 = None,
        top!: ?Float64 = None,
        width!: ?Float64 = None,
        height!: ?Float64 = None,
        icons!: ?ButtonIconOptions = None
    )
}
```

**功能：** 侧边栏控制按钮属性类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var left

```cangjie
public var left: ?Float64
```

**功能：** 设置侧边栏控制按钮距离容器左界限的间距。<br>单位：vp。

**类型：** ?Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var top

```cangjie
public var top: ?Float64
```

**功能：** 设置侧边栏控制按钮距离容器上界限的间距。<br>单位：vp。

**类型：** ?Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var width

```cangjie
public var width: ?Float64
```

**功能：** 设置侧边栏控制按钮的宽度。<br>单位：vp。

**类型：** ?Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var height

```cangjie
public var height: ?Float64
```

**功能：** 设置侧边栏控制按钮的高度。<br>单位：vp。

**类型：** ?Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var icons

```cangjie
public var icons: ?ButtonIconOptions
```

**功能：** 设置侧边栏控制按钮的图标。

**类型：** ?[ButtonIconOptions](#class-buttoniconoptions)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**读写能力：** 可读写

**起始版本：** 22

#### init(?Float64, ?Float64, ?Float64, ?Float64, ?ButtonIconOptions)

```cangjie
public init(
    left!: ?Float64 = None,
    top!: ?Float64 = None,
    width!: ?Float64 = None,
    height!: ?Float64 = None,
    icons!: ?ButtonIconOptions = None
)
```

**功能：** 构造ButtonStyle对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|left|?Float64|否|None|**命名参数。** 设置侧边栏控制按钮距离容器左界限的间距。<br>单位：vp。<br>初始值：16.0。|
|top|?Float64|否|None|**命名参数。** 设置侧边栏控制按钮距离容器上界限的间距。<br>单位：vp。<br>初始值：48.0。|
|width|?Float64|否|None|**命名参数。** 设置侧边栏控制按钮的宽度。<br>单位：vp。<br>初始值：24.0。|
|height|?Float64|否|None|**命名参数。** 设置侧边栏控制按钮的高度。<br>单位：vp。<br>初始值：24.0。|
|icons|?[ButtonIconOptions](#class-buttoniconoptions)|否|None|**命名参数。** 设置侧边栏控制按钮的图标。<br>初始值：ButtonIconOptions(shown: "", hidden: "")。|