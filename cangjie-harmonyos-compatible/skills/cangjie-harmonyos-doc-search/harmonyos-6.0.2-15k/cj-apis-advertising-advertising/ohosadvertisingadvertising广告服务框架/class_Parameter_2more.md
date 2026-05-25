## class Parameter

```cangjie
public class Parameter {
    public Parameter(
        let key: String,
        let value: ValueType
    )
}
```

**功能：** 用于储存数据的键值对类型。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

### Parameter(String, ValueType)

```cangjie
public Parameter(
    let key: String,
    let value: ValueType
)
```

**功能：** 构造Parameter实例。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|键值。|
|value|[ValueType](#enum-valuetype)|是|-|值对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AdsKit.*
import kit.AdsKit.ValueType as AdValueType

let strV = AdValueType.STRING("Hello")
let intV = AdValueType.INT(11)
let boolV = AdValueType.BOOL(false)
let parameters: Array<Parameter> = [Parameter("123", strV), Parameter("321", intV), Parameter("231", boolV)]
let adRequestParam: AdRequestParams = AdRequestParams(adId: "testdsjkhd", extraAttrs: parameters)
```

## enum ValueType

```cangjie
public enum ValueType {
    | INT(Int32)
    | BOOL(Bool)
    | STRING(String)
    | ...
}
```

**功能：** 数据类型枚举。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

### BOOL(Bool)

```cangjie
BOOL(Bool)
```

**功能：** 表示值类型为布尔值。

**起始版本：** 19

### INT(Int32)

```cangjie
INT(Int32)
```

**功能：** 表示值类型为Int32整数。

**起始版本：** 19

### STRING(String)

```cangjie
STRING(String)
```

**功能：** 表示值类型为字符串。

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AdsKit.*
import kit.AdsKit.ValueType as AdValueType

let intV = AdValueType.INT(11)
let boolV = AdValueType.BOOL(false)
let strV = AdValueType.STRING("Hello")
```