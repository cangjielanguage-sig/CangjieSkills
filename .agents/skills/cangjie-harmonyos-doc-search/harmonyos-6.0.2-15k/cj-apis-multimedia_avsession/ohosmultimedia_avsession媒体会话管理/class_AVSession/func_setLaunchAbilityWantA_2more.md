### func setLaunchAbility(WantAgent)

```cangjie
public func setLaunchAbility(ability: WantAgent): Unit
```

**功能：** 设置一个[WantAgent](../AbilityKit/cj-apis-ability.md#class-wantagent)用于拉起会话的Ability。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|ability|[WantAgent](../AbilityKit/cj-apis-ability.md#class-wantagent)|是|-|应用的相关属性信息，如bundleName，abilityName，deviceId等。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|

### func stopCasting()

```cangjie
public func stopCasting(): Unit
```

**功能：** 结束投播。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600109|The remote connection is not established.|