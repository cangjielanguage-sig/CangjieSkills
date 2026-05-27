## class AdLoader

```cangjie
public class AdLoader {
    public init(context: StageContext)
}
```

**功能：** 提供加载广告的功能。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

### init(StageContext)

```cangjie
public init(context: StageContext)
```

**功能：** 构造AdLoader实例。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[StageContext](../../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext)|是|-|ability或application的上下文环境。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AdsKit.*

let adloader: AdLoader = AdLoader(Global.getStageContext()) // 需获取Context应用上下文，详见本文使用说明
```

### func loadAd(AdRequestParams, AdOptions, AdLoadListener)

```cangjie
public func loadAd(adParam: AdRequestParams, adOptions: AdOptions, listener: AdLoadListener) : Unit
```

**功能：** 请求单广告位广告。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|adParam|[AdRequestParams](#class-adrequestparams)|是|-|广告请求参数。|
|adOptions|[AdOptions](#class-adoptions)|是|-|广告配置。|
|listener|[AdLoadListener](#class-adloadlistener)|是|-|请求广告回调监听。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[advertising错误码](../../errorcodes/cj-errorcode-advertising.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |21800001|System internal error.|
  |21800003|Failed to load the ad request.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AdsKit.*
import kit.AdsKit.ValueType as AdValueType

let adloader: AdLoader = AdLoader(Global.getStageContext()) // 需获取Context应用上下文，详见本文使用说明
let onAdLoadSuccess = {ad: Array<Advertisement> => AppLog.info("callback success")}
let onAdLoadFailure = {errorCode: Int32, errorMsg: String => AppLog.error(errorMsg)}
let adLoaderListener = AdLoadListener(onAdLoadSuccess, onAdLoadFailure)
let param: Array<Parameter> = [Parameter("tagForUnderAgeOfPromise", AdValueType.INT(-1)),
    Parameter("allowMobileTraffic", AdValueType.INT(0))]
let adOptions: AdOptions = AdOptions(tagForChildProtection: -1, nonPersonalizedAd: 1, adContentClassification: "A",
    extraAttrs: param)
let adRequestParam: AdRequestParams = AdRequestParams(adId: "testy63txaom86", adType: 3)
try {
    adloader.loadAd(adRequestParam, adOptions, adLoaderListener)
} catch (e: BusinessException) {
    AppLog.error("load ad failure")
}
```