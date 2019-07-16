# 安装

## JAVA

[java SE](https://www.oracle.com/technetwork/java/javase/downloads/index.html)

- [Win7设置Java环境变量](https://www.cnblogs.com/iwin12021/p/6057890.html)
- linux update to Java 12. `rpm -Uvh jdk-12.0.1_linux-x64_bin.rpm`

## WebGoat部署

```shell
nohup java -Dfile.encoding=UTF8 -jar /usr/webgoat/webgoat-server-8.0.0.M25.jar --server.port=8080 --server.address=10.1.121.141 &
nohup java --add-modules java.xml.bind -jar /usr/webgoat/webwolf-8.0.0.M25.jar --server.port=9090 --server.address=10.1.121.141 &
java -Dfile.encoding=UTF8 -jar webgoat-server-8.0.0.M25.jar
```

> VPN可能会导致脚本连接不到WebGoat（500）

## Git相关

### ssh

https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key

```shell
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
git push
```

### aliases

@`$Home` Path

> .gitconfig
>
> ```tex
> [alias]
>   co = checkout
>   ci = commit
>   st = status
>   br = branch
>   hist = log --pretty=format:\"%h %ad | %s%d [%an]\" --graph --date=short
>   type = cat-file -t
>   dump = cat-file -p
> ```
>

> .profile
>
> ```txt
> alias gs='git status'
> alias ga='git add'
> alias gb='git branch'
> alias gc='git commit'
> alias gd='git diff'
> alias go='git checkout'
> alias gk='gitk --all&'
> alias gx='gitx --all'
> ```
>
> 

### Reference

https://githowto.com/aliases

https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key