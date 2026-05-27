#### func insertAll(Int64, Collection\<T>)

```cangjie
public func insertAll(index: Int64, elements: Collection<T>): Unit
```

**功能：** 从指定位置开始，将指定集合中的所有元素插入此 ObservedArrayList。函数会按照迭代器顺序遍历入参中的集合，并且将所有元素插入到指定位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|插入集合的目标索引。|
|elements|Collection\<T>|是|-|要插入的 T 类型元素集合。|

#### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

**功能：** 判断 ObservedArrayList 是否为空。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|判断 ObservedArrayList 是否为空。如果为空，返回true；如果不为空，返回false。|

#### func prepend(T)

```cangjie
public func prepend(element: T): Unit
```

**功能：** 将指定的元素附加到此 ObservedArrayList 的末尾。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|element|T|是|-|插入的元素。|

#### func prependAll(Collection\<T>)

```cangjie
public func prependAll(elements: Collection<T>): Unit
```

**功能：** 从起始位置开始，将指定集合中的所有元素插入此 ObservedArrayList。函数会按照迭代器顺序遍历入参中的集合，并且将所有元素插入到指定位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|elements|Collection\<T>|是|-|需要插入的元素的集合。|

#### func remove(Int64)

```cangjie
public func remove(index: Int64): T
```

**功能：** 删除此 ObservedArrayList 中指定位置的元素。返回被移除的元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|被删除元素的索引。|

**返回值：**

|类型|说明|
|:----|:----|
|T|被移除的元素。|

#### func remove(Range\<Int64>)

```cangjie
public func remove(range: Range<Int64>): Unit
```

**功能：** 删除此 ObservedArrayList 中 Range 范围所包含的所有元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|range|[Range](../apis/IMEKit/cj-apis-inputmethod.md#class-range)\<Int64>|是|-|需要被删除的元素的范围。|

#### func removeIf((T) -> Bool)

```cangjie
public func removeIf(predicate: (T) -> Bool): Unit
```

**功能：** 删除此 ObservedArrayList 中满足给定 lambda 表达式或函数的所有元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|predicate|(T)->Bool|是|-|判断删除的条件。|

#### func set(ArrayList\<T>)

```cangjie
public func set(newValue: ArrayList<T>): Unit
```

**功能：** 通过一个ArrayList数组重置当前 ObservedArrayList 的值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|newValue|ArrayList\<T>|是|-|ArrayList数组，用来设置 ObservedArrayList 的值。|

#### func set(Array\<T>)

```cangjie
public func set(newValue: Array<T>): Unit
```

**功能：** 通过一个Array数组重置当前 ObservedArrayList 的值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|newValue|Array\<T>|是|-|Array数组，用来设置 ObservedArrayList 的值。|