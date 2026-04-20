### func addMethod(JSKeyable, JSFunction)

```cangjie
public func addMethod(key: JSKeyable, method: JSFunction): Unit
```

**功能：** 为当前 ArkTS 类定义一个方法。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|属性键。|
|method|[JSFunction](#class-jsfunction)|是|-|方法实现。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002   | Outside error occurred.                |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let ctor: JSLambda = { _, callInfo =>
        return callInfo.thisArg
    }
    let clazz = context.clazz(ctor)
    let getClassKind: JSLambda = { context, _ =>
        context.string("aaa").toJSValue()
    }
    clazz.addMethod("getClassKind", context.function(getClassKind))
    let obj = clazz.new()
    let classKind = obj.getProperty("classKind").toString()
    Hilog.info(0, "test", "class kind is ${classKind}")
    return obj
}
```

### func addMethod(JSKeyable, JSLambda)

```cangjie
public func addMethod(key: JSKeyable, method: JSLambda): Unit
```

**功能：** 为当前 ArkTS 类定义一个方法。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|属性键。|
|method|[JSLambda](#type-jslambda)|是|-|方法实现。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002   | Outside error occurred.                |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let ctor: JSLambda = { _, callInfo =>
        return callInfo.thisArg
    }
    let clazz = context.clazz(ctor)
    let getClassKind: JSLambda = { context, _ =>
        context.string("aaa").toJSValue()
    }
    clazz.addMethod("getClassKind", getClassKind)
    let obj = clazz.new()
    let classKind = obj.getProperty("classKind").toString()
    Hilog.info(0, "test", "class kind is ${classKind}")
    return obj
}
```

### func addProperty(JSKeyable, JSValue)

```cangjie
public func addProperty(key: JSKeyable, value: JSValue): Unit
```

**功能：** 为目标 ArkTS 类新增一个数据成员，一般用于定义不可变属性。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|属性键。|
|value|[JSValue](#class-jsvalue)|是|-|属性值。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002   | Outside error occurred.                |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let ctor: JSLambda = { _, callInfo =>
        return callInfo.thisArg
    }
    let clazz = context.clazz(ctor)
    clazz.addProperty("classKind", context.string("CustomClass").toJSValue())
    let obj = clazz.new()
    let classKind = obj.getProperty("classKind").toString()
    Hilog.info(0, "test", "class kind is ${classKind}")
    return obj
}
```