## class AdvertisingStateChangeInfo

```cangjie
public class AdvertisingStateChangeInfo {
    public var advertisingId: Int32
    public var state: AdvertisingState
}
```

**功能：** 描述BLE广播启动、停止的状态信息。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var advertisingId

```cangjie
public var advertisingId: Int32
```

**功能：** 首次启动广播时会分配该值，后续用于标识当前操作的广播。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var state

```cangjie
public var state: AdvertisingState
```

**功能：** 操作广播后，收到的BLE广播状态。

**类型：** [AdvertisingState](#enum-advertisingstate)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22