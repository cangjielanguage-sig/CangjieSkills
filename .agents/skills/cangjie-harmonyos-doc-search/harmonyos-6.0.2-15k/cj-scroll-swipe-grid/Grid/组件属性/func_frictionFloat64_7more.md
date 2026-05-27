### func friction(Float64)

```cangjie
public func friction(value: Float64): This
```

**功能：** 设置摩擦系数，手动划动滚动区域时生效，仅影响惯性滚动过程，对惯性滚动过程中的链式效果有间接影响。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|摩擦系数。<br>初始值：非可穿戴设备为0.75，可穿戴设备为0.9。<br> 取值范围：(0, +∞)，设置为小于等于0的值时，按初始值处理。|

### func friction(Int32)

```cangjie
public func friction(value: Int32): This
```

**功能：** 设置摩擦系数，手动划动滚动区域时生效，仅影响惯性滚动过程，对惯性滚动过程中的链式效果有间接影响。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|摩擦系数。<br>初始值：未调用该属性方法时，初始值参考[friction](#func-frictionfloat64)。<br> 取值范围：(0, +∞)，设置为小于等于0的值时，按初始值处理。|

### func layoutDirection(GridDirection)

```cangjie
public func layoutDirection(value: GridDirection): This
```

**功能：** 设置布局的主轴方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[GridDirection](#enum-griddirection)|是|-|布局的主轴方向。<br/>初始值：GridDirection.Row|

### func maxCount(Int32)

```cangjie
public func maxCount(value: Int32): This
```

**功能：** 设置可显示的最大行数或列数。设置为小于1的值时，按初始值显示。

当layoutDirection是Row/RowReverse时，表示可显示的最大列数。

当layoutDirection是Column/ColumnReverse时，表示可显示的最大行数。

当maxCount小于minCount时，maxCount和minCount都按初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|可显示的最大行数或列数。|

### func minCount(Int32)

```cangjie
public func minCount(value: Int32): This
```

**功能：** 设置可显示的最小行数或列数。设置为小于1的值时，按初始值显示。

当layoutDirection是Row/RowReverse时，表示可显示的最小列数。

当layoutDirection是Column/ColumnReverse时，表示可显示的最小行数。

当minCount大于maxCount时，minCount和maxCount都按初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|可显示的最小行数或列数。<br/>初始值：1|

### func multiSelectable(Bool)

```cangjie
public func multiSelectable(isSelectable: Bool): This
```

**功能：** 设置是否开启鼠标框选。开启框选后，可以配合Griditem的`selected`属性和`onSelect`事件获取GridItem的选中状态，还可以设置 <!-- [--> 选中态样式<!--]()-->（无默认选中样式）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isSelectable|Bool|是|-|是否开启鼠标框选。<br>初始值：false<br>false：关闭框选。true：开启框选。|

### func nestedScroll(NestedScrollOptions)

```cangjie
public func nestedScroll(value: NestedScrollOptions): This
```

**功能：** 设置嵌套滚动选项。设置向前和向后两个方向上的嵌套滚动模式，实现与父组件的滚动联动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[NestedScrollOptions](cj-scroll-swipe-common.md#class-nestedscrolloptions)|是|-|嵌套滚动选项。|