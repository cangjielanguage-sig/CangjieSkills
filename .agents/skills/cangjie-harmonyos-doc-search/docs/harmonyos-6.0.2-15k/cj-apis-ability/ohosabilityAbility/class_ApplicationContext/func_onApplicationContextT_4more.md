### func on(ApplicationContextType, ApplicationStateChangeCallback)

```cangjie
public func on(onType: ApplicationContextType, callback: ApplicationStateChangeCallback): Unit
```

**功能：** 注册对当前应用前后台变化的监听。使用callback异步回调。仅支持主线程调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onType|[ApplicationContextType](#enum-applicationcontexttype)|是|-|监听事件的类型。|
|callback|[ApplicationStateChangeCallback](#class-applicationstatechangecallback)|是|-|回调函数。可以对应用从后台切换到前台，以及前台切换到后台分别定义回调。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|

### func restartApp(Want)

```cangjie
public func restartApp(want: Want): Unit
```

**功能：** 应用重启并拉起自身指定UIAbility。重启时不会收到onDestroy回调。仅支持主线程调用，且待重启的应用需要处于获焦状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|want|[Want](#class-want)|是|-| Want类型参数，传入需要启动的Ability的信息，Bundle名称不做校验。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |16000050|Internal error.|
  |16000053|The ability is not on the top of the UI.|
  |16000063|The target to restart does not belong to the current application or is not a UIAbility.|
  |16000064|Restart too frequently. Try again at least 10s later.|

### func setColorMode(ConfigurationColorMode)

```cangjie
public func setColorMode(colorMode: ConfigurationColorMode): Unit
```

**功能：** 设置应用的颜色模式。仅支持主线程调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|colorMode|[ConfigurationColorMode](#enum-configurationcolormode)|是|-|设置颜色模式，包括：深色模式、浅色模式、不设置（跟随系统）。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |16000011|The context does not exist.|

### func setFont(String)

```cangjie
public func setFont(font: String): Unit
```

**功能：** 设置应用的字体类型。仅支持主线程调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|font|String|是|-|设置字体类型，字体可以通过registerFont方法进行注册使用。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |16000011|The context does not exist.|
  |16000050|Internal error.|