### func requireArkModule(String)

```cangjie
public func requireArkModule(path: String): JSValue
```

**功能：** 导入一个ArkTS模块，包括系统模块、HAP模块里的文件、HAR模块里的文件、HSP模块里的文件和Native模块，详见[在仓颉代码里导入ArkTS模块](../../learn-cj/FFI/cangjie-arkts/cangjie-load-arkts.md)。

**起始版本：** 23

**参数：**

| 参数名 | 类型   | 必填 | 默认值 | 说明         |
| :----- | :----- | :--- | :----- | :----------- |
| path   | String | 是   | -      | 模块标识符。 |

**返回值：**

| 类型                      | 说明                     |
| :------------------------ | :----------------------- |
| [JSValue](#class-jsvalue) | 返回ArkTS模块的JSValue。 |

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                                          |
| :------- | :---------------------------------------------------------------- |
| 34300002 | Module initialize fail.                                           |
| 34300004 | Thread mismatch.                                                  |
| 34300006 | Target module not exist.                                          |
| 34300007 | Can not requireArkModule during initializing cangjie module.      |
| 34300008 | Current application have not support requireArkModule of the url. |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog
import ohos.business_exception.BusinessException

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    try {
        let hilog = context.requireArkModule("@ohos.hilog").asObject()
        hilog.callMethod("info", [
            context.number(0).toJSValue(),
            context.string("test").toJSValue(),
            context.string("call hilog success").toJSValue()
        ])
    } catch (e: BusinessException) {
        Hilog.info(0, "test", e.message)
    }
    return context.undefined().toJSValue()
}
```

### func requireSystemNativeModule(String, ?String)

```cangjie
public func requireSystemNativeModule(moduleName: String, prefix!: ?String = None): JSValue
```

**功能：** 加载系统内置的 ArkTS napi 模块。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|moduleName|String|是|-|ArkTS napi 模块的注册名称|
|prefix|?String|否|None| **命名参数。** ArkTS napi 模块的归档目录，在 /system/lib64/module 下可省，在子目录下是子目录名称|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|模块返回值，一般是一个对象，如果加载出错将会返回 undefined|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002   | Outside error occurred.                |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
func doSth(context: JSContext): Unit {
    let hilog = context.requireSystemNativeModule("hilog")
    let pushService = context.requireSystemNativeModule("core.push.pushService", prefix: "hms")
}
```

### func string(String)

```cangjie
public func string(value: String): JSString
```

**功能：** 创建一个 ArkTS string。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|仓颉字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSString](#class-jsstring)|ArkTS 字符串引用。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002   | Outside error occurred.                |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let result = context.string("abc")
    return result.toJSValue()
}
```