## struct PhotoCaptureSetting

```cangjie
public struct PhotoCaptureSetting {
    public var quality: QualityLevel
    public var rotation: ImageRotation
    public var location: Location
    public var mirror: Bool
    public init(
        quality!: QualityLevel = QualityLevel.QUALITY_LEVEL_MEDIUM,
        rotation!: ImageRotation = ImageRotation.ROTATION_0,
        location!: Location = Location(-1.0, -1.0, -1.0),
        mirror!: Bool = false
    )
}
```

**功能：** 拍摄照片的设置。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### var location

```cangjie
public var location: Location
```

**功能：** 图片地理位置信息(默认以设备硬件信息为准)。

**类型：** [Location](#struct-location)

**读写能力：** 可读写

**起始版本：** 19

### var mirror

```cangjie
public var mirror: Bool
```

**功能：** 镜像使能开关(默认关)。使用之前需要使用isMirrorSupported进行判断是否支持。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var quality

```cangjie
public var quality: QualityLevel
```

**功能：** 图片质量(默认低)。

**类型：** [QualityLevel](#enum-qualitylevel)

**读写能力：** 可读写

**起始版本：** 19

### var rotation

```cangjie
public var rotation: ImageRotation
```

**功能：** 图片旋转角度(默认0度，顺时针旋转)。

**类型：** [ImageRotation](#enum-imagerotation)

**读写能力：** 可读写

**起始版本：** 19

### init(QualityLevel, ImageRotation, Location, Bool)

```cangjie
public init(
    quality!: QualityLevel = QualityLevel.QUALITY_LEVEL_MEDIUM,
    rotation!: ImageRotation = ImageRotation.ROTATION_0,
    location!: Location = Location(-1.0, -1.0, -1.0),
    mirror!: Bool = false
)
```

**功能：** 创建PhoroCaptureSetting对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|quality|[QualityLevel](#enum-qualitylevel)|否|QualityLevel.QUALITY_LEVEL_MEDIUM| **命名参数。** 图片质量(默认低)。|
|rotation|[ImageRotation](#enum-imagerotation)|否|ImageRotation.ROTATION_0| **命名参数。** 图片质量(默认低)。|
|location|[Location](#struct-location)|否|Location(- 1.0, - 1.0, - 1.0)| **命名参数。** 图片地理位置信息(默认以设备硬件信息为准)。|
|mirror|Bool|否|false| **命名参数。** 镜像使能开关(默认关)。使用之前需要使用[isMirrorSupported](#func-ismirrorsupported)进行判断是否支持。|