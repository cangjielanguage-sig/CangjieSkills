### class SectionOptions

```cangjie
public class SectionOptions {
    public var itemsCount: UInt32
    public var crossCount: Int32
    public var columnsGap: Option<Length>
    public var rowsGap: Option<Length>
    public var margin: Margin
    public var onGetItemMainSizeByIndex: Option <(Float64) -> Int32>
    public init(
        itemsCount!: UInt32,
        margin!: Margin,
        onGetItemMainSizeByIndex!: Option<(Float64)-> Int32> = None,
        crossCount!: Int32 = 1,
        columnsGap!: Option<Length> = None,
        rowsGap!: Option<Length> = None
    )
    public init(
        itemsCount!: UInt32,
        margin!: Length = 0.vp,
        onGetItemMainSizeByIndex!: Option<(Float64)-> Int32> = None,
        crossCount!: Int32 = 1,
        columnsGap!: Option<Length> = None,
        rowsGap!: Option<Length> = None
    )
}
```

**功能：** FlowItem分组配置信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var columnsGap

```cangjie
public var columnsGap: Option<Length>
```

**功能：** 该分组的列间距。

**类型：** Option\<[Length](cj-common-types.md#interface-length)>

**读写能力：** 可读写

**起始版本：** 19

#### var crossCount

```cangjie
public var crossCount: Int32
```

**功能：** 纵向布局时为列数，横向布局时为行数。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

#### var itemsCount

```cangjie
public var itemsCount: UInt32
```

**功能：** 分组中FlowItem数量。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

#### var margin

```cangjie
public var margin: Margin
```

**功能：** 该分组的外边距参数。

**类型：** [Margin](./cj-common-types.md#class-margin)

**读写能力：** 可读写

**起始版本：** 19

#### var onGetItemMainSizeByIndex

```cangjie
public var onGetItemMainSizeByIndex: Option <(Float64) -> Int32>
```

**功能：** 瀑布流组件布局过程中获取指定index的FlowItem的主轴大小，纵向瀑布流时为高度，横向瀑布流时为宽度，单位vp。

**类型：** Option\<(Float64)->Int32>

**读写能力：** 可读写

**起始版本：** 19

#### var rowsGap

```cangjie
public var rowsGap: Option<Length>
```

**功能：** 该分组的行间距。

**类型：** Option\<[Length](cj-common-types.md#interface-length)>

**读写能力：** 可读写

**起始版本：** 19