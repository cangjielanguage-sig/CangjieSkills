## class AVSession

```cangjie
public class AVSession {
    public let sessionId: String
    public let sessionType: AVSessionType
}
```

**功能：** 调用[avSession.createAVSession](#func-createavsessioncpointerunit-string-avsessiontype)后，返回会话的实例，可以获得会话ID，完成设置元数据，播放状态信息等操作。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

### let sessionId

```cangjie
public let sessionId: String
```

**功能：** [AVSession](#class-avsession)对象唯一的会话标识。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let sessionType

```cangjie
public let sessionType: AVSessionType
```

**功能：** [AVSession](#class-avsession)会话类型。

**类型：** [AVSessionType](#enum-avsessiontype)

**读写能力：** 只读

**起始版本：** 19

### func activate()

```cangjie
public func activate(): Unit
```

**功能：** 激活会话，激活后可正常使用会话。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|

### func deactivate()

```cangjie
public func deactivate(): Unit
```

**功能：** 禁用当前会话的功能，可通过activate恢复。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|

### func destroy()

```cangjie
public func destroy(): Unit
```

**功能：** 销毁当前会话，使当前会话完全失效。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|

### func dispatchSessionEvent(String, HashMap\<String, ValueType>)

```cangjie
public func dispatchSessionEvent(event: String, args: HashMap<String, ValueType>): Unit
```

**功能：** 媒体提供方设置一个会话内自定义事件，包括事件名和键值对形式的事件内容。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|String|是|-|需要设置的会话事件的名称。|
|args|HashMap\<String, [ValueType](#enum-valuetype)>|是|-|需要传递的会话事件内容。注：参数args支持的数据类型有：字符串、数字、布尔、文件描述符及以上类型的数组。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|