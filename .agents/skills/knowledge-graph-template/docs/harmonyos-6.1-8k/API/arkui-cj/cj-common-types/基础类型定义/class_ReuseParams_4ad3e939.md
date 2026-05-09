## class ReuseParams

```cangjie
public class ReuseParams {
    public init(arr: Array<(String, Any)>)
}
```

**功能：** aboutToReuse生命周期函数的参数，开发者可以从中获取可复用组件的构造参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(Array\<(String, Any)>)

```cangjie
public init(arr: Array<(String, Any)>)
```

**功能：** 创建一个ReuseParams对象，通常情况下开发者不会调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arr|Array\<(String, Any)>|是|-|存放组件构造参数元组的数组。|

### func get\<T>(String)

```cangjie
public func get<T>(key: String): ?T
```

**功能：** 通过key获取对应的构造参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|构造参数的名称。|

**返回值：**

|类型|说明|
|:----|:----|
|?T|构造参数的值。|