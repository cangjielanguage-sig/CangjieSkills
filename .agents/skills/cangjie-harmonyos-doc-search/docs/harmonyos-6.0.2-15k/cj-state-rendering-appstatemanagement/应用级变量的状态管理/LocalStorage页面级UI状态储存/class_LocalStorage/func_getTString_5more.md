#### func get\<T>(String)

```cangjie
public func get<T>(propName: String): ?T
```

**功能：** 获取propName在LocalStorage中对应的属性值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorage中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|?T|LocalStorage中propName对应的属性值，如果不存在则返回None。|

**示例：**

```cangjie
let storage = LocalStorage()
let res = storage.setOrCreate("PropA", 47)
let value = storage.get("PropA").getOrThrow() // 47
```

#### func has(String)

```cangjie
public func has(propName: String): Bool
```

**功能：** 判断propName对应的属性是否在LocalStorage中存在。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorage中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果propName对应的属性在LocalStorage中存在，则返回true。不存在则返回false。|

**示例：**

```cangjie
let storage = LocalStorage()
storage.has("key") // false
```

#### func keys()

```cangjie
public func keys(): EquatableCollection<String>
```

**功能：** 返回LocalStorage中所有的属性名。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|EquatableCollection\<String>|LocalStorage中所有的属性名。|

```cangjie
let storage = LocalStorage()
let tmp = storage.setOrCreate("PropA", 47)
let keys = storage.keys()
```

#### func link\<T>(String)

```cangjie
public func link<T>(propName: String): ?ObservedProperty<T>
```

**功能：** 如果给定的propName在LocalStorage实例中存在，则返回与LocalStorage中propName对应属性的双向绑定数据。

双向绑定数据的修改会被同步回LocalStorage中，LocalStorage会将变化同步到所有绑定该propName的数据和Component中。

如果LocalStorage中不存在propName，则返回None。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorage中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|?[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#class-observedproperty)\<T>| Option\<ObservedProperty\<T>>的实例，与LocalStorage中propName对应属性的双向绑定的数据，如果LocalStorage中不存在对应的propName，则返回None。|

**示例：**

```cangjie
let storage = LocalStorage()
let res = storage.setOrCreate("PropA", 47)
let linkToPropA1 = storage.link<Int64>("PropA").getOrThrow()
let linkToPropA2 = storage.link<Int64>("PropA").getOrThrow()
linkToPropA1.set(48) // linkToPropA1.get() == linkToPropA2.get() == 48
```

#### func set\<T>(String, T)

```cangjie
public func set<T>(propName: String, newValue: T): Bool
```

**功能：** 在LocalStorage中设置propName对应属性的值。如果newValue的值和propName对应属性的值相同，即不需要做赋值操作，状态变量不会通知UI刷新propName对应属性的值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorage中的属性名。|
|newValue|T|是|-|属性值|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果LocalStorage中不存在propName对应的属性，返回false。设置成功返回true。|

**示例：**

```cangjie
let storage = LocalStorage()
let res = storage.setOrCreate("PropA", 47)
let res1 = storage.set("PropA", 48) // true
let res2 = storage.set("PropB", 48) // false
```