### let preloads

```cangjie
public let preloads: Array<PreloadItem>
```

**功能：** 原子化服务中模块的预加载列表。

**类型：** Array\<[PreloadItem](#class-preloaditem)>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let routerMap

```cangjie
public let routerMap: Array<RouterItem>
```

**功能：** 模块的路由表配置。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_ROUTER_MAP获取。

**类型：** Array\<[RouterItem](#class-routeritem)>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22