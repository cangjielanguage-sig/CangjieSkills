### let metadata

```cangjie
public let metadata: Array<Metadata>
```

**功能：** Ability的元信息。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口获取，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE、GET_BUNDLE_INFO_WITH_ABILITY和GET_BUNDLE_INFO_WITH_METADATA的值。

**类型：** Array\<[Metadata](#class-metadata)>

**读写能力：** 只读

**起始版本：** 12

### let moduleName

```cangjie
public let moduleName: String
```

**功能：** Ability所属的HAP的名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let name

```cangjie
public let name: String
```

**功能：** Ability名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let orientation

```cangjie
public let orientation: DisplayOrientation
```

**功能：** Ability的显示模式。

**类型：** [DisplayOrientation](#enum-displayorientation)

**读写能力：** 只读

**起始版本：** 12

### let permissions

```cangjie
public let permissions: Array<String>
```

**功能：** 被其他应用Ability调用时需要申请的权限集合。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口获取，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE、GET_BUNDLE_INFO_WITH_ABILITY和GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION的值。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 12

### let process

```cangjie
public let process: String
```

**功能：** Ability的进程，如果不设置，默认为包的名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let skills

```cangjie
public let skills: Array<Skill>
```

**功能：** Ability的Skills信息。

**类型：** Array\<[Skill](#struct-skill)>

**读写能力：** 只读

**起始版本：** 19

### let supportWindowModes

```cangjie
public let supportWindowModes: Array<SupportWindowMode>
```

**功能：** Ability支持的窗口模式。

**类型：** Array\<[SupportWindowMode](#enum-supportwindowmode)>

**读写能力：** 只读

**起始版本：** 12

### let windowSize

```cangjie
public let windowSize: WindowSize
```

**功能：** Ability窗口尺寸。

**类型：** [WindowSize](#struct-windowsize)

**读写能力：** 只读

**起始版本：** 12