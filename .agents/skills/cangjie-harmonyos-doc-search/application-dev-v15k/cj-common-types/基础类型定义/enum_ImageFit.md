## enum ImageFit

```cangjie
public enum ImageFit {
    | Fill
    | Contain
    | Cover
    | Auto
    | None
    | ScaleDown
    | TOP_START
    | TOP
    | TOP_END
    | START
    | CENTER
    | END
    | BOTTOM_START
    | BOTTOM
    | BOTTOM_END
}
```

**功能：** 图片的显示适配方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Auto

```cangjie
Auto
```

**功能：** 图像会根据其自身尺寸和组件的尺寸进行适当缩放，以在保持比例的同时填充视图。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### BOTTOM

```cangjie
BOTTOM
```

**功能：** 图像显示在Image组件的底部横向居中，保持原有尺寸显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### BOTTOM_END

```cangjie
BOTTOM_END
```

**功能：** 图像显示在Image组件的底部尾端，保持原有尺寸显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### BOTTOM_START

```cangjie
BOTTOM_START
```

**功能：** 图像显示在Image组件的底部起始端，保持原有尺寸显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### CENTER

```cangjie
CENTER
```

**功能：** 图像显示在Image组件的横向和纵向居中，保持原有尺寸显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Contain

```cangjie
Contain
```

**功能：** 保持宽高比进行缩小或者放大，使得图片完全显示在显示边界内。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Cover

```cangjie
Cover
```

**功能：** 保持宽高比进行缩小或者放大，使得图片两边都大于或等于显示边界。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### END

```cangjie
END
```

**功能：** 图像显示在Image组件的尾端纵向居中，保持原有尺寸显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Fill

```cangjie
Fill
```

**功能：** 不保持宽高比进行放大缩小，使得图片充满显示边界。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### None

```cangjie
None
```

**功能：** 保持原有尺寸显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### ScaleDown

```cangjie
ScaleDown
```

**功能：** 保持宽高比显示，图片缩小或者保持不变。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### START

```cangjie
START
```

**功能：** 图像显示在Image组件的起始端纵向居中，保持原有尺寸显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### TOP

```cangjie
TOP
```

**功能：** 图像显示在Image组件的顶部横向居中，保持原有尺寸显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### TOP_END

```cangjie
TOP_END
```

**功能：** 图像显示在Image组件的顶部尾端，保持原有尺寸显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### TOP_START

```cangjie
TOP_START
```

**功能：** 图像显示在Image组件的顶部起始端，保持原有尺寸显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19