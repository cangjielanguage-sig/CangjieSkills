## struct ReqPermissionDetail

```cangjie
public struct ReqPermissionDetail {
    public var name: String
    public var moduleName: String
    public var reason: String
    public var reasonId: Int32
    public var usedScene: UsedScene
    public init(name: String, moduleName: String, reason: String, reasonId: Int32, usedScene: UsedScene)
}
```

**功能：** 应用运行时需向系统申请的权限集合的详细信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### var moduleName

```cangjie
public var moduleName: String
```

**功能：** 申请该权限的module名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var name

```cangjie
public var name: String
```

**功能：** 需要使用的权限名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var reason

```cangjie
public var reason: String
```

**功能：** 描述申请权限的原因。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var reasonId

```cangjie
public var reasonId: Int32
```

**功能：** 描述申请权限的原因ID。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

### var usedScene

```cangjie
public var usedScene: UsedScene
```

**功能：** 权限使用的场景和时机。

**类型：** [UsedScene](#struct-usedscene)

**读写能力：** 可读写

**起始版本：** 12

### init(String, String, String, Int32, UsedScene)

```cangjie
public init(name: String, moduleName: String, reason: String, reasonId: Int32, usedScene: UsedScene)
```

**功能：** 创建应用运行时需向系统申请的权限集合的详细信息对象。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|需要使用的权限名称。|
|moduleName|String|是|-|申请该权限的module名称。|
|reason|String|是|-|描述申请权限的原因。|
|reasonId|Int32|是|-|描述申请权限的原因ID。|
|usedScene|[UsedScene](#struct-usedscene)|是|-|权限使用的场景和时机。|