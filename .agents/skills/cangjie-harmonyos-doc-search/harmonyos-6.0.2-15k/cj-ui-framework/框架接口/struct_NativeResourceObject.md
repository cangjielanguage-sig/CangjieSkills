## struct NativeResourceObject

```cangjie
public struct NativeResourceObject {
    public NativeResourceObject(
        public let bundleName: CString,
        public let moduleName: CString,
        public let id: Int32,
        public let resType: Int32,
        public let paramsJsonStr: CString
    )
}
```

**功能：** 框架内使用结构体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let bundleName

```cangjie
public let bundleName: CString
```

**功能：** UI框架使用。

**类型：** [CString](./cj-common-types.md#string)

**读写能力：** 只读

**起始版本：** 12

### let id

```cangjie
public let id: Int32
```

**功能：** UI框架使用。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let moduleName

```cangjie
public let moduleName: CString
```

**功能：** UI框架使用。

**类型：**  [CString](./cj-common-types.md#string)

**读写能力：** 只读

**起始版本：** 12

### let paramsJsonStr

```cangjie
public let paramsJsonStr: CString
```

**功能：** UI框架使用。

**类型：**  [CString](./cj-common-types.md#string)

**读写能力：** 只读

**起始版本：** 12

### let resType

```cangjie
public let resType: Int32
```

**功能：** UI框架使用。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### NativeResourceObject(CString, CString, Int32, Int32, CString)

```cangjie
public NativeResourceObject(
    public let bundleName: CString,
    public let moduleName: CString,
    public let id: Int32,
    public let resType: Int32,
    public let paramsJsonStr: CString
)
```

**功能：** 创建NativeResourceObject类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bundleName| [CString](./cj-common-types.md#string)|是|-|应用包名。|
|moduleName| [CString](./cj-common-types.md#string)|是|-|HAP的模块名。|
|id|Int32|是|-|资源ID。|
|resType|Int32|是|-|资源类型。|
|paramsJsonStr| [CString](./cj-common-types.md#string)|是|-|配置参数JSON字符串。|