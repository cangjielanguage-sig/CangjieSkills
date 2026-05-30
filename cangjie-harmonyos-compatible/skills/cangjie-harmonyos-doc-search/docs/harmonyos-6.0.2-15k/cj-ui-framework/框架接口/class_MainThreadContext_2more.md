## class MainThreadContext

```cangjie
public class MainThreadContext <: ThreadContext {}
```

**功能：** 框架使用的线程上下文。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func end()

```cangjie
public func end(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func hasEnded()

```cangjie
public func hasEnded(): Bool
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|-|

## class Observable

```cangjie
public open class Observable {}
```

**功能：** 框架状态管理使用的基础类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func isSubscribed(Observer)

```cangjie
public func isSubscribed(observer: Observer): Bool
```

**功能：** 判断观察者是否订阅，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|observer|[Observer](#interface-observer)|是|-|观察者。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|订阅结果。|

### func numberOfSubscribers()

```cangjie
public func numberOfSubscribers(): Int64
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int64|观察者数量。|

### func subscribe(Observer)

```cangjie
public func subscribe(observer: Observer): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|observer|[Observer](#interface-observer)|是|-|观察者。|

### func unsubscribe(Observer)

```cangjie
public func unsubscribe(observer: Observer): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|observer|[Observer](#interface-observer)|是|-|观察者。|

### func unsubscribeAll()

```cangjie
public func unsubscribeAll(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12