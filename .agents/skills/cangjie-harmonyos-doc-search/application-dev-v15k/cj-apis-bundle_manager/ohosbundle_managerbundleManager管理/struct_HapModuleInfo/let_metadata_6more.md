### let metadata

```cangjie
public let metadata: Array<Metadata>
```

**功能：** Ability的元信息。

**类型：** Array\<[Metadata](#class-metadata)>

**读写能力：** 只读

**起始版本：** 12

### let moduleType

```cangjie
public let moduleType: ModuleType
```

**功能：** 标识当前模块的类型。

**类型：** [ModuleType](#enum-moduletype)

**读写能力：** 只读

**起始版本：** 12

### let name

```cangjie
public let name: String
```

**功能：** 模块名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let nativeLibraryPath

```cangjie
public let nativeLibraryPath: String
```

**功能：** 应用程序内某个hapModule的本地库文件路径。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let preloads

```cangjie
public let preloads: Array<PreloadItem>
```

**功能：** 元服务中模块的预加载列表。

**类型：** Array\<[PreloadItem](#struct-preloaditem)>

**读写能力：** 只读

**起始版本：** 12

### let routerMap

```cangjie
public let routerMap: Array<RouterItem>
```

**功能：** 模块的路由表配置。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口获取，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_ROUTER_MAP的值。

**类型：** Array\<[RouterItem](#struct-routeritem)>

**读写能力：** 只读

**起始版本：** 19