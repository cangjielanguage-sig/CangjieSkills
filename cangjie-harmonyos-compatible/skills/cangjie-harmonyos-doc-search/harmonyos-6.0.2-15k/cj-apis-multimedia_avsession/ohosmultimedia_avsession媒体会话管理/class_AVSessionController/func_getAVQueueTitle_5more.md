### func getAVQueueTitle()

```cangjie
public func getAVQueueTitle(): String
```

**功能：** 获取当前会话播放列表的名称。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回播放列表名称。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|
  |6600103|The session controller does not exist.|

### func getCallMetadata()

```cangjie
public func getCallMetadata(): CallMetadata
```

**功能：** 获取通话会话的元数据。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[CallMetadata](#class-callmetadata)|会话元数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|
  |6600103|The session controller does not exist.|

### func getExtras()

```cangjie
public func getExtras(): HashMap<String, ValueType>
```

**功能：** 获取媒体提供方设置的自定义媒体数据包。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|HashMap\<String, [ValueType](#enum-valuetype)>|回媒体提供方设置的自定义媒体数据包，数据包的内容与[setExtras](#func-setextrashashmapstring-valuetype)设置的内容完全一致。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|
  |6600103|The session controller does not exist.|
  |6600105|Invalid session command.|
  |6600107|Too many commands or events.|

### func getLaunchAbility()

```cangjie
public func getLaunchAbility(): WantAgent
```

**功能：** 获取应用在会话中保存的[WantAgent](../AbilityKit/cj-apis-ability.md#class-wantagent)对象。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[WantAgent](../AbilityKit/cj-apis-ability.md#class-wantagent)|[setLaunchAbility](#func-setlaunchabilitywantagent)保存的对象，包括应用的相关属性信息，如bundleName，abilityName，deviceId等。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|
  |6600103|The session controller does not exist.|

### func getOutputDevice()

```cangjie
public func getOutputDevice(): OutputDeviceInfo
```

**功能：** 获取当前输出设备信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[OutputDeviceInfo](#class-outputdeviceinfo)|当前输出设备信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600103|The session controller does not exist.|