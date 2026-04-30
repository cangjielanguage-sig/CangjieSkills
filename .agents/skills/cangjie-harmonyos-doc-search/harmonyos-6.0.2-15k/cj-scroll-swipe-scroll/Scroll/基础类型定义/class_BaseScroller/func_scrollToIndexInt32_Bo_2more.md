#### func scrollToIndex(Int32, Bool, ScrollAlign)

```cangjie
public func scrollToIndex(
    index: Int32,
    smooth!: Bool = false,
    align!: ScrollAlign = ScrollAlign.START
    ): This
```

**功能：** 滑动到指定Index。开启smooth动效时，会对经过的所有item进行加载和布局计算，当大量加载item时会导致性能问题。

> **说明：**
>
> 仅支持List、Grid、WaterFlow组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|要滑动到的目标元素在当前容器中的索引值。<br/>**说明：** <br/>index值设置成负值或者大于当前容器子组件的最大索引值，视为异常值，本次跳转不生效。|
|smooth|Bool|否|false| **命名参数。** 设置滑动到列表项在列表中的索引值时是否有动效，true表示有动效，false表示没有动效。<br>初始值：false。|
|align|[ScrollAlign](#enum-scrollalign)|否|ScrollAlign.START| **命名参数。** 指定滑动到的元素与当前容器的对齐方式。<br/>**说明：** <br/>仅List组件支持该参数。|

#### func scrollToIndex(Int32, Bool, ScrollAlign, Length)

```cangjie
public func scrollToIndex(
    index: Int32,
    smooth!: Bool = false,
    align!: ScrollAlign = ScrollAlign.START,
    extraOffset!: Length
    ): This
```

**功能：** 滑动到指定Index，支持设置滑动额外偏移量。开启smooth动效时，会对经过的所有item进行加载和布局计算，当大量加载item时会导致性能问题。

> **说明：**
>
> 仅支持List、Grid、WaterFlow组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|要滑动到的目标元素在当前容器中的索引值。<br/>**说明：** <br/>index值设置成负值或者大于当前容器子组件的最大索引值，视为异常值，本次跳转不生效。|
|smooth|Bool|否|false| **命名参数。** 设置滑动到列表项在列表中的索引值时是否有动效，true表示有动效，false表示没有动效。<br>初始值：false。|
|align|[ScrollAlign](#enum-scrollalign)|否|ScrollAlign.START| **命名参数。** 指定滑动到的元素与当前容器的对齐方式。<br/>**说明：** <br/>仅List、Grid组件支持该参数。|
|extraOffset|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 设置滑动到指定Index的选项，如额外偏移量。|