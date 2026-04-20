### struct OffsetOption

```cangjie
public struct OffsetOption {
    public OffsetOption (
        public let offsetRemain: Float64
    )
}
```

**功能：** 实际滑动量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let offsetRemain

```cangjie
public let offsetRemain: Float64
```

**功能：** 实际滑动量，单位vp。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 19

#### OffsetOption(Float64)

```cangjie
public OffsetOption (
    public let offsetRemain: Float64
)
```

**功能：** 创建一个OffsetOption类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offsetRemain|Float64|是|-|实际滑动量，单位vp。|

### enum GridDirection

```cangjie
public enum GridDirection {
    | Row
    | Column
    | RowReverse
    | ColumnReverse
}
```

**功能：** 主轴布局方向枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Column

```cangjie
Column
```

**功能：** 主轴布局方向沿垂直方向布局，即自上往下先填满一列，再去填下一列。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### ColumnReverse

```cangjie
ColumnReverse
```

**功能：** 主轴布局方向沿垂直方向反向布局，即自下往上先填满一列，再去填下一列。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Row

```cangjie
Row
```

**功能：** 主轴布局方向沿水平方向布局，即自左往右先填满一行，再去填下一行。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### RowReverse

```cangjie
RowReverse
```

**功能：** 主轴布局方向沿水平方向反向布局，即自右往左先填满一行，再去填下一行。

> **说明：**
>
> Grid组件[通用属性clip](cj-universal-attribute-shapclip.md#func-clipbool)的初始值为true。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum GridItemAlignment

```cangjie
public enum GridItemAlignment {
    | DEFAULT
    | STRETCH
}
```

**功能：** GridItem的对齐方式枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### DEFAULT

```cangjie
DEFAULT
```

**功能：** 使用Grid的默认对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### STRETCH

```cangjie
STRETCH
```

**功能：** 以一行中的最高的GridItem作为其他GridItem的高度。

> **说明：**
>
> - 1、只有可滚动的Grid中，设置STRETCH参数会生效，其他场景不生效。
> - 2、在Grid的一行中，如果每个GridItem都是大小规律的（只占一行一列），设置STRETCH参数会生效，存在跨行或跨列的GridItem的场景不生效。
> - 3、设置STRETCH后，只有不设置高度的GridItem才会以当前行中最高的GridItem作为自己的高度，设置过高度的GridItem高度不会变化。
> - 4、设置STRETCH后，Grid布局时会有额外的布局流程，可能会带来额外的性能开销。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19