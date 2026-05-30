#### init(String, Fonts, Length, ResourceColor, ResourceColor, Bool, Bool, Bool)

```cangjie
public init(content!: String = "HarmonyOS Sans", font!: Fonts = Fonts(), borderWidth!: Length = 1.vp,
    borderColor!: ResourceColor = Color(0x33007dff), fontColor!: ResourceColor = Color(0xff182431), showDefaultPercentage!: Bool = false,
    enableSmoothEffect!: Bool = true, enableScanEffect!: Bool = false)
```

**功能：** 构造一个CapsuleStyleOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|String|否|"HarmonyOS Sans"| **命名参数。** 文本内容，应用可自定义。|
|font|[Fonts](./cj-common-types.md#class-fonts)|否|Fonts()| **命名参数。** 文本样式。<br/>初始值：<br/>- 文本大小（不支持百分比设置）：12.fp<br/>其他文本参数跟随text组件的主题值。|
|borderWidth|[Length](./cj-common-types.md#interface-length)|否|1.vp| **命名参数。** 内描边宽度（不支持百分比设置）。|
|borderColor|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color(0x33007dff)| **命名参数。** 内描边颜色。|
|fontColor|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color(0xff182431)| **命名参数。** 文本颜色。|
|showDefaultPercentage|Bool|否|false| **命名参数。** 显示百分比文本的开关，开启后会在进度条上显示当前进度的百分比。设置了content属性时该属性不生效。|
|enableSmoothEffect|Bool|否|true| **命名参数。** 进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值。|
|enableScanEffect|Bool|否|false| **命名参数。** 扫光效果的开关。|