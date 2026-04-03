### enum RenderFit

```cangjie
public enum RenderFit {
    | CENTER
    | TOP
    | BOTTOM
    | LEFT
    | RIGHT
    | TOP_LEFT
    | TOP_RIGHT
    | BOTTOM_LEFT
    | BOTTOM_RIGHT
    | RESIZE_FILL
    | RESIZE_CONTAIN
    | RESIZE_CONTAIN_TOP_LEFT
    | RESIZE_CONTAIN_BOTTOM_RIGHT
    | RESIZE_COVER
    | RESIZE_COVER_TOP_LEFT
    | RESIZE_COVER_BOTTOM_RIGHT
}
```

**功能：** 组件内容填充样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### CENTER

```cangjie
CENTER
```

**功能：** 保持动画终态的内容大小，并且内容始终与组件保持中心对齐。

![renderfit_center](figures/renderfit_center.png)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### TOP

```cangjie
TOP
```

**功能：** 保持动画终态的内容大小，并且内容始终与组件保持顶部中心对齐。

![renderfit_top](figures/renderfit_top.png)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### BOTTOM

```cangjie
BOTTOM
```

**功能：** 保持动画终态的内容大小，并且内容始终与组件保持底部中心对齐。

![renderfit_bottom](figures/renderfit_bottom.png)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### LEFT

```cangjie
LEFT
```

**功能：** 保持动画终态的内容大小，并且内容始终与组件保持左侧对齐。

![renderfit_left](figures/renderfit_left.png)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### RIGHT

```cangjie
RIGHT
```

**功能：** 保持动画终态的内容大小，并且内容始终与组件保持右侧对齐。

![renderfit_right](figures/renderfit_right.png)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### TOP_LEFT

```cangjie
TOP_LEFT
```

**功能：** 保持动画终态的内容大小，并且内容始终与组件保持左上角对齐。

![renderfit_top_left](figures/renderfit_top_left.png)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### TOP_RIGHT

```cangjie
TOP_RIGHT
```

**功能：** 保持动画终态的内容大小，并且内容始终与组件保持右上角对齐。

![renderfit_top_right](figures/renderfit_top_right.png)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### BOTTOM_LEFT

```cangjie
BOTTOM_LEFT
```

**功能：** 保持动画终态的内容大小，并且内容始终与组件保持左下角对齐。

![renderfit_bottom_left](figures/renderfit_bottom_left.png)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### BOTTOM_RIGHT

```cangjie
BOTTOM_LEFT
```

**功能：** 保持动画终态的内容大小，并且内容始终与组件保持右下角对齐。

![renderfit_bottom_right](figures/renderfit_bottom_right.png)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### RESIZE_FILL

```cangjie
RESIZE_FILL
```

**功能：** 不考虑动画终态内容的宽高比，并且内容始终缩放到组件的大小。

![renderfit_resize_fill](figures/renderfit_resize_fill.png)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### RESIZE_CONTAIN

```cangjie
RESIZE_CONTAIN
```

**功能：** 保持动画终态内容的宽高比进行缩小或放大，使内容完整显示在组件内，且与组件保持中心对齐。

![renderfit_resize_contain](figures/renderfit_resize_contain.png)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### RESIZE_CONTAIN_TOP_LEFT

```cangjie
RESIZE_CONTAIN_TOP_LEFT
```

**功能：** 持动画终态内容的宽高比进行缩小或放大，使内容完整显示在组件内。当组件宽方向有剩余时，内容与组件保持左侧对齐，当组件高方向有剩余时，内容与组件保持顶部对齐。

 ![renderfit_resize_contain_top_left](figures/renderfit_resize_contain_top_left.png)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12