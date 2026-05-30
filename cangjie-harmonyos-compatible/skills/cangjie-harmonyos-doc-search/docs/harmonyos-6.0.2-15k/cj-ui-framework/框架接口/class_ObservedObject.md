## class ObservedObject

```cangjie
public abstract class ObservedObject <: ObservedComplexAbstract {}
```

**功能：** 框架状态管理使用的基础类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- [ObservedComplexAbstract](#class-observedcomplexabstract)

### func addPublishVar(ObservedPropertyAbstract)

```cangjie
public func addPublishVar(publishVar: ObservedPropertyAbstract)
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|publishVar|[ObservedPropertyAbstract](#class-observedpropertyabstract)|是|-|-|

### func getPublishVar()

```cangjie
public func getPublishVar(): ArrayList<ObservedPropertyAbstract>
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|ArrayList\<[ObservedPropertyAbstract](#class-observedpropertyabstract)>|-|

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