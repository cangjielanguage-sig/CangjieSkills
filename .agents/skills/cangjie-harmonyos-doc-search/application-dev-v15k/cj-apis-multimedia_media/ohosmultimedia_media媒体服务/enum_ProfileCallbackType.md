## enum ProfileCallbackType

```cangjie
public enum ProfileCallbackType <: Equatable<ProfileCallbackType> & Hashable & ToString {
    | CONNECTION_STATE_CHANGE
    | CONNECTION_ERROR
    | ...
}
```

**功能：** 连接管理。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

**父类型：**

- Equatable\<ProfileCallbackType>
- Hashable
- ToString

### CONNECTION_ERROR

```cangjie
CONNECTION_ERROR
```

**功能：** 连接无效。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

### CONNECTION_STATE_CHANGE

```cangjie
CONNECTION_STATE_CHANGE
```

**功能：** 连接状态。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

### func !=(ProfileCallbackType)

```cangjie
public operator func !=(other: ProfileCallbackType): Bool
```

**功能：** 对连接管理的枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ProfileCallbackType](#enum-profilecallbacktype)|是|-|连接管理类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个连接管理的枚举值不相等返回true，否则返回false。|

### func ==(ProfileCallbackType)

```cangjie
public operator func ==(other: ProfileCallbackType): Bool
```

**功能：** 对连接管理的枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ProfileCallbackType](#enum-profilecallbacktype)|是|-|连接管理类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个连接管理的枚举值相等返回true，否则返回false。|

### func hashCode()

```cangjie
public func hashCode(): Int64
```

**功能：** 获取连接管理类型的哈希值。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int64|连接管理类型的哈希值。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取连接管理的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|连接管理类型的字符串表示。|