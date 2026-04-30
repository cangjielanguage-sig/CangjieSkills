### class PersistentStorage

```cangjie
public class PersistentStorage <: Observer {}
```

**功能：** 用于提供状态变量持久化的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- [Observer](./cj-ui-framework.md#interface-observer)

#### static func deleteProp(String)

```cangjie
public static func deleteProp(key: String): Unit
```

**功能：** 将key对应的属性从PersistentStorage中删除。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|PersistentStorage中的属性名。|

**示例：**

```cangjie
PersistentStorage.deleteProp("Name")
```

#### static func keys()

```cangjie
public static func keys(): EquatableCollection<String>
```

**功能：** 返回所有持久化属性的属性名的集合。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|EquatableCollection\<String>|返回所有持久化属性的属性名的集合。|

**示例：**

```cangjie
let keys = PersistentStorage.keys()
```

#### static func persistProp\<T>(String, T)

```cangjie
public static func persistProp<T>(key: String, defaultValue: T): Unit
```

**功能：** 将AppStorage中key对应的属性持久化到文件中。该接口的调用通常在访问AppStorage之前。

确定属性的类型和值的顺序如下：

1. 如果PersistentStorage文件中存在key对应的属性，在AppStorage中创建对应的propName，并用在PersistentStorage中找到的key的属性初始化。

2. 如果PersistentStorage文件中没有查询到key对应的属性，则在AppStorage中查找key对应的属性。如果找到key对应的属性，则将该属性持久化。

3. 如果AppStorage中也没查找到key对应的属性，则在AppStorage中创建key对应的属性。用defaultValue初始化其值，并将该属性持久化。

根据上述的初始化流程，如果AppStorage中有该属性，则会使用其值，覆盖掉PersistentStorage文件中的值。由于AppStorage是内存内数据，该行为会导致数据丧失持久化能力。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|属性名。|
|defaultValue|T|是|-|在PersistentStorage和AppStorage中未查询到时，则使用默认值进行初始化。|

**示例：**

```cangjie
let a = PersistentStorage.persistProps([("A", "a"), ("B", "b")])
```

#### static func persistProps\<T>(Array\<(String,T)>)

```cangjie
public static func persistProps<T>(properties: Array<(String, T)>): Unit
```

**功能：** 行为和persistProp类似，不同在于可以一次性持久化多个数据，适合在应用启动的时候初始化。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|properties|Array\<(String,T)>|是|-|持久化数据数组，数组元素以元组(key, defaultValue)形式体现。|