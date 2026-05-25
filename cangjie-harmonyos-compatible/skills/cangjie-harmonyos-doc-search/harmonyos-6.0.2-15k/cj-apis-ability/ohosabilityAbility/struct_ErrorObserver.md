## struct ErrorObserver

```cangjie
public struct ErrorObserver {
    public let onUnhandledException:(String) -> Unit
    public let onException: Option <(ErrorObject) -> Unit>
    public init(onUnhandledException : (String)->Unit,
                onException !: Option<(ErrorObject)->Unit> = None)
}
```

**功能：** 定义异常监听，可以作为ErrorManager.on的入参监听当前应用发生的异常。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### let onException

```cangjie
public let onException: Option <(ErrorObject) -> Unit>
```

**功能：** 该回调函数调用场景：在程序运行中抛出异常且该异常未被任务‘try-catch’语句成功捕获。`errObject`中包含了该未被捕获的异常的异常名称、异常信息与栈追踪。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Option\<([ErrorObject](#struct-errorobject))->Unit>

**读写能力：** 只读

**起始版本：** 12

### let onUnhandledException

```cangjie
public let onUnhandledException:(String) -> Unit
```

**功能：** 该回调函数调用场景：在程序运行中抛出异常且该异常未被任务‘try-catch’语句成功捕获。`errMsg`的内容固定为`Uncaught exception was found.`。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** (String)->Unit

**读写能力：** 只读

**起始版本：** 12

### init((String) -> Unit, Option\<(ErrorObject) -> Unit>)

```cangjie
public init(onUnhandledException : (String)->Unit,
            onException !: Option<(ErrorObject)->Unit> = None)
```

**功能：** ErrorObserver的主构造函数。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onUnhandledException|(String)->Unit|是|-|该回调函数调用场景：在程序运行中抛出异常且该异常未被任务‘try-catch’语句成功捕获。errMsg的内容固定为Uncaught exception was found.。|
|onException|Option\<([ErrorObject](#struct-errorobject))->Unit>|否|None| **命名参数。** 该回调函数调用场景：在程序运行中抛出异常且该异常未被任务‘try-catch’语句成功捕获。errObject中包含了该未被捕获的异常的异常名称、异常信息与栈追踪。|