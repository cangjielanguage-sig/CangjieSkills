## class CJResource

```cangjie
public class CJResource {
    public var id: Int64
    public var ty: UInt32
    public var params: String
    public init(id: Int64, ty: UInt32, params: String)
}
```

**功能：** 系统资源，框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var id

```cangjie
public var id: Int64
```

**功能：** 资源的id值。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var ty

```cangjie
public var ty: UInt32
```

**功能：** 资源的类型。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var params

```cangjie
public var params: String
```

**功能：** 其他资源参数。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(Int64, UInt32, String)

```cangjie
public init(id: Int64, ty: UInt32, params: String)
```

**功能：** 创建CJResource类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|Int64|是|-|资源的id值。|
|ty|UInt32|是|-|资源的类型。|
|params|String|是|-|其他资源参数。|

## class CallbackCJWebResourceRequest

```cangjie
public class CallbackCJWebResourceRequest <: BaseCallBack {}
```

**功能：** 用于提供框架调用的回调函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func invoke(Int32, CPointer\<CPointer\<Unit>>, CPointer\<Unit>)

```cangjie
public func invoke(argc: Int32, argv: CPointer<CPointer<Unit>>, res: CPointer<Unit>): Unit
```

**功能：** 触发回调函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|argc|Int32|是|-|参数数量。|
|argv|CPointer\<CPointer\<Unit>>|是|-|参数列表。|
|res|CPointer\<Unit>|是|-|返回值。|

## class ContainerBase

```cangjie
public abstract class ContainerBase <: ViewBase {}
```

**功能：** UI框架使用的组件基础类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- [ViewBase](#class-viewbase)

### func initial()

```cangjie
public open override func initial()
```

**功能：** 初始化方法，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12