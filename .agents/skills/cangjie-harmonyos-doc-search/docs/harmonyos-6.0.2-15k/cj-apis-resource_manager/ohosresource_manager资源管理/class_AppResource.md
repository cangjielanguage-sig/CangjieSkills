## class AppResource

```cangjie
public class AppResource <: Length & ResourceColor {
    public AppResource(
        public let bundleName: String,
        public let moduleName: String,
        public let id: Int32,
        public let params!: ?Array<Any> = None,
        public let resType!: ?Int32 = None
    )
}
```

**功能：** 表示资源类型。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 19

**父类型：**

- [Length](../../arkui-cj/cj-common-types.md#interface-length)
- [ResourceColor](../../arkui-cj/cj-common-types.md#interface-resourcecolor)

### let bundleName

```cangjie
public let bundleName: String
```

**功能：** 应用的包名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let id

```cangjie
public let id: Int32
```

**功能：** 资源id。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let moduleName

```cangjie
public let moduleName: String
```

**功能：** 应用的模块名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let params

```cangjie
public let params: ?Array<Any> = None
```

**功能：** 其他资源参数（可选）。

**类型：** ?Array\<Any>

**读写能力：** 只读

**起始版本：** 19

### let resType

```cangjie
public let resType: ?Int32 = None
```

**功能：** 资源的类型（可选）。

**类型：** ?Int32

**读写能力：** 只读

**起始版本：** 19

### AppResource(String, String, Int32, ?Array\<Any>, ?Int32)

```cangjie
public AppResource(
    public let bundleName: String,
    public let moduleName: String,
    public let id: Int32,
    public let params!: ?Array<Any> = None,
    public let resType!: ?Int32 = None
)
```

**功能：** 构造资源类型对象。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bundleName|String|是|-|应用的包名称。|
|moduleName|String|是|-|应用的模块名称。|
|id|Int32|是|-|资源id。|
|params|?Array\<Any>|否|None| **命名参数。** 其他资源参数。|
|resType|?Int32|否|None| **命名参数。** 资源的类型。|