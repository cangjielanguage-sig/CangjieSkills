## class GattService

```cangjie
public class GattService {
    public var serviceUUID: String
    public var isPrimary: Bool
    public var characteristics: Array<BleCharacteristic>
    public var includeServices: Array<GattService>
    public init(
        serviceUUID: String,
        isPrimary: Bool,
        characteristics: Array<BleCharacteristic>,
        includeServices!: Array<GattService> = []
    )
}
```

**功能：** GATT服务结构定义，可包含多个特征值[BleCharacteristic](#class-blecharacteristic)和依赖的其他服务。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var characteristics

```cangjie
public var characteristics: Array<BleCharacteristic>
```

**功能：** 当前服务包含的特征值列表。

**类型：** Array\<[BleCharacteristic](#class-blecharacteristic)>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var includeServices

```cangjie
public var includeServices: Array<GattService>
```

**功能：** 当前服务依赖的其它服务。

**类型：** Array\<[GattService](#class-gattservice)>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var isPrimary

```cangjie
public var isPrimary: Bool
```

**功能：** 是否是主服务。true表示是主服务，false表示是次要服务。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var serviceUUID

```cangjie
public var serviceUUID: String
```

**功能：** 服务UUID，标识一个GATT服务。例如：00001888-0000-1000-8000-00805f9b34fb。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### init(String, Bool, Array\<BleCharacteristic>, Array\<GattService>)

```cangjie
public init(
    serviceUUID: String,
    isPrimary: Bool,
    characteristics: Array<BleCharacteristic>,
    includeServices!: Array<GattService> = []
)
```

**功能：** GattService 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|serviceUUID|String|是|-|服务UUID，标识一个GATT服务。例如：00001888-0000-1000-8000-00805f9b34fb。|
|isPrimary|Bool|是|-|是否是主服务。true表示是主服务，false表示是次要服务。|
|characteristics|Array\<[BleCharacteristic](#class-blecharacteristic)>|是|-|当前服务包含的特征值列表。|
|includeServices|Array\<[GattService](#class-gattservice)>|否|[]|**命名参数。** 当前服务依赖的其它服务。|