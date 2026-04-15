## class JSArrayEx\<T> where T <: JSInteropType\<T>

```cangjie
public class JSArrayEx<T> <: JSInteropType<JSArrayEx<T>> where T <: JSInteropType<T> {
    public init(arr: Array<T>)
}
```

**功能：** 在声明式互操作宏中使用，对应ArkTS的 Array\<T> 类型。

**起始版本：** 22

**父类型：**

- [JSInteropType\<JSArrayEx\<T>>](#interface-jsinteroptypet)

### prop size

```cangjie
public prop size: Int64
```

**功能：** 获取元素数量。

**起始版本：** 22

**类型：** Int64

**读写能力：** 只读

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息 |
|:------| :--- |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch. |

### init(Array\<T>)

```cangjie
public init(arr: Array<T>)
```

**功能：** 给定 Array\<T>，构造对应的 JSArrayEx\<T> 实例。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arr|Array\<T>|是|-|根据该 Array 实例创建。|

### static func fromJSValue(JSContext, JSValue)

```cangjie
public static func fromJSValue(context: JSContext, input: JSValue): JSArrayEx<T>
```

**功能：** 从 JSValue 转换为 JSArrayEx。声明式互操作宏框架场景使用，开发者不需要使用此API。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|
|input|[JSValue](#class-jsvalue)|是|-|ArkTS 统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSArrayEx](#class-jsarrayext-where-t--jsinteroptypet)\<T>|声明式互操作宏类型 JSArrayEx。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                     |
|:------|:-----------------------------------------|
| 34300003   | Accessing reference is beyond reach.     |
| 34300004   | Thread mismatch.                         |
| 34300005   | The ArkTS data types do not match.           |

### static func toArktsType()

```cangjie
public static func toArktsType(): String
```

**功能：** 获取仓颉类型对应的ArkTS类型名称。声明式互操作宏框架场景使用，开发者不需要使用此API。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后 ArkTS 类型名。|

### func clone()

```cangjie
public func clone(): JSArrayEx<T>
```

**功能：** 克隆 JSArrayEx，将对 JSArrayEx 数据进行深拷贝。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSArrayEx](#class-jsarrayext-where-t--jsinteroptypet)\<T>|克隆得到的新 JSArrayEx。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                     |
|:------|:-----------------------------------------|
| 34300003   | Accessing reference is beyond reach.     |
| 34300004   | Thread mismatch.                         |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func cloneArrayEx(context: JSContext): JSValue {
    let originalArray: Array<Int64> = [1, 2, 3, 4, 5]
    let jsArrayEx = JSArrayEx<Int64>(originalArray)
    let clonedArrayEx = jsArrayEx.clone()

    Hilog.info(0, "test", "Original size: ${jsArrayEx.size}")
    Hilog.info(0, "test", "Cloned size: ${clonedArrayEx.size}")

    return clonedArrayEx.toJSValue(context)
}
```