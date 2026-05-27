# ohos.advertising.advertising（广告服务框架）

本模块提供广告操作能力，包括请求广告、展示广告。

## 导入模块

```cangjie
import kit.AdsKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func getAdRequestBody(Array\<AdRequestParams>, AdOptions)

```cangjie
public func getAdRequestBody(adParams: Array<AdRequestParams>, adOptions: AdOptions): String
```

**功能：** 请求广告响应体。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|adParams|Array\<[AdRequestParams](#class-adrequestparams)>|是|-|广告请求参数。|
|adOptions|[AdOptions](#class-adoptions)|是|-|广告配置。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回字符串类型的广告数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[advertising错误码](../../errorcodes/cj-errorcode-advertising.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Invalid input parameter. Possible causes: 1. Mandatory parameters are left unspecified.|
  |801|Device not supported.|
  |21800004|System internal error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AdsKit.*

let adReqParamsArr: Array<AdRequestParams> = [AdRequestParams(adId: "testu7m3hc4gvm", adType: 3, adCount: 2,adWidth: 100, adHeight: 100)]
let adOptions: AdOptions = AdOptions(tagForChildProtection: -1, nonPersonalizedAd: 1, adContentClassification: "A")
try {
    let body: String = getAdRequestBody(adReqParamsArr, adOptions)
    AppLog.error(body)
} catch (e: BusinessException) {
    AppLog.info("get request ad body fail")
}
```

## func showAd(Advertisement, AdDisplayOptions, ?StageContext)

```cangjie
public func showAd(advertisement: Advertisement,
                   adDisplayoptions: AdDisplayOptions,
                   context: ?StageContext): Unit
```

**功能：** 展示全屏广告。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|advertisement|[Advertisement](#class-advertisement)|是|-|广告对象。|
|adDisplayoptions|[AdDisplayOptions](#class-addisplayoptions)|是|-|广告展示参数。|
|context|?[StageContext](../../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext)|是|-|UIAbility的上下文环境|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[advertising错误码](../../errorcodes/cj-errorcode-advertising.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |21800001|System internal error.|
  |21800004|Failed to display the ad.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AdsKit.*
import std.collection.HashMap

let adDisplayOptions: AdDisplayOptions = AdDisplayOptions(mute: false)
try {
    showAd(Advertisement(3, "32138728", false, false, false, HashMap<String, String>(), Array<Parameter>()),
            adDisplayOptions, Global.getStageContext()) // 需获取Context应用上下文，详见本文使用说明
    } catch (e: BusinessException) {
    AppLog.error("show ad failure")
}
```