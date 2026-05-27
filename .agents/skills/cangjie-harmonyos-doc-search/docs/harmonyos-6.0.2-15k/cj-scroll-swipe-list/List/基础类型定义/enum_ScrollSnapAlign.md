### enum ScrollSnapAlign

```cangjie
public enum ScrollSnapAlign {
    | NONE
    | START
    | CENTER
    | END
}
```

**功能：** 设置列表项滚动结束对齐效果。

只支持item等高场景限位，不等高场景可能存在不准确的情况。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### NONE

```cangjie
CARD
```

**功能：** 默认无项目滚动对齐效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### START

```cangjie
NONE
```

**功能：** 视图中的第一项将在列表的开头对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

> **说明：**
>
> 当列表位移至末端，需要将末端的item完整显示，可能出现开头不对齐的情况。

#### CENTER

```cangjie
NONE
```

**功能：** 视图中的中间项将在列表中心对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

> **说明：**
>
> 顶端和末尾的item都可以在列表中心对齐，列表显示可能露出空白，第一个或最后一个item会对齐到中间位置。

#### END

```cangjie
NONE
```

**功能：** 视图中的最后一项将在列表末尾对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

> **说明：**
>
> 当列表位移至顶端，需要将顶端的item完整显示，可能出现末尾不对齐的情况。