### let reqPermissionDetails

```cangjie
public let reqPermissionDetails: Array<ReqPermissionDetail>
```

**功能：** 应用运行时需向系统申请的权限集合的详细信息。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口获取，bundleFlags参数传入GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION的值。

**类型：** Array\<[ReqPermissionDetail](#class-reqpermissiondetail)>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let routerMap

```cangjie
public let routerMap: Array<RouterItem>
```

**功能：** 应用的路由表配置，由hapModulesInfo下的routerMap信息，根据RouterItem中的name字段进行去重后合并得到。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口获取，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_ROUTER_MAP的值。

**类型：** Array\<[RouterItem](#class-routeritem)>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let signatureInfo

```cangjie
public let signatureInfo: SignatureInfo
```

**功能：** 应用包的签名信息。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口获取，bundleFlags参数传入GET_BUNDLE_INFO_WITH_SIGNATURE_INFO的值。

**类型：** [SignatureInfo](#class-signatureinfo)

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let targetVersion

```cangjie
public let targetVersion: UInt32
```

**功能：** 应用运行目标版本，对应app.json5中配置的targetAPIVersion字段。

**类型：** UInt32

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let updateTime

```cangjie
public let updateTime: Int64
```

**功能：** 应用包更新时间戳，表示从1970-01-01 08:00:00 UTC+8逝去的毫秒数，单位毫秒。

**类型：** Int64

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let vendor

```cangjie
public let vendor: String
```

**功能：** 应用包的供应商，对应app.json5中配置的vendor字段。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let versionCode

```cangjie
public let versionCode: UInt32
```

**功能：** 应用包的版本号，对应app.json5中配置的versionCode字段。

**类型：** UInt32

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let versionName

```cangjie
public let versionName: String
```

**功能：** 应用包的版本文本描述信息，对应app.json5中配置的versionName字段。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22