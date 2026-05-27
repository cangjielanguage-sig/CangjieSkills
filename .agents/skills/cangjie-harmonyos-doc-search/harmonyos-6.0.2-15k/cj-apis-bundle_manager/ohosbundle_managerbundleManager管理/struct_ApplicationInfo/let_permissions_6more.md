### let permissions

```cangjie
public let permissions: Array<String>
```

**功能：** 访问应用程序所需的权限。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口获取，bundleFlags参数传入GET_BUNDLE_INFO_WITH_APPLICATION和GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION的值。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 12

### let process

```cangjie
public let process: String
```

**功能：** 应用程序的进程，如果不设置，默认为包的名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let releaseType

```cangjie
public let releaseType: String
```

**功能：** 标识应用打包时使用的SDK的发布类型。当前SDK的发布类型可能为Canary、Beta、Release，其中Canary和Beta可能通过序号进一步细分，例如Canary1、Canary2、Beta1、Beta2等。开发者可通过对比应用打包依赖的SDK发布类型和OS的发布类型（[deviceInfo.distributionOSReleaseType](../BasicServicesKit/cj-apis-device_info.md)）来判断兼容性。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let removable

```cangjie
public let removable: Bool
```

**功能：** 应用程序是否可以被移除。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let systemApp

```cangjie
public let systemApp: Bool
```

**功能：** 标识应用是否为系统应用。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let uid

```cangjie
public let uid: Int32
```

**功能：** 应用程序的uid。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12