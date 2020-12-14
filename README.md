* [subconverter wiki](https://github.com/tindy2013/subconverter)  
* 支持自定义节点列表地址生成订阅,格式参考[links.diy](/etc/links.diy)  
* 配置地址可使用[secret gist](https://gist.github.com/)  
* demo仅供测试,需长期稳定使用请自行搭建服务端  
  
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://dashboard.heroku.com/new?template=https://github.com/mixool/subconverterku)  
  
### 服务端
点击上面紫色`Deploy to Heroku`，会跳转到heroku app创建页面，填上app的名字、选择节点、按需修改部分参数后点击下面deploy创建app即可开始部署  
如出现错误，可以多尝试几次，待部署完成后页面底部会显示Your app was successfully deployed  
  * 点击Manage App可在Settings下的Config Vars项**查看和重新设置参数,立即生效**  
  * 点击Open app跳转域名即为heroku分配域名，格式为`appname.herokuapp.com`，用于客户端  
  
### 客户端
* **务必使用HTTPS访问**  
* **替换subku.herokuapp.com为heroku分配的项目域名**  
* **替换password为部署时设置的API_TOKEN值**  
> 以下demo中的大部分节点取自订阅: [Sansui233/proxypool](https://github.com/Sansui233/proxypool)  
* 订阅转换: https://subku.herokuapp.com/ [带参数的DEMO](https://subku.herokuapp.com/sub?target=clash&url=https%3a%2f%2fproxypoolss.tk%2fclash%2fproxies%3fc%3dJP%2cTW%26speed%3d15%26type%3dss)
* 订阅自定义节点列表: https://subku.herokuapp.com/getprofile?name=profiles/pro.ini&token=password  
