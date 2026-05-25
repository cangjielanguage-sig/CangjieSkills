## class FormInfo

```cangjie
public class FormInfo {}
```

**功能：** 卡片配置信息。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

### prop abilityName

```cangjie
public prop abilityName: String
```

**功能：** 卡片所属的Ability名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 20

### prop bundleName

```cangjie
public prop bundleName: String
```

**功能：** 卡片所属包的Bundle名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 20

### prop colorMode

```cangjie
public prop colorMode: ColorMode
```

**功能：** 卡片颜色模式。

**类型：** [ColorMode](#enum-colormode)

**读写能力：** 只读

**起始版本：** 20

### prop customizeData

```cangjie
public prop customizeData: HashMap<String,String>
```

**功能：** 卡片用户数据。

**类型：** HashMap\<String,String>

**读写能力：** 只读

**起始版本：** 20

### prop defaultDimension

```cangjie
public prop defaultDimension: FormDimension
```

**功能：** 卡片规格。

**类型：** [FormDimension](#enum-formdimension)

**读写能力：** 只读

**起始版本：** 20

### prop description

```cangjie
public prop description: String
```

**功能：** 卡片描述。

**类型：** String

**读写能力：** 只读

**起始版本：** 20

### prop descriptionId

```cangjie
public prop descriptionId: UInt32
```

**功能：** 卡片描述ID。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 20

### prop displayName

```cangjie
public prop displayName: String
```

**功能：** 卡片展示名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 20

### prop displayNameId

```cangjie
public prop displayNameId: UInt32
```

**功能：** 卡片预览时标识卡片名称的ID。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 20

### prop formConfigAbility

```cangjie
public prop formConfigAbility: String
```

**功能：** 卡片配置Ability。指定长按卡片弹出的选择框内，编辑选项所对应的Ability。

**类型：** String

**读写能力：** 只读

**起始版本：** 20

### prop formType

```cangjie
public prop formType: FormType
```

**功能：** 卡片类型。当前支持JS卡片、ArkTS卡片。

**类型：** [FormType](#enum-formtype)

**读写能力：** 只读

**起始版本：** 20

### prop formVisibleNotify

```cangjie
public prop formVisibleNotify: Bool
```

**功能：** 卡片是否使能可见通知。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 20

### prop isDefault

```cangjie
public prop isDefault: Bool
```

**功能：** 卡片是否是默认卡片。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 20

### prop isDynamic

```cangjie
public prop isDynamic: Bool
```

**功能：** 卡片是否为动态卡片。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 20

### prop jsComponentName

```cangjie
public prop jsComponentName: String
```

**功能：** JS卡片的组件名。

**类型：** String

**读写能力：** 只读

**起始版本：** 20

### prop moduleName

```cangjie
public prop moduleName: String
```

**功能：** 卡片所属模块的模块名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 20

### prop name

```cangjie
public prop name: String
```

**功能：** 卡片名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 20

### prop scheduledUpdateTime

```cangjie
public prop scheduledUpdateTime: String
```

**功能：** 卡片更新时间。

**类型：** String

**读写能力：** 只读

**起始版本：** 20

### prop supportDimensions

```cangjie
public prop supportDimensions: Array<FormDimension>
```

**功能：** 卡片支持的规格。具体可选规格参考[FormDimension](#enum-formdimension)

**类型：** Array\<[FormDimension](#enum-formdimension)>

**读写能力：** 只读

**起始版本：** 20

### prop supportedShapes

```cangjie
public prop supportedShapes: Array<FormShape>
```

**功能：** 卡片支持的形状。具体可选形状参考[FormShape](#enum-formshape)

**类型：** Array\<[FormShape](#enum-formshape)>

**读写能力：** 只读

**起始版本：** 20