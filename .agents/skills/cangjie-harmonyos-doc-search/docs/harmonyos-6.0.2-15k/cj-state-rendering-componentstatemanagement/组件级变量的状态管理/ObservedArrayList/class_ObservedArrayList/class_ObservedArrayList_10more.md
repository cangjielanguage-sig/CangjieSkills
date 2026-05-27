### class ObservedArrayList

```cangjie
public class ObservedArrayList<T> <: ObservedComplexAbstract & ArrayLike<T> {
    public init(initValue: ArrayList<T>)
    public init(initValue: Array<T>)
}
```

**功能：** 用于进行ArrayList数据状态管理的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- ObservedComplexAbstract
- ArrayLike\<T>

#### prop size

```cangjie
public prop size: Int64
```

**功能：** 此 ObservedArrayList 中的元素个数。

**类型：** Int64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(ArrayList\<T>)

```cangjie
public init(initValue: ArrayList<T>)
```

**功能：** 构造一个包含指定Array数组中所有元素的 ObservedArrayList。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|initValue|ArrayList\<T>|是|-|ArrayList数组,用来初始化ObservedArrayList。|

#### init(Array\<T>)

```cangjie
public init(initValue: Array<T>)
```

**功能：** 构造一个包含指定Array数组中所有元素的 ObservedArrayList。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|initValue|Array\<T>|是|-|Array数组,用来初始化ObservedArrayList。|

#### func append(T)

```cangjie
public func append(element: T): Unit
```

**功能：** 将指定的元素附加到此 ObservedArrayList 的末尾。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|element|T|是|-|插入的元素。|

#### func appendAll(Collection\<T>)

```cangjie
public func appendAll(elements: Collection<T>): Unit
```

**功能：** 将指定集合中的所有元素附加到此 ObservedArrayList 的末尾。函数会按照迭代器顺序遍历入参中的集合，并且将所有元素插入到此 ObservedArrayList 的尾部。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|elements|Collection\<T>|是|-| 需要插入的元素的集合。|

#### func clear()

```cangjie
public func clear(): Unit
```

**功能：** 从此 ObservedArrayList 中删除所有元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func clone()

```cangjie
public func clone(): ObservedArrayList<T>
```

**功能：** 返回此 ObservedArrayList 实例的拷贝(浅拷贝)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[ObservedArrayList](#class-observedarraylist)\<T>|此 ObservedArrayList 实例的拷贝(浅拷贝)。|

#### func get()

```cangjie
public func get(): ArrayList<T>
```

**功能：** 返回一个ArrayList数组，其中包含此 ObservedArrayList 中按正确顺序排列的所有元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|ArrayList\<T>|返回的ArrayList数组。|

#### func insert(Int64, T)

```cangjie
public func insert(index: Int64, element: T): Unit
```

**功能：** 在此 ObservedArrayList 中的指定位置插入指定元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|插入元素的目标索引。|
|element|T|是|-|要插入的 T 类型元素。|