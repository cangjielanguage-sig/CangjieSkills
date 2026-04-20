## enum PixelMapFormat

```cangjie
public enum PixelMapFormat <: Equatable<PixelMapFormat> & ToString {
    | Unknown
    | Rgb565
    | Rgba8888
    | Bgra8888
    | Rgb888
    | Alpha8
    | RgbaF16
    | Nv21
    | Nv12
    | Rgba1010102
    | YcbcrP010
    | YcrcbP010
    | ...
}
```

**功能：** 枚举，图片像素格式。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**父类型：**

- Equatable\<PixelMapFormat>
- ToString

### Alpha8

```cangjie
Alpha8
```

**功能：** 颜色信息仅包含透明度（Alpha），每个像素占8位。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### Bgra8888

```cangjie
Bgra8888
```

**功能：** 颜色信息由B（Blue），G（Green），R（Red）与透明度（Alpha）四部分组成，每个部分占8位，总共占32位。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### Nv12

```cangjie
Nv12
```

**功能：** YUV像素排列，U分量在V分量之前。颜色信息由亮度分量Y和交错排列的色度分量U和V组成，其中Y分量占8位，UV分量因4：2：0采样平均占4位，总共平均占12位。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### Nv21

```cangjie
Nv21
```

**功能：** YVU像素排列，V分量在U分量之前。颜色信息由亮度分量Y和交错排列的色度分量V和U组成，其中Y分量占8位，UV分量因4：2：0采样平均占4位，总共平均占12位。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### Rgb565

```cangjie
Rgb565
```

**功能：** 颜色信息由R（Red），G（Green），B（Blue）三部分组成，R占5位，G占6位，B占5位，总共占16位。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### Rgb888

```cangjie
Rgb888
```

**功能：** 颜色信息由R（Red），G（Green），B（Blue）三部分组成，每个部分占8位，总共占24位。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### Rgba1010102

```cangjie
Rgba1010102
```

**功能：** 颜色信息由R（Red），G（Green），B（Blue）与透明度（Alpha）四部分组成，其中R、G、B分别占10位，透明度占2位，总共占32位。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### Rgba8888

```cangjie
Rgba8888
```

**功能：** 颜色信息由R（Red），G（Green），B（Blue）与透明度（Alpha）四部分组成，每个部分占8位，总共占32位。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### RgbaF16

```cangjie
RgbaF16
```

**功能：** 颜色信息由R（Red），G（Green），B（Blue）与透明度（Alpha）四部分组成，每个部分占16位，总共占64位。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### Unknown

```cangjie
Unknown
```

**功能：** 未知格式。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### YcbcrP010

```cangjie
YcbcrP010
```

**功能：** 颜色信息由亮度分量Y和色度分量Cb与Cr组成，每个分量有效10位，实际存储时，Y平面每个像素占16位数据（10位有效），UV平面交错排列，每4个像素占32位数据（每色度分量10位有效），平均有效占15位。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### YcrcbP010

```cangjie
YcrcbP010
```

**功能：** 颜色信息由亮度分量Y和色度分量Cr与Cb组成，每个分量有效10位，实际存储时，Y平面每个像素占16位数据（10位有效），UV平面交错排列，每4个像素占32位数据（每色度分量10位有效），平均有效占15位。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22