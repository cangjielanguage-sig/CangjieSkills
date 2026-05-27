## class JSHashMapEx

```cangjie
public class JSHashMapEx<K, V> <: JSInteropType<JSHashMapEx<K,V>> where K <: JSKeyable & Hashable & Equatable <K> & JSInteropType <K>V <: JSInteropType <V> {
    public init(map: HashMap<K, V>)
    public init()
}
```

**功能：** 在声明式互操作宏中使用，对应ArkTS的 Map 类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**父类型：**

* [JSInteropType\<JSHashMapEx\<K,V>>](#interface-jsinteroptype)

### prop size

```cangjie
public prop size: Int64
```

**功能：** 返回键值对的个数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**类型：** Int64

**读写能力：** 只读

### init(HashMap\<K,V>)

```cangjie
public init(map: HashMap<K, V>)
```

**功能：** 构造空的 JSHashMapEx\<K, V> 实例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|map|HashMap\<K, V>|是|-|根据该 HashMap 实例创建。|

### init()

```cangjie
public init()
```

**功能：** 构造空的 JSHashMapEx\<K, V> 实例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

### static func fromJSValue(JSContext, JSValue)

```cangjie
public static func fromJSValue(context: JSContext, input: JSValue): JSHashMapEx<K, V>
```

**功能：** 从 JSValue 转换为 JSHashMapEx。声明式互操作宏框架场景使用，开发者不需要使用此API。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|
|input|[JSValue](#struct-jsvalue)|是|-|ArkTS 统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSHashMapEx](#class-jshashmapex)\<K, V>|声明式互操作宏类型 JSHashMapEx。|

### static func toArkTsType()

```cangjie
public static func toArkTsType(): String
```

**功能：** 获取仓颉类型对应的ArkTS类型名称。声明式互操作宏框架场景使用，开发者不需要使用此API。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后 ArkTS 类型名。|

### func clear()

```cangjie
public func clear(): Unit
```

**功能：** 从此 HashMapEx 中移除所有元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

### func clone()

```cangjie
public func clone(): JSHashMapEx<K, V>
```

**功能：** 克隆 JSHashMapEx，将对 JSHashMapEx 数据进行深拷贝。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|[JSHashMapEx](#class-jshashmapex)\<K, V>|克隆得到的新 JSHashMapEx。|

### func containsAll(Collection\<K>)

```cangjie
public func containsAll(keys: Collection<K>): Bool
```

**功能：** 判断是否包含指定集合中所有键的映射。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|keys|Collection\<K>|是|-|键传递待判断的 keys。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果都包含，则返回 true；否则，返回 false。|

### func contiansAll(Collection\<K>) <sub>(deprecated)</sub>

```cangjie
public func contiansAll(keys: Collection<K>): Bool
```

**功能：** 判断是否包含指定集合中所有键的映射。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|keys|Collection\<K>|是|-|键传递待判断的 keys。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果都包含，则返回 true；否则，返回 false。|