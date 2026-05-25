## class Session

```cangjie
public class Session {}
```

**功能：** Session的实例表示在某个SE Reader实例上创建连接会话。通过[Reader.openSession](#func-opensession)获取Session实例。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

### func close()

```cangjie
public func close(): Unit
```

**功能：** 关闭与SE的当前会话连接。这将关闭此Session打开的所有Channel。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[SE错误码](../../errorcodes/cj-errorcode-secure_element.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|
  |3300101|IllegalStateError, service state exception.|

### func closeChannels()

```cangjie
public func closeChannels(): Unit
```

**功能：** 关闭此Session上打开的所有Channel。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[SE错误码](../../errorcodes/cj-errorcode-secure_element.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|
  |3300101|IllegalStateError, service state exception.|

### func getATR()

```cangjie
public func getATR(): Array<Int32>
```

**功能：** 获取该SE的ATR。如果该SE的ATR不可用，则应返回空数组。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Int32>|返回SE的ATR，SE的ATR不可用时，返回空的数组。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[SE错误码](../../errorcodes/cj-errorcode-secure_element.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|
  |3300101|IllegalStateError, service state exception.|

### func getReader()

```cangjie
public func getReader(): Reader
```

**功能：** 获取提供此Session的Reader实例。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[Reader](#class-reader)|返回此Session的Reader实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|

### func isClosed()

```cangjie
public func isClosed(): Bool
```

**功能：** 检查Session是否关闭。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true：Session状态已关闭，false：Session是打开的。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|