#### static func has(String)

```cangjie
public static func has(propName: String): Bool
```

**功能：** 判断propName对应的属性是否在AppStorage中存在。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|AppStorage中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果propName对应的属性在AppStorage中存在，则返回true。不存在则返回false。|

#### static func keys()

```cangjie
public static func keys(): EquatableCollection<String>
```

**功能：** 返回AppStorage中所有的属性名。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|EquatableCollection\<String>|AppStorage中所有的属性名。|

**示例：**

```cangjie
let a = AppStorage.setOrCreate("PropB", 48)
let keys = AppStorage.keys()
```

#### static func link\<T>(String)

```cangjie
public static func link<T>(key: String): ?ObservedProperty<T>
```

**功能：** 如果给定的propName在AppStorage实例中存在，则返回与AppStorage中propName对应属性的双向绑定数据。

双向绑定数据的修改会被同步回AppStorage中，AppStorage会将变化同步到所有绑定该propName的数据和Component中。

如果AppStorage中不存在propName，则返回None。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|AppStorage中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|?[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#class-observedproperty)\<T>|Option\<ObservedProperty\<T>>的实例，与AppStorage中propName对应属性的双向绑定的数据，如果AppStorage中不存在对应的propName，则返回None。|

**示例：**

```cangjie
let a = AppStorage.setOrCreate("PropA", 47)
let linkToPropA1 = AppStorage.link<Int64>("PropA").getOrThrow()
let linkToPropA2 = AppStorage.link<Int64>("PropA").getOrThrow() // linkToPropA2.get() == 47
let res = linkToPropA1.set(48) // 双向同步: linkToPropA1.get() == linkToPropA2.get() == 48
```

#### static func set\<T>(String, T)

```cangjie
public static func set<T>(key: String, newValue: T): Bool
```

**功能：** 在AppStorage中设置propName对应属性的值。如果newValue的值和propName对应属性的值相同，即不需要做赋值操作，状态变量不会通知UI刷新propName对应属性的值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-| AppStorage中的属性名。|
|newValue|T|是|-|属性值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果AppStorage中不存在propName对应的属性，返回false。设置成功返回true。|

**示例：**

```cangjie
let a = AppStorage.setOrCreate("PropA", 48)
let res = AppStorage.set("PropA", 47) // true
let res1 = AppStorage.set("PropB", 47) // false
```