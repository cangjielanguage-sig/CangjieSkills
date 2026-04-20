## class SEService

```cangjie
public class SEService {}
```

**功能：** SEService表示可用于连接到系统中所有可用SE的连接（服务），通过[createService](#func-createservice)获取SEService实例。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

### func getReaders()

```cangjie
public func getReaders(): Array<Reader>
```

**功能：** 返回可用SE Reader的数组，包含该设备上支持的所有的安全单元。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[Reader](#class-reader)>|返回可用Reader对象数组。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|

### func getVersion()

```cangjie
public func getVersion(): String
```

**功能：** 返回此实现所基于的Open Mobile API规范的版本号。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|OMA版本号（例如，“3.3”表示Open Mobile API规范版本3.3）。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|

### func isConnected()

```cangjie
public func isConnected(): Bool
```

**功能：** 检查SE服务是否已连接。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true: SE服务状态已连接，false: SE服务状态已断开。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|

### func shutdown()

```cangjie
public func shutdown(): Unit
```

**功能：** 释放该Service分配的所有SE资源。此后[isConnected](#func-isconnected)将返回false。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|