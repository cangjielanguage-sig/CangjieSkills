## extend\<T> Option\<T> <: JSInteropType<Option\<T>> where T <: JSInteropType\<T>

**功能：** 该接口可用为类型 Option\<T> 实现扩展方法。

**起始版本：** 22

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func optionTranslate(context: JSContext): Unit {
    let sources: Array<?String> = ["abc", None, "123"]
    for (v in sources) {
        let value = v.toJSValue(context)
        let result = Option<String>.fromJSValue(context, value)
        Hilog.info(0, "test", "result: ${result}")
    }
}
```

### static func fromJSValue(JSContext, JSValue)

```cangjie
public static func fromJSValue(context: JSContext, input: JSValue): Option<T>
```

**功能：** 将 JSValue 类型数据转换为相应的 Option\<T> 类型。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|
|input|[JSValue](#class-jsvalue)|是|-|ArkTS 统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Option\<T>|仓颉 Option 类型。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息 |
|:------| :--- |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch. |

### static func toArktsType()

```cangjie
public static func toArktsType(): String
```

**功能：** 获取仓颉 Option\<T> 类型对应的ArkTS类型名称。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后 ArkTS 类型名。|

### func toJSValue(JSContext)

```cangjie
public func toJSValue(context: JSContext): JSValue
```

**功能：** 将仓颉 Option\<T> 类型数据转换为JSValue。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|ArkTS 统一类型。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息 |
|:------| :--- |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch. |