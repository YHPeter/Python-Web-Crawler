# Baidu Translate [EN]

By breakpoint and JS inverse technique in browse control panel, we can analysics and get post_param：
```
post_param = {  
            "from": info_list[1],
            "to": info_list[2],
            "query": info_list[0],
            "transtype": "translang",
            "simple_means_flag": "3",
            "sign": sign,
            "token": "3c7770359299deb6d5def1c1e45140d7",#self.getToken(),
            "domain": "common",
        }
```
token and sign are used to encrypted, if we can get the rule of two value, the rule is hiden in the JS file.

``` sign.js```  is the final simplifed JS code for geting sign value, considering the length of it, I create a file to store it.

### More deatils in my code.

# 百度翻译[CN]

通过断点+JS逆向判断出post_param里面的参数配置，如下：
```
post_param = {  
            "from": info_list[1],
            "to": info_list[2],
            "query": info_list[0],
            "transtype": "translang",
            "simple_means_flag": "3",
            "sign": sign,
            "token": "3c7770359299deb6d5def1c1e45140d7",#self.getToken(),
            "domain": "common",
        }
```
token 和 sign 是两个用来加密的参数，只要解决这两个就可以获取到百度翻译的结果。

``` sign.js``` 是最后分析完，计算sign值的JS的代码，由于比较长，未放入python代码中。

### 取余具体详见代码。
