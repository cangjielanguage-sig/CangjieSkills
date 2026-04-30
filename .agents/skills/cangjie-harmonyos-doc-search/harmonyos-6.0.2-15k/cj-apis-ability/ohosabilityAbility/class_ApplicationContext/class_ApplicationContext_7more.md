## class ApplicationContext

```cangjie
public class ApplicationContext <: Context {}
```

**功能：** 提供应用级别的的上下文的能力。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**父类型：**

- [Context](#class-context)

### func clearUpApplicationData()

```cangjie
public func clearUpApplicationData(): Unit
```

**功能：** 清理应用本身的数据，同时撤销应用向用户申请的权限。仅支持主线程调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |16000011|The context does not exist.|
  |16000050|Internal error.|

### func getApplicationInfo()

```cangjie
public func getApplicationInfo(): ApplicationInfo
```

**功能：** 获取应用信息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[ApplicationInfo](./cj-apis-bundle_manager.md#struct-applicationinfo)|当前应用程序的信息。|

### func getArea()

```cangjie
public func getArea(): Int64
```

**功能：** 功能辅助函数，仅适用于UItest测试框架。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int64|文件分区信息。|

### func getCurrentAppCloneIndex()

```cangjie
public func getCurrentAppCloneIndex(): Int32
```

**功能：** 获取当前应用的分身索引。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|当前应用的分身索引。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |16000011|The context does not exist.|
  |16000071|The MultiAppMode is not {@link APP_CLONE}.|

### func getRunningProcessInformation()

```cangjie
public func getRunningProcessInformation(): Array<ProcessInformation>
```

**功能：** 获取当前运行进程的有关信息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[ProcessInformation](#class-processinformation)>|返回有关运行进程的信息，可进行错误处理或其他自定义处理。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |16000050|Internal error.|

### func killAllProcesses(Bool)

```cangjie
public func killAllProcesses(clearPageStack!: Bool = true): Unit
```

**功能：** 终止应用的所有进程，进程退出时不会正常走完应用生命周期。仅支持主线程调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|clearPageStack|Bool|否|true| **命名参数。** 表示是否清除页面堆栈。true表示清除，false表示不清除。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |16000011|The context does not exist.|