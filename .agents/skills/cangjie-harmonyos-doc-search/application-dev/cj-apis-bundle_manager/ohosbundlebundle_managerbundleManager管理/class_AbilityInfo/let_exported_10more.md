### let exported

```cangjie
public let exported: Bool
```

**功能：** 判断Ability是否可以被其他应用拉起，true表示可以，false表示不可以。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let icon

```cangjie
public let icon: String
```

**功能：** Ability的图标资源描述符，对应module.json5中abilities下配置的icon字段。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let iconId

```cangjie
public let iconId: Int32
```

**功能：** Ability的图标资源id，是编译构建时根据应用配置abilities下的icon自动生成的资源id。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let label

```cangjie
public let label: String
```

**功能：** Ability对用户显示的名称的资源描述符，对应module.json5中abilities下配置的label字段。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let labelId

```cangjie
public let labelId: Int32
```

**功能：** Ability的标签资源id，编译构建时根据应用配置abilities下的label自动生成。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let launchType

```cangjie
public let launchType: LaunchType
```

**功能：** Ability的启动模式，决定该Ability在启动时是否以多实例启动，详情参考[启动模式枚举](#enum-launchtype) 。

**类型：** [LaunchType](#enum-launchtype)

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let metadata

```cangjie
public let metadata: Array<Metadata>
```

**功能：** Ability的元信息。可以配置成系统定义的参数，使用系统提供的能力，例如快捷方式、窗口元数据配置等。也可以自定义配置参数，通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE、GET_BUNDLE_INFO_WITH_ABILITY和GET_BUNDLE_INFO_WITH_METADATA获取。

**类型：** Array\<[Metadata](./cj-apis-metadata.md#class-metadata)>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let moduleName

```cangjie
public let moduleName: String
```

**功能：** Ability所属的模块名称。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let name

```cangjie
public let name: String
```

**功能：** Ability名称。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let orientation

```cangjie
public let orientation: DisplayOrientation
```

**功能：** Ability的显示模式。来源于module.json5中abilies标签下配置的orientation字段，如果module.json5配置文件中orientation配置枚举，orientation属性有值且非0，取值详情参考[显示模式枚举](#enum-displayorientation)；如果配置文件中配置的是资源索引，orientation属性值为0。

**类型：** [DisplayOrientation](#enum-displayorientation)

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22