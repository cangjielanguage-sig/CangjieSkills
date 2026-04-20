## struct TorchStatusInfo

```cangjie
public struct TorchStatusInfo {
    public let isTorchAvailable: Bool
    public let isTorchActive: Bool
    public let torchLevel: Float32
}
```

**功能：** 手电筒回调返回的接口实例，表示手电筒状态信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### let isTorchActive

```cangjie
public let isTorchActive: Bool
```

**功能：** 手电筒是否被激活。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let isTorchAvailable

```cangjie
public let isTorchAvailable: Bool
```

**功能：** 手电筒是否可用。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let torchLevel

```cangjie
public let torchLevel: Float32
```

**功能：** 手电筒亮度等级。取值范围为[0.0,1.0]，越靠近1，亮度越大。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 19