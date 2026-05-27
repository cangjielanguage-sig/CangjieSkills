#### init(UInt32, Length, Option\<(Float64) -> Int32>, Int32, Option\<Length>, Option\<Length>)

```cangjie
public init(
    itemsCount!: UInt32,
    margin!: Length = 0.vp,
    onGetItemMainSizeByIndex!: Option<(Float64)-> Int32> = None,
    crossCount!: Int32 = 1,
    columnsGap!: Option<Length> = None,
    rowsGap!: Option<Length> = None
)
```

**功能：** 构造一个SectionOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|itemsCount|UInt32|是|-| **命名参数。** 分组中FlowItem数量，必须是正整数。若splice、push、update方法收到的分组中有分组的itemsCount小于0，则不会执行该方法。|
|margin|[Length](cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 该分组的外边距参数为Length类型时，四个方向外边距同时生效。<br/>初始值：0。<br/>单位：vp。<br/>margin设置百分比时，上下左右外边距均以瀑布流的width作为基础值。|
|onGetItemMainSizeByIndex|Option\<(Float64)->Int32>|否|None| **命名参数。** 瀑布流组件布局过程中获取指定index的FlowItem的主轴大小，纵向瀑布流时为高度，横向瀑布流时为宽度，单位vp。<br/>**说明：**<br/>1. 同时使用onGetItemMainSizeByIndex和FlowItem的宽高属性时，主轴大小以onGetItemMainSizeByIndex返回结果为准，onGetItemMainSizeByIndex会覆盖FlowItem的主轴长度。<br/>2. 使用onGetItemMainSizeByIndex可以提高瀑布流跳转到指定位置或index时的效率，避免混用设置onGetItemMainSizeByIndex和未设置的分组，会导致布局异常。<br/>3.onGetItemMainSizeByIndex返回负数时FlowItem高度为0。|
|crossCount|Int32|否|1| **命名参数。** 纵向布局时为列数，横向布局时为行数。<br/>初始值：1。小于1的按初始值处理。|
|columnsGap|Option\<[Length](cj-common-types.md#interface-length)>|否|None| **命名参数。** 该分组的列间距，不设置时使用瀑布流的columnsGap，设置非法值时使用0.vp。|
|rowsGap|Option\<[Length](cj-common-types.md#interface-length)>|否|None| **命名参数。** 该分组的行间距，不设置时使用瀑布流的rowsGap，设置非法值时使用0vp。|