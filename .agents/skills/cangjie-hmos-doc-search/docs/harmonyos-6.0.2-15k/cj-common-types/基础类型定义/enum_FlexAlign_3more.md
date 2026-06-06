## enum FlexAlign

```cangjie
public enum FlexAlign {
    | Start
    | Center
    | End
    | SpaceBetween
    | SpaceAround
    | SpaceEvenly
}
```

**功能：** Flex容器对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Center

```cangjie
Center
```

**功能：** 元素在主轴方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### End

```cangjie
End
```

**功能：** 元素在主轴方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### SpaceAround

```cangjie
SpaceAround
```

**功能：** Flex主轴方向均匀分配弹性元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### SpaceBetween

```cangjie
SpaceBetween
```

**功能：** Flex主轴方向均匀分配弹性元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### SpaceEvenly

```cangjie
SpaceEvenly
```

**功能：** Flex主轴方向元素等间距布局，相邻元素之间的间距、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Start

```cangjie
Start
```

**功能：** 元素在主轴方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum FlexDirection

```cangjie
public enum FlexDirection {
    | Row
    | Column
    | RowReverse
    | ColumnReverse
}
```

**功能：** Flex布局容器方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Column

```cangjie
Column
```

**功能：** 主轴与列方向一致作为布局模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### ColumnReverse

```cangjie
ColumnReverse
```

**功能：** 与Column相反方向进行布局。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Row

```cangjie
Row
```

**功能：** 主轴与行方向一致作为布局模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### RowReverse

```cangjie
RowReverse
```

**功能：** 与Row方向相反方向进行布局。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum FlexWrap

```cangjie
public enum FlexWrap {
    | NoWrap
    | Wrap
    | WrapReverse
}
```

**功能：** Flex布局容器约束方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### NoWrap

```cangjie
NoWrap
```

**功能：** Flex容器的元素单行/列布局，子元素尽可能约束在容器内。当子元素有最小尺寸约束等设置时，Flex容器不会对其强制弹性压缩。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Wrap

```cangjie
Wrap
```

**功能：** Flex容器的元素多行/列排布，子项允许超出容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### WrapReverse

```cangjie
WrapReverse
```

**功能：** Flex容器的元素反向多行/列排布，子项允许超出容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12