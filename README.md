# 安全红蓝对抗

主要基于WebGoat学习

TODO: github md asset in child directory;
TODO: client side * 2
TODO: client side

## 真要求

1. [报告]()
2. [手册](Handbook.md)

## 关键词

网络攻防(红蓝对抗); 漏洞扫描; hacking; security; web applications

## 脚本

[所用脚本介绍](intro.md)

## 常见错误

1. 只把验证逻辑放到前端

## 模拟手段:WebGoat

- [java SE](https://www.oracle.com/technetwork/java/javase/downloads/index.html)
  
  - [Win7设置Java环境变量](https://www.cnblogs.com/iwin12021/p/6057890.html)
  - Install Java 12
  ```
  rpm -Uvh jdk-12.0.1_linux-x64_bin.rpm
  ```
  
- https://github.com/WebGoat/WebGoat
  - [Goat](localhost:8080/WebGoat)
  - [Wolf](http://localhost:9090/login)
  
- 实际(例子：`10.1.121.141:8080/WebGoat`；`https://10.1.121.141:9090/WebWolf`)
```bash
java -jar /usr/webgoat/webgoat-server-8.0.0.M25.jar --server.port=8080 --server.address=10.1.121.141
java -jar /usr/webgoat/webwolf-8.0.0.M25.jar --server.port=9090 --server.address=10.1.121.141
```

## 工具

1. 文件编辑器：[Typora](https://www.typora.io/#windows)
2. [Git](https://git-scm.com/download/win)和[github](https://github.com/)：管理各版本报告
3. `Xshell` + [WinSCP](https://winscp.net/eng/docs/lang:chs)
4. ...

## 参考资料

- 书籍
  - [企业安全建设指南：金融行业安全架构与技术实践](https://www.amazon.cn/dp/B07QG6LWRS/ref=rdr_ext_sb_ti_sims_1)
  - [Web安全防护指南：基础篇](https://www.amazon.cn/dp/B07PHSVJZC/ref=pd_sbs_351_3/458-1060962-6020426?_encoding=UTF8&pd_rd_i=B07PHSVJZC&pd_rd_r=acfbc196-9eb5-11e9-a8f6-f55e4c4bcf9a&pd_rd_w=XFdjh&pd_rd_wg=ldiyf&pf_rd_p=5d917973-0ef4-4b3e-aa18-2becf295a480&pf_rd_r=4FPT10KS9H3PT3X54YSD&psc=1&refRID=4FPT10KS9H3PT3X54YSD)
  - [黑客攻防技术宝典:Web实战篇(第2版)](https://www.amazon.cn/dp/B008FNO9GK/ref=sr_1_4?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords=web%E5%AE%89%E5%85%A8&qid=1562283478&s=gateway&sr=8-4)
- awesome
  - https://github.com/sbilly/awesome-security
  - https://github.com/jekil/awesome-hacking

src/main/java/org/owasp/webgoat/plugin
