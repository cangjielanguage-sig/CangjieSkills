## enum PixelMapFormat

```cangjie
public enum PixelMapFormat <: Equatable<PixelMapFormat> & ToString {
    | UNKNOWN
    | RGB_565
    | RGBA_8888
    | BGRA_8888
    | RGB_888
    | ALPHA_8
    | RGBA_F16
    | NV21
    | NV12
    | RGBA_1010102
    | YCBCR_P010
    | YCRCB_P010
    | ...
}
```

**功能：** 图片像素格式。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**父类型：**

- Equatable\<PixelMapFormat>
- ToString

### ALPHA_8

```cangjie
ALPHA_8
```

**功能：** 颜色信息仅包含透明度（Alpha），每个像素占8位。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### BGRA_8888

```cangjie
BGRA_8888
```

**功能：** 颜色信息由B（Blue），G（Green），R（Red）与透明度（Alpha）四部分组成，每个部分占8位，总共占32位

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### NV12

```cangjie
NV12
```

**功能：** YUV像素排列，U分量在V分量之前。颜色信息由亮度分量Y和交错排列的色度分量U和V组成，其中Y分量占8位，UV分量因4：2：0采样平均占4位，总共平均占12位。对应[相机服务CameraFormat中的CAMERA_FORMAT_YUV_420_SP](../CameraKit/cj-apis-multimedia-camera.md#camera_format_yuv_420_sp)。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### NV21

```cangjie
NV21
```

**功能：** YVU像素排列，V分量在U分量之前。颜色信息由亮度分量Y和交错排列的色度分量V和U组成，其中Y分量占8位，UV分量因4：2：0采样平均占4位，总共平均占12位。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### RGBA_1010102

```cangjie
RGBA_1010102
```

**功能：** 颜色信息由R（Red），G（Green），B（Blue）与透明度（Alpha）四部分组成，其中R、G、B分别占10位，透明度占2位，总共占32位。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### RGBA_8888

```cangjie
RGBA_8888
```

**功能：** 颜色信息由R（Red），G（Green），B（Blue）与透明度（Alpha）四部分组成，每个部分占8位，总共占32位。对应[相机服务CameraFormat中的CAMERA_FORMAT_RGBA_8888](../CameraKit/cj-apis-multimedia-camera.md#camera_format_rgba_8888)。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### RGBA_F16

```cangjie
RGBA_F16
```

**功能：** 颜色信息由R（Red），G（Green），B（Blue）与透明度（Alpha）四部分组成，每个部分占16位，总共占64位。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### RGB_565

```cangjie
RGB_565
```

**功能：** 颜色信息由R（Red），G（Green），B（Blue）三部分组成，R占5位，G占6位，B占5位，总共占16位。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### RGB_888

```cangjie
RGB_888
```

**功能：** 颜色信息由R（Red），G（Green），B（Blue）三部分组成，每个部分占8位，总共占24位。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** 未知格式。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### YCBCR_P010

```cangjie
YCBCR_P010
```

**功能：** 颜色信息由亮度分量Y和色度分量Cb与Cr组成，每个分量有效10位，实际存储时，Y平面每个像素占16位数据（10位有效），UV平面交错排列，每4个像素占32位数据（每色度分量10位有效），平均有效占15位。对应[相机服务CameraFormat中的CAMERA_FORMAT_YCBCR_P010](../CameraKit/cj-apis-multimedia-camera.md#camera_format_ycbcr_p010)。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19