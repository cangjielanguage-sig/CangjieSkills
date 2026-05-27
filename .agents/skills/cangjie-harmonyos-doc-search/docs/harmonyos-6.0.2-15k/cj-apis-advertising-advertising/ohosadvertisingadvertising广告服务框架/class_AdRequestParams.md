## class AdRequestParams

```cangjie
public class AdRequestParams {
    public AdRequestParams(
        public let adId!: String,
        public let adType!: ?UInt32 = None,
        public let adCount!: ?UInt32 = None,
        public let adWidth!: ?UInt32 = None,
        public let adHeight!: ?UInt32 = None,
        public let adSearchKeyword!: ?String = None,
        public let extraAttrs!: ?Array<Parameter> = None
    )
}
```

**功能：** 广告请求参数。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

### let adCount

```cangjie
public let adCount: ?UInt32 = None
```

**功能：** 请求的广告数量。

**类型：** ?UInt32

**读写能力：** 只读

**起始版本：** 19

### let adHeight

```cangjie
public let adHeight: ?UInt32 = None
```

**功能：** 广告位高度。

**类型：** ?UInt32

**读写能力：** 只读

**起始版本：** 19

### let adId

```cangjie
public let adId: String
```

**功能：** 广告位ID。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let adSearchKeyword

```cangjie
public let adSearchKeyword: ?String = None
```

**功能：** 广告关键字。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 19

### let adType

```cangjie
public let adType: ?UInt32 = None
```

**功能：** 请求的广告类型。<br>- 1：开屏广告。<br>- 3：原生广告。<br>- 7：激励广告。<br>- 8：banner广告。<br>- 12：插屏广告。<br>- 60：贴片广告。

**类型：** ?UInt32

**读写能力：** 只读

**起始版本：** 19

### let adWidth

```cangjie
public let adWidth: ?UInt32 = None
```

**功能：** 广告位宽度。

**类型：** ?UInt32

**读写能力：** 只读

**起始版本：** 19

### let extraAttrs

```cangjie
public let extraAttrs: ?Array<Parameter> = None
```

**功能：** 自定义参数。

**类型：** ?Array\<[Parameter](#class-parameter)>

**读写能力：** 只读

**起始版本：** 19

### AdRequestParams(String, ?UInt32, ?UInt32, ?UInt32, ?UInt32, ?String, ?Array\<Parameter>)

```cangjie
public AdRequestParams(
    public let adId!: String,
    public let adType!: ?UInt32 = None,
    public let adCount!: ?UInt32 = None,
    public let adWidth!: ?UInt32 = None,
    public let adHeight!: ?UInt32 = None,
    public let adSearchKeyword!: ?String = None,
    public let extraAttrs!: ?Array<Parameter> = None
)
```

**功能：** 构造AdRequestParams实例。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|adId|String|是|-| **命名参数。** 广告位ID。|
|adType|?UInt32|否|None| **命名参数。** 请求的广告类型。<br>- 1：开屏广告。<br>- 3：原生广告。<br>- 7：激励广告。<br>- 8：banner广告。<br>- 12：插屏广告。<br>- 60：贴片广告。|
|adCount|?UInt32|否|None| **命名参数。** 请求的广告数量。|
|adWidth|?UInt32|否|None| **命名参数。** 广告位宽度。|
|adHeight|?UInt32|否|None| **命名参数。** 广告位高度。|
|adSearchKeyword|?String|否|None| **命名参数。** 广告关键字。|
|extraAttrs|?Array\<[Parameter](#class-parameter)>|否|None| **命名参数。** 自定义参数。|

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