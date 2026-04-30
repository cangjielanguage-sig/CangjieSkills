### TRANSFER_FUNCTION

```cangjie
TRANSFER_FUNCTION
```

**功能：** 图像的传递函数，通常用于颜色校正。

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### USER_COMMENT

```cangjie
USER_COMMENT
```

**功能：** 用户注释。

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### WHITE_BALANCE

```cangjie
WHITE_BALANCE
```

**功能：** 白平衡。

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### WHITE_POINT

```cangjie
WHITE_POINT
```

**功能：** 图像的白点色度。

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### WIND_SNAPSHOT_MODE

```cangjie
WIND_SNAPSHOT_MODE
```

**功能：** 运动快拍模式。

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### XMAGE_BOTTOM

```cangjie
XMAGE_BOTTOM
```

**功能：** 水印区域Y2坐标。

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### XMAGE_LEFT

```cangjie
XMAGE_LEFT
```

**功能：** 水印区域X1坐标。

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### XMAGE_MODE

```cangjie
XMAGE_MODE
```

**功能：** XMAGE水印模式。

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### XMAGE_RIGHT

```cangjie
XMAGE_RIGHT
```

**功能：** 水印区域X2坐标。

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### XMAGE_TOP

```cangjie
XMAGE_TOP
```

**功能：** 水印区域Y1坐标。

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### X_RESOLUTION

```cangjie
X_RESOLUTION
```

**功能：** 图像宽度方向的分辨率。

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### YCBCR_COEFFICIENTS

```cangjie
YCBCR_COEFFICIENTS
```

**功能：** 从RGB到YCbCr图像数据的转换矩阵系数。

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### YCBCR_POSITIONING

```cangjie
YCBCR_POSITIONING
```

**功能：** 色度分量相对于亮度分量的位置。

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### YCBCR_SUB_SAMPLING

```cangjie
YCBCR_SUB_SAMPLING
```

**功能：** 色度分量与亮度分量的采样比率。

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### Y_RESOLUTION

```cangjie
Y_RESOLUTION
```

**功能：** 图像高度方向的分辨率。

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### func !=(PropertyKey)

```cangjie
public operator func !=(other: PropertyKey): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PropertyKey](#enum-propertykey)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(PropertyKey)

```cangjie
public operator func ==(other: PropertyKey): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PropertyKey](#enum-propertykey)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|