## enum ConnectionState

```cangjie
public enum ConnectionState <: Equatable<ConnectionState> & ToString {
    | STATE_CONNECTING
    | STATE_CONNECTED
    | STATE_DISCONNECTED
    | ...
}
```

**功能：** 连接状态枚举。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**父类型：**

- Equatable\<[ConnectionState](#enum-connectionstate)>
- ToString

### STATE_CONNECTED

```cangjie
STATE_CONNECTED
```

**功能：** 设备连接成功。

**起始版本：** 19

### STATE_CONNECTING

```cangjie
STATE_CONNECTING
```

**功能：** 设备连接中。

**起始版本：** 19

### STATE_DISCONNECTED

```cangjie
STATE_DISCONNECTED
```

**功能：** 设备断开连接。

**起始版本：** 19

### func !=(ConnectionState)

```cangjie
public operator func !=(other: ConnectionState): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ConnectionState](#enum-connectionstate)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(ConnectionState)

```cangjie
public operator func ==(other: ConnectionState): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ConnectionState](#enum-connectionstate)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表示。|