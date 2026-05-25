## class MultiSlotsAdLoadListener

```cangjie
public class MultiSlotsAdLoadListener {
    public MultiSlotsAdLoadListener(
        public let onAdLoadSuccess: (adsMap: HashMap<String, Array<Advertisement>>) -> Unit,
        public let onAdLoadFailure: (errorCode: Int32, errorMsg: String) -> Unit
    )
}
```

**功能：** 多广告位广告请求回调。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

### let onAdLoadFailure

```cangjie
public let onAdLoadFailure:(errorCode: Int32, errorMsg: String) -> Unit
```

**功能：** 广告请求失败回调。

**类型：** (Int32, String)->Unit

**读写能力：** 只读

**起始版本：** 19

### let onAdLoadSuccess

```cangjie
public let onAdLoadSuccess:(adsMap: HashMap<String, Array<Advertisement>>) -> Unit
```

**功能：** 广告请求成功后回调。

**类型：** (HashMap\<String,Array\<[Advertisement](#class-advertisement)>>)->Unit

**读写能力：** 只读

**起始版本：** 19

### MultiSlotsAdLoadListener((adsMap:HashMap\<String,Array\<Advertisement>>) -> Unit, (errorCode:Int32,errorMsg:String) -> Unit)

```cangjie
public MultiSlotsAdLoadListener(
    public let onAdLoadSuccess: (adsMap: HashMap<String, Array<Advertisement>>) -> Unit,
    public let onAdLoadFailure: (errorCode: Int32, errorMsg: String) -> Unit
)
```

**功能：** 构造MultiSlotsAdLoadListener实例。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onAdLoadSuccess|(HashMap\<String,Array\<[Advertisement](#class-advertisement)>>)->Unit|是|-|广告请求成功后回调。|
|onAdLoadFailure|(Int32, String)->Unit|是|-|广告请求失败回调。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AdsKit.*
import std.collection.HashMap

let adloader: AdLoader = AdLoader(Global.getStageContext()) // 需获取Context应用上下文，详见本文使用说明
let onAdLoadSuccess = {ads: HashMap<String, Array<Advertisement>> => AppLog.info("callback success")}
let onAdLoadFailure = {errorCode: Int32, errorMsg: String => AppLog.error(errorMsg)}
let multiSlotsAdLoaderListener = MultiSlotsAdLoadListener(onAdLoadSuccess, onAdLoadFailure)
```