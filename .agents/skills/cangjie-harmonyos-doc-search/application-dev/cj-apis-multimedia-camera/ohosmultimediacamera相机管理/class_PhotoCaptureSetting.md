## class PhotoCaptureSetting

```cangjie
public class PhotoCaptureSetting {
    public var quality: QualityLevel
    public var rotation: ImageRotation
    public var location:?Location
    public var mirror: Bool
    public init(
        quality!: QualityLevel = QualityLevel.QualityLevelLow,
        rotation!: ImageRotation = ImageRotation.Rotation0,
        location!: ?Location = None,
        mirror!: Bool = false
    )
}
```

**功能：** 拍摄照片的设置。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var location

```cangjie
public var location:?Location
```

**功能：** 图片地理位置信息。

**类型：** ?[Location](#class-location)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var mirror

```cangjie
public var mirror: Bool
```

**功能：** 镜像使能开关。使用之前需要使用[isMirrorSupported](#func-ismirrorsupported)进行判断是否支持。true表示使能，false表示不使能。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var quality

```cangjie
public var quality: QualityLevel
```

**功能：** 图片质量。

**类型：** [QualityLevel](#enum-qualitylevel)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var rotation

```cangjie
public var rotation: ImageRotation
```

**功能：** 图片旋转角度。

**类型：** [ImageRotation](#enum-imagerotation)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### init(QualityLevel, ImageRotation, ?Location, Bool)

```cangjie
public init(
    quality!: QualityLevel = QualityLevel.QualityLevelLow,
    rotation!: ImageRotation = ImageRotation.Rotation0,
    location!: ?Location = None,
    mirror!: Bool = false
)
```

**功能：** 创建PhoroCaptureSetting对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|quality|[QualityLevel](#enum-qualitylevel)|否|QualityLevel.QualityLevelLow|**命名参数。** 图片质量(默认低)。|
|rotation|[ImageRotation](#enum-imagerotation)|否|ImageRotation.Rotation0|**命名参数。** 图片旋转角度（默认0度，顺时针旋转）。|
|location|?[Location](#class-location)|否|None|**命名参数。** 图片地理位置信息(默认以设备硬件信息为准)。|
|mirror|Bool|否|false|**命名参数。** 镜像使能开关（默认关）。使用之前需要使用[isMirrorSupported](#func-ismirrorsupported)进行判断是否支持。true表示使能，false表示不使能。|