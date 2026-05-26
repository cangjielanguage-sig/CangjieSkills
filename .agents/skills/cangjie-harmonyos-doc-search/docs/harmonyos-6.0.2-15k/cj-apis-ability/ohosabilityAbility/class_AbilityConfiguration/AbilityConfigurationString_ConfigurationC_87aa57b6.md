### AbilityConfiguration(String, ConfigurationColorMode, ConfigurationDirection, ConfigurationScreenDensity, Int32, Bool, Float64, Float64, String, String)

```cangjie
public AbilityConfiguration (
    public var language: String,
    public var colorMode: ConfigurationColorMode,
    public var direction: ConfigurationDirection,
    public var screenDensity: ConfigurationScreenDensity,
    public var displayId: Int32,
    public var hasPointerDevice: Bool,
    public var fontSizeScale: Float64,
    public var fontWeightScale: Float64,
    public var mcc: String,
    public var mnc: String
)
```

**功能：** AbilityConfiguration的主构造器。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|language|String|是|-|表示应用程序的当前语言，例如“zh"。|
|colorMode|[ConfigurationColorMode](#enum-configurationcolormode)|是|-|表示深浅色模式，默认为浅色。取值范围：<br />- COLOR_MODE_NOT_SET：未设置<br />- COLOR_MODE_LIGHT：浅色模式<br />- COLOR_MODE_DARK：深色模式|
|direction|[ConfigurationDirection](#enum-configurationdirection)|是|-|表示屏幕方向，取值范围：<br />- DIRECTION_NOT_SET：未设置<br />- DIRECTION_HORIZONTAL：水平方向<br />- DIRECTION_VERTICAL：垂直方向|
|screenDensity|[ConfigurationScreenDensity](#enum-configurationscreendensity)|是|-|表示屏幕像素密度，取值范围：<br />- SCREEN_DENSITY_NOT_SET：未设置<br />- SCREEN_DENSITY_SDPI：120<br />- SCREEN_DENSITY_MDPI：160<br />- SCREEN_DENSITY_LDPI：240<br />- SCREEN_DENSITY_XLDPI：320<br />- SCREEN_DENSITY_XXLDPI：480<br />- SCREEN_DENSITY_XXXLDPI：640|
|displayId|Int32|是|-|表示应用所在的物理屏幕ID。|
|hasPointerDevice|Bool|是|-|指示指针类型设备是否已连接，如键鼠、触控板等。|
|fontSizeScale|Float64|是|-|字体大小缩放比例，取值为非负数，默认值为1。|
|fontWeightScale|Float64|是|-|字体粗细缩放比例，取值为非负数，默认值为1。|
|mcc|String|是|-|移动设备网络代码。|
|mnc|String|是|-|移动设备国家代码。|