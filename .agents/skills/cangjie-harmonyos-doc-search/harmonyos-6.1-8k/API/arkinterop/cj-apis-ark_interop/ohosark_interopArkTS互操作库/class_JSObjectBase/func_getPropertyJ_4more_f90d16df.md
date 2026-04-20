### func getProperty(JSKeyable)

```cangjie
public func getProperty(key: JSKeyable): JSValue
```

**功能：** 从当前对象获取目标属性值。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|目标键。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|获得的值。|

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
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let obj = callInfo[0].asObject()
    let result = obj.getProperty("a")
    return result
}
```

### func hasProperty(JSKeyable)

```cangjie
public func hasProperty(key: JSKeyable): Bool
```

**功能：** 判断当前对象是否存在目标属性。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|目标键。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表当前对象存在目标属性。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let obj = callInfo[0].asObject()
    let hasA = obj.hasProperty("a")
    Hilog.info(0, "test", "obj has property of a: ${hasA}")
    obj.toJSValue()
}
```

### func instanceOf(JSClass)

```cangjie
public func instanceOf(clazz: JSClass): Bool
```

**功能：** 判断当前的对象是否是目标 ArkTS 类的实例。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|clazz|[JSClass](#class-jsclass)|是|-|目标 ArkTS 类。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表该对象是目标 ArkTS 类的实例。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let ctor: JSLambda = { context, callInfo =>
        callInfo.thisArg
    }
    let classA = context.clazz(ctor)
    let obj = classA.new().asObject()
    let isClassA = obj.instanceOf(classA)
    Hilog.info(0, "test", "obj is classA: ${isClassA}")
    return obj.toJSValue()
}
```

### func keys()

```cangjie
public func keys(): Array<String>
```

**功能：** 枚举出当前对象所有可枚举的属性名。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|键列表。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let keys = context.global.keys()
    Hilog.info(0, "test", "global keys: ${keys}")
    context.undefined().toJSValue()
}
```