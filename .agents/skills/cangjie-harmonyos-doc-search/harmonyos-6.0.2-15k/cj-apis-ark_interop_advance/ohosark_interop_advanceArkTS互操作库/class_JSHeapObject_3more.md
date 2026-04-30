## class JSHeapObject

```cangjie
abstract sealed class JSHeapObject <: ForeignProxy {}
```

**功能：** 一个 ArkTS 运行时对象的强引用（但不会超过 ArkTS 运行时的生命周期，也不会阻止 ArkTS 运行时的销毁）。可以转换为JSValue。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**父类型：**

* ForeignProxy

它是所有安全引用的基类，用户不能创建它只能创建它的子类（隐藏构造函数），它的目标是让引用的 ArkTS 运行时对象持续时间超过这个仓颉对象本身。

### func toJSValue()

```cangjie
public func toJSValue(): JSValue
```

**功能：** 转换为 JSValue 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|ArkTS 统一类型。|

## class JSInteropException

```cangjie
public abstract class JSInteropException <: Exception {
    protected open func getClassName(): String
}
```

**功能：** 互操作异常基类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**父类型：**

* Exception

### func getClassName

```cangjie
protected open func getClassName(): String
```

**功能：** 获取类名。

**返回值：**

|类型|说明|
|:----|:----|
|String|类名。|

## class JSInteropNativeError

```cangjie
public class JSInteropNativeError <: JSInteropException {
    public init(message: String)
}
```

**功能：** 互操作C接口异常。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**父类型：**

* [JSInteropException](#class-jsinteropexception)

### init(String)

```cangjie
public init(message: String)
```

**功能：** 构造 JSInteropNativeError 对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|String|是|-|异常信息。|