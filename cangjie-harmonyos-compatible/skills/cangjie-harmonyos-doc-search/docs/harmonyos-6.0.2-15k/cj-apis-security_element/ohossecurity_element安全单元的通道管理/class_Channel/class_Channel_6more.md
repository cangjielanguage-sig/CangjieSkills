## class Channel

```cangjie
public class Channel {}
```

**功能：** Channel的实例表示在某个Session实例上创建通道，可能为基础通道或逻辑通道。通过[Session.openBasicChannel](#func-openbasicchannelarrayint32)或[Session.openLogicalChannel](#func-openbasicchannelarrayint32)获取Channel实例。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

### func close()

```cangjie
public func close(): Unit
```

**功能：** 关闭Channel。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|

### func getSelectResponse()

```cangjie
public func getSelectResponse(): Array<Int32>
```

**功能：** 获取SELECT Applet时的响应数据，包含状态字。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Int32>|SELECT Applet时的响应数据，包含状态字。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|

### func getSession()

```cangjie
public func getSession(): Session
```

**功能：** 获取打开该Channel的Session对象。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[Session](#class-session)|该Channel绑定的Session 对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|

### func isBasicChannel()

```cangjie
public func isBasicChannel(): Bool
```

**功能：** 检查该Channel是否为基础Channel。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true: 该Channel是基础Channel, false：该Channel逻辑Channel。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|

### func isClosed()

```cangjie
public func isClosed(): Bool
```

**功能：** 检查该Channel是否已被关闭。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true: Channel是关闭的，false: 不是关闭的。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|