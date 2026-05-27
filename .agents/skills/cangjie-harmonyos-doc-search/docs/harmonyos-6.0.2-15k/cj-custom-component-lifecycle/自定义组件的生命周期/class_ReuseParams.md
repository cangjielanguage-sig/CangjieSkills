## class ReuseParams

```cangjie
public class ReuseParams {
    public init()
    public init(arr: Array<(String, Any)>)
}
```

**功能：** aboutToReuse生命周期函数的参数，开发者可以从中获取可复用组件的构造参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### prop size

```cangjie
public prop size
```

**功能：** 获取ReusePrams中存放的构造参数键值对数量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init()

```cangjie
public init()
```

**功能：** 创建一个ReuseParams对象，通常情况下开发者不会调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(Array\<(String, Any)>)

```cangjie
public init(arr: Array<(String, Any)>)
```

**功能：** 创建一个ReuseParams对象，通常情况下开发者不会调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 参数类型 | 必填 | 默认值 | 描述 |
| :--- | :--- | :--- | :--- | :--- |
| arr | Array\<(String, Any)> | 是 | - | 存放组件构造参数元组的数组。 |

### func get(String)

```cangjie
public func get(key: String): ?Any
```

**功能：** 通过key获取对应的构造参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 参数类型 | 必填 | 默认值 | 描述 |
| :--- | :--- | :--- | :--- | :--- |
| key | String | 是 | - | 构造参数的名称。 |

**返回值：**

| 类型 | 描述 |
| :--- | :--- |
| ?Any | 构造参数的值。|

### func contains(String)

```cangjie
public func contains(key: String): Bool
```

**功能：** 判断构造参数是否存在。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 参数类型 | 必填 | 默认值 | 描述 |
| :--- | :--- | :--- | :--- | :--- |
| key | String | 是 | - | 构造参数的名称。 |

**返回值：**

| 类型 | 描述 |
| :--- | :--- |
| Bool | true: 存在。false: 不存在。 |

### func add(String, Any)

```cangjie
public func add(key: String, value: Any): ?Any
```

**功能：** 添加构造参数键值对，通常情况下开发者不会调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 参数类型 | 必填 | 默认值 | 描述 |
| :--- | :--- | :--- | :--- | :--- |
| key | String | 是 | - | 构造参数的名称。 |
| value | Any | 是 | - | 构造参数的值。 |

**返回值：**

| 类型 | 描述 |
| :--- | :--- |
| ?Any | 构造参数的值。如果key已存在，该键的值将被新值替换，否则，返回Option\<Any>.None。|

### func aboutToRecycle()

```cangjie
protected open func aboutToRecycle()
```

**功能：** 组件的生命周期回调，在可复用组件从组件树上被加入到复用缓存之前调用。

**起始版本：** 12