#### func set(ObservedComplexAbstract)

```cangjie
public func set(newValue: ObservedComplexAbstract): Unit
```

**功能：** 通过ObservedComplexAbstract重置当前 ObservedArrayList 的值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|newValue|ObservedComplexAbstract|是|-|ObservedComplexAbstract数据，用来设置ObservedArrayList的值。|

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

**功能：** 操作符重载 - get。返回索引位置的元素的值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|表示 get 接口的索引。|

**返回值：**

|类型|说明|
|:----|:----|
|T|返回的索引位置元素的值。|

#### func [](Int64, T)

```cangjie
public operator func [](index: Int64, value!: T): Unit
```

**功能：** 操作符重载 - set，通过下标运算符用指定的元素替换此列表中指定位置的元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|要设置的索引值。|
|value|T|是|-| **命名参数。** 要设置的 T 类型的值。|