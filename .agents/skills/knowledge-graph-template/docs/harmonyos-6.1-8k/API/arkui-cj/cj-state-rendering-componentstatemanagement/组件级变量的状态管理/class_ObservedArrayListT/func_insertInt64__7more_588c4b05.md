### func insert(Int64, T)

```cangjie
public func insert(index: Int64, element: T): Unit
```

**功能：** 在状态管理数组列表指定位置插入元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|插入位置的索引。|
|element|T|是|-|要插入的元素。|

### func insertAll(Int64, Collection\<T>)

```cangjie
public func insertAll(index: Int64, elements: Collection<T>): Unit
```

**功能：** 在状态管理数组列表指定位置插入多个元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|插入位置的索引。|
|elements|Collection\<T>|是|-|要插入的元素集合。|

### func prepend(T)

```cangjie
public func prepend(element: T): Unit
```

**功能：** 在状态管理数组列表开头添加元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|element|T|是|-|要添加的元素。|

### func prependAll(Collection\<T>)

```cangjie
public func prependAll(elements: Collection<T>): Unit
```

**功能：** 在状态管理数组列表开头添加多个元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|elements|Collection\<T>|是|-|要添加的元素集合。|

### func remove(Int64)

```cangjie
public func remove(index: Int64): T
```

**功能：** 删除状态管理数组列表指定位置的元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|要删除元素的索引。|

**返回值：**

|类型|说明|
|:----|:----|
|T|被删除的元素。|

### func remove(Range\<Int64>)

```cangjie
public func remove(range: Range<Int64>): Unit
```

**功能：** 删除状态管理数组列表指定范围的元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|range|Range\<Int64>|是|-|要删除元素的范围。|

### func removeIf((T) -> Bool)

```cangjie
public func removeIf(predicate: (T) -> Bool): Unit
```

**功能：** 根据条件删除状态管理数组列表中的元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|predicate|(T) -> Bool|是|-|删除条件。|