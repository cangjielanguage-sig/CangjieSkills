### enum LayoutStyle

```cangjie
public enum LayoutStyle {
    | ALWAYS_CENTER
    | ALWAYS_AVERAGE_SPLIT
    | SPACE_BETWEEN_OR_CENTER
}
```

**功能：** Scrollable模式下不滚动时的页签排布方式枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### ALWAYS_AVERAGE_SPLIT

```cangjie
ALWAYS_AVERAGE_SPLIT
```

**功能：** 当页签内容超过TabBar宽度时，TabBar可滚动。当页签内容不超过TabBar宽度时，TabBar不可滚动，且所有页签平均分配TabBar宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### ALWAYS_CENTER

```cangjie
ALWAYS_CENTER
```

**功能：** 当页签内容超过TabBar宽度时，TabBar可滚动。当页签内容不超过TabBar宽度时，TabBar不可滚动，页签紧凑居中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### SPACE_BETWEEN_OR_CENTER

```cangjie
SPACE_BETWEEN_OR_CENTER
```

**功能：** 当页签内容超过TabBar宽度时，TabBar可滚动。当页签内容不超过TabBar宽度但超过TabBar宽度一半时，TabBar不可滚动，页签紧凑居中。当页签内容不超过TabBar宽度一半时，TabBar不可滚动，保证页签居中排列在TabBar宽度一半，且间距相同。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum BarPosition

```cangjie
public enum LayoutStyle {
    | Start
    | End
}
```

**功能：** Tabs页签位置枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Start

```cangjie
Start
```

**功能：** vertical属性方法设置为true时，页签位于容器左侧；vertical属性方法设置为false时，页签位于容器顶部。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### End

```cangjie
End
```

**功能：** vertical属性方法设置为true时，页签位于容器右侧；vertical属性方法设置为false时，页签位于容器底部。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### enum BarMode

```cangjie
public enum LayoutStyle {
    | Fixed
    | Scrollable
}
```

**功能：** TabBar布局模式枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Fixed

```cangjie
Fixed
```

**功能：** 所有TabBar平均分配barWidth宽度（纵向时平均分配barHeight高度）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Scrollable

```cangjie
Scrollable
```

**功能：** 每一个TabBar均使用实际布局宽度，超过总长度（横向Tabs的barWidth，纵向Tabs的barHeight）后可滑动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12