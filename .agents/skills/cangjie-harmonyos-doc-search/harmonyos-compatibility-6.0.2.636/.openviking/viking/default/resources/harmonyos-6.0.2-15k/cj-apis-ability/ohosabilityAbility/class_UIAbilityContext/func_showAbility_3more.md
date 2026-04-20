### func showAbility()

```cangjie
public func showAbility(): Unit
```

**功能：** 显示当前UIAbility。仅在2in1和tablet设备上生效。仅支持在主线程调用。调用此接口前要求确保应用已添加至状态栏。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not support.|
  |16000050|Internal error.|
  |16000067|The StartOptions check failed.|

### func startAbility(Want)

```cangjie
public func startAbility(want: Want): Future<Unit>
```

**功能：** 携带启动参数，启动Ability。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|want|[Want](#class-want)|是|-|启动Ability的want信息。|

### func startAbility(Want, StartOptions)

```cangjie
public func startAbility(want: Want, options: StartOptions): Future<Unit>
```

**功能：** 携带启动参数，启动Ability。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|want|[Want](#class-want)|是|-|启动Ability的want信息。|
|options|[StartOptions](#class-startoptions)|是|-|启动Ability所携带的参数。|