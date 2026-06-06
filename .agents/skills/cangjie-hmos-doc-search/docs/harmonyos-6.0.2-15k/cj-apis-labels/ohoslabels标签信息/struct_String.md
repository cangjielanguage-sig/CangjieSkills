## struct String

```cangjie
extend String <: PermissionValue {}
```

**功能：** 扩展PermissionValue接口，使用字符串表示单个权限。

**起始版本：** 19

**父类型：**

- [PermissionValue](#interface-permissionvalue)

### func &(PermissionValue)

```cangjie
public const operator func &(rhs: PermissionValue): PermissionValue
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
|[PermissionValue](#interface-permissionvalue)|此权限与另一个权限集与后的权限集。|

### func |(PermissionValue)

```cangjie
public const operator func |(rhs: PermissionValue): PermissionValue
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
|[PermissionValue](#interface-permissionvalue)|此权限与另一个权限集或操作后的权限集。|