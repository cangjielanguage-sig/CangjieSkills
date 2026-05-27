## class Reader

```cangjie
public class Reader {}
```

**功能：** Reader的实例表示该设备支持的SE，如果支持eSE和SIM，则返回两个实例。通过[SEService.getReaders](#func-getreaders)获取Reader实例。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

### func closeSessions()

```cangjie
public func closeSessions(): Unit
```

**功能：** 关闭在此Reader上打开的所有Session。所有这些Session打开的所有Channel都将关闭。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[SE错误码](../../errorcodes/cj-errorcode-secure_element.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|
  |3300101|IllegalStateError, service state exception.|

### func getName()

```cangjie
public func getName(): String
```

**功能：** 返回此Reader的名称。如果此读卡器是SIM Reader，则其名称必须为“SIM”。如果读卡器是eSE，则其名称须为“eSE”。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|[Reader](#class-reader)名称。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|

### func isSecureElementPresent()

```cangjie
public func isSecureElementPresent(): Bool
```

**功能：** 检查当前Reader所对应的安全单元是否可用。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true: 安全单元可用， false: 安全单元不可用。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[SE错误码](../../errorcodes/cj-errorcode-secure_element.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|
  |3300101|IllegalStateError, service state exception.|

### func openSession()

```cangjie
public func openSession(): Session
```

**功能：** 在SE Reader实例上创建连接会话，返回Session实例。在一个Reader上可能同时打开多个会话。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[Session](#class-session)|连接会话Session实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[SE错误码](../../errorcodes/cj-errorcode-secure_element.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|
  |3300101|IllegalStateError, service state exception.|
  |3300104|IOError, there is a communication problem to the reader or the SE.|