## func mapToJSValue\<T>(JSContext, ?HashMap\<String,T>, (JSContext,T) -> JSValue)

```cangjie
public func mapToJSValue<T>(
    context: JSContext,
    parameter: ?HashMap<String, T>,
    convert: (JSContext, T) -> JSValue
): JSValue
```

**功能：** 把 HashMap 格式的数据转换成 JSValue 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](cj-apis-ark_interop.md#class-jscontext)|是|-|互操作上下文。|
|parameter|?HashMap\<String, T>|是|-|需要转换的 HashMap 数据。|
|convert|([JSContext](cj-apis-ark_interop.md#class-jscontext), T)->[JSValue](cj-apis-ark_interop.md#struct-jsvalue)|是|-|把 HashMap 的 T 转换成 JSValue。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](cj-apis-ark_interop.md#struct-jsvalue)|转换后的 JSValue 数据。|

## type FAContext

```cangjie
public type FAContext = CPointer<Unit>
```

**功能：** FAContext 是 CPointer\<Unit> 类型的别名。

## type StageContext

```cangjie
public type StageContext = CPointer<Unit>
```

**功能：** StageContext 是 CPointer\<Unit> 类型的别名。