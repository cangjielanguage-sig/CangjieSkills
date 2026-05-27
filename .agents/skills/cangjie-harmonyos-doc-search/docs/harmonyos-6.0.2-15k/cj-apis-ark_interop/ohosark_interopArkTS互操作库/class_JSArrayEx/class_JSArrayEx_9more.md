## class JSArrayEx

```cangjie
public class JSArrayEx<T> <: JSInteropType<JSArrayEx<T>> where T <: JSInteropType <T> {
    public init(arr: Array<T>)
}
```

**功能：** 在声明式互操作宏中使用，对应ArkTS的 Array\<T> 类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**父类型：**

* [JSInteropType\<JSArrayEx\<T>>](#interface-jsinteroptype)

### prop size

```cangjie
public prop size: Int64
```

**功能：** 获取元素数量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**类型：** Int64

**读写能力：** 只读

### init(Array\<T>)

```cangjie
public init(arr: Array<T>)
```

**功能：** 给定 Array\<T>，构造对应的 JSArrayEx\<T> 实例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arr|Array\<T>|是|-|根据该 Array 实例创建。|

### static func fromJSValue(JSContext, JSValue)

```cangjie
public static func fromJSValue(context: JSContext, input: JSValue): JSArrayEx<T>
```

**功能：** 从 JSValue 转换为 JSArrayEx。声明式互操作宏框架场景使用，开发者不需要使用此API。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|
|input|[JSValue](#struct-jsvalue)|是|-|ArkTS 统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSArrayEx](#class-jsarrayex)\<T>|声明式互操作宏类型 JSArrayEx。|

### static func toArkTsType()

```cangjie
public static func toArkTsType(): String
```

**功能：** 获取仓颉类型对应的ArkTS类型名称。声明式互操作宏框架场景使用，开发者不需要使用此API。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后 ArkTS 类型名。|

### func clone()

```cangjie
public func clone(): JSArrayEx<T>
```

**功能：** 克隆 JSArrayEx，将对 JSArrayEx 数据进行深拷贝。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[JSArrayEx](#class-jsarrayex)\<T>|克隆得到的新 JSArrayEx。|

### func concat(JSArrayEx\<T>)

```cangjie
public func concat(other: JSArrayEx<T>): JSArrayEx<T>
```

**功能：** 该函数将创建一个新的 JSArrayEx，内容是当前 JSArrayEx 后面串联 other 指向的 JSArrayEx。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[JSArrayEx](#class-jsarrayex)\<T>|是|-|串联到末尾的 JSArrayEx。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSArrayEx](#class-jsarrayex)\<T>|串联得到的新 JSArrayEx。|

### func get(Int64)

```cangjie
public func get(index: Int64): Option<T>
```

**功能：** 获取数组中下标 index 对应的元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|要获取的值的下标。|

**返回值：**

|类型|说明|
|:----|:----|
|Option\<T>|当前数组中下标 index 对应的值。|

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

**功能：** 判断数组是否为空。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果数组为空，返回 true，否则，返回 false。|