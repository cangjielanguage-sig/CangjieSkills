# 使用Web组件的广告过滤功能

ArkWeb为应用提供广告过滤功能，支持通过云端推送默认的easylist规则，或允许应用通过接口设定自定义规则文件。它在网络层拦截广告资源的下载，或在网页中注入CSS规则以隐藏特定的广告元素。

当前配置文件格式为easylist语法规则。

## 常用easylist语法规则

| 规则类别     | 说明   | 示例 |
| :---------- | :------ | :---- |
| URL拦截规则 | 拦截所有网站中url能匹配"example.com/js/*_tv.js"的子资源请求。用于定义域名过滤规则，用于匹配特定的域名及其所有子域名。 | \|\|example.com/js/*_tv.js   |
| URL拦截规则 | 拦截非alimama.com、非taobao.com域名网站中的url匹配"alimama.cn"的第三方资源。\$third\_party是一种options语法，表示匹配第三方资源；域名前使用'~'表示不包括该域名。 | \|\|alimama.cn^$third-party,domain\=~alimama.com\|\~taobao.com   |
| 例外规则 | 关闭example.com网页内的广告过滤。@@是例外规则的语法关键字，表示不过滤。 | \@\@\|\|example.com^$document   |
| 例外规则 | 在域名为litv.tv的网页中，不过滤能匹配上".adserver."的子资源。 | \@\@.adserver.$domain=litv.tv   |
| 元素隐藏规则 | 隐藏myabandonware.com和myware.com域名中所有class="i528"的元素。##用于表示元素隐藏。 | myabandonware.com, myware.com##.i528   |
| 元素隐藏例外规则 | 不隐藏sdf-event.sakura.ne.jp网站中id="ad_1"的元素。 | sdf-event.sakura.ne.jp#@##ad_1   |

例外规则，通常是配合普通规则一起使用的，使普通规则在某些场景下不起作用，单独应用例外规则没有意义。

例如先配置了一条过滤所有网站的拦截规则，||abc.com/js/123.js，但是某些网站中出现了误拦截或者不能拦截的场景，就可以针对这些网站配置新的例外规则。