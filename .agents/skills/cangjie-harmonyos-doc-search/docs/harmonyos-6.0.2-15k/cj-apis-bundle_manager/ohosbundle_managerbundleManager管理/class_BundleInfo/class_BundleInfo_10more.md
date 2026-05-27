## class BundleInfo

```cangjie
public class BundleInfo {
    public let name: String
    public let vendor: String
    public let versionCode: UInt32
    public let versionName: String
    public let minCompatibleVersionCode: UInt32
    public let targetVersion: UInt32
    public let appInfo: ApplicationInfo
    public let hapModulesInfo: Array<HapModuleInfo>
    public let reqPermissionDetails: Array<ReqPermissionDetail>
    public let permissionGrantStates: Array<PermissionGrantState>
    public let signatureInfo: SignatureInfo
    public let installTime: Int64
    public let updateTime: Int64
    public let uid: Int32
    public let routerMap: Array<RouterItem>
    public let appIndex: Int32
}
```

**功能：** 包信息。三方应用可以通过[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)获取自身的应用包信息，其中入参bundleFlags指定所返回的BundleInfo中所包含的信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### let appIndex

```cangjie
public let appIndex: Int32
```

**功能：** 应用包的分身索引标识，仅在分身应用中生效。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let appInfo

```cangjie
public let appInfo: ApplicationInfo
```

**功能：** 应用程序的配置信息。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口获取，bundleFlags参数传入GET_BUNDLE_INFO_WITH_APPLICATION的值。

**类型：** [ApplicationInfo](#struct-applicationinfo)

**读写能力：** 只读

**起始版本：** 12

### let hapModulesInfo

```cangjie
public let hapModulesInfo: Array<HapModuleInfo>
```

**功能：** 模块的配置信息。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口获取，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE的值。

**类型：** Array\<[HapModuleInfo](#struct-hapmoduleinfo)>

**读写能力：** 只读

**起始版本：** 12

### let installTime

```cangjie
public let installTime: Int64
```

**功能：** 应用包安装时间。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

### let minCompatibleVersionCode

```cangjie
public let minCompatibleVersionCode: UInt32
```

**功能：** 分布式场景下的应用包兼容的最低版本。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### let name

```cangjie
public let name: String
```

**功能：** 应用包的名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let permissionGrantStates

```cangjie
public let permissionGrantStates: Array<PermissionGrantState>
```

**功能：** 申请权限的授予状态。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口获取，bundleFlags参数传入GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION的值。

**类型：** Array\<[PermissionGrantState](#enum-permissiongrantstate)>

**读写能力：** 只读

**起始版本：** 12

### let reqPermissionDetails

```cangjie
public let reqPermissionDetails: Array<ReqPermissionDetail>
```

**功能：** 应用运行时需向系统申请的权限集合的详细信息。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口获取，bundleFlags参数传入GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION的值。

**类型：** Array\<[ReqPermissionDetail](#struct-reqpermissiondetail)>

**读写能力：** 只读

**起始版本：** 12

### let routerMap

```cangjie
public let routerMap: Array<RouterItem>
```

**功能：** 应用的路由表配置，由hapModulesInfo下的routerMap信息，根据RouterItem中的name字段进行去重后合并得到。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口获取，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_ROUTER_MAP的值。

**类型：** Array\<[RouterItem](#struct-routeritem)>

**读写能力：** 只读

**起始版本：** 19