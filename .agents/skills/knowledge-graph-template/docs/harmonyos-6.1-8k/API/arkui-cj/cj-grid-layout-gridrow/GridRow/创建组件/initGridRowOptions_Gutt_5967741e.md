### init(?GridRowOptions, ?GutterOption, ?BreakPoints, ?GridRowDirection, () -> Unit)

```cangjie
public init(
    columns!: ?GridRowOptions = None,
    gutter!: ?GutterOption,
    breakpoints!: ?BreakPoints = Option.None,
    direction!: ?GridRowDirection = Option.None,
    child!: () -> Unit = {=>})
```

**功能：** 创建一个可包含子组件的GridRow容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|columns|?[GridRowOptions](#class-gridrowoptions)|否|None| **命名参数。** 布局列数设置。<br>初始值：GridRowOptions()。|
|gutter|?[GutterOption](#class-gutteroption)|是|-| **命名参数。** 栅格布局间距。|
|breakpoints|?[BreakPoints](#class-breakpoints)|否|Option.None| **命名参数。** 断点值的断点数列以及基于窗口或容器尺寸的相应参照。<br>初始值：BreakPoints()。|
|direction|?[GridRowDirection](#enum-gridrowdirection)|否|Option.None| **命名参数。** 栅格布局排列方向。<br>初始值：GridRowDirection.Row。|
|child|() -> Unit|否|{=>}| **命名参数。** GridRow容器的子组件。|