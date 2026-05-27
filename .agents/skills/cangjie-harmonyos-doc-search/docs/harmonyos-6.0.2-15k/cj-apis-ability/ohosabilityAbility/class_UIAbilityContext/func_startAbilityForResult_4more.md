### func startAbilityForResult(Want, AsyncCallback\<AbilityResult>)

```cangjie
public func startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): Unit
```

**功能：** 启动Ability并在该Ability退出的时候返回执行结果（callback形式）。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

| 参数名  | 类型   | 必填 | 说明 |
| :------- | :------ | :---- | :---- |
| want | [Want](#class-want) |  是 |   启动Ability的want信息。|
| callback | [AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<[AbilityResult](#struct-abilityresult)> |  是 |   执行结果回调函数。|

### func startAbilityForResult(Want, StartOptions, AsyncCallback\<AbilityResult>)

```cangjie
public func startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): Unit
```

**功能：** 启动Ability并在该Ability退出的时候返回执行结果（callback形式）。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

| 参数名  | 类型   | 必填 | 说明 |
| :------- | :------ | :---- | :---- |
| want | [Want](#class-want) |  是 |  启动Ability的want信息。|
| options | [StartOptions](#class-startoptions) |  是 |   启动Ability所携带的参数。|
| callback | [AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<[AbilityResult](#struct-abilityresult)> |  是 |   执行结果回调函数。|

### func terminateSelf()

```cangjie
public func terminateSelf(): Future<Unit>
```

**功能：** 停止UIAbility自身。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**返回值：**

| 类型       | 说明                       |
| :----------| :-------------------------- |
| Future\<Unit> | Future对象可以获取thread的结果。 |

### func terminateSelfWithResult(AbilityResult)

```cangjie
public func terminateSelfWithResult(parameter: AbilityResult): Future<Unit>
```

**功能：** 停止UIAbility，配合startAbilityForResult使用，返回给接口调用方AbilityResult信息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|parameter|[AbilityResult](#struct-abilityresult)|是|-|停止Ability，配合startAbilityForResult使用，返回给接口调用方AbilityResult信息。|

**返回值：**

| 类型       | 说明                       |
| :----------| :-------------------------- |
| Future\<Unit> | Future对象可以获取thread的结果。|