### func barBackgroundColor(ResourceColor)

```cangjie
public func barBackgroundColor(color: ResourceColor): This
```

**功能：** 设置TabBar的背景颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|TabBar的背景颜色。<br> 初始值：初始值为Color.TRANSPARENT，透明|

### func barBackgroundEffect(BackgroundEffectOptions)

```cangjie
public func barBackgroundEffect(options: BackgroundEffectOptions): This
```

**功能：** 设置TabBar背景属性，包含背景模糊半径，亮度，饱和度，颜色等参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[BackgroundEffectOptions](cj-universal-attribute-background.md#class-backgroundeffectoptions)|是|-|设置TabBar背景属性包括：模糊半径，亮度，饱和度，颜色等。|

### func barGridAlign(BarGridColumnOptions)

```cangjie
public func barGridAlign(options: BarGridColumnOptions): This
```

**功能：** 以栅格化方式设置TabBar的可见区域。具体参见BarGridColumnOptions对象。仅水平模式下有效，不适用于[XS、XL和XXL设备](../../../Dev_Guide/arkui-cj/cj-layout-development-grid-layout.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[BarGridColumnOptions](#class-bargridcolumnoptions)|是|-|以栅格化方式设置TabBar的可见区域。|

### func barHeight(Length)

```cangjie
public func barHeight(height: Length): This
```

**功能：** 设置TabBar的高度值。设置为小于0或大于Tabs高度值时，按初始值显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|height|[Length](cj-common-types.md#interface-length)|是|-|TabBar 的高度值。<br> 初始值：<br> 未设置带样式的TabBar且vertical属性为false时，初始值为56.vp。<br>未设置带样式的TabBar且vertical属性为true时，初始值为Tabs的高度。<br> 设置[SubTabBarStyle](cj-navigation-switching-tabcontent.md#class-subtabbarstyle)样式且vertical属性为false时，初始值为56.vp。<br> 设置SubTabBarStyle样式且vertical属性为true时，初始值为Tabs的高度。<br> 设置[BottomTabBarStyle](cj-navigation-switching-tabcontent.md#class-bottomtabbarstyle)样式且vertical属性为true时，初始值为Tabs的高度。<br> 设置BottomTabBarStyle样式且vertical属性为false时，初始值为48.vp。|

### func barMode(BarMode)

```cangjie
public func barMode(mode: BarMode): This
```

**功能：** 设置TabBar布局模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[BarMode](#enum-barmode)|是|-|布局模式。|

### func barMode(BarMode, ScrollableBarModeOptions)

```cangjie
public func barMode(mode: BarMode, options: ScrollableBarModeOptions): This
```

**功能：** 设置TabBar布局模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[BarMode](#enum-barmode)|是|-|布局模式。<br> 初始值：BarMode.Fixed|
|options|[ScrollableBarModeOptions](#class-scrollablebarmodeoptions)|是|-|Scrollable模式下的TabBar的布局样式。<br> **说明：** <br>仅Scrollable且水平模式下有效。|