### FNumber

```cangjie
FNumber
```

**功能：** 光圈值，例如f/1.8。

修改传参格式说明：非负有理数字符串。

修改示例：`imageSource.modifyImageProperty(key,'1');`或`imageSource.modifyImageProperty(key,'1/2');`

读取结果示例："f/1.0"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### FaceCount

```cangjie
FaceCount
```

**功能：** 人脸数量。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### Flash

```cangjie
Flash
```

**功能：** 闪光灯，记录闪光灯状态。

修改传参格式说明：修改时传入相应的数字或者字符串。

修改示例：`imageSource.modifyImageProperty(key,'0x00');`或`imageSource.modifyImageProperty(key,'Flash did not fire');`

读取结果示例："Flash did not fire"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### FocalLength

```cangjie
FocalLength
```

**功能：** 焦距。

修改传参格式说明：非负有理数字符串。

修改示例：`imageSource.modifyImageProperty(key,'50');`或`imageSource.modifyImageProperty(key,'50/1');`

读取结果示例："50.0 mm"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### FocalLengthIn35mmFilm

```cangjie
FocalLengthIn35mmFilm
```

**功能：** 焦距35毫米胶片。

修改传参格式说明：非负整数字符串。

修改示例：`imageSource.modifyImageProperty(key,'50');`

读取结果示例：*"50"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### FocusMode

```cangjie
FocusMode
```

**功能：** 对焦模式。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### GpsDateStamp

```cangjie
GpsDateStamp
```

**功能：** GPS日期戳。

修改传参格式说明：格式为“YY:MM:DD”。

修改示例：`imageSource.modifyImageProperty(key,'2020:07:07');`

读取结果示例："2020:07:07"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### GpsLatitude

```cangjie
GpsLatitude
```

**功能：** 图片纬度。修改时应按"度，分，秒"格式传入，如"39，54，7.542"

修改传参格式说明：三个非负有理数字符串，逗号隔开。

修改示例：`imageSource.modifyImageProperty(key,'39,54,7.542');`

读取结果示例："39,54,7.542"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### GpsLatitudeRef

```cangjie
GpsLatitudeRef
```

**功能：** 用于标识图像拍摄地点的纬度方向（北半球或南半球）。

78："North"。

83："South"。

修改传参格式说明： 修改时传入相应的数字或者字符串。

修改示例：`imageSource.modifyImageProperty(key,'78');`或`imageSource.modifyImageProperty(key,'North');`

读取结果示例："N"或"78"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### GpsLongitude

```cangjie
GpsLongitude
```

**功能：** 图片经度。修改时应按"度，分，秒"格式传入，如"116，19，42.16"

修改传参格式说明：三个非负有理数字符串，逗号隔开。

修改示例：`imageSource.modifyImageProperty(key,'116,19,42.16');`

读取结果示例："116,19,42.16"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### GpsLongitudeRef

```cangjie
GpsLongitudeRef
```

**功能：** 经度引用，例如W或E， 用于标识图像拍摄地点的经度方向（东半球或西半球）。

69："East"。

87："West"。

修改传参格式说明：修改时传入相应的数字或者字符串。

修改示例：`imageSource.modifyImageProperty(key,'69');`或`imageSource.modifyImageProperty(key,'East');`

读取结果示例："69"或"E"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22