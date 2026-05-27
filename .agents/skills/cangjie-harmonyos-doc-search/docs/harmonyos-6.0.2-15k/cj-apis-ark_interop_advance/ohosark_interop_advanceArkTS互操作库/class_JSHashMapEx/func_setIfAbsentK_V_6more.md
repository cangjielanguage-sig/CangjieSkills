### func setIfAbsent(K, V)

```cangjie
public func setIfAbsent(key: K, value: V): Bool
```

**功能：** 当此 JSHashMapEx 中不存在键 key 时，向 JSHashMapEx 中插入键值对(key, value)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|K|是|-|要放置的键。|
|value|V|是|-|要分配的值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果赋值之前 key 存在，则返回 false ，否则返回 true 。|

### func toHashMap()

```cangjie
public func toHashMap(): HashMap<K, V>
```

**功能：** 转换为 HashMap。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|HashMap\<K, V>|转换后的 HashMap。|

### func toJSValue(JSContext)

```cangjie
public func toJSValue(_: JSContext): JSValue
```

**功能：** 转换为 JSValue。声明式互操作宏框架场景使用，开发者不需要使用此API。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|ArkTS 统一类型。|

### func values()

```cangjie
public func values(): Collection<V>
```

**功能：** 返回 JSHashMapEx 中包含的值，并将所有的 value 存储在一个 Values 容器中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|Collection\<V>|保存所有返回的 value。|

### func \[](K)

```cangjie
public operator func [](key: K): V
```

**功能：** 运算符重载 set 方法，如果键存在，新 value 覆盖旧 value，如果键不存在，添加此键值对。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|K|是|-|要放置的键。|

**返回值：**

|类型|说明|
|:----|:----|
|V|键对应的值。|

### func \[](K, V)

```cangjie
public operator func [](key: K, value!: V): Unit
```

**功能：** 运算符重载 set 方法，如果键存在，新 value 覆盖旧 value，如果键不存在，添加此键值对。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|K|是|-|要放置的键。|
|value|V|是|-| **命名参数。** 要分配的值。|