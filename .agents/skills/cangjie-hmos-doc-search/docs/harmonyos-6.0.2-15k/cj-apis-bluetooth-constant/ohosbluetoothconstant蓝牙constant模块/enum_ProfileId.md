## enum ProfileId

```cangjie
public enum ProfileId <: Equatable<ProfileId> & ToString {
    | PROFILE_A2DP_SOURCE
    | PROFILE_HANDSFREE_AUDIO_GATEWAY
    | PROFILE_HID_HOST
    | PROFILE_PAN_NETWORK
    | ...
}
```

**功能：** 蓝牙 profile id类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<ProfileId>
- ToString

### PROFILE_A2DP_SOURCE

```cangjie
PROFILE_A2DP_SOURCE
```

**功能：** 表示A2DP profile。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### PROFILE_HANDSFREE_AUDIO_GATEWAY

```cangjie
PROFILE_HANDSFREE_AUDIO_GATEWAY
```

**功能：** 表示HFP profile。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### PROFILE_HID_HOST

```cangjie
PROFILE_HID_HOST
```

**功能：** 表示HID profile。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### PROFILE_PAN_NETWORK

```cangjie
PROFILE_PAN_NETWORK
```

**功能：** 表示PAN profile。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(ProfileId)

```cangjie
public operator func !=(other: ProfileId): Bool
```

**功能：** 对蓝牙 profile 进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[ProfileId](#enum-profileid)|是|蓝牙 profile。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果蓝牙 profile 不同返回 true，否则返回 false。|

### func ==(ProfileId)

```cangjie
public operator func ==(other: ProfileId): Bool
```

**功能：** 对蓝牙 profile 进行判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[ProfileId](#enum-profileid)|是|蓝牙 profile。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果蓝牙 profile 相同返回 true，否则返回 false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回蓝牙 profile 的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|蓝牙 profile 的字符串表示。|