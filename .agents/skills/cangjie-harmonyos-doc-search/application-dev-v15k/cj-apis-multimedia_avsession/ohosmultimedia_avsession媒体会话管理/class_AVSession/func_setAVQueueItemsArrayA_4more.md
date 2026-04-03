### func setAVQueueItems(Array\<AVQueueItem>)

```cangjie
public func setAVQueueItems(items: Array<AVQueueItem>): Unit
```

**功能：** 设置媒体播放列表。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|items|Array\<[AVQueueItem](#class-avqueueitem)>|是|-|播放列表单项的队列，用以表示播放列表。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|

### func setAVQueueTitle(String)

```cangjie
public func setAVQueueTitle(title: String): Unit
```

**功能：** 设置媒体播放列表名称。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|String|是|-|播放列表的名称。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|

### func setCallMetadata(CallMetadata)

```cangjie
public func setCallMetadata(data: CallMetadata): Unit
```

**功能：** 设置通话会话元数据。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|[CallMetadata](#class-callmetadata)|是|-|通话会话元数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|

### func setExtras(HashMap\<String, ValueType>)

```cangjie
public func setExtras(extras: HashMap<String, ValueType>): Unit
```

**功能：** 媒体提供方设置键值对形式的自定义媒体数据包。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|extras|HashMap\<String, [ValueType](#enum-valuetype)>|是|-|需要传递的自定义媒体数据包键值对。ValueType支持STRING、INT32、FLOAT、BOOL、FD、ARRSTRING、ARRAYI32、ARRAYBOOL、ARRAYF64、ARRAYFD、HASH_MAP|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|

- IllegalArgumentException:

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |Unsupported ValueType.|传入不支持的[ValueType](#enum-valuetype)类型|检查传入[ValueType](#enum-valuetype)类型是否满足要求|