## enum ImageRepeat

```cangjie
public enum ImageRepeat {
    | NoRepeat
    | X
    | Y
    | XY
}
```

**功能：** 图片重复方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### NoRepeat

```cangjie
NoRepeat
```

**功能：** 不重复绘制图片。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### X

```cangjie
X
```

**功能：** 只在水平轴上重复绘制图片。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### XY

```cangjie
XY
```

**功能：** 在两个轴上重复绘制图片。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Y

```cangjie
Y
```

**功能：** 只在竖直轴上重复绘制图片。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum ImageSize

```cangjie
public enum ImageSize {
    | Contain
    | Cover
    | Auto
    | FILL
}
```

**功能：** 图片尺寸显示设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Auto

```cangjie
Auto
```

**功能：** 默认值，保持原图的比例不变。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

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

### FILL

```cangjie
FILL
```

**功能：** 不保持宽高比进行放大缩小，使得图片充满显示边界。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum ImageSpanAlignment

```cangjie
public enum ImageSpanAlignment {
    | TOP
    | CENTER
    | BOTTOM
    | BASELINE
}
```

**功能：** 图片基于行高的对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### BASELINE

```cangjie
BASELINE
```

**功能：** 图片下边沿与文本BaseLine对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### BOTTOM

```cangjie
BOTTOM
```

**功能：** 图片下边沿与行下边沿对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### CENTER

```cangjie
CENTER
```

**功能：** 图片中间与行中间对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### TOP

```cangjie
TOP
```

**功能：** 图片上边沿与行上边沿对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum ImageType

```cangjie
public enum ImageType {
    | png
    | jpeg
    | webp
}
```

**功能：** 指定图像格式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### jpeg

```cangjie
jpeg
```

**功能：** jpeg图片格式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### png

```cangjie
png
```

**功能：** png图片格式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### webp

```cangjie
webp
```

**功能：** webp图片格式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19