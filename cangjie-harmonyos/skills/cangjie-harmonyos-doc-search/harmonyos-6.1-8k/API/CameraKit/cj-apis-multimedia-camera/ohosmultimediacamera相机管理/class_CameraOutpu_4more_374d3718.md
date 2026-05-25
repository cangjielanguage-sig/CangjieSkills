## class CameraOutputCapability

```cangjie
public class CameraOutputCapability {
    public let previewProfiles: Array<Profile>
    public let photoProfiles: Array<Profile>
    public let videoProfiles: Array<VideoProfile>
    public let supportedMetadataObjectTypes: Array<MetadataObjectType>
}
```

**功能：** 相机输出能力项。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### let photoProfiles

```cangjie
public let photoProfiles: Array<Profile>
```

**功能：** 支持的拍照配置信息集合。

**类型：** Array\<[Profile](#class-profile)>

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### let previewProfiles

```cangjie
public let previewProfiles: Array<Profile>
```

**功能：** 支持的预览配置信息集合。

**类型：** Array\<[Profile](#class-profile)>

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### let supportedMetadataObjectTypes

```cangjie
public let supportedMetadataObjectTypes: Array<MetadataObjectType>
```

**功能：** 支持的metadata流类型信息集合。

**类型：** Array\<[MetadataObjectType](#enum-metadataobjecttype)>

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### let videoProfiles

```cangjie
public let videoProfiles: Array<VideoProfile>
```

**功能：** 支持的录像配置信息集合。

**类型：** Array\<[VideoProfile](#class-videoprofile)>

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

## class CameraStatusInfo

```cangjie
public class CameraStatusInfo {
    public var camera: CameraDevice
    public var status: CameraStatus
}
```

**功能：** 相机管理器回调返回的接口实例，该实例表示相机状态信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var camera

```cangjie
public var camera: CameraDevice
```

**功能：** 相机信息。

**类型：** [CameraDevice](#class-cameradevice)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var status

```cangjie
public var status: CameraStatus
```

**功能：** 相机状态。

**类型：** [CameraStatus](#enum-camerastatus)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

## class CaptureEndInfo

```cangjie
public class CaptureEndInfo {
    public var captureId: Int32
    public var frameCount: Int32
}
```

**功能：** 拍照停止信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var captureId

```cangjie
public var captureId: Int32
```

**功能：** 拍照的ID。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var frameCount

```cangjie
public var frameCount: Int32
```

**功能：** 帧数。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

## class CaptureStartInfo

```cangjie
public class CaptureStartInfo {
    public var captureId: Int32
    public var time: Int64
}
```

**功能：** 拍照开始信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var captureId

```cangjie
public var captureId: Int32
```

**功能：** 拍照的ID。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var time

```cangjie
public var time: Int64
```

**功能：** 预估的单次拍照底层出sensor采集帧时间，如果上报-1，代表没有预估时间。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22