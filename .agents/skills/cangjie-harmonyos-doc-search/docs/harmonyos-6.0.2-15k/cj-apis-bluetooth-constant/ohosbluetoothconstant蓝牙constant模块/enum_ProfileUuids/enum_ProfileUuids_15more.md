## enum ProfileUuids

```cangjie
public enum ProfileUuids <: ToString & Equatable<ProfileUuids> {
    | PROFILE_UUID_HFP_AG
    | PROFILE_UUID_HFP_HF
    | PROFILE_UUID_HSP_AG
    | PROFILE_UUID_HSP_HS
    | PROFILE_UUID_A2DP_SRC
    | PROFILE_UUID_A2DP_SINK
    | PROFILE_UUID_AVRCP_CT
    | PROFILE_UUID_AVRCP_TG
    | PROFILE_UUID_HID
    | PROFILE_UUID_HOGP
    | PROFILE_UUID_UNKNOWN
    | ...
}
```

**功能：** 表示不同类型 Profile 的 UUID。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<ProfileUuids>

### PROFILE_UUID_A2DP_SINK

```cangjie
PROFILE_UUID_A2DP_SINK
```

**功能：** 代表A2DPSINK Profile的UUID。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### PROFILE_UUID_A2DP_SRC

```cangjie
PROFILE_UUID_A2DP_SRC
```

**功能：** 代表A2DPSRC Profile的UUID。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### PROFILE_UUID_AVRCP_CT

```cangjie
PROFILE_UUID_AVRCP_CT
```

**功能：** 代表AVRCPCT Profile的UUID。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### PROFILE_UUID_AVRCP_TG

```cangjie
PROFILE_UUID_AVRCP_TG
```

**功能：** 代表AVRCPTG Profile的UUID。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### PROFILE_UUID_HFP_AG

```cangjie
PROFILE_UUID_HFP_AG
```

**功能：** 代表HFPAG Profile的UUID。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### PROFILE_UUID_HFP_HF

```cangjie
PROFILE_UUID_HFP_HF
```

**功能：** 代表HFPHF Profile的UUID。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### PROFILE_UUID_HID

```cangjie
PROFILE_UUID_HID
```

**功能：** 代表HID Profile的UUID。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### PROFILE_UUID_HOGP

```cangjie
PROFILE_UUID_HOGP
```

**功能：** 代表HOGP Profile的UUID。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### PROFILE_UUID_HSP_AG

```cangjie
PROFILE_UUID_HSP_AG
```

**功能：** 代表HSPAG Profile的UUID。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### PROFILE_UUID_HSP_HS

```cangjie
PROFILE_UUID_HSP_HS
```

**功能：** 代表HSPHS Profile的UUID。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### PROFILE_UUID_UNKNOWN

```cangjie
PROFILE_UUID_UNKNOWN
```

**功能：** 代表暂未定义的UUID。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(ProfileUuids)

```cangjie
public operator func !=(other: ProfileUuids): Bool
```

**功能：** 对 Profile 的 UUID 判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[ProfileUuids](#enum-profileuuids)|是|Profile 的 UUID。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果 Profile 的 UUID 不同返回 true，否则返回 false。|

### func ==(ProfileUuids)

```cangjie
public operator func ==(other: ProfileUuids): Bool
```

**功能：** 对 Profile 的 UUID 进行判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[ProfileUuids](#enum-profileuuids)|是|Profile 的 UUID。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果 Profile 的 UUID 相同返回 true，否则返回 false。|

### func toString()

```cangjie
public override func toString(): String
```

**功能：** 返回 Profile 的 UUID 的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|Profile 的 UUID 的字符串表示。|