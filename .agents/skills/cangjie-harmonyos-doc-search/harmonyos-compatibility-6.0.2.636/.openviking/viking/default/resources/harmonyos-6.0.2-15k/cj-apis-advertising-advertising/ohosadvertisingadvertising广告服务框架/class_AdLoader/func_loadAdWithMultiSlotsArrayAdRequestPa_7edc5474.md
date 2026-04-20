### func loadAdWithMultiSlots(Array\<AdRequestParams>, AdOptions, MultiSlotsAdLoadListener)

```cangjie
public func loadAdWithMultiSlots(adParams: Array<AdRequestParams>,
                                 adOptions: AdOptions,
                                 listener: MultiSlotsAdLoadListener) : Unit
```

**功能：** 请求多广告位广告。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|adParams|Array\<[AdRequestParams](#class-adrequestparams)>|是|-|广告请求参数。|
|adOptions|[AdOptions](#class-adoptions)|是|-|广告配置。|
|listener|[MultiSlotsAdLoadListener](#class-multislotsadloadlistener)|是|-|请求广告回调监听。|

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
import std.collection.HashMap

let adloader: AdLoader = AdLoader(Global.getStageContext()) // 需获取Context应用上下文，详见本文使用说明
let onAdLoadSuccess = {ads: HashMap<String, Array<Advertisement>> => AppLog.info("callback success")}
let onAdLoadFailure = {errorCode: Int32, errorMsg: String => AppLog.error(errorMsg)}
let multiSlotsAdLoaderListener = MultiSlotsAdLoadListener(onAdLoadSuccess, onAdLoadFailure)
let param: Array<Parameter> = [Parameter("tagForUnderAgeOfPromise", AdValueType.INT(-1)),
    Parameter("allowMobileTraffic", AdValueType.INT(0))]
let adOptions: AdOptions = AdOptions(tagForChildProtection: -1, nonPersonalizedAd: 1, adContentClassification: "A",
    extraAttrs: param)
let adRequestParams: Array<AdRequestParams> = [AdRequestParams(adId: "testy63txaom86", adType: 3),
    AdRequestParams(adId: "testy63txaom86", adType: 3)]
try {
    adloader.loadAdWithMultiSlots(adRequestParams, adOptions, multiSlotsAdLoaderListener)
} catch (e: BusinessException) {
    AppLog.error("load multi ad failure")
}
```