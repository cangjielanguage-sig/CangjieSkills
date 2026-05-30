# 网页接入密码保险箱

网页中的登录表单，登录成功后，用户可将用户名和密码保存到HarmonyOS系统密码保险箱中。再次打开该网页时，密码保险箱可以提供用户名、密码的自动填充。

## 手机使用场景

以下以[https://developer.huawei.com/](https://developer.huawei.com/)网站为例：

1. 在网站中输入用户名、密码，登陆成功后，ArkWeb会提示将用户名和密码保存到密码保险箱中。

    ![arkweb-save-name-pwd.png](./figures/arkweb-save-name-pwd.png)

2. 再次打开相同的网站，点击用户名或者密码框中时，会弹出密码保险箱的填充提示。

    ![hint2.png](./figures/hint1.png) ![hint2.png](./figures/hint2.png)

3. 可以选择提示框中的用户名，通过认证，就能直接在网页中填入之前保存的用户名、密码。

    ![input-saved.png](./figures/input-saved.png)

4. 点击“使用其他账号”，选择密码保险箱中保存的其他账号。认证后在网页中填入选择的用户名、密码。

    ![other-account.png](./figures/other-account.png) ![choose-other.png](./figures/choose-other.png)

    ![use-other.png](./figures/use-other.png)

5. 点击“手动输入”或者提示框之外的地方，会弹出小艺输入法，会提示可用于密码填充的用户名和钥匙图标。

    点击用户名可触发在网页中填入用户名、密码；点击钥匙图标，进入选择账号的界面。

    ![choose-manual-input.png](./figures/choose-manual-input.png) ![manual-input.png](./figures/manual-input.png)

    ![choose-other-manual.png](./figures/choose-other-manual.png)

## 2in1使用场景

以下以[https://developer.huawei.com/](https://developer.huawei.com/)网站为例：

1. 在网站中输入用户名、密码，登陆成功后，ArkWeb会提示将用户名和密码保存到密码保险箱中。

    ![arkweb-hint.png](./figures/arkweb-hint.png)

2. 再次打开相同的网站，点击用户名或者密码框中时，会弹出密码保险箱的下拉框。

    ![select-box.png](./figures/select-box.png)

3. 选择下拉框中的用户名，通过认证，就能直接在网页中填入之前保存的用户名、密码。

    ![choose-select-box.png](./figures/choose-select-box.png)

4. 也可以点击下拉框中的“使用其他账号”，选择密码保险箱中保存的其他账号。认证后在网页中填入选择的用户名、密码。

    ![choose-other-account-on-web.png](./figures/choose-other-account-on-web.png)

## 网页密码保存规格

1. ArkWeb依赖密码表单提交成功后，触发页面跳转到其他页面，才能触发密码保存。
2. Native应用通过ArkWeb实现H5登入，登录成功后请勿立即销毁ArkWeb实例，否则将无法提示密码保存。