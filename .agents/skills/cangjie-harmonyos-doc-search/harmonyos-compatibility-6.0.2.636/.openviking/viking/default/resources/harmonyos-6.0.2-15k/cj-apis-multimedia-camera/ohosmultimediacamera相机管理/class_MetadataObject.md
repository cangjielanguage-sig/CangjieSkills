## class MetadataObject

```cangjie
public class MetadataObject {
    public let `type`: MetadataObjectType
    public let timestamp: Int32
    public let boundingBox: Rect
}
```

**功能：** 相机元能力信息，CameraInput相机信息中的数据来源。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### let \`type\`

```cangjie
public let `type`: MetadataObjectType
```

**功能：** metadata 类型。

**类型：** [MetadataObjectType](#enum-metadataobjecttype)

**读写能力：** 只读

**起始版本：** 19

### let boundingBox

```cangjie
public let boundingBox: Rect
```

**功能：** metadata 区域框。

**类型：** [Rect](#struct-rect)

**读写能力：** 只读

**起始版本：** 19

### let timestamp

```cangjie
public let timestamp: Int32
```

**功能：** 当前时间戳（毫秒）。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19