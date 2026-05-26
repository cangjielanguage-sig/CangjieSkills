### func delete(String)

```cangjie
public func delete(propName: String): Bool
```

**功能：** 在[LocalStorageInterOp](#class-localstorageinterop)中删除propName对应的属性。

> **说明：**
>
> 在LocalStorageInterOp中删除该属性的前提是必须保证该属性没有订阅者。
> 属性的订阅者为：
>
> - [@StorageLink](../../../Dev_Guide/arkui-cj/state_management/cj-appstorage.md#storagelink)、[@StorageProp](../../../Dev_Guide/arkui-cj/state_management/cj-appstorage.md#storageprop)装饰的变量。
> - 通过[link](#func-linktstring-where-t--jsinteroptype-t)、[prop](#func-proptstring-where-t--jsinteroptype-t)、[setAndLink](#func-setandlinktstring-t-where-t--jsinteroptype-t)、[setAndProp](#func-setandproptstring-t-where-t--jsinteroptype-t)接口返回的SubscribedAbstractProperty的实例。
>
> 如果想要删除这些订阅者，可以通过以下方式：
>
> - 删除@StorageLink、@StorageProp所在的自定义组件。删除自定义组件请参考[自定义组件的删除](../../../Dev_Guide/arkui-cj/paradigm/cj-page-custom-components-lifecycle.md)。
> - 对link、prop、setAndLink、setAndProp接口返回的[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#class-observedproperty)的实例调用[aboutToBeDeleted](#func-abouttobedeleted)接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorageInterOp中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果[LocalStorageInterOp](#class-localstorageinterop)中有对应的属性，且该属性已经没有订阅者，则删除成功，返回true。如果属性不存在，或者该属性还存在订阅者，则返回false。|

### func get\<T>(String) where T <: JSInteropType \<T>

```cangjie
public func get<T>(propName: String): T where T <: JSInteropType<T>
```

**功能：** 获取propName在[LocalStorageInterOp](#class-localstorageinterop)中对应的属性值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|[LocalStorageInterOp](#class-localstorageinterop)中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|T|当前组件的实例。|

### func has(String)

```cangjie
public func has(propName: String): Bool
```

**功能：** 判断propName对应的属性是否在[LocalStorageInterOp](#class-localstorageinterop)中存在。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|[LocalStorageInterOp](#class-localstorageinterop)中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果propName对应的属性在[LocalStorageInterOp](#class-localstorageinterop)中存在，则返回true。不存在则返回false。|

### func hasChanged(JSContext, JSCallInfo)

```cangjie
public func hasChanged(context: JSContext, callInfo: JSCallInfo): JSValue
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是|-|互操作上下文。|
|callInfo|[JSCallInfo](../arkinterop/cj-apis-ark_interop.md#struct-jscallinfo)|是|-|ArkTS函数调用的相关信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](../arkinterop/cj-apis-ark_interop.md#class-jsvalue)|-|

### func keys()

```cangjie
public func keys()
```

**功能：** 返回LocalStorageInterOp中所有的属性名。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12