### func itemConstraintSize(Length, Length, Length, Length)

```cangjie
public func itemConstraintSize(minWidth: Length, maxWidth: Length, minHeight: Length, maxHeight: Length): This
```

**功能：** 设置约束尺寸，子组件布局时，进行尺寸范围限制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|minWidth|[Length](cj-common-types.md#interface-length)|是|-|元素最小宽度。|
|maxWidth|[Length](cj-common-types.md#interface-length)|是|-|元素最大宽度。|
|minHeight|[Length](cj-common-types.md#interface-length)|是|-|元素最小高度。|
|maxHeight|[Length](cj-common-types.md#interface-length)|是|-|元素最大高度。|

### func layoutDirection(FlexDirection)

```cangjie
public func layoutDirection(value: FlexDirection): This
```

**功能：** 设置布局的主轴方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FlexDirection](cj-common-types.md#enum-flexdirection)|是|-|设置布局的主轴方向，<br/>初始值：FlexDirection.Column。|

ayoutDirection优先级高于rowsTemplate和columnsTemplate。根据layoutDirection设置情况，分为以下三种设置模式：

* layoutDirection设置纵向布局（FlexDirection.Column 或 FlexDirection.ColumnReverse）
    此时columnsTemplate有效（如果未设置，取初始值）。例如columnsTemplate设置为"1fr 1fr"、rowsTemplate设置为"1fr 1fr 1fr"时，瀑布流组件纵向布局，辅轴均分成横向2列。
* layoutDirection设置横向布局（FlexDirection.Row 或 FlexDirection.RowReverse）
    此时rowsTemplate有效（如果未设置，取初始值）。例如columnsTemplate设置为"1fr 1fr"、rowsTemplate设置为"1fr 1fr 1fr"时，瀑布流组件横向布局，辅轴均分成纵向3列。
* layoutDirection未设置布局方向
    布局方向为layoutDirection的初始值：FlexDirection.Column，此时columnsTemplate有效。例如columnsTemplate设置为"1fr 1fr"、rowsTemplate设置为"1fr 1fr 1fr"时，瀑布流组件纵向布局，辅轴均分成横向2列。

### func nestedScroll(NestedScrollMode, NestedScrollMode)

```cangjie
public func nestedScroll(
    scrollForward !: NestedScrollMode = NestedScrollMode.SELF_ONLY,
    scrollBackward !: NestedScrollMode = NestedScrollMode.SELF_ONLY
): This
```

**功能：** 设置向前和向后两个方向上的嵌套滚动模式，实现与父组件的滚动联动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scrollForward|[NestedScrollMode](cj-common-types.md#enum-nestedscrollmode)|否|NestedScrollMode.SELF_ONLY| **命名参数。** 滚动组件往末尾端滚动时的嵌套滚动选项。|
|scrollBackward|[NestedScrollMode](cj-common-types.md#enum-nestedscrollmode)|否|NestedScrollMode.SELF_ONLY| **命名参数。** 滚动组件往起始端滚动时的嵌套滚动选项。|

### func nestedScroll(NestedScrollOptions)

```cangjie
public func nestedScroll(value: NestedScrollOptions): This
```

**功能：** 设置向前和向后两个方向上的嵌套滚动模式，实现与父组件的滚动联动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[NestedScrollOptions](./cj-scroll-swipe-common.md#class-nestedscrolloptions)|是|-|嵌套滚动选项。|