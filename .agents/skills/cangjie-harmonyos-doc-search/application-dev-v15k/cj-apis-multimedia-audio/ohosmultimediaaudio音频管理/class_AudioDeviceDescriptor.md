## class AudioDeviceDescriptor

```cangjie
public class AudioDeviceDescriptor {}
```

**功能：** 描述音频设备。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### prop address

```cangjie
public prop address: String
```

**功能：** 设备地址。

如果是蓝牙设备，需要申请权限ohos.permission.USE_BLUETOOTH。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### prop channelCounts

```cangjie
public prop channelCounts: Array<Int32>
```

**功能：** 支持的通道数。

**类型：** Array\<Int32>

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### prop channelMasks

```cangjie
public prop channelMasks: Array<Int32>
```

**功能：** 支持的通道掩码。

**类型：** Array\<Int32>

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### prop deviceRole

```cangjie
public prop deviceRole: DeviceRole
```

**功能：** 设备角色。

**类型：** [DeviceRole](#enum-devicerole)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### prop deviceType

```cangjie
public prop deviceType: DeviceType
```

**功能：** 设备类型。

**类型：** [DeviceType](#enum-devicetype)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### prop displayName

```cangjie
public prop displayName: String
```

**功能：** 设备显示名。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### prop encodingTypes

```cangjie
public prop encodingTypes: ?Array<AudioEncodingType>
```

**功能：** 支持的编码类型。

**类型：** ?Array\<[AudioEncodingType](#enum-audioencodingtype)>

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### prop id

```cangjie
public prop id: Int32
```

**功能：** 设备id，唯一。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### prop name

```cangjie
public prop name: String
```

**功能：** 设备名称。

如果是蓝牙设备，需要申请权限ohos.permission.USE_BLUETOOTH。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### prop sampleRates

```cangjie
public prop sampleRates: Array<Int32>
```

**功能：** 支持的采样率。

**类型：** Array\<Int32>

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19