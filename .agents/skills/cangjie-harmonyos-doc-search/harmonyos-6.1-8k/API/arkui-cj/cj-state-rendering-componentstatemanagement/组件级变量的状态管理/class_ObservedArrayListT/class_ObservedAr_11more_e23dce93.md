## class ObservedArrayList\<T>

```cangjie
public class ObservedArrayList<T> <:  CollectionEx<T> {
    public init(initValue: ArrayList<T>)
    public init(initValue: Array<T>)
}
```

**功能：** 表示用于进行状态管理的数组列表类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [CollectionEx](./cj-common-types.md#interface-collectionext)\<T>

### prop size

```cangjie
public prop size: Int64
```

**功能：** 获取状态管理数组列表的大小。

**类型：** Int64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(ArrayList\<T>)

```cangjie
public init(initValue: ArrayList<T>)
```

**功能：** 定义一个ObservedArrayList类型的数组列表。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|initValue|ArrayList\<T>|是|-|状态管理数组列表类型的初始化值。|

### init(Array\<T>)

```cangjie
public init(initValue: Array<T>)
```

**功能：** 定义一个ObservedArrayList类型的数组列表。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|initValue|Array\<T>|是|-|状态管理数组列表类型的初始化值。|

### operator func [](Int64)

```cangjie
public operator func [](index: Int64): T
```

**功能：** 通过索引获取数组列表中的元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|元素索引。|

**返回值：**

|类型|说明|
|:----|:----|
|T|指定索引位置的元素。|

### operator func [](Int64, T)

```cangjie
public operator func [](index: Int64, value!: T): Unit
```

**功能：** 通过索引设置数组列表中的元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|元素索引。|
|value|T|是|-| **命名参数。** 要设置的元素值。|

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

**功能：** 判断状态管理数组列表是否为空。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|状态管理数组列表是否为空。|

### func clone()

```cangjie
public func clone(): ObservedArrayList<T>
```

**功能：** 克隆状态管理数组列表。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[ObservedArrayList](#class-observedarraylistt)\<T>|克隆的状态管理数组列表。|

### func clear()

```cangjie
public func clear(): Unit
```

**功能：** 清空状态管理数组列表。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func append(T)

```cangjie
public func append(element: T): Unit
```

**功能：** 在状态管理数组列表末尾添加元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|element|T|是|-|要添加的元素。|

### func appendAll(Collection\<T>)

```cangjie
public func appendAll(elements: Collection<T>): Unit
```

**功能：** 在状态管理数组列表末尾添加多个元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|elements|Collection\<T>|是|-|要添加的元素集合。|