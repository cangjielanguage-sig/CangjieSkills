## ObservedArray

用于进行状态管理的数组类型。

### class ObservedArray

```cangjie
public class ObservedArray<T> <: ObservedComplexAbstract & ArrayLike<T> {
    public init(initValue: Array<T>)
}
```

**功能：** 表示用于进行状态管理的数组类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- ObservedComplexAbstract
- ArrayLike\<T>

#### prop size

```cangjie
public prop size: Int64
```

**功能：** 获取状态管理数组的大小。

**类型：** Int64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(Array\<T>)

```cangjie
public init(initValue: Array<T>)
```

**功能：** 定义一个ObservedArray类型的数组。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|initValue|Array\<T>|是|-|状态管理数组类型的初始化值。|

#### func get()

```cangjie
public func get(): Array<T>
```

**功能：** 获取状态管理的数组元素集合。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Array\<T>|获取的状态管理数组集合。|

#### func set(Array\<T>)

```cangjie
public func set(newValue: Array<T>): Unit
```

**功能：** 设置状态管理数组类型的新数组值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|newValue|Array\<T>|是|-|状态管理数组被设置的新数组值。|

#### func set(ObservedComplexAbstract)

```cangjie
public func set(newValue: ObservedComplexAbstract): Unit
```

**功能：** 设置状态管理数组类型的新数组值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|newValue|ObservedComplexAbstract|是|-|状态管理数组被设置的新值。|

#### func subscribeInner(Observer)

```cangjie
public func subscribeInner(observer: Observer): Unit
```

**功能：** 对状态管理数组的每一项进行递归的观察绑定。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|observer|Observer|是|-|绑定的观察类。|

#### func unsubscribeInner(Observer)

```cangjie
public func unsubscribeInner(observer: Observer): Unit
```

**功能：** 对状态管理数组的每一项进行递归的解绑。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|observer|Observer|是|-|解绑的观察类。|

#### func \[](Int64)

```cangjie
public operator func [](index: Int64): T
```

**功能：** 读取数组中指定索引对应的数组项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|指定读取数组项的索引。|

**返回值：**

|类型|说明|
|:----|:----|
|T|数组中指定索引对应的数组项。|

#### func [](Int64, T)

```cangjie
public operator func [](index: Int64, value!: T): Unit
```

**功能：** 改变数组中指定索引对应的数组项的值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|指定数组项的索引。|
|value|T|是|-| **命名参数。** 指定索引对应的数组项的新值。|