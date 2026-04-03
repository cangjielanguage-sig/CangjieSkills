## class TorchStatusInfo

```cangjie
public class TorchStatusInfo {
    public let isTorchAvailable: Bool
    public let isTorchActive: Bool
    public let torchLevel: Float64
}
```

**功能：** 手电筒回调返回的接口实例，表示手电筒状态信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### let isTorchActive

```cangjie
public let isTorchActive: Bool
```

**功能：** 手电筒是否被激活。true表示手电筒被激活，false表示手电筒未被激活。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### let isTorchAvailable

```cangjie
public let isTorchAvailable: Bool
```

**功能：** 手电筒是否可用。true表示手电筒可用，false表示手电筒不可用。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### let torchLevel

```cangjie
public let torchLevel: Float64
```

**功能：** 手电筒亮度等级。取值范围为[0.0,1.0]，越靠近1，亮度越大。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22