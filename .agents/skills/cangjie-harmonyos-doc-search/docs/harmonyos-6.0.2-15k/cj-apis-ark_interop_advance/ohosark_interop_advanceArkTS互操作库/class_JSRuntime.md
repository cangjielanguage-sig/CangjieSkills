## class JSRuntime

```cangjie
public class JSRuntime {
    public init()
}
```

**功能：** 仓颉创建的 ArkTS 运行时。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

> **注意：**
>
> 仓颉应用中只能在主线程上使用 JSRuntime() 创建 ArkTS 运行时。

### prop mainContext

```cangjie
public prop mainContext: JSContext
```

**功能：** 互操作上下文。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**类型：** [JSContext](#class-jscontext)

**读写能力：** 只读

### init()

```cangjie
public init()
```

**功能：** 构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

### func getNapiEnv()

```cangjie
public func getNapiEnv(): CPointer<Unit>
```

**功能：** 获取环境指针。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

### func importFromEntry(String, String)

```cangjie
public func importFromEntry(entryPoint: String, importName: String): JSValue
```

**功能：** 从 ArkTS 文件里导入符号。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|entryPoint|String|是|-|ArkTS 文件的标签。|
|importName|String|是|-|要导入的符号。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|ArkTS统一类型。|

### func loadEntryFromAbc(String, String, Bool)

```cangjie
public func loadEntryFromAbc(abcPath: String, entryPoint: String, forceLoad!: Bool = false): Bool
```

**功能：** 加载一个 ArkTS 文件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|abcPath|String|是|-|abc文件的沙箱路径。|
|entryPoint|String|是|-|一个abc文件可以是由多个源码文件合成的，entryPoint与文件是一一对应的关系。|
|forceLoad|Bool|否|false| **命名参数。** 当一个abc被成功加载之后，重新加载时如果forceLoad为false，不会再次初始化其全局变量。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|是否成功。|