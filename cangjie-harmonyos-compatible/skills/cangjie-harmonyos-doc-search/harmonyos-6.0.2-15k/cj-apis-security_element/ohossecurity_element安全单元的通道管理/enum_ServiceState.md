## enum ServiceState

```cangjie
public enum ServiceState <: Equatable<ServiceState> & ToString {
    | DISCONNECTED
    | CONNECTED
    | ...
}
```

**功能：** 定义不同的SE服务状态值。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**父类型：**

- Equatable\<ServiceState>

### CONNECTED

```cangjie
CONNECTED
```

**功能：** SE服务状态已连接。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

### DISCONNECTED

```cangjie
DISCONNECTED
```

**功能：** SE服务状态已断开。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

### func !=(ServiceState)

```cangjie
public operator func !=(other: ServiceState): Bool
```

**功能：** 对SE服务状态值进行判不等。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[ServiceState](#enum-servicestate)|是|SE服务状态值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果SE服务状态值不同，返回true，否则返回false。|

### func ==(ServiceState)

```cangjie
public operator func ==(other: ServiceState): Bool
```

**功能：** 对SE服务状态值进行判等。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[ServiceState](#enum-servicestate)|是|SE服务状态值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果SE服务状态值相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回SE服务状态值的字符串表示。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|SE服务状态值的字符串表示。|