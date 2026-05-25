### func toHashMap()

```cangjie
public func toHashMap(): HashMap<K, V>
```

**功能：** 转换为 HashMap。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|HashMap\<K, V>|转换后的 HashMap。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                  |
|:------|:--------------------------------------|
| 34300003   | Accessing reference is beyond reach.  |
| 34300004   | Thread mismatch.                      |

### func toJSValue(JSContext)

```cangjie
public func toJSValue(c: JSContext): JSValue
```

**功能：** 转换为 JSValue。声明式互操作宏框架场景使用，开发者不需要使用此API。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|c|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|ArkTS 统一类型。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                  |
|:------|:--------------------------------------|
| 34300003   | Accessing reference is beyond reach.  |
| 34300004   | Thread mismatch.                      |

### func values()

```cangjie
public func values(): Collection<V>
```

**功能：** 返回 JSHashMapEx 中包含的值，并将所有的 value 存储在一个 Values 容器中。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Collection\<V>|保存所有返回的 value。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                  |
|:------|:--------------------------------------|
| 34300003   | Accessing reference is beyond reach.  |
| 34300004   | Thread mismatch.                      |

### operator func \[](K)

```cangjie
public operator func [](key: K): V
```

**功能：** 运算符重载 set 方法，如果键存在，新 value 覆盖旧 value，如果键不存在，添加此键值对。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|K|是|-|要放置的键。|

**返回值：**

|类型|说明|
|:----|:----|
|V|键对应的值。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002   | Outside error occurred.　             |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func getIndexOperatorHashMapEx(context: JSContext): JSValue {
    let jsHashMapEx = JSHashMapEx<String, Int64>()
    jsHashMapEx.set("myKey", 100)

    let value = jsHashMapEx["myKey"]
    Hilog.info(0, "test", "Value for 'myKey': ${value}")

    return context.number(Float64(value)).toJSValue()
}
```

### operator func \[](K, V)

```cangjie
public operator func [](key: K, value!: V): Unit
```

**功能：** 运算符重载 set 方法，如果键存在，新 value 覆盖旧 value，如果键不存在，添加此键值对。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|K|是|-|要放置的键。|
|value|V|是|-| **命名参数。** 要分配的值。|

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

func setIndexOperatorHashMapEx(context: JSContext): JSValue {
    let jsHashMapEx = JSHashMapEx<String, Int64>()
    jsHashMapEx["newKey"] = 200

    Hilog.info(0, "test", "Set value using index operator")

    return jsHashMapEx.toJSValue(context)
}
```