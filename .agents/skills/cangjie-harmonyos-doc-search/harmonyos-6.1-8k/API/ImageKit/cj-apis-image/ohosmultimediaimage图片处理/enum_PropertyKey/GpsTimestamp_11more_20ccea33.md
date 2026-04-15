### GpsTimestamp

```cangjie
GpsTimestamp
```

**功能：** GPS时间戳。

修改传参格式说明：格式为"HH:mm:ss.ddd"。

修改示例：`imageSource.modifyImageProperty(key,'12:30:30.123');`

读取结果示例："12:30:30.123"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### IsoSpeed

```cangjie
IsoSpeed
```

**功能：** ISO速度等级。

修改传参格式说明：非负整数字符串。

修改示例：`imageSource.modifyImageProperty(key,'3200');`

读取结果示例："3200"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### IsoSpeedRatings

```cangjie
IsoSpeedRatings
```

**功能：** ISO感光度，例如400。

修改传参格式说明：非负整数字符串。

修改示例：`imageSource.modifyImageProperty(key,'3200');`

读取结果示例："3200"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### ImageDescription

```cangjie
ImageDescription
```

**功能：** 图像信息描述。

修改传参格式说明：字符串。

修改示例：`imageSource.modifyImageProperty(key,'Image description info');`

读取结果示例："Image description info"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### ImageLength

```cangjie
ImageLength
```

**功能：** 图片长度。

修改传参格式说明：非负整数字符串。

修改示例：`imageSource.modifyImageProperty(key,'3072');`

读取结果示例："3072"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### ImageWidth

```cangjie
ImageWidth
```

**功能：** 图片宽度。

修改传参格式说明：非负整数字符串。

修改示例：`imageSource.modifyImageProperty(key,'4096');`

读取结果示例："4096"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### LightSource

```cangjie
LightSource
```

**功能：** 光源。例如Fluorescent。

修改传参格式说明：修改时传入相应的数字或者字符串。

修改示例：`imageSource.modifyImageProperty(key,'1');`或`imageSource.modifyImageProperty(key,'Daylight');`

读取结果示例："Daylight"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### Make

```cangjie
Make
```

**功能：** 生产商。

修改传参格式说明：字符串。

修改示例：`imageSource.modifyImageProperty(key,'Make');`

读取结果示例："Make"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### MeteringMode

```cangjie
MeteringMode
```

**功能：** 测光模式。

修改传参格式说明：修改时传入相应的数字或者字符串。

修改示例：`imageSource.modifyImageProperty(key,'1');`或`imageSource.modifyImageProperty(key,'Average');`

读取结果示例："Average"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### Model

```cangjie
Model
```

**功能：** 设备型号。

修改传参格式说明：字符串。

修改示例：`imageSource.modifyImageProperty(key,'Model');`

读取结果示例："Model"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### Orientation

```cangjie
Orientation
```

**功能：** 图片方向。

1："Top-left"，图像未旋转。

2："Top-right"，镜像水平翻转。

3："Bottom-right"，图像旋转180°。

4："Bottom-left"，镜像垂直翻转。

5："Left-top"，镜像水平翻转再顺时针旋转270°。

6："Right-top"，顺时针旋转90°。

7："Right-bottom"，镜像水平翻转再顺时针旋转90°。

8："Left-bottom"，顺时针旋转270°。

如果读到未定义值会返回"Unknown Value 0"。获取该属性时会以字符串的形式返回。修改该属性时既可以以数字形式指定，也可以以字符串形式指定。

修改传参格式说明：修改时传入相应的数字或者字符串。

修改示例：`imageSource.modifyImageProperty(key,'1');`或`imageSource.modifyImageProperty(key,'Top-left');`

读取结果示例："Top-left"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22