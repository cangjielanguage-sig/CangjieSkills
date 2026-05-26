## class LocalStorageInterOp

```cangjie
public open class LocalStorageInterOp {}
```

**功能：** LocalStorage内部使用的类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### static func getOrCreate()

```cangjie
public static func getOrCreate(): LocalStorageInterOp
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[LocalStorageInterOp](#class-localstorageinterop)|获取或创建的LocalStorageInterOp对象。|

### func \`prop`\<T>(String) where T <: JSInteropType \<T>

```cangjie
public func `prop`<T>(propName: String): ObservedProperty<T> where T <: JSInteropType<T>
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorageInterOp中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#class-observedproperty)\<T>|-|

### func aboutToBeDeleted()

```cangjie
public func aboutToBeDeleted(): Bool
```

**功能：** 取消ObservedProperty实例对AppStorage/LocalStorage的单/双向同步关系，并无效化ObservedProperty实例，即当调用aboutToBeDeleted方法之后不能再使用ObservedProperty实例调用set或get方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|-|

### func clear()

```cangjie
public func clear(): Bool
```

**功能：** 删除[LocalStorageInterOp](#class-localstorageinterop)中所有属性。

> **说明：**
>
> - 删除所有属性的前提是，AppStorage已经没有任何订阅者。如果有订阅者，clear将不会生效并返回false。如果没有订阅者，则删除成功，并返回true。
> - 订阅者的含义参考[delete](#func-deletestring)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果LocalStorageInterOp中的属性已经没有订阅者则删除成功，返回true。否则返回false。|