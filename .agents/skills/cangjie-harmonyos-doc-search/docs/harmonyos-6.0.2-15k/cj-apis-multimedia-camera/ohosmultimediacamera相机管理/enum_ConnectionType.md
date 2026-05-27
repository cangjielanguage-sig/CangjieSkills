## enum ConnectionType

```cangjie
public enum ConnectionType <: Equatable<ConnectionType> & ToString {
    | CAMERA_CONNECTION_BUILT_IN
    | CAMERA_CONNECTION_USB_PLUGIN
    | CAMERA_CONNECTION_REMOTE
    | ...
}
```

**功能：** 相机连接类型。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- Equatable\<ConnectionType>
- ToString

### CAMERA_CONNECTION_BUILT_IN

```cangjie
CAMERA_CONNECTION_BUILT_IN
```

**功能：** 内置相机。

**起始版本：** 19

### CAMERA_CONNECTION_REMOTE

```cangjie
CAMERA_CONNECTION_REMOTE
```

**功能：** 远程连接的相机。

**起始版本：** 19

### CAMERA_CONNECTION_USB_PLUGIN

```cangjie
CAMERA_CONNECTION_USB_PLUGIN
```

**功能：** USB连接的相机。

**起始版本：** 19

### func !=(ConnectionType)

```cangjie
public operator func !=(other: ConnectionType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ConnectionType](#enum-connectiontype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ConnectionType)

```cangjie
public operator func ==(other: ConnectionType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ConnectionType](#enum-connectiontype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|