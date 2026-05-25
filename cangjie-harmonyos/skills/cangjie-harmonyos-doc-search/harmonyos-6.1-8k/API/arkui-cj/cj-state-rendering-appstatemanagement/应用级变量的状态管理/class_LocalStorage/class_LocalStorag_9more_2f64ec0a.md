## class LocalStorage

```cangjie
public class LocalStorage {
    public init()
}
```

**功能：** LocalStorage是页面级的UI状态存储，通过装饰器和AppStorage进行交互。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init()

```cangjie
public init()
```

**功能：** LocalStorage的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func clear()

```cangjie
public func clear(): Bool
```

**功能：** 删除LocalStorage中所有的属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果LocalStorage中的属性已经没有任何订阅者，则删除成功，并返回true。否则返回false。|

### func delete(String)

```cangjie
public func delete(propName: String): Bool
```

**功能：** 在LocalStorage中删除propName对应的属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorage中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果LocalStorage中存在对应的属性，且该属性已经没有任何订阅者，则删除成功，并返回true。否则返回false。|

### func get\<T>(String)

```cangjie
public func get<T>(propName: String): ?T
```

**功能：** 获取LocalStorage中propName对应的属性值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorage中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|?T|返回LocalStorage中对应属性的值，如果不存在则返回None。|

### func has(String)

```cangjie
public func has(propName: String): Bool
```

**功能：** 判断LocalStorage中是否存在propName对应的属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorage中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果LocalStorage中存在对应的属性，则返回true，否则返回false。|

### func keys()

```cangjie
public func keys(): EquatableCollection<String>
```

**功能：** 获取LocalStorage中所有属性的键名。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|EquatableCollection\<String>|返回LocalStorage中所有属性的键名集合。|

### func link\<T>(String)

```cangjie
public func link<T>(propName: String): ?ObservedProperty<T>
```

**功能：** 与LocalStorage中对应的propName建立双向属性绑定。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorage中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|?ObservedProperty\<T>|返回双向绑定的数据，如果LocalStorage中不存在对应的属性值，则返回None。|

### func property\<T>(String)

```cangjie
public func property<T>(propName: String): ?ObservedProperty<T>
```

**功能：** 与LocalStorage中对应的propName建立单向属性绑定。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorage中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|?ObservedProperty\<T>|返回单向绑定的数据，如果LocalStorage中不存在对应的属性值，则返回None。|