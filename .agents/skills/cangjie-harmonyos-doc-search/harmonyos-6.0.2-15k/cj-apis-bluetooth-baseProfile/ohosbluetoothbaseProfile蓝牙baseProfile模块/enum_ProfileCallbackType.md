## enum ProfileCallbackType

```cangjie
public enum ProfileCallbackType <: Equatable<ProfileCallbackType> & Hashable & ToString {
    | CONNECTION_STATE_CHANGE
    | ...
}
```

**功能：** bluetooth baseprofile 回调事件。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<ProfileCallbackType>
- Hashable
- ToString

### CONNECTION_STATE_CHANGE

```cangjie
CONNECTION_STATE_CHANGE
```

**功能：** 表示连接状态变化事件类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(ProfileCallbackType)

```cangjie
public operator func !=(other: ProfileCallbackType): Bool
```

**功能：** 对bluetooth baseprofile 回调事件进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[ProfileCallbackType](#enum-profilecallbacktype)|是|bluetooth baseprofile 回调事件。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果bluetooth baseprofile 回调事件不同，返回true，否则返回false。|

### func ==(ProfileCallbackType)

```cangjie
public operator func ==(other: ProfileCallbackType): Bool
```

**功能：** 对bluetooth baseprofile 回调事件进行判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[ProfileCallbackType](#enum-profilecallbacktype)|是|bluetooth baseprofile 回调事件。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果bluetooth baseprofile 回调事件相同，返回true，否则返回false。|

### func hashCode()

```cangjie
public func hashCode(): Int64
```

**功能：** 获取回调事件的哈希值。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int64|回调事件的哈希值。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取回调事件类型的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|回调事件类型的字符串表示。|