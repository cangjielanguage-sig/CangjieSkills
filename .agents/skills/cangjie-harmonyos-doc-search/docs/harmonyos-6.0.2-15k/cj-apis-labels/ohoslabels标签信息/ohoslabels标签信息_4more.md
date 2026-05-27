# ohos.labels（标签信息）

标签说明。标签包括atomicservice（是否支持元服务）、crossplatform（是否支持跨平台）、deprecated（废弃版本）、form（是否支持在form中使用）、permission（所需权限）、since（api等级）、stagemodelonly（是否仅支持Stage模型）、syscap（所需系统能力）等信息。

## 导入模块

```cangjie
import ohos.labels.*
```

## 使用说明

此包用于将标签以注解的形式打在api上，是对其中注解信息的说明。不推荐用户使用。

## interface PermissionValue

```cangjie
public interface PermissionValue {
    operator func &(rhs: PermissionValue): PermissionValue
    operator func |(rhs: PermissionValue): PermissionValue
}
```

**功能：** 用于处理权限的与或关系。

**起始版本：** 19

### func &(PermissionValue)

```cangjie
operator func &(rhs: PermissionValue): PermissionValue
```

**功能：** 和另一个权限集的与。返回与操作后的权限集。

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
operator func |(rhs: PermissionValue): PermissionValue
```

**功能：** 和另一个权限或。返回或操作后的权限。

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rhs|[PermissionValue](#interface-permissionvalue)|是|-|或操作的另一个权限集。|

**返回值：**

|类型|说明|
|:----|:----|
|[PermissionValue](#interface-permissionvalue)|此权限集与另一个权限集或后的权限集。|