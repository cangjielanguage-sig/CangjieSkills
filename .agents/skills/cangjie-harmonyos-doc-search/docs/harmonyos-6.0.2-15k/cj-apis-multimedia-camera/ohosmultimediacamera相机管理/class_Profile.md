## class Profile

```cangjie
public open class Profile {
    public let format: CameraFormat
    public let size: Size
}
```

**功能：** 相机配置信息项。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### let format

```cangjie
public let format: CameraFormat
```

**功能：** 输出格式。

**类型：** [CameraFormat](#enum-cameraformat)

**读写能力：** 只读

**起始版本：** 19

### let size

```cangjie
public let size: Size
```

**功能：** 分辨率。设置的是相机分辨率宽高，非实际出图宽高。

**类型：** [Size](#struct-size)

**读写能力：** 只读

**起始版本：** 19