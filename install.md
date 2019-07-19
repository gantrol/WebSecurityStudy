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

### [Generating a new SSH key](https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)

1. Open Git Bash.

2. Paste the text below, substituting in your GitHub email address.

   ```shell
   $ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```

   This creates a new ssh key, using the provided email as a label.

   ```shell
   > Generating public/private rsa key pair.
   ```

3. When you're prompted to "Enter a file in which to save the key," press Enter. This accepts the default file location.

   ```shell
   > Enter a file in which to save the key (/c/Users/you/.ssh/id_rsa):[Press enter]
   ```

4. At the prompt, type a secure passphrase. For more information, see ["Working with SSH key passphrases"](https://help.github.com/en/articles/working-with-ssh-key-passphrases).

   ```shell
   > Enter passphrase (empty for no passphrase): [Type a passphrase]
   > Enter same passphrase again: [Type passphrase again]
   ```

### [Adding your SSH key to the ssh-agent](https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent)

Before adding a new SSH key to the ssh-agent to manage your keys, you should have [checked for existing SSH keys](https://help.github.com/en/articles/checking-for-existing-ssh-keys) and [generated a new SSH key](https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key).

If you have [GitHub Desktop](https://desktop.github.com/) installed, you can use it to clone repositories and not deal with SSH keys. It also comes with the Git Bash tool, which is the preferred way of running `git` commands on Windows.

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

### Reference

https://githowto.com/aliases

https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key