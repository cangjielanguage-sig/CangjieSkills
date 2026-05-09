## class JSModule

```cangjie
public class JSModule {}
```

**功能：** 一个提供导出符号注册接口的静态类。

JSModule的目标是提供符号导出能力（导出到ArkTS）。配合自定义静态初始化函数，在动态库被加载时把导出目标注册到全局表，并由ArkTS引擎来执行导出。

**起始版本：** 22

### static func registerClass(String, ClassRegister)

```cangjie
public static func registerClass(name: String, register: ClassRegister): Unit
```

**功能：** 注册一个要导出到 ArkTS 的 ArkTS 类（构造函数）。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|导出名称。|
|register|[ClassRegister](#type-classregister)|是|-|一个返回 ArkTS 类的函数。|

**示例：**

<!--compile-->
```cangjie
class Main {
    static init() {
        JSModule.registerClass("SomeClass") { context =>
            let ctor: JSLambda = { context, callInfo =>
                return callInfo.thisArg
            }
            context.clazz(ctor)
        }
    }
}
```

### static func registerFunc(String, FuncRegister)

```cangjie
public static func registerFunc(name: String, register: FuncRegister): Unit
```

**功能：** 注册一个要导出到 ArkTS 的函数。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|导出函数名称。|
|register|[FuncRegister](#type-funcregister)|是|-|一个返回 JSFunction 的函数。|

**示例：**

<!--compile-->
```cangjie
class Main {
    static init() {
        JSModule.registerFunc("doSth") { context, callInfo =>
            return context.undefined().toJSValue()
        }
    }
}
```

### static func registerFunc(String, JSLambda)

```cangjie
public static func registerFunc(name: String, lambda: JSLambda): Unit
```

**功能：** 注册一个要导出到 ArkTS 的函数。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|导出函数名称。|
|lambda|[JSLambda](#type-jslambda)|是|-|要导出的函数。|

**示例：**

<!--compile-->
```cangjie
class Main {
    static init() {
        JSModule.registerFunc("doSth") { context, callInfo =>
            return context.undefined().toJSValue()
        }
    }
}
```

### static func registerModule(ModuleRegister)

```cangjie
public static func registerModule(register: ModuleRegister): Unit
```

**功能：** 注册要导出到 ArkTS 接口。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|register|[ModuleRegister](#type-moduleregister)|是|-|一个能够返回 ArkTS 类（构造函数）的函数。|

**示例：**

<!--compile-->
```cangjie
class Main {
    static init() {
        JSModule.registerModule { context, exports =>
            exports["doSth"] = context.function { context, callInfo =>
                context.undefined().toJSValue()
            }.toJSValue()
        }
    }
}
```