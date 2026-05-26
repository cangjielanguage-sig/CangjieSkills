### func canLoop(Bool)

```cangjie
public func canLoop(value: Bool): This
```

**功能：** 设置是否可循环滚动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否可循环滚动。<br>true：可循环，false：不可循环。<br>初始值：true。|

### func defaultPickerItemHeight(Length)

```cangjie
public func defaultPickerItemHeight(height: Length): This
```

**功能：** 设置Picker各选择项的高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|height|[Length](./cj-common-types.md#interface-length)|是|-|Picker各选择项的高度。|

### func defaultPickerItemHeight(Float64)

```cangjie
public func defaultPickerItemHeight(height: Float64): This
```

**功能：** 设置Picker各选择项的高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|height|Float64|是|-|Picker各选择项的高度。|

### func defaultPickerItemHeight(Int64)

```cangjie
public func defaultPickerItemHeight(height: Int64): This
```

**功能：** 设置Picker各选择项的高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|height|Int64|是|-|Picker各选择项的高度。|

### func divider(?DividerOptions)

```cangjie
public func divider(value!: ?DividerOptions = None): This
```

**功能：** 设置分割线样式，不设置该属性则按初始值展示分割线。

startMargin + endMargin 超过组件宽度后startMargin和endMargin会被置0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[DividerOptions](./cj-button-picker-select.md#class-divideroptions)|否|None| **命名参数。** 1.设置DividerOptions，则按设置的样式显示分割线。<br/>初始值：DividerOptions(strokeWidth: 2.px,color:0x33000000)<br/>2.设置为None时，不显示分割线。|

### func gradientHeight(Length)

```cangjie
public func gradientHeight(value: Length): This
```

**功能：** 设置渐隐效果高度，不设置该属性则显示默认渐隐效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|内容区上下边缘的渐隐高度（支持百分比，100.percent为TextPicker高度的一半即最大值），设置为0时不显示渐隐效果，负数等非法值显示默认渐隐效果。初始值为36.vp。|

### func selectedIndex(UInt32)

```cangjie
public func selectedIndex(value: UInt32): This
```

**功能：** 单列数据选择器设置默认选中项在数组中的索引值，优先级高于options中的选中值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|UInt32|是|-|默认选中项在数组中的索引值。<br>初始值：0。|

### func selectedIndex(Array\<UInt32>)

```cangjie
public func selectedIndex(value: Array<UInt32>): This
```

**功能：** 多列、多列联动数据选择器设置默认选中项在数组中的索引值，优先级高于options中的选中值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Array\<UInt32>|是|-|默认选中项在数组中的索引值。初始值：0。|