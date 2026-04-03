### func popupItemFont(Length, FontWeight, AppResource, FontStyle)

```cangjie
public func popupItemFont(
    size!: Length = 24.vp,
    weight!: FontWeight = FontWeight.Medium,
    family!: AppResource,
    style!: FontStyle = FontStyle.Normal
): This
```

**功能：** 设置提示弹窗二级索引项文本样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|否|24.vp| **命名参数。** 设置提示弹窗二级索引项字体大小。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Medium| **命名参数。** 设置提示弹窗二级索引项字体粗细。|
|family|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 设置提示弹窗二级索引项字体家族。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 设置提示弹窗二级索引项字体样式。|

### func popupPosition(Length, Length)

```cangjie
public func popupPosition(x!: Length = 60.vp, y!: Length = 48.vp): This
```

**功能：** 设置弹出窗口相对于索引器条上边框中点的位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|[Length](./cj-common-types.md#interface-length)|否|60.vp| **命名参数。** 弹出窗口相对于索引器条上边框中点的位置。|
|y|[Length](./cj-common-types.md#interface-length)|否|48.vp| **命名参数。** 弹出窗口相对于索引器条上边框中点的位置。|

### func popupSelectedColor(ResourceColor)

```cangjie
public func popupSelectedColor(value: ResourceColor): This
```

**功能：** 设置提示弹窗二级索引选中项文本颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|提示弹窗二级索引选中项文本颜色。<br>初始值：0xFF182431。|

### func popupTitleBackground(ResourceColor)

```cangjie
public func popupTitleBackground(value: ResourceColor): This
```

**功能：** 设置提示弹窗一级索引项背景颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|提示弹窗一级索引项背景颜色。<br>提示弹窗只有一个索引项初始值：0xFFFFFFFF。<br>提示弹窗有多个索引项初始值：0x0c182431。|

### func popupUnselectedColor(ResourceColor)

```cangjie
public func popupUnselectedColor(value: ResourceColor): This
```

**功能：** 设置提示弹窗二级索引未选中项文本颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|提示弹窗二级索引未选中项文本颜色。<br>初始值：0xFF182431。|

### func selected(UInt32)

```cangjie
public func selected(idx: UInt32): This
```

**功能：** 设置选中项索引值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|idx|UInt32|是|-|选中项索引值。<br>初始值：0。|