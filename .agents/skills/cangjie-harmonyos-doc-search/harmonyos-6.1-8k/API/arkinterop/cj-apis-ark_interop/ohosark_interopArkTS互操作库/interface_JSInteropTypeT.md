## interface JSInteropType\<T>

```cangjie
public interface JSInteropType<T> {
    static func fromJSValue(context: JSContext, input: JSValue): T
    func toJSValue(context: JSContext): JSValue
    static func toArktsType(): String
}
```

**功能：** 该接口为支持声明式互操作宏的类型提供扩展方法。此接口仅供声明式互操作宏框架内部使用，开发者无需直接调用。

如下类型扩展了此接口：

- 被@Interop[ArkTS]修饰的用户自定义class

- 被@Interop[ArkTS]修饰的用户自定义interface

**起始版本：** 22

**示例：**

<!--compile-->
```cangjie
@Interop[ArkTS]
public class MyCustomClass {
    public let name: String   // String实现了JSInteropType<String>，所以可以在这里使用。
    public let age: Int64     // Int64实现了JSInteropType<Int64>，所以可以在这里使用。

    public init(name: String, age: Int64) {
        this.name = name
        this.age = age
    }
}
```

### static func fromJSValue(JSContext, JSValue)

```cangjie
static func fromJSValue(context: JSContext, input: JSValue): T
```

**功能：** 将 JSValue 类型数据转换为相应的仓颉类型。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|
|input|[JSValue](#class-jsvalue)|是|-|ArkTS 统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|T|仓颉类型。|

### static func toArktsType()

```cangjie
static func toArktsType(): String
```

**功能：** 获取仓颉类型对应的ArkTS类型名称。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后 ArkTS 类型名。|

### func toJSValue(JSContext)

```cangjie
func toJSValue(context: JSContext): JSValue
```

**功能：** 将仓颉类型数据转换为JSValue。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|ArkTS 统一类型。|