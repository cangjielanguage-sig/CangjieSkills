### uri匹配规则

具体的匹配规则如下：

- 如果s_uri的scheme为空，当w_uri为空时匹配成功，否则匹配失败。
- 如果s_uri的host为空，当w_uri和s_uri的scheme相同时匹配成功，否则匹配失败。
- 如果s_uri的port为空，当w_uri和s_uri中的scheme和host相同时匹配成功，否则匹配失败。
- 如果s_uri的path、pathStartWith和pathRegex都为空，当w_uri和s_uri中的scheme，host和port相同时匹配成功，否则匹配失败。
- 如果s_uri的path不为空，当w_uri和s_uri**全路径表达式**相同时匹配成功，否则继续进行pathStartWith的匹配。
- 如果s_uri的pathStartWith不为空，当w_uri包含s_uri**前缀表达式**时匹配成功，否则继续进行pathRegex的匹配。
- 如果s_uri的pathRegex不为空，当w_uri满足s_uri**正则表达式**时匹配成功，否则匹配失败。

> **说明：**
>
> 待匹配应用组件的skills配置的uris中scheme、host、port、path、pathStartWith和pathRegex属性拼接，如果依次声明了path、pathStartWith和pathRegex属性时，uris将分别拼接为如下四种表达式：
>
> - **前缀uri表达式**：当配置文件只配置scheme，或者只配置scheme和host，或者只配置scheme，host和port时，参数传入以配置文件为前缀的Uri
>     - `scheme://`
>     - `scheme://host`
>     - `scheme://host:port`
> - **全路径表达式**：`scheme://host:port/path`
> - **前缀表达式**：`scheme://host:port/pathStartWith`
> - **正则表达式**：`scheme://host:port/pathRegex`
>
> 系统应用预留uri的scheme统一以`ohos`开头，例如`ohosclock://`。三方应用组件配置的uri不能与系统应用重复，否则会导致无法通过该uri拉起三方应用组件。

**图5** want参数中uri的匹配规则示例

![want-uri-case](figures/want-uri-case.png)

### type匹配规则

> **说明：**
>
> 本章节所述的type匹配规则的适用性需建立在want参数内type不为空的基础上。当want参数内type为空时请参见[want参数的uri和type匹配规则](#want参数的uri和type匹配规则)。

具体的匹配规则如下：

- 如果s_type为空，则匹配失败。
- 如果s_type或者w_type为通配符`*/*`，则匹配成功。
- 如果s_type最后一个字符为通配符`*`，如`prefixType/*`，则当w_type包含`prefixType/`时匹配成功，否则匹配失败。
- 如果w_type最后一个字符为通配符`*`，如`prefixType/*`，则当s_type包含`prefixType/`时匹配成功，否则匹配失败。

### linkFeature匹配规则

> **说明：**
>
> 本章节所述的linkFeature匹配规则适用于want参数中的parameters包含linkFeature键，且对应取值不为空的场景。

将调用方传入的want参数的parameters与待匹配应用组件的skills配置中的uris进行匹配。为了简化描述, 称调用方传入的want参数中的linkFeature参数为w_linkFeature, 具体的匹配规则如下：

- want参数的uri和type均为空, 只匹配linkFeature，当w_linkFeature和s_uri的linkFeature相同时匹配成功，否则匹配失败。
- want参数的uri或type不为空, 依次匹配linkFeature、uri、type (参见[want参数的uri和type匹配规则](#want参数的uri和type匹配规则))，当三个字段均匹配成功时，则匹配成功，否则匹配失败。

**图6** want参数中linkFeature具体匹配规则

![want-linkFeature](figures/linkFeature.png)
![want-linkFeature-case](figures/want-linkFeature-case.png)