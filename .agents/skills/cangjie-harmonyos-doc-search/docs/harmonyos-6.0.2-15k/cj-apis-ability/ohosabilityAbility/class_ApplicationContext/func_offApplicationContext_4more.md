### func off(ApplicationContextType, Int32)

```cangjie
public func off(onType: ApplicationContextType, callbackId: Int32): Unit
```

**功能：** 取消对系统环境变化的监听。仅支持主线程调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onType|[ApplicationContextType](#enum-applicationcontexttype)|是|-|监听事件的类型。|
|callbackId|Int32|是|-|注册监听系统环境变化的ID。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|

### func off(ApplicationContextType, ?ApplicationStateChangeCallback)

```cangjie
public func off(onType: ApplicationContextType, callback!: ?ApplicationStateChangeCallback = None): Unit
```

**功能：** 取消当前应用注册的前后台变化的全部监听。仅支持主线程调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onType|[ApplicationContextType](#enum-applicationcontexttype)|是|-|监听事件的类型。|
|callback|?[ApplicationStateChangeCallback](#class-applicationstatechangecallback)|否|None| **命名参数。** 回调函数。可以对应用从后台切换到前台，以及前台切换到后台分别定义回调。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|

### func on(ApplicationContextType, EnvironmentCallback)

```cangjie
public func on(onType: ApplicationContextType, callback: EnvironmentCallback): Int32
```

**功能：** 注册对系统环境变化的监听。使用callback异步回调。仅支持主线程调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onType|[ApplicationContextType](#enum-applicationcontexttype)|是|-|监听事件的类型。|
|callback|[EnvironmentCallback](#class-environmentcallback)|是|-|回调方法，提供应用上下文ApplicationContext对系统环境变量监听回调的能力。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回的此次注册监听系统环境变化的ID（每次注册该ID会自增+1，当超过监听上限数量2^32-1时，返回-1）。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|

### func on(ApplicationContextType, AbilityLifecycleCallback)

```cangjie
public func on(onType: ApplicationContextType, callback: AbilityLifecycleCallback): Int32
```

**功能：** 注册监听应用内生命周期。使用callback异步回调。仅支持主线程调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onType|[ApplicationContextType](#enum-applicationcontexttype)|是|-|监听事件的类型。|
|callback|[AbilityLifecycleCallback](#class-abilitylifecyclecallback)|是|-|回调方法。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回的此次注册监听系统环境变化的ID（每次注册该ID会自增+1，当超过监听上限数量2^32-1时，返回-1）。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|