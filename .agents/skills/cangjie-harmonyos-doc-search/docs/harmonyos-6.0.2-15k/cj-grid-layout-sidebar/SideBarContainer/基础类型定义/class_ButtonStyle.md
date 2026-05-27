### class ButtonStyle

```cangjie
public class ButtonStyle {
    public init(
        left!: Int64 = 16,
        top!: Int64 = 48,
        width!: Int64 = 32,
        height!: Int64 = 32,
        icons!: Icons = Icons(shown: "", hidden: ""))
}
```

**功能：** 侧边栏控制按钮属性类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Int64, Int64, Int64, Int64, Icons)

```cangjie
public init(
    left!: Int64 = 16,
    top!: Int64 = 48,
    width!: Int64 = 32,
    height!: Int64 = 32,
    icons!: Icons = Icons(shown: "", hidden: ""))
```

**功能：** 构造ButtonStyle对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|left|Int64|否|16| **命名参数。** 设置侧边栏控制按钮距离容器左界限的间距。<br>单位：vp。|
|top|Int64|否|48| **命名参数。** 设置侧边栏控制按钮距离容器上界限的间距。<br>单位：vp。|
|width|Int64|否|32| **命名参数。** 设置侧边栏控制按钮的宽度。<br>单位：vp。|
|height|Int64|否|32| **命名参数。** 设置侧边栏控制按钮的高度。<br>单位：vp。|
|icons|[Icons](#class-icons)|否|Icons(shown: "", hidden: "")| **命名参数。** 设置侧边栏控制按钮的图标。|