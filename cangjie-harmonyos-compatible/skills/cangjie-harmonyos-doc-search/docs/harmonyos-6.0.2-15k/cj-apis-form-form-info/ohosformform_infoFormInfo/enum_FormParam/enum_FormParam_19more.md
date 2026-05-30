## enum FormParam

```cangjie
public enum FormParam <: Equatable<FormParam> {
    | IdentityKey
    | DimensionKey
    | NameKey
    | ModuleNameKey
    | WidthKey
    | HeightKey
    | TemporaryKey
    | AbilityNameKey
    | BundleNameKey
    | LaunchReasonKey
    | ParamFormCustomizeKey
    | FormRenderingModeKey
    | HostBgInverseColorKey
    | FormLocationKey
    | FormPermissionNameKey
    | FormPermissionGrantedKey
    | ...
}
```

**功能：** 卡片参数枚举。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**父类型：**

- Equatable\<FormParam>

### AbilityNameKey

```cangjie
AbilityNameKey
```

**功能：** 值为ohos.extra.param.key.ability_name。Ability名称。

**起始版本：** 20

### BundleNameKey

```cangjie
BundleNameKey
```

**功能：** 值为ohos.extra.param.key.bundle_name。Bundle名称。

**起始版本：** 20

### DimensionKey

```cangjie
DimensionKey
```

**功能：** 值为ohos.extra.param.key.form_dimension。卡片规格样式。

**起始版本：** 20

### FormLocationKey

```cangjie
FormLocationKey
```

**功能：** 值为ohos.extra.param.key.form_location。卡片位置。

**起始版本：** 20

### FormPermissionGrantedKey

```cangjie
FormPermissionGrantedKey
```

**功能：** 值为ohos.extra.param.key.permission_granted。用户是否授权。

**起始版本：** 20

### FormPermissionNameKey

```cangjie
FormPermissionNameKey
```

**功能：** 值为ohos.extra.param.key.permission_name。用户授权权限名称。

**起始版本：** 20

### FormRenderingModeKey

```cangjie
FormRenderingModeKey
```

**功能：** 值为ohos.extra.param.key.form_rendering_mode。卡片渲染模式。

**起始版本：** 20

### HeightKey

```cangjie
HeightKey
```

**功能：** 值为ohos.extra.param.key.form_height。卡片高度。

**起始版本：** 20

### HostBgInverseColorKey

```cangjie
HostBgInverseColorKey
```

**功能：** 值为ohos.extra.param.key.host_bg_inverse_color。卡片使用方的背景反色颜色值。

**起始版本：** 20

### IdentityKey

```cangjie
IdentityKey
```

**功能：** 值为ohos.extra.param.key.form_identity。卡片标识。

**起始版本：** 20

### LaunchReasonKey

```cangjie
LaunchReasonKey
```

**功能：** 值为ohos.extra.param.key.form_launch_reason。卡片创建原因。

**起始版本：** 20

### ModuleNameKey

```cangjie
ModuleNameKey
```

**功能：** 值为ohos.extra.param.key.module_name。卡片所属模块名称。

**起始版本：** 20

### NameKey

```cangjie
NameKey
```

**功能：** 值为ohos.extra.param.key.form_name。卡片名称。

**起始版本：** 20

### ParamFormCustomizeKey

```cangjie
ParamFormCustomizeKey
```

**功能：** 值为ohos.extra.param.key.form_customize。自定义数据。

**起始版本：** 20

### TemporaryKey

```cangjie
TemporaryKey
```

**功能：** 值为ohos.extra.param.key.form_temporary。 临时卡片。

**起始版本：** 20

### WidthKey

```cangjie
WidthKey
```

**功能：** 值为ohos.extra.param.key.form_width。卡片宽度。

**起始版本：** 20

### func !=(FormParam)

```cangjie
public operator func !=(other: FormParam): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FormParam](#enum-formparam)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(FormParam)

```cangjie
public operator func ==(other: FormParam): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FormParam](#enum-formparam)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|