## class Advertisement

```cangjie
public class Advertisement {
    public Advertisement(
        public let adType: UInt32,
        public let uniqueId: String,
        public let rewarded: Bool,
        public let shown: Bool,
        public let clicked: Bool,
        public let rewardVerifyConfig: HashMap<String, String>,
        public let extraAttrs: Array<Parameter>
    )
}
```

**功能：** 请求的广告内容。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

### let adType

```cangjie
public let adType: UInt32
```

**功能：** 广告类型。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let clicked

```cangjie
public let clicked: Bool
```

**功能：** 广告是否被点击。

- true：被点击。

- false：未被点击。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let extraAttrs

```cangjie
public let extraAttrs: Array<Parameter>
```

**功能：** 自定义参数。

- isFullScreen：类型Bool。开屏广告自定义参数，用于标识返回的广告是否为全屏，true为全屏广告，false为半屏广告。

**类型：** Array\<[Parameter](#class-parameter)>

**读写能力：** 只读

**起始版本：** 19

### let rewardVerifyConfig

```cangjie
public let rewardVerifyConfig: HashMap<String, String>
```

**功能：** 服务器验证参数。

**类型：** HashMap\<String, String>

**读写能力：** 只读

**起始版本：** 19

### let rewarded

```cangjie
public let rewarded: Bool
```

**功能：** 广告是否获得奖励。

- true：获得奖励。

- false：没有获得奖励。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let shown

```cangjie
public let shown: Bool
```

**功能：** 广告是否展示。

- true：展示。

- false：未展示。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let uniqueId

```cangjie
public let uniqueId: String
```

**功能：** 广告唯一标识。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### Advertisement(UInt32, String, Bool, Bool, Bool, HashMap\<String,String>, Array\<Parameter>)

```cangjie
public Advertisement(
    public let adType: UInt32,
    public let uniqueId: String,
    public let rewarded: Bool,
    public let shown: Bool,
    public let clicked: Bool,
    public let rewardVerifyConfig: HashMap<String, String>,
    public let extraAttrs: Array<Parameter>
)
```

**功能：** 构造Advertisement实例。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|adType|UInt32|是|-|广告类型。|
|uniqueId|String|是|-|广告唯一标识。|
|rewarded|Bool|是|-|广告是否获得奖励。<br>- true：获得奖励。<br>- false：没有获得奖励。|
|shown|Bool|是|-|广告是否展示。<br>- true：展示。<br>- false：未展示。|
|clicked|Bool|是|-|广告是否被点击。<br>- true：被点击。<br>- false：未被点击。|
|rewardVerifyConfig|HashMap\<String, String>|是|-|服务器验证参数。<br>{<br>customData: "test",userId: "12345"<br>}|
|extraAttrs|Array\<[Parameter](#class-parameter)>|是|-|可选自定义参数。<br>- isFullScreen：类型boolean。开屏广告自定义参数，用于标识返回的广告是否为全屏，true为全屏广告，false为半屏广告。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AdsKit.*
import std.collection.HashMap

let rr = HashMap<String, String>()
rr.add("customData", "test")
let advertisement: Advertisement = Advertisement(3, "32138728", false, false, false, rr, Array<Parameter>())
```