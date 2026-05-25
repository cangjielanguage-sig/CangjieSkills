## class JSHashMapEx<K, V> where K <: JSKeyable & Hashable & Equatable\<K> & JSInteropType\<K>, V <: JSInteropType\<V>

```cangjie
public class JSHashMapEx<K, V> <: JSInteropType<JSHashMapEx<K, V>> where K <: JSKeyable & Hashable & Equatable<K> & JSInteropType<K>, V <: JSInteropType<V> {
    public init(map: HashMap<K, V>)
    public init()
}
```

**功能：** 在声明式互操作宏中使用，对应ArkTS的 Map 类型。

**起始版本：** 22

**父类型：**

- [JSInteropType\<JSHashMapEx\<K,V>>](#interface-jsinteroptypet)

### prop size

```cangjie
public prop size: Int64
```

**功能：** 返回键值对的个数。

**起始版本：** 22

**类型：** Int64

**读写能力：** 只读

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

### init(HashMap\<K,V>)

```cangjie
public init(map: HashMap<K, V>)
```

**功能：** 构造空的 JSHashMapEx\<K, V> 实例。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|map|HashMap\<K, V>|是|-|根据该 HashMap 实例创建。|

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog
import std.collection.HashMap

func createHashMapExFromHashMap(context: JSContext): JSValue {
    let hashMap = HashMap<String, Int64>()
    hashMap["key1"] = 1
    hashMap["key2"] = 2

    let jsHashMapEx = JSHashMapEx<String, Int64>(hashMap)
    Hilog.info(0, "test", "Created JSHashMapEx from HashMap with ${jsHashMapEx.size} elements")

    return jsHashMapEx.toJSValue(context)
}
```

### init()

```cangjie
public init()
```

**功能：** 构造空的 JSHashMapEx\<K, V> 实例。

**起始版本：** 22

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func createEmptyHashMapEx(context: JSContext): JSValue {
    let jsHashMapEx = JSHashMapEx<String, Int64>()
    Hilog.info(0, "test", "Created empty JSHashMapEx")

    return jsHashMapEx.toJSValue(context)
}
```

### static func fromJSValue(JSContext, JSValue)

```cangjie
public static func fromJSValue(context: JSContext, input: JSValue): JSHashMapEx<K, V>
```

**功能：** 从 JSValue 转换为 JSHashMapEx。声明式互操作宏框架场景使用，开发者不需要使用此API。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|
|input|[JSValue](#class-jsvalue)|是|-|ArkTS 统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSHashMapEx](#class-jshashmapexk-v-where-k--jskeyable--hashable--equatablek--jsinteroptypek-v--jsinteroptypev)\<K, V>|声明式互操作宏类型 JSHashMapEx。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func convertJSValueToStringHashMapEx(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 创建一个 JSHashMapEx<String, String>
    let source = JSHashMapEx<String, String>()
    // 填入键值对
    source["key1"] = "value1"
    // 转换为 JSValue
    let jsValue = source.toJSValue(context)

    // 从 JSValue 转换为 JSHashMapEx<String, String>
    let received = JSHashMapEx<String, String>.fromJSValue(context, jsValue)

    // 获取所有键
    let keys = received.keys()

    // 遍历所有键值对
    for (key in keys) {
        let value = source[key]
        Hilog.info(0, "test", "Key: ${key}, Value: ${value}")
    }

    return jsValue
}
```