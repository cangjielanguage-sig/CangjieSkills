#### init(ScrollSnapAlign, Length, Bool, Bool)

```cangjie
public init(
    snapAlign: ScrollSnapAlign,
    snapPagination!: Length,
    enableSnapToStart!: Bool = true,
    enableSnapToEnd!: Bool = true
)
```

**功能：** 构造一个ScrollSnapOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|snapAlign|[ScrollSnapAlign](./cj-scroll-swipe-common.md#enum-scrollsnapalign)|是|-|设置Scroll组件限位滚动时的对齐方式。<br>初始值：ScrollSnapAlign.NONE。|
|snapPagination|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 设置Scroll组件限位滚动时的分页点。<br>**说明：**<br>1.Length表示每页的大小，系统按照该大小进行分页。<br>2.Length为小于等于0的输入时，按异常值，无限位滚动处理。<br>3.当输入为百分比时，实际的大小为Scroll组件的视口与百分比数值之积。|
|enableSnapToStart|Bool|否|true| **命名参数。** 在Scroll组件限位滚动模式下，该属性设置为false后，允许Scroll在开头和第一页间自由滑动。|
|enableSnapToEnd|Bool|否|true| **命名参数。** 在Scroll组件限位滚动模式下，该属性设置为false后，允许Scroll在最后一页和末尾间自由滑动。|