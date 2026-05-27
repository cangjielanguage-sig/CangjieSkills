## class GattService

```cangjie
public class GattService {
    public GattService(
        public var serviceUuid: String,
        public var isPrimary: Bool,
        public var characteristics: Array<BLECharacteristic>,
        public var includeServices: Array<GattService>
    )
}
```

**功能：** 描述service的接口参数定义。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### var characteristics

```cangjie
public var characteristics: Array<BLECharacteristic>
```

**功能：** 当前服务包含的特征列表。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Array\<[BLECharacteristic](#class-blecharacteristic)>

**读写能力：** 可读写

**起始版本：** 19

### var includeServices

```cangjie
public var includeServices: Array<GattService>
```

**功能：** 当前服务依赖的其它服务。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Array\<[GattService](#class-gattservice)>

**读写能力：** 可读写

**起始版本：** 19

### var isPrimary

```cangjie
public var isPrimary: Bool
```

**功能：** 特如果是主服务设置为true，否则设置为false。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var serviceUuid

```cangjie
public var serviceUuid: String
```

**功能：** 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### GattService(String, Bool, Array\<BLECharacteristic>, Array\<GattService>)

```cangjie
public GattService(
    public var serviceUuid: String,
    public var isPrimary: Bool,
    public var characteristics: Array<BLECharacteristic>,
    public var includeServices: Array<GattService>
)
```

**功能：** GattService 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|serviceUuid|String|是|特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。|
|isPrimary|Bool|是|如果是主服务设置为true，否则设置为false。|
|characteristics|Array\<[BLECharacteristic](#class-blecharacteristic)>|是|当前服务包含的特征列表。|
|includeServices|Array\<[GattService](#class-gattservice)>|是|当前服务依赖的其它服务。|