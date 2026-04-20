### let debug

```cangjie
public let debug: Bool
```

**功能：** 标识应用是否处于调试模式，取值为true表示应用处于调试模式，取值为false表示应用处于非调试模式。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let description

```cangjie
public let description: String
```

**功能：** 标识应用的描述信息，对应app.json5中配置的description字段。关于description的详细信息详见本表中的descriptionResource字段说明。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let descriptionId

```cangjie
public let descriptionId: Int32
```

**功能：** 标识应用的描述信息的资源id，编译构建时根据应用配置的description自动生成。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let descriptionResource

```cangjie
public let descriptionResource: AppResource
```

**功能：** 应用程序的描述资源信息，包含bundleName、moduleName和id，可以调用全球化的接口[getMediaContent](../LocalizationKit/cj-apis-resource_manager.md#func-getmediacontentuint32-screendensity)来获取详细的资源数据信息。

**类型：** [AppResource](../LocalizationKit/cj-apis-resource.md#class-appresource)

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let enabled

```cangjie
public let enabled: Bool
```

**功能：** 判断应用程序是否可以使用，取值为true表示可以使用，取值为false表示不可使用。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let icon

```cangjie
public let icon: String
```

**功能：** 应用程序的图标，对应app.json5中配置的icon字段。关于icon的详细信息详见本表中的iconResource字段说明。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let iconId

```cangjie
public let iconId: Int32
```

**功能：** 应用程序图标的资源id，是编译构建时根据应用配置的icon自动生成的资源id。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let iconResource

```cangjie
public let iconResource: AppResource
```

**功能：** 应用程序的图标资源信息，包含bundleName、moduleName和id，可以调用全球化的接口[getMediaContent](../LocalizationKit/cj-apis-resource_manager.md#func-getmediacontentuint32-screendensity)来获取详细的资源数据信息。

**类型：** [AppResource](../LocalizationKit/cj-apis-resource.md#class-appresource)

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let installSource

```cangjie
public let installSource: String
```

**功能：** 应用程序的安装来源，支持的取值如下：

- pre-installed表示应用为第一次开机时安装的预置应用。

- ota表示应用为系统升级时新增的预置应用。

- recovery表示卸载后再恢复的预置应用。

- bundleName表示应用由此包名对应的应用安装。

- unknown表示应用安装来源未知。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let label

```cangjie
public let label: String
```

**功能：** 标识应用的名称，对应app.json5中配置的label字段。关于label的详细信息详见本表中的labelResource字段说明。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22