### func deleteIf((K,V) -> Bool)

```cangjie
public func deleteIf(predicate: (K, V) -> Bool): Unit
```

**功能：** 传入 lambda 表达式，如果满足条件，则删除对应的键值对。

该函数会遍历整个 JSHashMapEx，所有满足 predicate(K, V) == true 的键值对都会被删除。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|predicate|(K, V)->Bool|是|-|传递一个 lambda 表达式进行判断。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

### func get(K)

```cangjie
public func get(key: K): Option<V>
```

**功能：** 返回指定键映射到的值，如果不包含指定键的映射，则返回 Option\<V>.None。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|K|是|-|传入的键。|

**返回值：**

|类型|说明|
|:----|:----|
|Option\<V>|键对应的值。用 Option 封装。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

### func has(K)

```cangjie
public func has(key: K) : Bool
```

**功能：** 判断是否包含指定键的映射。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|K|是|-|传递要判断的 key。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果存在，则返回 true；否则，返回 false。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

**功能：** 判断 JSHashMapEx 是否为空，如果是，则返回 true；否则，返回 false。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|JSHashMapEx 是否为空。|

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

func checkHashMapExEmpty(context: JSContext): JSValue {
    let emptyMap = JSHashMapEx<String, Int64>()
    let nonEmptyMap = JSHashMapEx<String, Int64>()
    nonEmptyMap.set("key", 1)

    Hilog.info(0, "test", "Is empty map empty: ${emptyMap.isEmpty()}")
    Hilog.info(0, "test", "Is non-empty map empty: ${nonEmptyMap.isEmpty()}")

    return context.boolean(emptyMap.isEmpty()).toJSValue()
}
```