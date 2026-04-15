### func keys()

```cangjie
public func keys(): EquatableCollection<K>
```

**功能：** 返回 JSHashMapEx 中所有的 key，并将所有 key 存储在一个 Keys 容器中。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|EquatableCollection\<K>|保存所有返回的 key。|

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

func getHashMapExKeys(context: JSContext): JSValue {
    let jsHashMapEx = JSHashMapEx<String, Int64>()
    jsHashMapEx.set("key1", 1)
    jsHashMapEx.set("key2", 2)
    jsHashMapEx.set("key3", 3)

    let keys = jsHashMapEx.keys()
    Hilog.info(0, "test", "HashMapEx has ${keys.size} keys")

    return context.number(Float64(keys.size)).toJSValue()
}
```

### func set(K, V)

```cangjie
public func set(key: K, value: V): Unit
```

**功能：** 将键值对放入 JSHashMapEx 中。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|K|是|-|要放置的键。|
|value|V|是|-|要分配的值。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                  |
|:------|:--------------------------------------|
| 34300003   | Accessing reference is beyond reach.  |
| 34300004   | Thread mismatch.                      |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func setHashMapExValue(context: JSContext): JSValue {
    let jsHashMapEx = JSHashMapEx<String, Int64>()
    jsHashMapEx.set("myKey", 42)

    Hilog.info(0, "test", "Set value in HashMapEx")

    return jsHashMapEx.toJSValue(context)
}
```

### func setAll(Collection\<(K,V)>)

```cangjie
public func setAll(elements: Collection<(K, V)>): Unit
```

**功能：** 按照 elements 的迭代器顺序将新的键值对集合放入 JSHashMapEx 中。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|elements|Collection\<(K, V)>|是|-|需要添加进 JSHashMapEx 的键值对集合。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                  |
|:------|:--------------------------------------|
| 34300003   | Accessing reference is beyond reach.  |
| 34300004   | Thread mismatch.                      |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func setAllHashMapExValues(context: JSContext): JSValue {
    let jsHashMapEx = JSHashMapEx<String, Int64>()
    let elements: Array<(String, Int64)> = [("key1", 1), ("key2", 2), ("key3", 3)]

    jsHashMapEx.setAll(elements)
    Hilog.info(0, "test", "Set all values in HashMapEx")

    return jsHashMapEx.toJSValue(context)
}
```

### func setIfAbsent(K, V)

```cangjie
public func setIfAbsent(key: K, value: V): Bool
```

**功能：** 当此 JSHashMapEx 中不存在键 key 时，向 JSHashMapEx 中插入键值对(key, value)。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|K|是|-|要放置的键。|
|value|V|是|-|要分配的值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果赋值之前 key 存在，则返回 false，否则返回 true。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                  |
|:------|:--------------------------------------|
| 34300003   | Accessing reference is beyond reach.  |
| 34300004   | Thread mismatch.                      |