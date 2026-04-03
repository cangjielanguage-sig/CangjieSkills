### func link\<T>(String) where T <: JSInteropType \<T>

```cangjie
public func link<T>(propName: String): ObservedProperty<T> where T <: JSInteropType<T>
```

**功能：** 与[LocalStorageInterOp](#class-localstorageinterop)中对应的propName建立双向数据绑定。

> **说明：**
>
> - 双向绑定数据的修改会同步回[LocalStorageInterOp](#class-localstorageinterop)中，[LocalStorageInterOp](#class-localstorageinterop)会将变化同步到所有绑定该propName的数据和自定义组件中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorageInterOp中的属性名。|

**返回值：**

|类型|说明|
|:----|:----|
|[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#class-observedproperty)\<T>|双向绑定的数据。|

### func set\<T>(String, T) where T <: JSInteropType \<T>

```cangjie
public func set<T>(propName: String, value: T): Bool where T <: JSInteropType<T>
```

**功能：** 在[LocalStorageInterOp](#class-localstorageinterop)中设置propName对应属性的值。

> **说明：**
>
> 如果newValue的值和propName对应属性的值相同，即不需要做赋值操作，状态变量不会通知UI刷新propName对应属性的值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|[LocalStorageInterOp](#class-localstorageinterop)中的属性名。|
|value|T|是|-|属性值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果[LocalStorageInterOp](#class-localstorageinterop)中不存在propName对应的属性，或设值失败，则返回false。设置成功则返回true。|

### func setAndLink\<T>(String, T) where T <: JSInteropType \<T>

```cangjie
public func setAndLink<T>(propName: String, value: T): ObservedProperty<T> where T <: JSInteropType<T>
```

**功能：** 与[LocalStorageInterOp](#class-localstorageinterop)中对应的propName建立双向数据绑定。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|AppStorage中的属性名。|
|value|T|是|-|当propName在[LocalStorageInterOp](#class-localstorageinterop)中不存在时，使用defaultValue在[LocalStorageInterOp](#class-localstorageinterop)中初始化对应的propName。|

**返回值：**

|类型|说明|
|:----|:----|
|[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#class-observedproperty)\<T>|该propName对应的属性的双向绑定数据。|

### func setAndProp\<T>(String, T) where T <: JSInteropType \<T>

```cangjie
public func setAndProp<T>(propName: String, value: T): ObservedProperty<T> where T <: JSInteropType<T>
```

**功能：** 与[LocalStorageInterOp](#class-localstorageinterop)中对应的propName建立单向属性绑定。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|[LocalStorageInterOp](#class-localstorageinterop)中的属性名。|
|value|T|是|-|当propName在[LocalStorageInterOp](#class-localstorageinterop)中不存在时，使用defaultValue在[LocalStorageInterOp](#class-localstorageinterop)中初始化对应的propName|

**返回值：**

|类型|说明|
|:----|:----|
|[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#class-observedproperty)\<T>|单向绑定的数据。|