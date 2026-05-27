## class SubscriberManager

```cangjie
public class SubscriberManager {}
```

**功能：** 框架状态管理使用的基础类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### static func getInstance()

```cangjie
public static func getInstance(): SubscriberManager
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[SubscriberManager](#class-subscribermanager)|订阅管理器。|

### func add(Observer)

```cangjie
public func add(value: Observer): Bool
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Observer](#interface-observer)|是|-|观察者。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|-|

### func delete(Observer)

```cangjie
public func delete(value: Observer): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Observer](#interface-observer)|是|-|观察者。|

### func dumpSubscriberInfo()

```cangjie
public func dumpSubscriberInfo(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func get(Int64)

```cangjie
public func get(id: Int64): Option<Observer>
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|Int64|是|-|观察者id。|

**返回值：**

|类型|说明|
|:----|:----|
|[Option](#initoptioncustomview-optionlocalstorage)\<[Observer](#interface-observer)>|观察者。|

### func has(Int64)

```cangjie
public func has(id: Int64): Bool
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|Int64|是|-|观察者id。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|判断结果。|

### func makeId()

```cangjie
public func makeId(): Int64
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int64|id。|

### func sizeOfManager()

```cangjie
public func sizeOfManager(): Int64
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int64|管理器大小。|