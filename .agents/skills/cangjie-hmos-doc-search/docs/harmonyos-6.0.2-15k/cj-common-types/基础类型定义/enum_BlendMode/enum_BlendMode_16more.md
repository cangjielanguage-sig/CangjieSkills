## enum BlendMode

```cangjie
public enum BlendMode {
    | NONE
    | CLEAR
    | SRC
    | DST
    | SRC_OVER
    | DST_OVER
    | SRC_IN
    | DST_IN
    | SRC_OUT
    | DST_OUT
    | SRC_ATOP
    | DST_ATOP
    | XOR
    | PLUS
    | MODULATE
    | SCREEN
    | OVERLAY
    | DARKEN
    | LIGHTEN
    | COLOR_DODGE
    | COLOR_BURN
    | HARD_LIGHT
    | SOFT_LIGHT
    | DIFFERENCE
    | EXCLUSION
    | MULTIPLY
    | HUE
    | SATURATION
    | COLOR
    | LUMINOSITY
}
```

**功能：** 混合模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

> **说明：**
>
> blendMode枚举中，s表示源像素，d表示目标像素，sa表示原像素透明度，da表示目标像素透明度，r表示混合后像素，ra表示混合后像素透明度。

### CLEAR

```cangjie
CLEAR
```

**功能：** 将源像素覆盖的目标像素清除为完全透明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### COLOR

```cangjie
COLOR
```

**功能：** 保留源像素的饱和度和色调，但会使用目标像素的亮度来替换源像素的亮度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### COLOR_BURN

```cangjie
COLOR_BURN
```

**功能：** 使目标像素变得更暗来反映源像素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### COLOR_DODGE

```cangjie
COLOR_DODGE
```

**功能：** 使目标像素变得更亮来反映源像素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### DARKEN

```cangjie
DARKEN
```

**功能：** rc = s + d - max(s *da, d* sa), ra = kSrcOver，当两个颜色重叠时，较暗的颜色会覆盖较亮的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### DIFFERENCE

```cangjie
DIFFERENCE
```

**功能：** rc = s + d - 2 *(min(s* da, d * sa)), ra = kSrcOver，对比源像素和目标像素，亮度更高的像素减去亮度更低的像素，产生高对比度的效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### DST

```cangjie
DST
```

**功能：** r = d，只显示目标像素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### DST_ATOP

```cangjie
DST_ATOP
```

**功能：** r = d *sa + s* (1 - da)，在源像素和目标像素重叠的地方绘制目标像素，在源像素和目标像素不重叠的地方绘制源像素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### DST_IN

```cangjie
DST_IN
```

**功能：** r = d * sa，只显示目标像素中与源像素重叠的部分。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### DST_OUT

```cangjie
DST_OUT
```

**功能：** r = d * (1 - sa)，只显示目标像素中与源像素不重叠的部分。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### DST_OVER

```cangjie
DST_OVER
```

**功能：** r = d + (1 - da) * s，将目标像素按照透明度进行混合，覆盖在源像素上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### EXCLUSION

```cangjie
EXCLUSION
```

**功能：** rc = s + d - two(s * d), ra = kSrcOver，对比源像素和目标像素，亮度更高的像素减去亮度更低的像素，产生柔和的效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### HARD_LIGHT

```cangjie
HARD_LIGHT
```

**功能：** 根据源像素的值来决定目标像素变得更亮或者更暗。根据源像素来决定使用MULTIPLY混合模式还是SCREEN混合模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### HUE

```cangjie
HUE
```

**功能：** 保留源图像的亮度和饱和度，但会使用目标图像的色调来替换源图像的色调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### LIGHTEN

```cangjie
LIGHTEN
```

**功能：** rc = s + d - min(s *da, d* sa), ra = kSrcOver，将源图像和目标图像中的像素进行比较，选取两者中较亮的像素作为最终的混合结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19