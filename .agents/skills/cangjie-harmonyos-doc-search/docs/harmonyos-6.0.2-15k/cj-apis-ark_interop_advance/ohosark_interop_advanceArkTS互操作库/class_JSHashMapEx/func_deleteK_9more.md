### func delete(K)

```cangjie
public func delete(key: K): Bool
```

**功能：** 从此 JSHashMapEx 中删除指定键的映射（如果存在）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|K|是|-|传入要删除的 key。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果删除之前 key 存在且删除成功，则返回 true ，不存在则返回 false 。|

### func deleteAll(Collection\<K>)

```cangjie
public func deleteAll(keys: Collection<K>): Unit
```

**功能：** 从此 JSHashMapEx 中删除指定集合中键的映射（如果存在）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|keys|Collection\<K>|是|-|传入要删除的键的集合。|

### func deleteIf((K,V) -> Bool)

```cangjie
public func deleteIf(predicate: (K, V) -> Bool): Unit
```

**功能：** 传入 lambda 表达式，如果满足条件，则删除对应的键值对。

该函数会遍历整个 JSHashMapEx，所有满足 predicate(K, V) == true 的键值对都会被删除。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|predicate|(K, V)->Bool|是|-|传递一个 lambda 表达式进行判断。|

### func get(K)

```cangjie
public func get(key: K): Option<V>
```

**功能：** 返回指定键映射到的值，如果不包含指定键的映射，则返回 Option\<V>.None。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|K|是|-|传入的键。|

**返回值：**

|类型|说明|
|:----|:----|
|Option\<V>|键对应的值。用 Option 封装。|

### func has(K)

```cangjie
public func has(key: K) : Bool
```

**功能：** 判断是否包含指定键的映射。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|K|是|-|传递要判断的 key。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果存在，则返回 true；否则，返回 false。|

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

**功能：** 判断 JSHashMapEx 是否为空，如果是，则返回 true；否则，返回 false。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|Bool|JSHashMapEx 是否为空。|

### func keys()

```cangjie
public func keys(): EquatableCollection<K>
```

**功能：** 返回 JSHashMapEx 中所有的 key，并将所有 key 存储在一个 Keys 容器中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|EquatableCollection\<K>|保存所有返回的 key。|

### func set(K, V)

```cangjie
public func set(key: K, value: V): Unit
```

**功能：** 将键值对放入 JSHashMapEx 中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|K|是|-|要放置的键。|
|value|V|是|-|要分配的值。|

### func setAll(Collection\<(K,V)>)

```cangjie
public func setAll(elements: Collection<(K, V)>): Unit
```

**功能：** 按照 elements 的迭代器顺序将新的键值对集合放入 JSHashMapEx 中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|elements|Collection\<(K, V)>|是|-|需要添加进 JSHashMapEx 的键值对集合。|