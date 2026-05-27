## class PermissionRequestResult

```cangjie
public class PermissionRequestResult {
    public var permissions: Array<String>
    public var authResults: Array<Int32>
    public var dialogShownResults: ?Array<Bool> = None

    public init(
        permissions: Array<String>,
        authResults: Array<Int32>
    )
}
```

**功能：** 权限请求结果对象，在调用[requestPermissionsFromUser](./cj-apis-ability_access_ctrl.md#func-requestpermissionsfromuserstagecontext-arraypermissions-asynccallbackaccessctrlpermissionrequestresult)申请权限时返回此对象表明此次权限申请的结果。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 12

### var authResults

```cangjie
public var authResults: Array<Int32>
```

**功能：** 相应请求权限的结果。

- -1：未授权。①dialogShownResults返回为true，表示用户首次申请；②dialogShownResults返回为false，表示权限已设置，无需弹窗，需要用户在"设置"中修改。
- 0：已授权。
- 2：未授权，表示请求无效。可能原因有：①未在设置文件中声明目标权限；②权限名非法；③部分权限存在特殊申请条件，在申请对应权限时未满足其指定的条件，见[ohos.permission.LOCATION](../../../../Dev_Guide/security/AccessToken/cj-permissions-for-all-user.md#ohospermissionlocation)与[ohos.permission.APPROXIMATELY_LOCATION](../../../../Dev_Guide/security/AccessToken/cj-permissions-for-all-user.md#ohospermissionapproximately_location)。

**类型：** Array\<Int32>

**读写能力：** 可读写

**起始版本：** 12

### var dialogShownResults

```cangjie
public var dialogShownResults: ?Array<Bool>
```

**功能：** 此权限申请是否有弹窗：

- true：有弹窗。

- false：无弹窗。

**类型：** ?Array\<Bool>

**读写能力：** 可读写

**起始版本：** 19

### var permissions

```cangjie
public var permissions: Array<String>
```

**功能：** 用户传入的权限。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 12

### init(Array\<String>, Array\<Int32>)

```cangjie
public init(
    permissions: Array<String>,
    authResults: Array<Int32>
)
```

**功能：** PermissionRequestResult实例构造。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.Security.AccessToken

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|permissions|Array\<String>|是|-|用户传入的权限。|
|authResults|Array\<Int32>|是|-|相应请求权限的结果：<br>- -1：未授权。①dialogShownResults返回为true，表示用户首次申请；②dialogShownResults返回为false，表示权限已设置，无需弹窗，需要用户在"设置"中修改。<br>- 0：已授权。<br>- 2：未授权，表示请求无效。可能原因有：①未在设置文件中声明目标权限；②权限名非法；③部分权限存在特殊申请条件，在申请对应权限时未满足其指定的条件，见[ohos.permission.LOCATION](../../../../Dev_Guide/security/AccessToken/cj-permissions-for-all-user.md#ohospermissionlocation)与[ohos.permission.APPROXIMATELY_LOCATION](../../../../Dev_Guide/security/AccessToken/cj-permissions-for-all-user.md#ohospermissionapproximately_location)。|