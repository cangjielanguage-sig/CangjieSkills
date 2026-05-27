## class PermissionAnd

```cangjie
public class PermissionAnd <: PermissionValue {
    public const init(lhs: PermissionValue, rhs: PermissionValue)
}
```

**功能：** 表示若干个权限的与。

**起始版本：** 19

**父类型：**

- [PermissionValue](#interface-permissionvalue)

### init(PermissionValue, PermissionValue)

```cangjie
public const init(lhs: PermissionValue, rhs: PermissionValue)
```

**功能：** 构造PermissionAnd与权限集，表示两个权限集的与。

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|lhs|[PermissionValue](#interface-permissionvalue)|是|-|构造与权限集的一个权限集。|
|rhs|[PermissionValue](#interface-permissionvalue)|是|-|构造与权限集的另一个权限集。|

### func &(PermissionValue)

```cangjie
public const override operator func &(rhs: PermissionValue): PermissionValue
```

**功能：** 和另一个权限集与。返回与操作后的权限集。

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rhs|[PermissionValue](#interface-permissionvalue)|是|-|与操作的另一个权限集。|

**返回值：**

|类型|说明|
|:----|:----|
|[PermissionValue](#interface-permissionvalue)|此权限集与另一个权限集与后的权限集。|

### func |(PermissionValue)

```cangjie
public const override operator func |(rhs: PermissionValue): PermissionValue
```

**功能：** 和另一个权限集或。返回或操作后的权限集。

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rhs|[PermissionValue](#interface-permissionvalue)|是|-|或操作的另一个权限集。|

**返回值：**

|类型|说明|
|:----|:----|
|[PermissionValue](#interface-permissionvalue)|此权限集与另一个权限集或后的权限集。|

## class PermissionOr

```cangjie
public class PermissionOr <: PermissionValue {
    public const init(lhs: PermissionValue, rhs: PermissionValue)
}
```

**功能：** 表示若干个权限的或。

**起始版本：** 19

**父类型：**

- [PermissionValue](#interface-permissionvalue)

### init(PermissionValue, PermissionValue)

```cangjie
public const init(lhs: PermissionValue, rhs: PermissionValue)
```

**功能：** 构造PermissionOr或权限集，表示两个权限集的或。

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|lhs|[PermissionValue](#interface-permissionvalue)|是|-|构造或权限集的一个权限集。|
|rhs|[PermissionValue](#interface-permissionvalue)|是|-|构造或权限集的另一个权限集。|

### func &(PermissionValue)

```cangjie
public const override operator func &(rhs: PermissionValue): PermissionValue
```

**功能：** 和另一个权限集与。返回与操作后的权限集。

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rhs|[PermissionValue](#interface-permissionvalue)|是|-|与操作的另一个权限集。|

**返回值：**

|类型|说明|
|:----|:----|
|[PermissionValue](#interface-permissionvalue)|此权限集与另一个权限集与后的权限集。|

### func |(PermissionValue)

```cangjie
public const override operator func |(rhs: PermissionValue): PermissionValue
```

**功能：** 和另一个权限集或。返回或操作后的权限集。

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rhs|[PermissionValue](#interface-permissionvalue)|是|-|或操作的另一个权限集。|

**返回值：**

|类型|说明|
|:----|:----|
|[PermissionValue](#interface-permissionvalue)|此权限集与另一个权限集或后的权限集。|