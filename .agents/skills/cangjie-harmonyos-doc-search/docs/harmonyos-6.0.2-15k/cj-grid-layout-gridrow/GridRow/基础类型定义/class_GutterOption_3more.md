### class GutterOption

```cangjie
public class GutterOption {
    public init(x!: Length, y!: Length)
    public init(x!: GridRowSizeOption, y!: GridRowSizeOption)
}
```

**功能：** 栅格布局间距类型，用于描述栅格子组件不同方向的间距。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(Length, Length)

```cangjie
public init(x!: Length, y!: Length)
```

**功能：** 构造一个GutterOption类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 栅格子组件x方向的间距|
|y|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 栅格子组件y方向的间距|

#### init(GridRowSizeOption, GridRowSizeOption)

```cangjie
public init(x!: GridRowSizeOption, y!: GridRowSizeOption)
```

**功能：** 构造一个GutterOption类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|[GridRowSizeOption](#class-gridrowsizeoption)|是|-| **命名参数。** 栅格子组件x方向的间距|
|y|[GridRowSizeOption](#class-gridrowsizeoption)|是|-| **命名参数。** 栅格子组件y方向的间距|

### enum BreakpointsReference

```cangjie
public enum BreakpointsReference {
    | WindowSize
    | ComponentSize
}
```

**功能：** 设置以窗口为参照或以容器为参照。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### ComponentSize

```cangjie
ComponentSize
```

**功能：** 以容器为参照。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### WindowSize

```cangjie
WindowSize
```

**功能：** 以窗口为参照。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### enum GridRowDirection

```cangjie
public enum GridRowDirection {
    | GridRowRow
    | RowReverse
}
```

**功能：** 栅格元素按照行或列方向排列。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

> **说明：**
>
> - 栅格元素仅支持GridRowRow/RowReverse排列，不支持column/ColumnReverse方向排列。
> - 栅格子组件仅能通过span、offset计算子组件位置与大小。多个子组件span超过规定列数时自动换行。
> - 单个元素span大小超过最大列数时，后台默认span为columns数。
> - 新一行的offset加上子组件的span超过总列数时，将下一个子组件在新的一行放置。
> - 例：Item1: GridCol(span: 6)，Item2: GridCol(span: 8, offset:11)。

|1|2|3|4|5|6|7|8|9|10|11|12|
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|$\circ$|$\circ$|$\circ$|$\circ$|$\circ$|$\circ$|-|-|-|-|-|-|
|-|-|-|-|-|-|-|-|-|-|-|-|
|$\circ$|$\circ$|$\circ$|$\circ$|$\circ$|$\circ$|$\circ$|$\circ$|-|-|-|-|

#### GridRowRow

```cangjie
GridRowRow
```

**功能：** 栅格元素按照行方向排列。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### RowReverse

```cangjie
RowReverse
```

**功能：** 栅格元素按照逆序行方向排列。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12