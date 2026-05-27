### class AppStorage

```cangjie
public class AppStorage {}
```

**功能：** 用于提供应用状态数据的中心存储的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### static func `prop`\<T>(String)

```cangjie
public static func `prop`<T>(key: String): ?ObservedProperty<T>
```

**功能：** 与AppStorage中对应的propName建立单向属性绑定。如果给定的propName在AppStorage中存在，则返回与AppStorage中propName对应属性的单向绑定数据。如果AppStorage中不存在propName，则返回None。单向绑定数据的修改不会被同步回AppStorage中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|AppStorage中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|?[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#observedpropertyt)\<T>|返回单向绑定的数据，如果AppStorage中不存在对应的属性值，则返回None。|

#### static func clear()

```cangjie
public static func clear(): Bool
```

**功能：** 删除AppStorage中所有的属性。删除所有属性的前提是已经没有任何订阅者。如果有订阅者，clear不会生效并返回false。如果没有订阅者则删除成功并返回true。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果AppStorage中的属性已经没有任何订阅者，则删除成功，并返回true。否则返回false。|

**示例：**

```cangjie
let tmp = AppStorage.setOrCreate("PropA", 47)
let res = AppStorage.clear()
```

#### static func delete(String)

```cangjie
public static func delete(key: String): Bool
```

**功能：** 在AppStorage中删除propName对应的属性。在AppStorage中删除属性的前提是该属性已经没有订阅者，如果有订阅者，则返回false。如果没有订阅者则删除成功并返回true。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

属性的订阅者为link等接口绑定的propName，以及@StorageLink["propName"]和@StorageProp["propName"]。如果自定义组件中使用@StorageLink["propName"]和@StorageProp["propName"]或者ObservedProperty实例（link接口的返回类型）依旧对propName有同步关系，则该属性不能从AppStorage中删除。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|AppStorage中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool| 如果AppStorage中有对应的属性，且该属性已经没有订阅者，则删除成功，返回true。如果属性不存在，或者该属性还存在订阅者，则返回false。|

**示例：**

```cangjie
let a = AppStorage.setOrCreate("PropA", 47)
let a1 = AppStorage.link<Int64>("PropA")

// UI代码中
@StorageLink["PropA"]
var a: Int64 = 0

let res = AppStorage.delete("PropA") // false, PropA still has a subscriber
let res1 = AppStorage.delete("PropB") // false, PropB is not in storage

let a2 = AppStorage.setOrCreate("PropB", 48)
let res2 = AppStorage.delete("PropB") // true
```

#### static func get\<T>(String)

```cangjie
public static func get<T>(key: String): ?T
```

**功能：** 获取propName在AppStorage中对应的属性值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|AppStorage中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|?T|AppStorage中propName对应的属性值，如果不存在则返回None。|

**示例：**

```cangjie
let a = AppStorage.setOrCreate("PropA", 47)
let value = AppStorage.get<Int64>("PropA").getOrThrow() // 47
```