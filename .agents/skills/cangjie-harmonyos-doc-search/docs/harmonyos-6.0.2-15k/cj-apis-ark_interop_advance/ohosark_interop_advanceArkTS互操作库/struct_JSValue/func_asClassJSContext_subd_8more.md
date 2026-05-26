### func asClass(JSContext) <sub>(deprecated)</sub>

```cangjie
public func asClass(_: JSContext): JSClass
```

**功能：** 把一个 JSValue 转换为 JSClass 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSClass](#class-jsclass)|一个ArkTS 类的引用。|

### func asExternal()

```cangjie
public func asExternal(): JSExternal
```

**功能：** 把一个 JSValue 转换为 JSExternal 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[JSExternal](#class-jsexternal)|一个 ArkTS 对仓颉对象引用的引用。|

### func asExternal(JSContext) <sub>(deprecated)</sub>

```cangjie
public func asExternal(_: JSContext): JSExternal
```

**功能：** 把一个 JSValue 转换为 JSExternal 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSExternal](#class-jsexternal)|一个 ArkTS 对仓颉对象引用的引用。|

### func asFunction()

```cangjie
public func asFunction(): JSFunction
```

**功能：** 把一个 JSValue 转换为 JSFunction 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[JSFunction](#class-jsfunction)|一个 ArkTS 函数的引用。|

### func asFunction(JSContext) <sub>(deprecated)</sub>

```cangjie
public func asFunction(_: JSContext): JSFunction
```

**功能：** 把一个 JSValue 转换为 JSFunction 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSFunction](#class-jsfunction)|一个 ArkTS 函数的引用。|

### func asNull()

```cangjie
public func asNull(): JSNull
```

**功能：** 把一个 JSValue 转换为 JSNull 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[JSNull](#struct-jsnull)|一个 ArkTS null|

### func asNumber()

```cangjie
public func asNumber(): JSNumber
```

**功能：** 把一个 JSValue 转换为 JSNumber 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[JSNumber](#struct-jsnumber)|一个 ArkTS number。|

### func asObject()

```cangjie
public func asObject(): JSObject
```

**功能：** 把一个 JSValue 转换为 JSObject 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[JSObject](#class-jsobject)|一个 ArkTS object 引用。|

> **注意：**
>
> 当 JSValue 的类型不是 object 时，会抛出 JSTypeMisMatch 异常。比如在仓颉互操作ArkTS时，会把ArkTS的类型统一转换成 JSValue ，再通过 asObject 转换到仓颉类型，如果从ArkTS侧返回的类型不是实际类型，则会抛异常。