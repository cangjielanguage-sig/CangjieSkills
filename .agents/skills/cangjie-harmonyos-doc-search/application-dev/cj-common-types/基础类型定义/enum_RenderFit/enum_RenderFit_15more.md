## enum RenderFit

```cangjie
public enum RenderFit <: Equatable<RenderFit> {
    | Center
    | Top
    | Bottom
    | Left
    | Right
    | TopLeft
    | TopRight
    | BottomLeft
    | BottomRight
    | ResizeFill
    | ResizeContain
    | ResizeContainTopLeft
    | ResizeContainBottomRight
    | ResizeCover
    | ResizeCoverTopLeft
    | ResizeCoverBottomRight
    | ...
}
```

**功能：** 组件内容填充样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[RenderFit](#enum-renderfit)>

### Center

```cangjie
Center
```

**功能：** 保持动画终态的内容大小，并且内容始终与组件保持中心对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Top

```cangjie
Top
```

**功能：** 保持动画终态的内容大小，并且内容始终与组件保持顶部中心对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Bottom

```cangjie
Bottom
```

**功能：** 保持动画终态的内容大小，并且内容始终与组件保持底部中心对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Left

```cangjie
Left
```

**功能：** 保持动画终态的内容大小，并且内容始终与组件保持左侧对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Right

```cangjie
Right
```

**功能：** 保持动画终态的内容大小，并且内容始终与组件保持右侧对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### TopLeft

```cangjie
TopLeft
```

**功能：** 保持动画终态的内容大小，并且内容始终与组件保持左上角对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### TopRight

```cangjie
TopRight
```

**功能：** 保持动画终态的内容大小，并且内容始终与组件保持右上角对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### BottomLeft

```cangjie
BottomLeft
```

**功能：** 保持动画终态的内容大小，并且内容始终与组件保持左下角对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### BottomRight

```cangjie
BottomRight
```

**功能：** 保持动画终态的内容大小，并且内容始终与组件保持右下角对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### ResizeFill

```cangjie
ResizeFill
```

**功能：** 不考虑动画终态内容的宽高比，并且内容始终缩放到组件的大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### ResizeContain

```cangjie
ResizeContain
```

**功能：** 保持动画终态内容的宽高比进行缩小或放大，使内容完整显示在组件内，且与组件保持中心对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### ResizeContainTopLeft

```cangjie
ResizeContainTopLeft
```

**功能：** 持动画终态内容的宽高比进行缩小或放大，使内容完整显示在组件内。当组件宽方向有剩余时，内容与组件保持左侧对齐，当组件高方向有剩余时，内容与组件保持顶部对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### ResizeContainBottomRight

```cangjie
ResizeContainBottomRight
```

**功能：** 保持动画终态内容的宽高比进行缩小或放大，使内容的两边都恰好大于或等于组件两边。当内容宽方向有剩余时，内容与组件保持右侧对齐，显示内容的右侧部分。当内容高方向有剩余时，内容与组件保持底部对齐，显示内容的底侧部分。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### ResizeCover

```cangjie
ResizeCover
```

**功能：** 保持动画终态内容的宽高比进行缩小或放大，使内容两边都大于或等于组件两边，且与组件保持中心对齐，显示内容的中间部分。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22