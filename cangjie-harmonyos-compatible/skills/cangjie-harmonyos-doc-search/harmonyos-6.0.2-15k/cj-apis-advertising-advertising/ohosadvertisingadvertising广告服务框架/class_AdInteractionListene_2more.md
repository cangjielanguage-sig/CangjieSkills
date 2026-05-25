## class AdInteractionListener

```cangjie
public class AdInteractionListener {
    public AdInteractionListener(
        public let onStatusChanged: (status: String, ad: Advertisement, data: String) -> Unit
    )
}
```

**功能：** 广告状态变化回调。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

### let onStatusChanged

```cangjie
public let onStatusChanged:(status: String, ad: Advertisement, data: String) -> Unit
```

**功能：** 广告状态回调。

**类型：** (status: String, ad: [Advertisement](#class-advertisement), data: String)->Unit

**读写能力：** 只读

**起始版本：** 19

### AdInteractionListener((status:String,ad:Advertisement,data:String) -> Unit)

```cangjie
public AdInteractionListener(
    public let onStatusChanged: (status: String, ad: Advertisement, data: String) -> Unit
)
```

**功能：** 构造AdInteractionListener实例。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onStatusChanged|(status:String,ad : [Advertisement](#class-advertisement), data: String)->Unit|是|-|广告状态回调。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AdsKit.*

let onStatusChanged = {status: String, ad: Advertisement, data: String => AppLog.info("run success")}
let adInteractionListener: AdInteractionListener = AdInteractionListener(onStatusChanged)
```

## class AdLoadListener

```cangjie
public class AdLoadListener {
    public AdLoadListener(
        public let onAdLoadSuccess: (ads: Array<Advertisement>) -> Unit,
        public let onAdLoadFailure: (errorCode: Int32, errorMsg: String) -> Unit
    )
}
```

**功能：** 单广告位广告请求回调。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

### let onAdLoadFailure

```cangjie
public let onAdLoadFailure:(errorCode: Int32, errorMsg: String) -> Unit
```

**功能：** 广告请求失败回调。

**类型：** (Int32,String)->Unit

**读写能力：** 只读

**起始版本：** 19

### let onAdLoadSuccess

```cangjie
public let onAdLoadSuccess:(ads: Array<Advertisement>) -> Unit
```

**功能：** 广告请求成功后回调。

**类型：** (ads:Array\<[Advertisement](#class-advertisement)>)->Unit

**读写能力：** 只读

**起始版本：** 19

### AdLoadListener((ads:Array\<Advertisement>) -> Unit, (errorCode:Int32,errorMsg:String) -> Unit)

```cangjie
public AdLoadListener(
    public let onAdLoadSuccess: (ads: Array<Advertisement>) -> Unit,
    public let onAdLoadFailure: (errorCode: Int32, errorMsg: String) -> Unit
)
```

**功能：** 构造AdLoadListener实例。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onAdLoadSuccess|(ads:Array\<[Advertisement](#class-advertisement)>)->Unit|是|-|广告请求成功后回调。|
|onAdLoadFailure|(Int32,String)->Unit|是|-|广告请求失败回调。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AdsKit.*

let onAdLoadSuccess = {ad: Array<Advertisement> => AppLog.info("callback success")}
let onAdLoadFailure = {errorCode: Int32, errorMsg: String => AppLog.error("callback failure")}
let adLoaderListener = AdLoadListener(onAdLoadSuccess, onAdLoadFailure)
```