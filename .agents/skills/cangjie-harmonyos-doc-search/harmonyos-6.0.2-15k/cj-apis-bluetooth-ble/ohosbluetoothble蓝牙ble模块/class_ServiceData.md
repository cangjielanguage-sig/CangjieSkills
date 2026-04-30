## class ServiceData

```cangjie
public class ServiceData {
    public ServiceData(
        public var serviceUuid: String,
        public var serviceValue: Array<Byte>
    )
}
```

**功能：** 描述广播包中服务数据内容。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### var serviceUuid

```cangjie
public var serviceUuid: String
```

**功能：** 表示服务的UUID。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var serviceValue

```cangjie
public var serviceValue: Array<Byte>
```

**功能：** 表示服务数据。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Array\<Byte>

**读写能力：** 可读写

**起始版本：** 19

### ServiceData(String, Array\<Byte>)

```cangjie
public ServiceData(
    public var serviceUuid: String,
    public var serviceValue: Array<Byte>
)
```

**功能：** ServiceData 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|serviceUuid|String|是|表示服务的UUID。|
|serviceValue|Array\<Byte>|是|表示服务数据。|