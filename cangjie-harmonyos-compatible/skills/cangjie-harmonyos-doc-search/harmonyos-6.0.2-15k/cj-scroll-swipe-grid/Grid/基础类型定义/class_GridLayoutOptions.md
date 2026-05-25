### class GridLayoutOptions

```cangjie
public class GridLayoutOptions {
    public init (
        regularSize: (Int32, Int32),
        irregularIndexes!: Option<Array<Int32>> = Option.None,
        onGetIrregularSizeByIndex!: Option<(Int32) -> (Int32, Int32)> = Option.None,
        onGetRectByIndex!: Option<(Int32) -> (Int32, Int32, Int32, Int32)> = Option.None
    )
}
```

**功能：** Grid布局选项。其中，irregularIndexes和onGetIrregularSizeByIndex可对仅设置rowsTemplate或columnsTemplate的Grid使用，可以指定一个index数组，并为其中的index对应的GridItem设置其占据的行数与列数；onGetRectByIndex可对同时设置rowsTemplate和columnsTemplate的Grid使用，为指定的index对应的GridItem设置位置和大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init((Int32,Int32), Option\<Array\<Int32>>, Option\<(Int32) -> (Int32,Int32)>, Option\<(Int32) -> (Int32,Int32,Int32,Int32)>)

```cangjie
public init (
    regularSize: (Int32, Int32),
    irregularIndexes!: Option<Array<Int32>> = Option.None,
    onGetIrregularSizeByIndex!: Option<(Int32) -> (Int32, Int32)> = Option.None,
    onGetRectByIndex!: Option<(Int32) -> (Int32, Int32, Int32, Int32)> = Option.None
)
```

**功能：** 创建一个GridLayoutOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|regularSize|(Int32,Int32)|是|-|大小规则的GridItem在Grid中占的行数和列数，只支持占1行1列即(1, 1)。|
|irregularIndexes|Option\<Array\<Int32>>|否|Option.None| **命名参数。** 指定的GridItem索引在Grid中的大小是不规则的。当不设置onGetIrregularSizeByIndex时，irregularIndexes中GridItem的默认大小为垂直滚动Grid的一整行或水平滚动Grid的一整列。|
|onGetIrregularSizeByIndex|Option\<(Int32)->(Int32,Int32)>|否|Option.None| **命名参数。** 配合irregularIndexes使用，设置不规则GridItem占用的行数和列数。开发者可为irregularIndexes中指明的index对应的GridItem设置占用的行数和列数。|
|onGetRectByIndex|Option\<(Int32)->(Int32,Int32,Int32,Int32)>|否|Option.None| **命名参数。** 设置指定索引index对应的GridItem的位置及大小(rowStart,columnStart,rowSpan,columnSpan)。其中rowStart为行起始位置，columnStart为列起始位置，无单位。rowSpan为GridItem占用的行数，columnSpan为GridItem占用的列数，无单位。rowStart和columnStart取大于等于0的自然数，若取负数时，rowStart和columnStart默认为0。rowSpan和columnSpan取大于等于1的自然数。<br> **说明：** 第一种情况：某个GridItem发现给它指定的起始位置被占据了，则从起始位置(0,0)开始按顺序从左到右，从上到下寻找起始的放置位置。<br>第二种情况：如果起始位置没有被占据，但其他位置被占据了，无法显示全部的GridItem大小，则只会布局一部分。|