## class CameraDevice

```cangjie
public class CameraDevice {
    public let cameraId: String
    public let cameraPosition: CameraPosition
    public let cameraType: CameraType
    public let connectionType: ConnectionType
    public let cameraOrientation: UInt32
}
```

**功能：** 相机设备信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### let cameraId

```cangjie
public let cameraId: String
```

**功能：** 相机id。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let cameraOrientation

```cangjie
public let cameraOrientation: UInt32
```

**功能：** 镜头的安装角度，不会随着屏幕旋转而改变，取值范围为0-360。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let cameraPosition

```cangjie
public let cameraPosition: CameraPosition
```

**功能：** 相机位置。

**类型：** [CameraPosition](#enum-cameraposition)

**读写能力：** 只读

**起始版本：** 19

### let cameraType

```cangjie
public let cameraType: CameraType
```

**功能：** 相机类型。

**类型：** [CameraType](#enum-cameratype)

**读写能力：** 只读

**起始版本：** 19

### let connectionType

```cangjie
public let connectionType: ConnectionType
```

**功能：** 相机连接类型。

**类型：** [ConnectionType](#enum-connectiontype)

**读写能力：** 只读

**起始版本：** 19