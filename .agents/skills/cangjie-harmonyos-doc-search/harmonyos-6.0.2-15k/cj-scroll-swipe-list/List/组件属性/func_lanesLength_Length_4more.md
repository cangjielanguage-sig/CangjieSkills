### func lanes(Length, Length)

```cangjie
public func lanes(minLength!: Length, maxLength!: Length): This
```

**功能：** 设置List组件的布局列数或行数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|minLength|[Length](cj-common-types.md#interface-length)|是|-| **命名参数。** 组件最小长度。|
|maxLength|[Length](cj-common-types.md#interface-length)|是|-| **命名参数。** 组件最大长度。|

### func lanes(Length, Length, Length)

```cangjie
public func lanes(minLength!: Length, maxLength!: Length, gutter!: Length): This
```

**功能：** 设置List组件的布局列数或行数。gutter为列间距，当列数大于1时生效。

规则如下：

* lanes为指定的数量时，根据指定的数量与List组件的交叉轴尺寸除以列数作为列的宽度。
* lanes设置了{minLength，maxLength}时，根据List组件的宽度自适应决定lanes数量（即列数），保证缩放过程中lane的宽度符合{minLength，maxLength}的限制。其中，minLength条件会被优先满足，即优先保证符合ListItem的交叉轴尺寸符合最小限制。
* lanes设置了{minLength，maxLength}，如果父组件交叉轴方向尺寸约束为无穷大时，固定按一列排列，列宽度按显示区域内最大的ListItem计算。
* ListItemGroup在多列模式下也是独占一行，ListItemGroup中的ListItem按照List组件的lanes属性设置值来布局。
* lanes设置了{minLength，maxLength}时，计算列数会按照ListItemGroup的交叉轴尺寸计算。当ListItemGroup交叉轴尺寸与List交叉轴尺寸不一致时ListItemGroup中的列数与List中的列数可能不一样。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|minLength|[Length](cj-common-types.md#interface-length)|是|-| **命名参数。** 组件最小长度。|
|maxLength|[Length](cj-common-types.md#interface-length)|是|-| **命名参数。** 组件最大长度。|
|gutter|[Length](cj-common-types.md#interface-length)|是|-| **命名参数。** 列间距。<br />初始值：0。<br />取值范围：[0, +∞)。|

### func listDirection(Axis)

```cangjie
public func listDirection(value: Axis): This
```

**功能：** 设置List组件排列方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Axis](cj-common-types.md#enum-axis)|是|-|组件的排列方向。<br/>初始值：Axis.Vertical。|

### func maintainVisibleContentPosition(Bool)

```cangjie
public func maintainVisibleContentPosition(enabled: Bool): This
```

**功能：** 设置显示区域上方插入或删除数据时是否要保持可见内容位置不变。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enabled|Bool|是|-|设置显示区域上方插入或删除数据时是否要保持可见内容位置不变。<br/>初始值：false，显示区域上方插入或删除数据时可见内容位置会跟随变化。 true：显示区域上方插入或删除数据时可见内容位置不变。|

> **说明：**
>
> * 只有使用LazyForEach在显示区域外插入或删除数据时，才能保持可见内容位置不变。使用ForEach插入或删除数据或使用LazyForEach重新加载数据时，即使maintainVisibleContentPosition属性设置为true，可见区内容位置也会跟随变化。
> * maintainVisibleContentPosition属性设置为true后，在显示区域上方插入或删除数据，会触发onDidScroll、onScrollIndex事件。
> * maintainVisibleContentPosition属性设置为true后，在多列场景下，一次插入或删除整行数据，可以保持可见内容位置不变，如果不是插入或删除整行数据，可见内容位置还是会发生变化。