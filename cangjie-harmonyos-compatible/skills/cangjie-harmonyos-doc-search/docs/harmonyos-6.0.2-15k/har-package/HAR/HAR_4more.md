# HAR

HAR（Harmony Archive）是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或多个工程共享仓颉组件、资源等相关代码。

## 使用场景

- 支持应用内共享，也可以作为二方库（SDK）、三方库（SDK）发布后供其他应用使用。

- 作为二方库（SDK），发布到[OHPM私仓](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo)，供公司内部其他应用使用。

- 作为三方库（SDK），发布到[OHPM中心仓](https://ohpm.openharmony.cn/)，供其他应用使用。

## 约束限制

- HAR不支持在设备上单独安装或运行，只能作为应用模块的依赖项被引用。

- HAR不支持在配置文件中声明pages页面，但是可以包含pages页面，并通过Navigation跳转的方式进行跳转。

- HAR不支持引用AppScope目录中的资源。在编译构建时，AppScope中的内容不会打包到HAR中，因此会导致HAR资源引用失败。

- 多包（HAP）引用相同的HAR时，会造成多包间代码和资源的重复拷贝，从而导致应用包变大。

- HAR可以依赖其他HAR，但不支持循环依赖，也不支持依赖传递。

- HAP引用HAR时，在编译构建过程中系统会自动合并两者的权限配置。因此开发者无需在HAP和HAR中重复申请相同权限。

- 当仓颉二进制HAR<!-- add link -->被集成使用时，要求该工程使用和编译二进制HAR相同版本的SDK编译。

- 当模块中有自定义宏并且需要给其他模块使用时，本模块和其他模块不支持编译成二进制HAR，需要编译成源码格式的仓颉HAR<!-- add link -->。

- 二进制HAR默认打包仓颉so和cjo产物，并且放在HAR包中libs/arm64-v8a/cjbins/package或libs/x86_64/cjbins/package包目录下；如果需要仓颉so产物平铺在libs/arm64-v8a或libs/x86_64目录下，例如在纯ArkTS HAP依赖二进制格式的仓颉HAR场景下，可以在仓颉HAR模块中设置[flattenLibs配置项](../../../Cangjie_Deveco_Studio/source_zh_cn/build/configuration-files/cj-build-module-build-profile.md#buildoption)值为true。

> **说明：**
>
> 循环依赖：例如有三个HAR，HAR-A、HAR-B和HAR-C，循环依赖指HAR-A依赖HAR-B，HAR-B依赖HAR-C，HAR-C又依赖HAR-A。
>
> 依赖传递：例如有三个HAR，HAR-A、HAR-B和HAR-C，依赖关系是HAR-A依赖HAR-B，HAR-B依赖HAR-C。不支持传递依赖指HAR-A可以使用HAR-B的方法和组件，但是HAR-A不能直接使用HAR-C的方法和组件。

## 创建

开发者可以通过DevEco Studio创建一个HAR模块，详见创建库模块<!-- add link -->。