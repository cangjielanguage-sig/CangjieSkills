### LUMINOSITY

```cangjie
LUMINOSITY
```

**功能：** 保留目标像素的色调和饱和度，但会用源像素的亮度替换目标像素的亮度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### MODULATE

```cangjie
MODULATE
```

**功能：** r = s * d，将源像素与目标像素进行乘法运算，并将结果作为新的像素值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### MULTIPLY

```cangjie
MULTIPLY
```

**功能：** r = s *(1 - da) + d* (1 - sa) + s * d，将源图像与目标图像进行乘法混合，得到一张新的图像。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### NONE

```cangjie
NONE
```

**功能：** 将上层图像直接覆盖到下层图像上，不进行任何混合操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OVERLAY

```cangjie
OVERLAY
```

**功能：** 根据目标像素来决定使用MULTIPLY混合模式还是SCREEN混合模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### PLUS

```cangjie
PLUS
```

**功能：** r = min(s + d, 1)，将源像素值与目标像素值相加，并将结果作为新的像素值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SATURATION

```cangjie
SATURATION
```

**功能：** 保留目标像素的亮度和色调，但会使用源像素的饱和度来替换目标像素的饱和度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SCREEN

```cangjie
SCREEN
```

**功能：** r = s + d - s * d，将两个图像的像素值相加，然后减去它们的乘积来实现混合。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SOFT_LIGHT

```cangjie
SOFT_LIGHT
```

**功能：** 根据源像素来决定使用LIGHTEN混合模式还是DARKEN混合模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SRC

```cangjie
SRC
```

**功能：** r = s，只显示源像素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SRC_ATOP

```cangjie
SRC_ATOP
```

**功能：** r = s *da + d* (1 - sa)，在源像素和目标像素重叠的地方绘制源像素，在源像素和目标像素不重叠的地方绘制目标像素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SRC_IN

```cangjie
SRC_IN
```

**功能：** r = s * da，只显示源像素中与目标像素重叠的部分。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SRC_OUT

```cangjie
SRC_OUT
```

**功能：** r = s * (1 - da)，只显示源像素中与目标像素不重叠的部分。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SRC_OVER

```cangjie
SRC_OVER
```

**功能：** r = s + (1 - sa) * d，将源像素按照透明度进行混合，覆盖在目标像素上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### XOR

```cangjie
XOR
```

**功能：** r = s *(1 - da) + d* (1 - sa)，只显示源像素与目标像素不重叠的部分。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19