### func font(Length, FontWeight, AppResource, FontStyle)

```cangjie
public func font(
    size!: Length = 10.vp,
    weight!: FontWeight = FontWeight.Normal,
    family!: AppResource,
    style!: FontStyle = FontStyle.Normal
): This
```

**功能：** 设置选中项文字样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|否|10.vp| **命名参数。** 选中项文字大小。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Normal| **命名参数。** 选中项文字字体粗细。|
|family|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 选中项文字字体家族。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 选中项文字样式。|

### func itemBorderRadius(Float64)

```cangjie
public func itemBorderRadius(value: Float64): This
```

**功能：** 设置索引项背板圆角半径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|设置索引项背板圆角半径。<br>不支持百分比，小于0时按照0设置。<br>索引条背板圆角自适应变化（索引项圆角半径+4.vp）。<br>初始值：8.vp。<br>单位：vp。|

### func itemSize(Length)

```cangjie
public func itemSize(size: Length): This
```

**功能：** 设置索引项区域大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|是|-|索引项区域大小，索引项区域为正方形，即正方形边长。<br>不支持设置为百分比。<br>初始值：16.vp。<br>单位：vp。|

### func popupBackground(ResourceColor)

```cangjie
public func popupBackground(value: ResourceColor): This
```

**功能：** 设置提示弹窗背景颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|提示弹窗背景颜色。<br>弹窗的背景模糊材质效果会对背景色产生影响，可通过设置[popupBackgroundBlurStyle](#func-popupbackgroundblurstyleblurstyle)属性值为NONE关闭背景模糊材质效果。<br>初始值：0x66808080。|

### func popupBackgroundBlurStyle(BlurStyle)

```cangjie
public func popupBackgroundBlurStyle(value: BlurStyle): This
```

**功能：** 设置提示弹窗的背景模糊材质。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)|是|-|设置提示弹窗的背景模糊材质。<br>弹窗的背景模糊材质效果会对背景色[popupBackground](#func-popupbackgroundresourcecolor)产生影响，可通过设置属性值为NONE关闭背景模糊材质效果。<br>初始值：COMPONENT_REGULAR。|

### func popupColor(ResourceColor)

```cangjie
public func popupColor(value: ResourceColor): This
```

**功能：** 设置提示弹窗一级索引项文本颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|提示弹窗一级索引项文本颜色。<br>初始值：0xFF007DFF。|