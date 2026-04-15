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

### func clear()

```cangjie
public func clear(): Unit
```

**功能：** 从此 HashMapEx 中移除所有元素。

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

### func clone()

```cangjie
public func clone(): JSHashMapEx<K, V>
```

**功能：** 克隆 JSHashMapEx，将对 JSHashMapEx 数据进行深拷贝。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSHashMapEx](#class-jshashmapexk-v-where-k--jskeyable--hashable--equatablek--jsinteroptypek-v--jsinteroptypev)\<K, V>|克隆得到的新 JSHashMapEx。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

### func containsAll(Collection\<K>)

```cangjie
public func containsAll(keys: Collection<K>): Bool
```

**功能：** 判断是否包含指定集合中所有键的映射。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|keys|Collection\<K>|是|-|键传递待判断的 keys。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果都包含，则返回 true；否则，返回 false。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

### func delete(K)

```cangjie
public func delete(key: K): Bool
```

**功能：** 从此 JSHashMapEx 中删除指定键的映射（如果存在）。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|K|是|-|传入要删除的 key。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果删除之前 key 存在且删除成功，则返回 true，不存在则返回 false。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

### func deleteAll(Collection\<K>)

```cangjie
public func deleteAll(keys: Collection<K>): Unit
```

**功能：** 从此 JSHashMapEx 中删除指定集合中键的映射（如果存在）。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|keys|Collection\<K>|是|-|传入要删除的键的集合。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |