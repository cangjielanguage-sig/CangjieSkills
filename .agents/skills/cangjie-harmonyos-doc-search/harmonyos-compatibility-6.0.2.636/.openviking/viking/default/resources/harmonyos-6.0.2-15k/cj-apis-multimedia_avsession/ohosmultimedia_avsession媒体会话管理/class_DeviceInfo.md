## class DeviceInfo

```cangjie
public class DeviceInfo {
    public DeviceInfo (
        public var castCategory: AVCastCategory,
        public var deviceId: String,
        public var deviceName: String,
        public var deviceType: DeviceType,
        public var supportedProtocols: ?Array<ProtocolType>,
        public var supportedDrmCapabilities: ?Array<String>
    )
    public init(castCategory: AVCastCategory, deviceId: String, deviceName: String, deviceType: DeviceType)
}
```

**功能：** 播放设备的相关信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

### var castCategory

```cangjie
public var castCategory: AVCastCategory
```

**功能：** 投播的类别。

**类型：** [AVCastCategory](#enum-avcastcategory)

**读写能力：** 可读写

**起始版本：** 19

### var deviceId

```cangjie
public var deviceId: String
```

**功能：** 播放设备的ID。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var deviceName

```cangjie
public var deviceName: String
```

**功能：** 播放设备的名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var deviceType

```cangjie
public var deviceType: DeviceType
```

**功能：** 播放设备的类型。

**类型：** [DeviceType](#enum-devicetype)

**读写能力：** 可读写

**起始版本：** 19

### var supportedDrmCapabilities

```cangjie
public var supportedDrmCapabilities: ?Array<String>
```

**功能：** 播放设备支持的DRM能力。

**类型：** ?Array\<String>

**读写能力：** 可读写

**起始版本：** 19

### var supportedProtocols

```cangjie
public var supportedProtocols: ?Array<ProtocolType>
```

**功能：** 播放设备支持的协议。默认为TYPE_LOCAL。具体取值参考[ProtocolType](#enum-protocoltype)。

**类型：** ?Array\<[ProtocolType](#enum-protocoltype)>

**读写能力：** 可读写

**起始版本：** 19

### DeviceInfo(AVCastCategory, String, String, DeviceType, ?Array\<ProtocolType>, ?Array\<String>)

```cangjie
public DeviceInfo (
    public var castCategory: AVCastCategory,
    public var deviceId: String,
    public var deviceName: String,
    public var deviceType: DeviceType,
    public var supportedProtocols: ?Array<ProtocolType>,
    public var supportedDrmCapabilities: ?Array<String>
)
```

**功能：** [DeviceInfo](#class-deviceinfo)构造函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|castCategory|[AVCastCategory](#enum-avcastcategory)|是|-|投播的类别。|
|deviceId|String|是|-|播放设备的ID。|
|deviceName|String|是|-|播放设备的名称。|
|deviceType|[DeviceType](#enum-devicetype)|是|-|播放设备的类型。|
|supportedProtocols|?Array\<[ProtocolType](#enum-protocoltype)>|是|-|播放设备支持的协议。默认为TYPE_LOCAL。具体取值参考ProtocolType。|
|supportedDrmCapabilities|?Array\<String>|是|-|播放设备支持的DRM能力。|

### init(AVCastCategory, String, String, DeviceType)

```cangjie
public init(castCategory: AVCastCategory, deviceId: String, deviceName: String, deviceType: DeviceType)
```

**功能：** [DeviceInfo](#class-deviceinfo)构造函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|castCategory|[AVCastCategory](#enum-avcastcategory)|是|-|投播的类别。|
|deviceId|String|是|-|播放设备的ID。|
|deviceName|String|是|-|播放设备的名称。|
|deviceType|[DeviceType](#enum-devicetype)|是|-|播放设备的类型。|