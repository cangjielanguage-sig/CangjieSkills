## enum OfflineResourceType

```cangjie
public enum OfflineResourceType <: Equatable<OfflineResourceType> & ToString {
    | IMAGE
    | CSS
    | CLASSIC_JS
    | MODULE_JS
    | ...
}
```

**功能：** 本地离线资源的接口类型。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**父类型：**

- Equatable\<OfflineResourceType>
- ToString

### CLASSIC_JS

```cangjie
CLASSIC_JS
```

**功能：** 通过\<script src=“” \/>标签加载的Javascript资源。

**起始版本：** 19

### CSS

```cangjie
CSS
```

**功能：** CSS类型的资源。

**起始版本：** 19

### IMAGE

```cangjie
IMAGE
```

**功能：** 图片类型的资源。

**起始版本：** 19

### MODULE_JS

```cangjie
MODULE_JS
```

**功能：** 通过\<script src=“” type=“module” \/>标签加载的Javascript资源。

**起始版本：** 19

### func !=(OfflineResourceType)

```cangjie
public operator func !=(other: OfflineResourceType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[OfflineResourceType](#enum-offlineresourcetype)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(OfflineResourceType)

```cangjie
public operator func ==(other: OfflineResourceType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[OfflineResourceType](#enum-offlineresourcetype)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|