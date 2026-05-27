### class LocalStorage

```cangjie
public open class LocalStorage {
    public init()
}
```

**功能：** 用于提供页面级的UI状态存储的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init()

```cangjie
public init()
```

**功能：** 构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func `prop`\<T>(String)

```cangjie
public func `prop`<T>(propName: String): ?ObservedProperty<T>
```

**功能：** 如果给定的propName在LocalStorage中存在，则返回与LocalStorage中propName对应属性的单向绑定数据。如果LocalStorage中不存在propName，则返回None。单向绑定数据的修改不会被同步回LocalStorage中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorage中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|?[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#class-observedproperty)\<T>|ObservedProperty\<T>的实例，和LocalStorage中propName对应属性的单向绑定的数据。如果LocalStorage中不存在对应的propName，则返回None。|

**示例：**

```cangjie
let storage = LocalStorage()
let tmp = storage.setOrCreate("PropA", 47)

let prop1 = storage.prop("PropA")
let prop2 = storage.prop("PropA")

prop1.set(1)// one-way sync: prop1.get()=1; but prop2.get() == 47
```

#### func clear()

```cangjie
public func clear(): Bool
```

**功能：** 删除LocalStorage中所有的属性。删除所有属性的前提是已经没有任何订阅者。如果有订阅者，clear不会生效并返回false。如果没有订阅者则删除成功并返回true。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果LocalStorage中的属性已经没有任何订阅者，则删除成功，并返回true。否则返回false|

**示例：**

```cangjie
let storage = LocalStorage()
let tmp = storage.setOrCreate("PropA", 47)
let res = storage.clear()
```

#### func delete(String)

```cangjie
public func delete(propName: String): Bool
```

**功能：** 在LocalStorage中删除propName对应的属性。在LocalStorage中删除属性的前提是该属性已经没有订阅者，如果有订阅者，则返回false。如果没有订阅者则删除成功并返回true。

属性的订阅者为link等接口绑定的propName，以及@LocalStorageLink["propName"]和@LocalStorageProp["propName"]。如果自定义组件中使用@LocalStorageLink["propName"]和@LocalStorageProp["propName"]或者ObservedProperty实例（link接口的返回类型）依旧对propName有同步关系，则该属性不能从LocalStorage中删除。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorage中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果LocalStorage中有对应的属性，且该属性已经没有订阅者，则删除成功，返回true。如果属性不存在，或者该属性还存在订阅者，则返回false。|

**示例：**

```cangjie
let storage = LocalStorage()
let tmp = storage.setOrCreate("PropA", 47)

// UI代码中
@LocalStorageLink["PropA"]
var a: Int64 = 0

let res = storage.delete("PropA") // false, PropA still has a subscriber
let res1 = storage.delete("PropB") // false, PropB is not in storage

let tmp1 = storage.setOrCreate("PropB", 48)
let res2 = storage.delete("PropB") // true
```