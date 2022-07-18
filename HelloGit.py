print("hello git!")

# 练习回退操作

# 已commit，没有push
# git reset --soft 目标版本号 撤销commit
# git reset --mixed 目标版本号 撤销commit和add

# 已push
# git reset --hard 目标版本号 撤销并舍弃版本号之后的记录，谨慎使用。 本地文件回滚之后需要使用 git push -f 强制回滚远程仓库
# git revert 撤销但是保留了提交记录

# 测试git revert
