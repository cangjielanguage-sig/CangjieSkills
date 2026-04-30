# 自定义组件成员属性访问限定符使用限制

在状态管理中，当组件开发者封装了自定义组件后，由于组件没有明确的输入输出标识，使得调用方无法按照统一的标准判断传入哪些变量作为组件入参。在状态管理中，不可以使用限定符修饰状态变量。

仓颉会对自定义组件的成员变量使用的访问限定符private/public/protected进行校验，当不按规范使用访问限定符private/public/protected时，会产生对应的日志信息。

在阅读本文档前，建议提前阅读：[状态管理概述](../state_management/cj-state-management-overview.md)。

## 使用限制

- [@State](../state_management/cj-macro-state.md)/[@Prop](../state_management/cj-macro-prop.md)/[@Provide](../state_management/cj-macro-provide-and-consume.md)/[@BuilderParam](./cj-macro-builderparam.md)/常规成员变量(不涉及更新的普通变量)的初始化规则为可以被外部初始化。

- [@StorageLink](../state_management/cj-appstorage.md#storagelink)/[@StorageProp](../state_management/cj-appstorage.md#storageprop)/[@LocalStorageLink](../state_management/cj-localstorage.md#localstoragelink)/[@LocalStorageProp](../state_management/cj-localstorage.md#localstorageprop)/[@Consume](../state_management/cj-macro-provide-and-consume.md)变量的初始化规则为不可以被外部初始化。

- [@Link](../state_management/cj-macro-link.md)变量的初始化规则为必须被外部初始化，禁止本地初始化。