## 存取账号的授权令牌

具体开发实例如下：

1. 准备参数，指定账号名、账号所有者、授权类型和授权令牌。

   ```cangjie
   let name: String = 'ZhangSan'
   let owner: String = 'com.example.accountjsdemo'
   let authType: String = 'getSocialData'
   let token: String = 'xxxxxx'
   ```

2. 调用[setAuthToken](../../../API_Reference/source_zh_cn/apis/BasicServicesKit/cj-apis-account-appAccount.md#func-setauthtokenstring-string-string)接口，设置指定授权类型的授权令牌。

   ```cangjie
   appAccountManager.setAuthToken(name, authType, token)
   ```

3. 调用[getAuthToken](../../../API_Reference/source_zh_cn/apis/BasicServicesKit/cj-apis-account-appAccount.md#func-getauthtokenstring-string-string)接口，获取指定授权类型的授权令牌。

   ```cangjie
   appAccountManager.getAuthToken(name, owner, authType)
   ```

## 删除应用账号

用户退出登录后，应用需及时将相应的应用账号从系统中删除。

具体开发实例如下：

指定要删除的账号名称，调用[removeAccount](../../../API_Reference/source_zh_cn/apis/BasicServicesKit/cj-apis-account-appAccount.md#func-removeaccountstring)接口删除账号。

```cangjie
      try {
         let name: string = 'Zhangsan'
         appAccountManager.removeAccount(name)
         AppLog.info("removeaccoutn success")
      } catch (e: BusinessException) {
         AppLog.error("removeAccount : ${e.message.toString()}")
      }
   ```