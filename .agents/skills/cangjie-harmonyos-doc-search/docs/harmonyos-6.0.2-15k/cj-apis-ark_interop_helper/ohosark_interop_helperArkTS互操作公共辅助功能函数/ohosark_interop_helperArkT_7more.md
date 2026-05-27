# ohos.ark_interop_helper（ArkTS互操作公共辅助功能函数）

提供一些公共的辅助功能函数。

## 导入模块

```cangjie
import ohos.ark_interop_helper.*
```

## func arkTsValuetoNapiValue(napi_env, JSValue)

```cangjie
public func arkTsValuetoNapiValue(env: napi_env, ark_value: JSValue): napi_value
```

**功能：** 将 JSValue 类型转化为 napi_value 类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|env|[napi_env](cj-apis-ark_interop.md#type-napi_env)|是|-|环境上下文。|
|ark_value|[JSValue](cj-apis-ark_interop.md#struct-jsvalue)|是|-|需要转换的值。|

**返回值：**

|类型|说明|
|:----|:----|
|[napi_value](cj-apis-ark_interop.md#type-napi_value)|转化的 napi_value 值。|

## func getContextStageMode(napi_env, napi_value)

```cangjie
public func getContextStageMode(env: napi_env, object: napi_value): StageContext
```

**功能：** 根据napi环境、对象信息获取应用上下文。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|env|[napi_env](cj-apis-ark_interop.md#type-napi_env)|是|-|环境信息。|
|object|[napi_value](cj-apis-ark_interop.md#type-napi_value)|是|-|napi值信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[StageContext](#type-stagecontext)|获取到的应用上下文。|

## func getJSContext(JSRuntime, UIAbilityContext)

```cangjie
public func getJSContext(runtime: JSRuntime, abilityContext: UIAbilityContext): JSValue
```

**功能：** 根据运行时信息获取ArkTS UIAbiltiy的上下文。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|runtime|[JSRuntime](cj-apis-ark_interop.md#class-jsruntime)|是|-|ArkTS 运行时对象。|
|abilityContext|UIAbilityContext|是|-|仓颉 UIAbiltiy 上下文信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](cj-apis-ark_interop.md#struct-jsvalue)|获取到的 ArkTS UIAbiltiy 上下文。|

## func isStageMode(napi_env, napi_value)

```cangjie
public func isStageMode(env: napi_env, context: napi_value): Bool
```

**功能：** 判断是否处于应用模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|env|[napi_env](cj-apis-ark_interop.md#type-napi_env)|是|-|环境信息。|
|context|[napi_value](cj-apis-ark_interop.md#type-napi_value)|是|-|上下文信息。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|是否处于应用模式。|

## func mapFromJSValue\<T>(JSContext, JSValue, (JSContext,JSValue) -> T)

```cangjie
public func mapFromJSValue<T>(
    context: JSContext,
    value: JSValue,
    convert: (JSContext, JSValue) -> T
): ?HashMap<String, T>
```

**功能：** 把 JSValue 格式的数据转换成 HashMap 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](cj-apis-ark_interop.md#class-jscontext)|是|-|互操作上下文。|
|value|[JSValue](cj-apis-ark_interop.md#struct-jsvalue)|是|-|需要转换的 JSValue 数据。|
|convert|([JSContext](cj-apis-ark_interop.md#class-jscontext), [JSValue](cj-apis-ark_interop.md#struct-jsvalue))->T|是|-|把 JSValue 当作一个 HashMap 后，获取这个 HashMap 的 key 对应的 value 转换成 T。|

**返回值：**

|类型|说明|
|:----|:----|
|?HashMap\<String, T>|转换后的 HashMap 数据。|