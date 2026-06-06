#### func setAndLink\<T>(String, T)

```cangjie
public func setAndLink<T>(propName: String, defaultValue: T): ObservedProperty<T>
```

**功能：** 与link接口类似，如果给定的propName在LocalStorage中存在，则返回该propName对应的属性的双向绑定数据。如果不存在，则使用defaultValue在LocalStorage中创建和初始化propName对应的属性，返回其双向绑定数据。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorage中的属性名。|
|defaultValue|T|是|-|当propName在LocalStorage中不存在时，使用defaultValue在LocalStorage中初始化对应的propName。|

**返回值：**

|类型|说明|
|:----|:----|
|[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#class-observedproperty)\<T>|ObservedProperty\<T>的实例，与LocalStorage中propName对应属性的双向绑定的数据。|

**示例：**

```cangjie
let storage = LocalStorage()
let res = storage.setOrCreate("PropA", 47)
let linkToPropA1 = storage.setAndLink("PropB", 49) // Create PropB 49
let linkToPropA2 = storage.setAndLink("PropA", 50) // PropA exists, remains 47
```

#### func setAndProp\<T>(String, T)

```cangjie
public func setAndProp<T>(propName: String, defaultValue: T): ObservedProperty<T>
```

**功能：** 与prop接口类似。如果propName在LocalStorage中存在，则返回该propName对应的属性的单向绑定数据。如果不存在，则使用defaultValue在LocalStorage中创建和初始化propName对应的属性，返回其单向绑定数据。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorage中的属性名。|
|defaultValue|T|是|-|当propName在LocalStorage中不存在时，使用defaultValue在LocalStorage中初始化对应的propName。|

**返回值：**

|类型|说明|
|:----|:----|
|[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#class-observedproperty)\<T>|ObservedProperty\<T>的实例，和LocalStorage中propName对应属性的单向绑定的数据。|

**示例：**

```cangjie
let storage = LocalStorage()
let tmp = storage.setOrCreate("PropA", 47)

let prop = storage.setAndProp('PropB', 49); // PropA -> 47, PropB -> 49
```

#### func setOrCreate\<T>(String, T)

```cangjie
public func setOrCreate<T>(propName: String, newValue: T): Bool
```

**功能：** 如果propName已经在LocalStorage中存在，并且newValue和propName对应属性的值不同，则设置propName对应属性的值为newValue，否则状态变量不会通知UI刷新propName对应属性的值。 如果propName不存在，则创建propName属性，值为newValue。setOrCreate只可以创建单个LocalStorage的键值对，如果想创建多个LocalStorage键值对，可以多次调用此方法。

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
|Bool|如果LocalStorage中存在propName，则更新其值为newValue，返回true。<br/>如果LocalStorage中不存在propName，则创建propName，并初始化其值为newValue，返回true。|

**示例：**

```cangjie
let storage = LocalStorage()
let res = storage.setOrCreate("PropA", 47)
let res1 = storage.setOrCreate("PropA", 48) // true
let res2 = storage.setOrCreate("PropB", 48) // true
```