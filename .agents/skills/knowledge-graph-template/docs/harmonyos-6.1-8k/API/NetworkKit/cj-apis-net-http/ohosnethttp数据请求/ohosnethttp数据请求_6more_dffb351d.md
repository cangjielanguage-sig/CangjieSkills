# ohos.net.http（数据请求）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

http模块提供HTTP数据请求能力。应用可以通过HTTP发起一个数据请求，支持常见的GET、POST、OPTIONS、HEAD、PUT、DELETE、TRACE、CONNECT方法。

## 导入模块

```cangjie
import kit.NetworkKit.*
```

## 权限列表

ohos.permission.INTERNET

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。

## func createHttp()

```cangjie
public func createHttp(): HttpRequest
```

**功能：** 创建一个HTTP请求，里面包括发起请求、中断请求、订阅/取消订阅HTTP Response Header事件。当发起多个HTTP请求时，需为每个HTTP请求创建对应HttpRequest对象。每一个HttpRequest对象对应一个HTTP请求。

> **说明：**
>
> 当该请求使用完毕时，需调用destroy方法主动销毁HttpRequest对象，否则会出现资源泄露问题。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[HttpRequest](#class-httprequest)|返回一个HttpRequest对象，里面包括request、requestInStream、destroy、on和off方法。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let httpRequest = createHttp()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## func createHttpResponseCache(UInt32)

```cangjie
public func createHttpResponseCache(cacheSize!: UInt32 = MAX_CACHE_SIZE): HttpResponseCache
```

**功能：** 创建一个HttpResponseCache对象，可用于存储HTTP请求的响应数据。对象中可调用[flush](#func-flush)与[delete](#delete)方法，cacheSize指定缓存大小。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cacheSize|UInt32|否|MAX_CACHE_SIZE|**命名参数。** 缓存大小。最大为10\*1024\*1024（10MB），默认最大。|

**返回值：**

|类型|说明|
|:----|:----|
|[HttpResponseCache](#class-httpresponsecache)|返回一个存储HTTP访问请求响应的对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let httpResponseCache = createHttpResponseCache()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```