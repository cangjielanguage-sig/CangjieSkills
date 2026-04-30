### func build()

```cangjie
public func build(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func declareWatch\<T>(ObservedProperty\<T>, () -> Unit)

```cangjie
public func declareWatch<T>(propMember: ObservedProperty<T>, callBack: () -> Unit)
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propMember|[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#class-observedproperty)\<T>|是|-|-|
|callBack|()->Unit|是|-|-|

### func delayCompleteRerender(Bool)

```cangjie
public func delayCompleteRerender(deep: Bool)
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deep|Bool|是|-|-|

### func flushDelayCompleteRerender()

```cangjie
public func flushDelayCompleteRerender()
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### func forEachUpdateFunction\<T>(Int64, ArrayLike\<T>, (T,Int64) -> Unit, (T,Int64) -> String)

```cangjie
public func forEachUpdateFunction<T>(
    elmtId: Int64,
    arr: ArrayLike<T>,
    itemGenFunc!: (T, Int64) -> Unit,
    keyGeneratorFunc!: (T, Int64) -> String = { realData: T, idx: Int64 =>
        match(realData) {
            case realDataStr: ToString => idx.toString() + "_" + realDataStr.toString()
            case _ => idx.toString()
        }
    }
): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|elmtId|Int64|是|-|-|
|arr|[ArrayLike](#interface-arraylike)\<T>|是|-|-|
|itemGenFunc|(T,Int64)->Unit|是|-| **命名参数。** -|
|keyGeneratorFunc|(T,Int64)->String|否|{ realData: T, idx: Int64 => match(realData) {<br>case realDataStr: ToString => idx.toString() + "_" + realDataStr.toString()<br>case \_ => idx.toString()<br>} }| **命名参数。** -|

### func getLocalStorage()

```cangjie
public func getLocalStorage(): LocalStorage
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[LocalStorage](./cj-state-rendering-appstatemanagement.md#class-localstorage)|-|

### func id()

```cangjie
public func id(): Int64
```

**功能：** 设置目标控件id属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回指定目标控件id属性的对象。|

### func ifElseBranchUpdateFunction(Int32, () -> Unit)

```cangjie
public func ifElseBranchUpdateFunction(branchId: Int32, branchFunc: () -> Unit)
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|branchId|Int32|是|-|-|
|branchFunc|()->Unit|是|-|-|

### func initializeConsume(String)

```cangjie
public func initializeConsume(name: String): ObservedPropertyAbstract
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|-|

**返回值：**

|类型|说明|
|:----|:----|
|[ObservedPropertyAbstract](#class-observedpropertyabstract)|-|