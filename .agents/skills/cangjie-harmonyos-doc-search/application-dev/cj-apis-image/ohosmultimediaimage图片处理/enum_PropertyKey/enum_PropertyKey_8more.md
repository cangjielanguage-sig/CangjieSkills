## enum PropertyKey

```cangjie
public enum PropertyKey <: ToString {
    | BitsPerSample
    | Orientation
    | ImageLength
    | ImageWidth
    | GpsLatitude
    | GpsLongitude
    | GpsLatitudeRef
    | GpsLongitudeRef
    | DateTimeOriginal
    | ExposureTime
    | SceneType
    | IsoSpeedRatings
    | FNumber
    | DateTime
    | GpsTimestamp
    | GpsDateStamp
    | ImageDescription
    | Make
    | Model
    | PhotoMode
    | SensitivityType
    | StandardOutputSensitivity
    | RecommendedExposureIndex
    | IsoSpeed
    | ApertureValue
    | ExposureBiasValue
    | MeteringMode
    | LightSource
    | Flash
    | FocalLength
    | UserComment
    | PixelXDimension
    | PixelYDimension
    | WhiteBalance
    | FocalLengthIn35mmFilm
    | CaptureMode
    | PhysicalAperture
    | RollAngle
    | PitchAngle
    | SceneFoodConf
    | SceneStageConf
    | SceneBlueSkyConf
    | SceneGreenPlantConf
    | SceneBeachConf
    | SceneSnowConf
    | SceneSunsetConf
    | SceneFlowersConf
    | SceneNightConf
    | SceneTextConf
    | FaceCount
    | FocusMode
    | ...
}
```

**功能：** 枚举，Exif（Exchangeable image file format）图像信息。

- 格式示例中的key为：PropertyKey.XXX（XXX为枚举的名称，如：.PropertyKey.ImageWidth）。

- 格式示例仅用于说明修改传值和读取结果的格式。具体接口使用方法请参考：[modifyImageProperty](#func-modifyimagepropertypropertykey-string)（修改单个Exif字段）、[getImageProperty](#func-getimagepropertypropertykey-imagepropertyoptions)（读取单个Exif字段）。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**父类型：**

- ToString

### ApertureValue

```cangjie
ApertureValue
```

**功能：** 光圈值。格式如4/1。

修改传参格式说明：非负有理数字符串。

修改示例：`imageSource.modifyImageProperty(key,'5.6');`

读取结果示例："5.60 EV (f/7.0)"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### BitsPerSample

```cangjie
BitsPerSample
```

**功能：** 像素各分量的位数，如RGB，3分量，格式是8,8,8。

修改传参格式说明：三个非负整数字符串，空格或者英文逗号隔开。

修改示例：`imageSource.modifyImageProperty(key,'8 8 8');`或`imageSource.modifyImageProperty(key,'8,8,8');`

读取结果示例："8,8,8

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### CaptureMode

```cangjie
CaptureMode
```

**功能：** 捕获模式。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### DateTime

```cangjie
DateTime
```

**功能：** 日期时间。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### DateTimeOriginal

```cangjie
DateTimeOriginal
```

**功能：** 日期时间。

修改传参格式说明：有两种格式，YYYY:MM:DD或者YYYY:MM:DD HH:MM:SS

修改示例：`imageSource.modifyImageProperty(key,'2024:07:07 13:45:59');`<br />或`imageSource.modifyImageProperty(key,'2024:07:07');`

读取结果示例："2024:07:07 13:45:59"或"2024:07:07"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### ExposureBiasValue

```cangjie
ExposureBiasValue
```

**功能：** 曝光偏差值。

修改传参格式说明：非负有理数字符串。

修改示例：`imageSource.modifyImageProperty(key,'1');`

读取结果示例：1.00 EV

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### ExposureTime

```cangjie
ExposureTime
```

**功能：** 曝光时间，例如1/33 sec。

修改传参格式说明：非负有理数字符串。

修改示例：`imageSource.modifyImageProperty(key,'1');`或`imageSource.modifyImageProperty(key,'1/2');`

读取结果示例："1/33 sec."

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22