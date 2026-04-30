### func set(Int64, T)

```cangjie
public func set(index: Int64, element: T): Unit
```

**功能：** 修改数组中下标 index 对应的值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|需要修改的值的下标，取值范围为 [0..this.size]。|
|element|T|是|-|修改的目标值。|

### func toArray()

```cangjie
public func toArray(): Array<T>
```

**功能：** 转换为 Array。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Array\<T>|转换后的仓颉数组。|

### func toJSValue(JSContext)

```cangjie
public func toJSValue(context: JSContext): JSValue
```

**功能：** 转换为 JSValue。声明式互操作宏框架场景使用，开发者不需要使用此API。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|ArkTS 统一类型。|

### func \[](Int64)

```cangjie
public operator func[](index: Int64): T
```

**功能：** 获取数组下标 index 对应的值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|要获取的值的下标。|

**返回值：**

|类型|说明|
|:----|:----|
|T|当前数组中下标 index 对应的值。|

### func \[](Int64, T)

```cangjie
public operator func[](index: Int64, value!: T)
```

**功能：** 修改数组中下标 index 对应的值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|需要修改的值的下标，取值范围为 [0..this.size]。|
|value|T|是|-| **命名参数。** 修改的目标值。|