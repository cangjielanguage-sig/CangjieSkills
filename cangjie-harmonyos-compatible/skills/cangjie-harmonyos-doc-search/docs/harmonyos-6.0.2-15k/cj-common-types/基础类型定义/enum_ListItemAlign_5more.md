## enum ListItemAlign

```cangjie
public enum ListItemAlign {
    | Start
    | Center
    | End
}
```

**功能：** ListItem在List中，交叉轴方向的对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Center

```cangjie
Center
```

**功能：** ListItem在List中，交叉轴方向居中对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### End

```cangjie
End
```

**功能：** ListItem在List中，交叉轴方向尾部对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Start

```cangjie
Start
```

**功能：** ListItem在List中，交叉轴方向首部对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum ListItemGroupArea

```cangjie
public enum ListItemGroupArea {
    | NONE
    | IN_LIST_ITEM_AREA
    | IN_HEADER_AREA
    | IN_FOOTER_AREA
}
```

**功能：** 表示处于ListItemGroup的哪一个区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### IN_FOOTER_AREA

```cangjie
IN_FOOTER_AREA
```

**功能：** 当前页面可视边处于footer位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### IN_HEADER_AREA

```cangjie
IN_HEADER_AREA
```

**功能：** 当前页面可视边处于header位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### IN_LIST_ITEM_AREA

```cangjie
IN_LIST_ITEM_AREA
```

**功能：** 当前页面可视边处于ListItem位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### NONE

```cangjie
NONE
```

**功能：** 当前页面可视边处于none位置。例如，ListItemGroup中既没有header、footer，也没有ListItem。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum MarqueeUpdateStrategy

```cangjie
public enum MarqueeUpdateStrategy {
    | DEFAULT
    | PRESERVE_POSITION
}
```

**功能：** 跑马灯效果更新策略。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### DEFAULT

```cangjie
DEFAULT
```

**功能：** 跑马灯组件属性更新后， 从开始位置， 运行跑马灯效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### PRESERVE_POSITION

```cangjie
PRESERVE_POSITION
```

**功能：** 跑马灯组件属性更新后， 保持当前位置， 运行跑马灯效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum MenuPolicy

```cangjie
public enum MenuPolicy {
    | Default
    | Hide
    | Show
}
```

**功能：** 菜单弹出的策略。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### DEFAULT

```cangjie
DEFAULT
```

**功能：** 按照底层默认逻辑决定是否弹出菜单。

**起始版本：** 12

### HIDE

```cangjie
HIDE
```

**功能：** 始终不弹出菜单。

**起始版本：** 12

### SHOW

```cangjie
SHOW
```

**功能：** 始终弹出菜单。

**起始版本：** 12

## enum MenuPreviewMode

```cangjie
public enum MenuPreviewMode {
    | NONE
    | IMAGE
}
```

**功能：** 菜单的预览内容样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### IMAGE

```cangjie
IMAGE
```

**功能：** 预览内容为触发长按悬浮菜单组件的截图。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### NONE

```cangjie
NONE
```

**功能：** 不显示预览内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19