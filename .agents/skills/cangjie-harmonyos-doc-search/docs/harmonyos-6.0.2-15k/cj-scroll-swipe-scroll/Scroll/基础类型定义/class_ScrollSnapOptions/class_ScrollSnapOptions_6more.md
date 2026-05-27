### class ScrollSnapOptions

```cangjie
public class ScrollSnapOptions {
    public var snapAlign: ScrollSnapAlign
    public var snapPagination: Array<Length>
    public var enableSnapToStart: Bool = true
    public var enableSnapToEnd: Bool = true
    public init(
        snapAlign: ScrollSnapAlign,
        snapPagination!: Option<Array<Length>> = None,
        enableSnapToStart!: Bool = true,
        enableSnapToEnd!: Bool = true
    )
    public init(
        snapAlign: ScrollSnapAlign,
        snapPagination!: Length,
        enableSnapToStart!: Bool = true,
        enableSnapToEnd!: Bool = true
    )
}
```

**功能：** 限位滚动模式对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var enableSnapToEnd

```cangjie
public var enableSnapToEnd: Bool = true
```

**功能：** 在Scroll组件限位滚动模式下，该属性设置为false后，允许Scroll在最后一页和末尾间自由滑动。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var enableSnapToStart

```cangjie
public var enableSnapToStart: Bool = true
```

**功能：** 在Scroll组件限位滚动模式下，该属性设置为false后，允许Scroll在开头和第一页间自由滑动。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var snapAlign

```cangjie
public var snapAlign: ScrollSnapAlign
```

**功能：** 设置Scroll组件限位滚动时的对齐方式。

**类型：** [ScrollSnapAlign](./cj-scroll-swipe-common.md#enum-scrollsnapalign)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var snapPagination

```cangjie
public var snapPagination: Array<Length>
```

**功能：** 设置Scroll组件限位滚动时的分页点。

**类型：** Array\<[Length](./cj-common-types.md#interface-length)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(ScrollSnapAlign, Option\<Array\<Length>>, Bool, Bool)

```cangjie
public init(
    snapAlign: ScrollSnapAlign,
    snapPagination!: Option<Array<Length>> = None,
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
|snapPagination|Option\<Array\<[Length](./cj-common-types.md#interface-length)>>|否|None| **命名参数。** 设置Scroll组件限位滚动时的分页点。<br>**说明：**<br>1.Length数组中每个Length表示分页点，系统按照分页点进行分页。每个Length的范围为[0,可滑动距离]。<br>2.Length数组中的数值必须为单调递增。<br>3.当输入为百分比时，实际的大小为Scroll组件的视口与百分比数值之积。|
|enableSnapToStart|Bool|否|true| **命名参数。** 在Scroll组件限位滚动模式下，该属性设置为false后，允许Scroll在开头和第一页间自由滑动。|
|enableSnapToEnd|Bool|否|true| **命名参数。** 在Scroll组件限位滚动模式下，该属性设置为false后，允许Scroll在最后一页和末尾间自由滑动。|