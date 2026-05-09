### var parameters

```cangjie
public var parameters: HashMap<String, WantValueType>
```

**功能：** 表示WantParams描述。

以下Key均由系统赋值，开发者手动修改也不会生效，系统在数据传递时会自动修改为实际值。

- ohos.aafwk.param.callerPid：表示拉起方的pid，值为字符串类型。
- ohos.aafwk.param.callerBundleName：表示拉起方的BundleName，值为字符串类型。
- ohos.aafwk.param.callerAbilityName：表示拉起方的AbilityName，值为字符串类型。
- ohos.aafwk.param.callerNativeName：表示native调用时拉起方的进程名，值为字符串类型。
- ohos.aafwk.param.callerAppId：表示拉起应用的AppId信息，值为字符串类型。
- ohos.aafwk.param.callerAppIdentifier：表示拉起应用的AppIdentifier信息，值为字符串类型。
- ohos.aafwk.param.callerToken：表示拉起方的token，值为字符串类型。
- ohos.aafwk.param.callerUid：表示[BundleInfo](./cj-apis-bundle_manager.md#class-bundleinfo)中的uid，应用包里应用程序的uid，值为数值类型。
- ohos.param.callerAppCloneIndex：表示拉起方应用的分身索引，值为数值类型。
- component.startup.newRules：表示是否启用新的管控规则，值为布尔类型。
- moduleName：表示拉起方的moduleName，值为字符串类型。
- ohos.ability.params.abilityRecoveryRestart：表示当前Ability是否发生了故障恢复重启，值为布尔类型。

**类型：** HashMap\<String,[WantValueType](#enum-wantvaluetype)>

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### var uri

```cangjie
public var uri: String
```

**功能：** 统一资源标识符，一般在应用启动场景中配合type使用，指明待处理的数据类型。如果在Want中指定了uri，则Want将匹配指定的Uri信息，包括`scheme`、`schemeSpecificPart`、`authority`和`path`信息。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### var dataType

```cangjie
public var dataType: String
```

**功能：** 表示MIME type类型描述，打开文件的类型，主要用于文管打开文件。比如：'text/xml' 、 'image/*'等，MIME定义请参见[Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml?utm_source=ld246.com)。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22