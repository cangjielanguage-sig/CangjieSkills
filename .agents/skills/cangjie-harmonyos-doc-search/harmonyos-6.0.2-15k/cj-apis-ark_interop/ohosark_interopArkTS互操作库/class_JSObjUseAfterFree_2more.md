## class JSObjUseAfterFree

```cangjie
public class JSObjUseAfterFree <: JSInteropException {
    public init(message!: String = "use after free")
}
```

**功能：** 生命周期异常。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**父类型：**

* [JSInteropException](#class-jsinteropexception)

### init(String)

```cangjie
public init(message!: String = "use after free")
```

**功能：** 构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|String|否|"use after free"| **命名参数。** 异常消息。|

## class JSObject

```cangjie
public class JSObject <: JSObjectBase {}
```

**功能：** 一个ArkTS对象的安全引用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**父类型：**

* [JSObjectBase](#class-jsobjectbase)