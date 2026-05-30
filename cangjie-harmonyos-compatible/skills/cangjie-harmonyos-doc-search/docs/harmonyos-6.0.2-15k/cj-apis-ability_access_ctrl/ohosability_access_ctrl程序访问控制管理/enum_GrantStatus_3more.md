## enum GrantStatus

```cangjie
public enum GrantStatus <: Equatable<GrantStatus> & ToString {
    | PERMISSION_DENIED
    | PERMISSION_GRANTED
    | ...
}
```

**功能：** 表示授权状态。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 12

**父类型：**

- Equatable\<GrantStatus>
- ToString

### PERMISSION_DENIED

```cangjie
PERMISSION_DENIED
```

**功能：** 未授权。

**起始版本：** 12

### PERMISSION_GRANTED

```cangjie
PERMISSION_GRANTED
```

**功能：** 已授权。

**起始版本：** 12

### operator func !=(GrantStatus)

```cangjie
public operator func !=(other: GrantStatus): Bool
```

**功能：** 对授权状态进行判不等。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[GrantStatus](#enum-grantstatus)|是|-|授权状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果授权状态不同，返回true，否则返回false。|

### operator func ==(GrantStatus)

```cangjie
public operator func ==(other: GrantStatus): Bool
```

**功能：** 对授权状态进行判等。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[GrantStatus](#enum-grantstatus)|是|-|授权状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果授权状态相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回授权状态的字符串表示。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|授权状态的字符串表示。|

## enum SwitchType

```cangjie
public enum SwitchType <: Equatable<SwitchType> & ToString {
    | CAMERA
    | MICROPHONE
    | LOCATION
    | ...
}
```

**功能：** 表示全局开关类型。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 19

**父类型：**

- Equatable\<SwitchType>
- ToString

### CAMERA

```cangjie
CAMERA
```

**功能：** 相机全局开关。

**起始版本：** 19

### LOCATION

```cangjie
LOCATION
```

**功能：** 位置全局开关。

**起始版本：** 19

### MICROPHONE

```cangjie
MICROPHONE
```

**功能：** 麦克风全局开关。

**起始版本：** 19

### operator func !=(SwitchType)

```cangjie
public operator func !=(other: SwitchType): Bool
```

**功能：** 对全局开关类型进行判不等。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SwitchType](#enum-switchtype)|是|-|全局开关类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果全局开关类型不同，返回true，否则返回false。|

### operator func ==(SwitchType)

```cangjie
public operator func ==(other: SwitchType): Bool
```

**功能：** 对全局开关类型进行判等。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SwitchType](#enum-switchtype)|是|-|全局开关类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果全局开关类型相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回全局开关类型的字符串表示。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|全局开关类型的字符串表示。|

## type Permissions

```cangjie
public type Permissions = String
```

**功能：** 权限名，为一个字符串。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 12