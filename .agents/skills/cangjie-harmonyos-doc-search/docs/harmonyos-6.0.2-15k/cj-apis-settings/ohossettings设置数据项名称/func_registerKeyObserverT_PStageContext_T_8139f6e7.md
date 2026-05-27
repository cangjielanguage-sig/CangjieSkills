## func registerKeyObserver\<T, P>(StageContext, T, P, Callback0Argument) where T <: ToStringP <: ToString

```cangjie
public func registerKeyObserver<T, P>(context: StageContext, name: T, domainName: P, observer: Callback0Argument): Bool where T <: ToString, P <: ToString
```

**功能：** 用于在指定上下文中注册一个观察者，以便于在指定域名中观察指定的域名。当该键值发生变化时，将调用注册的回调函数，如果成功注册则返回true，否则返回false。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[StageContext](../../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext)|是|-|应用上下文。context的获取方式请参见[getStageContext](../AbilityKit/cj-apis-ability.md#func-getstagecontextabilitycontext)。 |
|name|T|是|-|类型T需实现ToString接口。数据项的名称。数据项名称分为以下两种：<br> - 上述任意一个数据库中已存在的数据项。<br>- 开发者自行添加的数据项。|
|domainName|P|是|-|类型P需实现ToString 接口。指定要设置的域名<br> - domainName为DomainName.DEVICE_SHARED，<br>&nbsp;&nbsp;&nbsp;表示设备属性共享域。<br>- domainName为DomainName.USER_PROPRERTY，<br>&nbsp;&nbsp;&nbsp;表示为用户属性域。|
|observer|[Callback0Argument](../BasicServicesKit/cj-apis-base.md#class-callback0argument) |是|-|键值变化回调。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回设置数据项的观察者是否成功的结果，true表示设置成功，false表示设置失败。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*
import ohos.ability.*

// 此处代码可添加在依赖项定义中
class MyObserver <: Callback0Argument {
    let callback_: () -> Unit
    public init(callback: () -> Unit) {
        callback_ = callback
    }
    public open func invoke(): Unit {
        callback_()
    }
}

let ret = registerKeyObserver(getStageContext(Global.getAbilityContext()), Display.SCREEN_BRIGHTNESS_STATUS,
    DomainName.USER_PROPERTY, MyObserver({=> AppLog.info("Display SCREEN_BRIGHTNESS_STATUS changed.")})) // 需获取Context应用上下文，详见本文使用说明
```