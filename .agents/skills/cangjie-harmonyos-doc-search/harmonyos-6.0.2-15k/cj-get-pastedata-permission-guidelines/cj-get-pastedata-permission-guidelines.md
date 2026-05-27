# 申请访问剪贴板权限

## 访问剪贴板内容

剪贴板为应用提供如下访问内容的方式。

- 申请ohos.permission.READ_PASTEBOARD权限

    ohos.permission.READ_PASTEBOARD是受限的user_grant（用户授权）权限，使用自定义控件的应用可以通过申请ohos.permission.READ_PASTEBOARD权限，在用户授权的场景下访问剪贴板内容。

    权限申请步骤：

    1. 通过[ACL方式](../../security/AccessToken/cj-permissions-for-acl.md)，申请高级别权限。

    2. 在module.json5配置文件中[声明权限](../../security/AccessToken/cj-declare-permissions.md)。

    3. 通过弹窗[向用户申请权限](../../security/AccessToken/cj-request-user-authorization.md)。
