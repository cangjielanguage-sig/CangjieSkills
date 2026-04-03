## 框架原理

### 应用文件访问框架

应用文件访问框架是通过基础文件操作接口（[ohos.file_fs](../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_fs.md)）实现。开发者无需了解内部实现，基础文件操作接口功能详情请参见[接口说明](./cj-app-file-access.md#接口说明)。

### 用户文件访问框架

用户文件访问框架（File Access Framework）是一套提供给开发者访问和管理用户文件的基础框架。该框架依托于HarmonyOS的ExtensionAbility组件机制，提供了一套统一访问用户文件的方法和接口。

**图2** 用户文件访问框架示意图

![User file access framework](figures/user-file-access-framework.png)

- 各类系统应用或三方应用（即图中的文件访问客户端）若需访问用户文件，如选择一张照片或保存多个文档等，可以通过拉起“文件选择器应用”来实现。

- FilePicker：系统预置应用，提供文件访问客户端选择和保存文件的能力，且不需要配置任何权限。FilePicker的使用指导请参见[选择用户文件](./cj-select-user-file.md)。

- FileManager：对于设备开发者，还可以按需开发自己的文件选择器或文件管理器应用。

- File Access Framework（用户文件访问框架）的主要功能模块如下：
    - File Access Helper：提供给文件管理器和文件选择器访问用户文件的API接口。
    - File Access ExtensionAbility：提供文件访问框架能力，由内卡文件管理服务UserFileManager和外卡文件管理服务ExternalFileManager组成，实现对应的文件访问功能。
        - UserFileManager：内卡文件管理服务，基于File Access ExtensionAbility框架实现，用于管理内置存储设备上的文件。
        - ExternalFileManager：外卡文件管理服务，基于File Access ExtensionAbility框架实现，用于管理外置存储设备上的文件。

## 与相关Kit的关系

Ability Kit: Core File Kit中用户文件访问框架依赖Ability Kit提供的Extension基础能力，受Ability Kit服务调度管理。