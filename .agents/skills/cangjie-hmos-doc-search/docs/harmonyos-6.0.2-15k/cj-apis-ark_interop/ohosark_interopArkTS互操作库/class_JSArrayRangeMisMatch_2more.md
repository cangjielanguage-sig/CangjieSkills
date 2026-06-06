## class JSArrayRangeMisMatch

```cangjie
public class JSArrayRangeMisMatch <: JSInteropException {
    public init(min: Int64, max: Int64, given: Int64, message!: String = "js array range mismatch")
}
```

**功能：** 访问越界异常。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**父类型：**

* [JSInteropException](#class-jsinteropexception)

### init(Int64, Int64, Int64, String)

```cangjie
public init(min: Int64, max: Int64, given: Int64, message!: String = "js array range mismatch")
```

**功能：** 构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|min|Int64|是|-|有效值的下限。|
|max|Int64|是|-|有效值的上限（不包含）。|
|given|Int64|是|-|当前值。|
|message|String|否|"js array range mismatch"| **命名参数。** 异常消息。|

## class JSBigInt

```cangjie
public class JSBigInt <: JSHeapObject {}
```

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**功能：** JSBigInt 对象用来表示 JS bigint 类型的安全引用。通过创建 JS bigint 对象，可以转换为仓颉 Int64，转换为仓颉 BigInt。

**父类型：**

* [JSHeapObject](#class-jsheapobject)

### func toBigInt()

```cangjie
public func toBigInt(): BigInt
```

**功能：** 转换为仓颉 BigInt。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|BigInt|仓颉 BigInt。|