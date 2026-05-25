## class AppStorage

```cangjie
public class AppStorage {}
```

**功能：** AppStorage是应用全局的UI状态存储，是和应用的进程绑定的，由UI框架在应用程序启动时创建，为应用程序UI状态属性提供中央存储。与AppStorage中对应的propName建立单向属性绑定。如果给定的propName在AppStorage中存在，则返回与AppStorage中propName对应属性的单向绑定数据。如果AppStorage中不存在propName，则返回None。单向绑定数据的修改不会被同步回AppStorage中。

和页面级UI状态存储LocalStorage不同，AppStorage是应用级的全局UI状态存储，相当于整个应用的"中枢"，持久化数据PersistentStorage和环境变量Environment通过AppStorage中转，才可以和UI交互。

> **说明：**
>
> AppStorage仅支持纯仓颉场景，不支持用于ArkTS与仓颉混合开发场景。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### static func clear()

```cangjie
public static func clear(): Bool
```

**功能：** 删除AppStorage中所有的属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果AppStorage中的属性已经没有任何订阅者，则删除成功，并返回true。否则返回false。|

### static func delete(String)

```cangjie
public static func delete(propName: String): Bool
```

**功能：** 在AppStorage中删除propName对应的属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|AppStorage中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果AppStorage中存在对应的属性，且该属性已经没有任何订阅者，则删除成功，并返回true。否则返回false。|

### static func get\<T>(String)

```cangjie
public static func get<T>(propName: String): ?T
```

**功能：** 获取AppStorage中propName对应的属性值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|AppStorage中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|?T|返回AppStorage中对应属性的值，如果不存在则返回None。|

### static func has(String)

```cangjie
public static func has(propName: String): Bool
```

**功能：** 判断AppStorage中是否存在propName对应的属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|AppStorage中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果AppStorage中存在对应的属性，则返回true，否则返回false。|

### static func keys()

```cangjie
public static func keys(): EquatableCollection<String>
```

**功能：** 获取AppStorage中所有属性的键名。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|EquatableCollection\<String>|返回AppStorage中所有属性的键名集合。|

### static func link\<T>(String)

```cangjie
public static func link<T>(propName: String): ?ObservedProperty<T>
```

**功能：** 与AppStorage中对应的propName建立双向属性绑定。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|AppStorage中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|?ObservedProperty\<T>|返回双向绑定的数据，如果AppStorage中不存在对应的属性值，则返回None。|