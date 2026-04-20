# HAP

HAP（Harmony Ability Package）是应用安装和运行的基本单元。HAP包是由代码、资源、第三方库、配置文件等打包生成的模块包，其主要分为两种类型：entry和feature。

- entry：应用的主模块，作为应用的入口，提供了应用的基础功能。
- feature：应用的动态特性模块，作为应用能力的扩展，可以根据用户的需求和设备类型进行选择性安装。

应用程序包可以只包含一个基础的entry包，也可以包含一个基础的entry包和多个功能性的feature包。

## 使用场景

- 单HAP场景：如果只包含UIAbility组件，无需使用ExtensionAbility组件，优先采用单HAP（即一个entry包）来实现应用开发。虽然一个HAP中可以包含一个或多个UIAbility组件，为了避免不必要的资源加载，推荐采用“一个UIAbility+多个页面”的方式。

- 多HAP场景：如果应用的功能比较复杂，需要使用ExtensionAbility组件，可以采用多HAP（即一个entry包+多个feature包）来实现应用开发，每个HAP中包含一个UIAbility组件或者一个ExtensionAbility组件。在这种场景下，多个HAP引用相同的库文件，可能导致重复打包的问题。

## 约束限制

- 不支持导出接口和仓颉组件，给其他模块使用。

- 多HAP场景下，App Pack包中同一设备类型的所有HAP中最多只能包含一个Entry类型的HAP，也可以不包含；Feature类型的HAP可以包含一个或者多个，也可以不包含。

- 多HAP场景下，同一应用中的所有HAP的配置文件中的bundleName、versionCode、versionName、minCompatibleVersionCode、debug、minAPIVersion、targetAPIVersion、apiReleaseType相同，同一设备类型的所有HAP对应的moduleName标签必须唯一。HAP打包生成App Pack包时，会对上述参数配置进行校验。

- 多HAP场景下，同一应用的所有HAP的签名证书要保持一致。上架应用市场是以App Pack形式上架，应用市场分发时会将所有HAP从App Pack中拆分出来，同时对所有HAP进行重签名，以保证签名证书的一致性。在调试阶段，开发者通过命令行或DevEco Studio将HAP安装到设备上时，要保证所有HAP签名证书一致，否则会出现安装失败的问题，签名操作请参考[应用/元服务签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing)。

## 创建

下面简要介绍如何通过DevEco Studio新建一个HAP模块。

1. 创建工程，构建第一个HarmonyOS应用（仓颉）。

2. 在工程目录上单击右键，选择New > Module。

3. 在弹出的对话框中选择"[Cangjie] Empty Ability"模板，单击Next。

4. 在Module配置界面，配置Module name，选择Module Type和Device Type，然后单击Next。

5. 在Ability配置界面，配置Ability name，然后单击Finish完成创建。

## 开发

- 仓颉HAP中支持引用HAR，详见[HAR的使用](./har-package.md#HAR)。