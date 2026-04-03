#### static func setAndLink\<T>(String, T)

```cangjie
public static func setAndLink<T>(key: String, defaultValue: T): ObservedProperty<T>
```

**功能：** 与link接口类似，如果给定的propName在AppStorage中存在，则返回该propName对应的属性的双向绑定数据。如果不存在，则使用defaultValue在AppStorage中创建和初始化propName对应的属性，返回其双向绑定数据。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|AppStorage中的属性名。|
|defaultValue|T|是|-|当propName在AppStorage中不存在时，使用defaultValue在AppStorage中初始化对应的propName。|

**返回值：**

|类型|说明|
|:----|:----|
|[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#class-observedproperty)\<T>|ObservedProperty\<T>的实例，与AppStorage中propName对应属性的双向绑定的数据。|

**示例：**

```cangjie
let a = AppStorage.setOrCreate("PropA", 47)
let link1 = AppStorage.setAndLink("PropB", 49) // Create PropB 49
let link2 = AppStorage.setAndLink("PropA", 50) // PropA exists, remains 47
```

#### static func setAndProp\<T>(String, T)

```cangjie
public static func setAndProp<T>(propName: String, defaultValue: T): ObservedProperty<T>
```

**功能：** 与Prop接口类似。如果给定的propName在AppStorage中存在，则返回该propName对应的属性的单向绑定数据。如果不存在，则使用defaultValue在AppStorage中创建和初始化propName对应的属性，返回其单向绑定数据。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|AppStorage中的属性名。|
|defaultValue|T|是|-|当propName在AppStorage中不存在时，使用defaultValue在AppStorage中初始化对应的propName，defaultValue不能为None。|

**返回值：**

|类型|说明|
|:----|:----|
|[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#class-observedproperty)\<T>|ObservedProperty\<T>的实例。|

#### static func setOrCreate\<T>(String, T)

```cangjie
public static func setOrCreate<T>(key: String, newValue: T): Unit
```

**功能：** 如果propName已经在AppStorage中存在，并且newValue和propName对应属性的值不同，则设置propName对应属性的值为newValue，否则状态变量不会通知UI刷新propName对应属性的值。

如果propName不存在，则创建propName属性，值为newValue。setOrCreate只可以创建单个AppStorage的键值对，如果想创建多个AppStorage键值对，可以多次调用此方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|AppStorage中的属性名。|
|newValue|T|是|-| 属性值。|

**示例：**

```cangjie
let a = AppStorage.setOrCreate("simpleProp", 121)
```

#### static func size()

```cangjie
public static func size(): Int64
```

**功能：** 返回AppStorage中的属性数量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int64|AppStorage中属性的数量。|

**示例：**

```cangjie
let tmp = AppStorage.setOrCreate("PropA", 47)
let res = AppStorage.clear()
```