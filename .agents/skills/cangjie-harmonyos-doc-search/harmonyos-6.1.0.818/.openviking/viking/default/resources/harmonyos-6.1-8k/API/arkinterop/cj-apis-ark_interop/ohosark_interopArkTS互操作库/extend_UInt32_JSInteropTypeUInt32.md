## extend UInt32 <: JSInteropType\<UInt32>

**功能：** 该接口可用为内置类型 UInt32 实现扩展方法。

**起始版本：** 22

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func uint32Translate(context: JSContext): Unit {
    let source: UInt32 = 123
    let value = source.toJSValue(context)
    let result = UInt32.fromJSValue(context, value)
    Hilog.info(0, "test", "result: ${result}")
}
```

### static func fromJSValue(JSContext, JSValue)

```cangjie
public static func fromJSValue(_: JSContext, input: JSValue): UInt32
```

**功能：** 将 JSValue 类型数据转换为相应的 UInt32 类型。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|
|input|[JSValue](#class-jsvalue)|是|-|ArkTS 统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|仓颉类型。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002     | Outside error occurred.              |
| 34300003     | Accessing reference is beyond reach. |
| 34300004     | Thread mismatch.                     |
| 34300005     | The ArkTS data types do not match.   |

### static func toArktsType()

```cangjie
public static func toArktsType(): String
```

**功能：** 获取仓颉 UInt32 类型对应的ArkTS类型名称。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后 ArkTS 类型名。|

### func toJSValue(JSContext)

```cangjie
public func toJSValue(context: JSContext): JSValue
```

**功能：** 将仓颉 UInt32 类型数据转换为JSValue。

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
| 34300003     | Accessing reference is beyond reach. |
| 34300004     | Thread mismatch. |