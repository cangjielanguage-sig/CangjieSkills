## class ObservedComplexAbstract

```cangjie
public abstract class ObservedComplexAbstract <: Observable {}
```

**功能：** 框架状态管理使用的基础类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- [Observable](#class-observable)

### func addPropsInfo(String)

```cangjie
public func addPropsInfo(info: String): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|info|String|是|-|属性信息。|

### func getInfo()

```cangjie
public func getInfo(): String
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|信息值。|

### func getPropsInfo()

```cangjie
public func getPropsInfo(): ArrayList<String>
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|ArrayList\<String>|属性信息数组。|

### func inheritObservers(ArrayList\<Observer>)

```cangjie
public func inheritObservers(newObservers: ArrayList<Observer>)
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|newObservers|ArrayList\<[Observer](#interface-observer)>|是|-|观察者列表。|

### func notifyChanges()

```cangjie
public func notifyChanges()
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func set(ObservedComplexAbstract)

```cangjie
public func set(v: ObservedComplexAbstract): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|v|[ObservedComplexAbstract](#class-observedcomplexabstract)|是|-|-|

### func setDependentElementIds(ArrayList\<Int64>)

```cangjie
public func setDependentElementIds(dependentElementIds: ArrayList<Int64>)
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dependentElementIds|ArrayList\<Int64>|是|-|-|

### func setInfo(String)

```cangjie
public func setInfo(info: String)
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|info|String|是|-|-|

### func subscribeInner(Observer)

```cangjie
public func subscribeInner(observer: Observer): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|observer|[Observer](#interface-observer)|是|-|观察者。|

### func unsubscribeInner(Observer)

```cangjie
public func unsubscribeInner(observer: Observer): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|observer|[Observer](#interface-observer)|是|-|观察者。|