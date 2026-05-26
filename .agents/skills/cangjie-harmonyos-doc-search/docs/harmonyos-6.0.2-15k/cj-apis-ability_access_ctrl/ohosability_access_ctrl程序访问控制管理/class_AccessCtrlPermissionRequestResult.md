## class AccessCtrlPermissionRequestResult

```cangjie
public class AccessCtrlPermissionRequestResult {
    public AccessCtrlPermissionRequestResult(
        public let permissions: Array<String>,
        public let authResults: Array<Int32>,
        public let dialogShownResults!: ?Array<Bool> = None
    )
}
```

**功能：** 权限请求结果对象，在调用[requestPermissionsFromUser](#func-requestpermissionsfromuserstagecontext-arraypermissions-asynccallbackaccessctrlpermissionrequestresult)申请权限时返回此对象表明此次权限申请的结果。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 12

### let authResults

```cangjie
public let authResults: Array<Int32>
```

**功能：** 相应请求权限的结果。

**类型：** Array\<Int32>

**读写能力：** 只读

**起始版本：** 12

### let dialogShownResults

```cangjie
public let dialogShownResults: ?Array<Bool> = None
```

**功能：** 此权限申请是否有弹窗。

**类型：** ?Array\<Bool>

**读写能力：** 只读

**起始版本：** 19

### let permissions

```cangjie
public let permissions: Array<String>
```

**功能：** 用户传入的权限。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 12

### AccessCtrlPermissionRequestResult(Array\<String>, Array\<Int32>, ?Array\<Bool>)

```cangjie
public AccessCtrlPermissionRequestResult(
    public let permissions: Array<String>,
    public let authResults: Array<Int32>,
    public let dialogShownResults!: ?Array<Bool> = None
)
```

**功能：** 构建权限请求结果对象。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|permissions|Array\<String>|是|-|用户传入的权限。|
|authResults|Array\<Int32>|是|-|相应请求权限的结果：<br>- -1：未授权。①dialogShownResults返回为true，表示用户首次申请；②dialogShownResults返回为false，表示权限已设置，无需弹窗，需要用户在"设置"中修改。<br>- 0：已授权。<br>- 2：未授权，表示请求无效，可能原因有：<br>  -未在设置文件中声明目标权限。<br>  -权限名非法。<br>  -部分权限存在特殊申请条件，在申请对应权限时未满足其指定的条件，见[ohos.permission.LOCATION](../../../../Dev_Guide/security/AccessToken/cj-permissions-for-all-user.md#ohospermissionlocation)与[ohos.permission.APPROXIMATELY_LOCATION](../../../../Dev_Guide/security/AccessToken/cj-permissions-for-all-user.md#ohospermissionapproximately_location)。|
|dialogShownResults|?Array\<Bool>|否|None| **命名参数。** 此权限申请是否有弹窗：<br>- true：有弹窗。<br>- false：无弹窗。|