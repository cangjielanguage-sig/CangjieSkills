### func asObject(JSContext) <sub>(deprecated)</sub>

```cangjie
public func asObject(_: JSContext): JSObject
```

**功能：** 把一个 JSValue 转换为 JSObject 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSObject](#class-jsobject)|一个 ArkTS object 引用。|

> **注意：**
>
> 当 JSValue 的类型不是 object 时，会抛出 JSTypeMisMatch 异常。比如在仓颉互操作ArkTS时，会把ArkTS的类型统一转换成 JSValue ，再通过 asObject 转换到仓颉类型，如果从ArkTS侧返回的类型不是实际类型，则会抛异常。

### func asPromise()

```cangjie
public func asPromise(): JSPromise
```

**功能：** 把一个 JSValue 转换为 JSPromise 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[JSPromise](#class-jspromise)|ArkTS promise的引用。|

### func asPromise(JSContext) <sub>(deprecated)</sub>

```cangjie
public func asPromise(_: JSContext): JSPromise
```

**功能：** 把一个 JSValue 转换为 JSPromise 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSPromise](#class-jspromise)|ArkTS promise的引用。|

### func asString()

```cangjie
public func asString(): JSString
```

**功能：**： 把一个 JSValue 转换为 JSString 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**返回值：**

|类型|说明|
|:----|:----|
|[JSString](#class-jsstring)|一个 ArkTS string的引用。|

### func asString(JSContext) <sub>(deprecated)</sub>

```cangjie
public func asString(_: JSContext): JSString
```

**功能：** 把一个 JSValue 转换为 JSString 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSString](#class-jsstring)|一个 ArkTS string的引用。|

### func asSymbol()

```cangjie
public func asSymbol(): JSSymbol
```

**功能：** 把一个 JSValue 转换为 JSSymbol 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[JSSymbol](#class-jssymbol)|一个 ArkTS symbol的引用。|

### func asSymbol(JSContext) <sub>(deprecated)</sub>

```cangjie
public func asSymbol(_: JSContext): JSSymbol
```

**功能：** 把一个 JSValue 转换为 JSSymbol 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSSymbol](#class-jssymbol)|一个 ArkTS symbol的引用。|

### func asUndefined()

```cangjie
public func asUndefined(): JSUndefined
```

**功能：** 把一个 JSValue 转换为 JSUndefined 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[JSUndefined](#struct-jsundefined)|一个ArkTS undefined。|